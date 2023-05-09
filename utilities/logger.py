import structlog


class MyLogger:
    def __init__(self, logger_name: str):
        self.logger = structlog.get_logger(logger_name=logger_name)
        structlog.wrap_logger(self.logger,
                              logger_factory=structlog.stdlib.LoggerFactory(),
                              wrapper_class=structlog.stdlib.BoundLogger,
                              processors=[
                                  structlog.stdlib.filter_by_level,
                                  structlog.stdlib.add_log_level,
                                  structlog.stdlib.add_logger_name,
                                  structlog.dev.ConsoleRenderer(),
                                  structlog.processors.JSONRenderer(),
                                  structlog.processors.format_exc_info])

    def info(self, message, **kwargs):
        self.logger.info(message, **kwargs)

    def warning(self, message, **kwargs):
        self.logger.warning(message, **kwargs)

    def error(self, message, **kwargs):
        self.logger.error(message, **kwargs)


logger = MyLogger(logger_name="test")

logger.info("Hello, world!", foo="bar", count=42)
logger.error("Shit, Its Broken!", foo="ass", count=1000)
