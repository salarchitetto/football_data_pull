from configs import Variables
from utilities.processor import Processor
from utilities.configurator import Configurator

if __name__ == "__main__":

    # for league in Variables.league_dictionary:
    import time

    start_time = time.time()

    #Premier League
    configs = Configurator("England", "premier_league")
    processor = Processor(configs)
    processor.process()

    #Seria A
    configs_italy = Configurator("Italy", "seriea")
    processor_italy = Processor(configs_italy)
    processor_italy.process()

    #La Liga
    configs_spain = Configurator("Spain", "laliga1")
    processor_spain = Processor(configs_spain)
    processor_spain.process()

    #french1
    configs_france = Configurator("France", "french1")
    processor_france = Processor(configs_france)
    processor_france.process()

    print("--- %s seconds ---" % (time.time() - start_time))
