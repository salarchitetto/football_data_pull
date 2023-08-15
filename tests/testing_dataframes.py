import pandas as pd


class TestingDataframes:
    test_ids = [1, 2, 3]
    test_names = ["premier_leage", "serie_a", "la_liga"]
    test_names_none = [None, None, None]
    test_times = ["2023-05-29", "2023-05-31", "2000-01-01"]
    test_times_none = [None, None, None]
    teams = ["Juventus", "Arsenal"]
    test_dataframe = pd.DataFrame(zip(test_ids, test_names, test_times),
                                  columns=["id", "division", "date"])
    test_dataframe_missing_cols = pd.DataFrame(test_ids, columns=["id"])
    cleaned_dataframe = pd.DataFrame(zip(test_ids, test_names_none, test_times_none),
                                     columns=["id", "division", "date"])
    uppercase_dataframe = pd.DataFrame(zip(test_ids, test_names_none, test_times_none),
                                       columns=["id", "date", "division"])
    unnamed_dataframe = pd.DataFrame(zip(test_ids, test_names_none, test_times_none,
                                         test_times_none, test_times_none),
                                     columns=["id", "date", "division", "Unnamed", "unnamed"])
    empty_dataframe = pd.DataFrame(zip(test_ids, test_names_none, test_times_none),
                                   columns=["id", "date", "division"])
    teams_dataframe = pd.DataFrame(zip(teams, teams), columns=["home_team", "away_team"])
