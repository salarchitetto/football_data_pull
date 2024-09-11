from datetime import datetime
from dateutil.relativedelta import relativedelta
import polars as pl
from polars import col

from configuration.configuration_enums import Leagues
from postgres.postgres_utils import FootyPostgres
from utilities.logger import Logger


class HighWaterMarkProcessor:
    """
    This should store all the HWM stuff for the code
    should be used throughout all sources
    """

    def __init__(self, dataframe: pl.DataFrame, table_name: str, league_name: Leagues, season: str):
        """
        Initialize the HighWaterMarkProcessor.

        :param dataframe: The dataframe that contains the data to process.
        :param table_name: The name of the table where the data is stored.
        :param league_name: The league name (from the Leagues enum).
        :param season: The season for which the data is being processed.
        """
        self.dataframe = dataframe
        self.table_name = table_name
        self.league_name = league_name
        self.season = season
        self.postgres = FootyPostgres()
        # A random date to look back to since it's the initial run
        self.initial_ingestion_date = datetime.now() - relativedelta(years=20)
        self.logger = Logger("HighWaterMarkProcessor")

    def get_high_watermark_value(self) -> datetime:
        """
        Retrieves the High WaterMark (HWM) date from the database.
        If no HWM exists, it returns the initial ingestion date.

        :return: The date of the highest watermark or the initial ingestion date.
        """
        query = f"""
            select 
            max(date) as max_date 
            from {self.table_name} 
            where league_name = '{self.league_name.name.lower()}'
            and season = '{self.season}'
        """

        hwm = self.postgres.execute(query=query, fetch_results=True)[0][0]["max_date"]

        if hwm is not None:
            self.logger.info(f"HWM exists in DB, setting it as {hwm}")
            return hwm
        else:
            self.logger.info(f"HWM does not exist in DB, setting to initial timestamp {self.initial_ingestion_date}")
            return self.initial_ingestion_date

    def get_filtered_dataframe(self):
        """
        Filters the dataframe based on the High Water Mark (HWM) value,
        returning only records with a 'date' greater than the HWM.

        :return: A filtered Polars DataFrame containing only new data since the HWM date.
        """
        hwm_date = self.get_high_watermark_value()
        return self.dataframe.filter(col("date") > hwm_date)
