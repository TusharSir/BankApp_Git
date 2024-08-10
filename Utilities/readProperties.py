import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


class ReadConfigFile:

    @staticmethod
    def GetUsername():
        username = config.get('login data', 'username')
        return username

    @staticmethod
    def GetPassword():
        password = config.get('login data', 'password')
        return password
