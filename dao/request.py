# from config.dbconfig import pg_config
# import psycopg2

# dummyDB is a dummy array that simulates a database. This is for Phase1 purposes.
dummyDB = [["1", "113", "21Jan17"]]

class requestDAO:

    # This is an implementation for a future phase of the project
    # def __init__(self):
    #     connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
    #                                                         pg_config['user'],
    #                                                         pg_config['psswd'])
    #     self.conn = psycopg2._connect(connection_url)


    def getAllRequest(self):
        result = dummyDB
        return result

    def getRequestWithAllAttributes(self, reqId, uid, reqDate):
        result = dummyDB
        return result

    def getRequestWithAllAttributesExceptreqDate(self, reqId, uid):
        result = dummyDB
        return result

    def getRequestWithAllAttributesExceptuid(self, reqId, reqDate):
        result = dummyDB
        return result

    def getRequestWithAllAttributesExceptreqId(self, uid, reqDate):
        result = dummyDB
        return result

    def getRequestByreqId(self, reqId):
        result = dummyDB
        return result

    def getRequestByuid(self, uid):
        result = dummyDB
        return result

    def getRequestByreqDate(self, reqDate):
        result = dummyDB
        return result