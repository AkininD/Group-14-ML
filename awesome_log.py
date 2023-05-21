import logging


class Logger:
    def __init__(self, filename):
        self.filename = filename
        self.logging = logging

    def printer(self):
        filename = f'./logs/{self.filename}.log'
        self.logging.basicConfig(filename=filename)
        logger = self.logging.getLogger("Catista")
        logger.setLevel(self.logging.INFO)
        return logger
