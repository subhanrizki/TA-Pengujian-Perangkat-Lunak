import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\Salim\\eclipse-workspace\\orangeHRM\\Configurations\\config.ini")

class ReadConfig:
    
    @staticmethod
    def getApplicationURL():
        url = config.get("common info", "baseURL")
        return url
    
    @staticmethod
    def getUsername():
        username = config.get("common info", "username")
        return username
    
    @staticmethod
    def getPassword():
        password = config.get("common info", "password")
        return password
    
    @staticmethod
    def getUser():
        normal_user = config.get("common info","user_1")
        return normal_user
    
    @staticmethod
    def getPass():
        normal_pass = config.get("common info","pwd_1")
        return normal_pass