import logging

import yaml

_logger = logging.getLogger(__name__)


class Configuration(object):
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.api_key = ''
        self.mbta_root_url = ''
        self.canned_data = False

    def load_configuration(self):
        with open(self.config_file_path, "r") as config_file:
            dict_representation = yaml.load(config_file, Loader=yaml.FullLoader)
            self.__dict__.update(dict_representation)

        _logger.info("App configuration loaded")
