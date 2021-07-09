import json

from utils.logger import Logger


class Application(object):
    def __init__(self):
        self.cleanup()
        self.logger = Logger("application")

        self.running = True
        self.run()

    def cleanup(self):
        with open("data/logs.json", "w") as f:
            json.dump([], f)

    def run(self):
        self.logger.log_neutral("running...")