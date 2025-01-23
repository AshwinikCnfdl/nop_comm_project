import configparser
import os

class ReadConfigData:
    config_file = "C:/Users/hp/PycharmProjects/nop_comm_project/Configrations/config.ini" # file path
    config = configparser.RawConfigParser()

    if os.path.exists(config_file):
        config.read(config_file)
    else:
        raise FileNotFoundError(f"Configuration file not found at {config_file}")

    @staticmethod
    def get_application_url():
        try:
            return ReadConfigData.config.get("common info", "URL")
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            print(f"Error retrieving URL: {e}")
            return None

    @staticmethod
    def get_demoapplication_url():
        try:
            return ReadConfigData.config.get("common info", "DemoURL")
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            print(f"Error retrieving URL: {e}")
            return None

    @staticmethod
    def get_email_id():
        try:
            return ReadConfigData.config.get("common info", "email_id")
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            print(f"Error retrieving email_id: {e}")
            return None

    @staticmethod
    def get_pwd():
        try:
            return ReadConfigData.config.get("common info", "pwd")
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            print(f"Error retrieving password: {e}")
            return None
