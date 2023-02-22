from utilities.processor import Processor
from utilities.configurator import Configurator

if __name__ == "__main__":
    configs = Configurator("England", "premier_league")
    processor = Processor(configs)
    processor.process()

    configs_italy = Configurator("Italy", "seriea")
    processor_italy = Processor(configs_italy)
    processor_italy.process()


