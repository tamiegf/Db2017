# from config.dbconfig import pg_config
# import psycopg2


# dummyDB is a dummy array that simulates a database. This is for Phase1 purposes.
dummyDB = [["1", "gas", "12", "Combustion"]]

class CreditCardDAO:

    # This is an implementation for a future phase of the project
    # def __init__(self):
    #     connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
    #                                                         pg_config['user'],
    #                                                         pg_config['psswd'])
    #     self.conn = psycopg2._connect(connection_url)

    def getAllCategory(self):
        result = dummyDB
        return result

    def getCreditCardWithAllAttributes(self, ccNumber, cvv, ccExpirationDate):
        result = dummyDB
        return result

    def getCreditCardByAllAttributesExceptExpirationDate(self, ccNumber, cvv):
        result = dummyDB
        return result

    def getCreditCardByAllAttributesExceptCVV(self, ccNumber, ccExpirationDate):
        result = dummyDB
        return result

    def getCreditCardByAllAttributesExceptccNumber(self, cvv, ccExpirationDate):
        result = dummyDB
        return result

    def getCreditCardByccNumber(self, ccNumber):
        result = dummyDB
        return result

    def getCreditCardBycvv(self, cvv):
        result = dummyDB
        return result

    def getCreditCardByExpirationDate(self, ccExpirationDate):
        result = dummyDB
        return result

