import structlog


class Logger:
    """
    A wrapper for Structlog that initializes a logger with standard processors and methods for different log levels.
    """

    def __init__(self, logger_name: str):
        """
        Initializes the Logger instance.

        :param logger_name: The name to identify the logger.
        """
        self.logger = structlog.get_logger(logger_name=logger_name)
        structlog.wrap_logger(self.logger,
                              logger_factory=structlog.stdlib.LoggerFactory(),
                              wrapper_class=structlog.stdlib.BoundLogger,
                              processors=[
                                  structlog.stdlib.filter_by_level,
                                  structlog.stdlib.add_log_level,
                                  structlog.stdlib.add_logger_name,
                                  structlog.dev.ConsoleRenderer(colors=True),
                                  structlog.processors.JSONRenderer(),
                                  structlog.processors.format_exc_info])

    def info(self, message, **kwargs):
        """
        Logs an info-level message.

        :param message: The message to log.
        :param kwargs: Additional contextual arguments to pass into the logger.
        :return: None
        """
        self.logger.info(message, **kwargs)

    def debug(self, message, **kwargs):
        """
        Logs a debug-level message.

        :param message: The message to log.
        :param kwargs: Additional contextual arguments to pass into the logger.
        :return: None
        """
        self.logger.debug(message, **kwargs)

    def warning(self, message, **kwargs):
        """
        Logs a warning-level message.

        :param message: The message to log.
        :param kwargs: Additional contextual arguments to pass into the logger.
        :return: None
        """
        self.logger.warning(message, **kwargs)

    def error(self, message, **kwargs):
        """
        Logs an error-level message.

        :param message: The message to log.
        :param kwargs: Additional contextual arguments to pass into the logger.
        :return: None
        """
        self.logger.error(message, **kwargs)