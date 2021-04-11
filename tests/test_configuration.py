from unittest import TestCase

from src.backend.util.configuration import Configuration

TEST_CONFIG_FILE = 'data/test_app_config.yml'


class TestConfiguration(TestCase):
    """ Tests for Configuration object. """

    def test_configuration_creation(self):
        configuration = Configuration(TEST_CONFIG_FILE)

        self.assertEqual(configuration.api_key, "")
        self.assertEqual(configuration.mbta_root_url, "")
        self.assertEqual(configuration.canned_data, False)
        self.assertEqual(configuration.config_file_path, TEST_CONFIG_FILE)

    def test_load_configuration(self):
        configuration = Configuration(TEST_CONFIG_FILE)
        configuration.load_configuration()

        self.assertEqual(configuration.api_key, "r@nd0mKy3")
        self.assertEqual(configuration.mbta_root_url, "")
        self.assertEqual(configuration.canned_data, True)
        self.assertEqual(configuration.config_file_path, TEST_CONFIG_FILE)
