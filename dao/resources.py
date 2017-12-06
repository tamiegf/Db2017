# from config.dbconfig import pg_config
# import psycopg2

# dummyDB is a dummy array that simulates a database. This is for Phase1 purposes.
dummyDB = [["1", "customer", "Jan Li", "PO BOX 231", "Mayaguez", "Mayaguez"]]

class resourcesDAO:

    # This is an implementation for a future phase of the project
    # def __init__(self):
    #     connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
    #                                                         pg_config['user'],
    #                                                         pg_config['psswd'])
    #     self.conn = psycopg2._connect(connection_url)

    def getAllResources(self):
        result = dummyDB
        return result

    def getResourceWithAllAttributes(self, rName, rqty, cid, price, rdId, rid):
        result = dummyDB
        return result

    def getResourceWithAllAttributesExceptRid(self, rName, rqty, cid, price, rdId):
        result = dummyDB
        return result

    def getResourceWithAllAttributesExceptRDid(self, rName, rqty, cid, price, rid):
        result = dummyDB
        return result

    def getResourceByRnameAndRqtyAndCidAndPrice(self, rName, rqty, cid, price):
        result = dummyDB
        return result

    def getResourceByRnameAndRqtyAndCidAndRdid(self, rName, rqty, cid, rdId):
        result = dummyDB
        return result

    def getResourceByRnameAndRqtyAndCidAndRid(self, rName, rqty, cid, rid):
        result = dummyDB
        return result

    def getResourceByRnameAndRqtyAndCid(self, rName, rqty, cid):
        result = dummyDB
        return result

    def getResourceByRnameAndRqtyAndPrice(self, rName, rqty, price):
        result = dummyDB
        return result

    def getResourceByRnameAndRqtyAndRdid(self, rName, rqty, rdId):
        result = dummyDB
        return result

    def getResourceByRnameAndRqtyAndRid(self, rName, rqty, rid):
        result = dummyDB
        return result

    def getResourceByRnameAndRqty(self, rName, rqty):
        result = dummyDB
        return result

    def getResourceByRnameAndCid(self, rName, cid):
        result = dummyDB
        return result

    def getResourceByRnameAndPrice(self, rName, price):
        result = dummyDB
        return result

    def getResourceByRnameAndRid(self, rName, rdId):
        result = dummyDB
        return result

    def getResourceByRnameAndRid(self, rName, rdId):
        result = dummyDB
        return result

    def getResourceByRname(self, rName):
        result = dummyDB
        return result

    def getResourceByRqty(self, rqty):
        result = dummyDB
        return result

    def getResourceByCid(self, cid):
        result = dummyDB
        return result

    def getResourceByPrice(self, price):
        result = dummyDB
        return result

    def getResourceByRdid(self, rdId):
        result = dummyDB
        return result

    def getResourcesByRid(self,rid):
        result = ["1", "customer", "Jan Li", "PO BOX 231", "Mayaguez", "Mayaguez"]
        return result

    def getUserByRid(self, rid):
        result = dummyDB
        return result

    def getCategoryByRid(self, rid):
        result = dummyDB
        return result

    def getReqDetailByRid(self, rid):
        result = dummyDB
        return result
