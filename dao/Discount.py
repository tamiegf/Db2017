# from config.dbconfig import pg_config
# import psycopg2


# dummyDB is a dummy array that simulates a database. This is for Phase1 purposes.
dummyDB = [["1", "gas", "12", "Combustion"]]

class DiscountDAO:

    # This is an implementation for a future phase of the project
    # def __init__(self):
    #     connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
    #                                                         pg_config['user'],
    #                                                         pg_config['psswd'])
    #     self.conn = psycopg2._connect(connection_url)

    def getAllCategory(self):
        result = dummyDB
        return result

    def getDiscountWithAllAttributes(self,did, dPercent, stackable):
        result = dummyDB
        return result

    def getDiscountByAllAttributesExceptdid(self, dPercent, stackable):
        result = dummyDB
        return result

    def getDiscountByAllAttributesExceptdPercent(self, did, stackable):
        result = dummyDB
        return result

    def getDiscountByAllAttributesExceptStackable(self, did, dPercent):
        result = dummyDB
        return result

    def getDiscountBydid(self, did):
        result = dummyDB
        return result

    def getDiscountBydPercent(self, dPercent):
        result = dummyDB
        return result

    def getDiscountByStackable(self, stackable):
        result = dummyDB
        return result

