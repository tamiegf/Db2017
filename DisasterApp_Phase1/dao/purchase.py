# from config.dbconfig import pg_config
# import psycopg2

# dummyDB is a dummy array that simulates a database. This is for Phase1 purposes.
dummyDB = [["1", "customer", "Jan Li", "PO BOX 231", "Mayaguez", "Mayaguez"]]

class purchaseDAO:

    # This is an implementation for a future phase of the project
    # def __init__(self):
    #     connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
    #                                                         pg_config['user'],
    #                                                         pg_config['psswd'])
    #     self.conn = psycopg2._connect(connection_url)

    def getAllPurchase(self):
        result = dummyDB
        return result

    def getPurchaseWithAllAttributes(self, reqId, purchaseDate, ptqy, uid):
        result = dummyDB
        return result

    def getPurchaseByReqidAndPurchasedateAndPtqyAndRid(self, reqId, purchaseDate, ptqy, rid):
        result = dummyDB
        return result

    def getPurchaseByReqidAndPurchasedateAndPtqyAndUid(self, reqId, purchaseDate, ptqy, uid):
        result = dummyDB
        return result

    def getPurchaseByReqidAndPurchasedateAndPtqy(self, reqId, purchaseDate, ptqy):
        result = dummyDB
        return result

    def getPurchaseByReqidAndPurchasedateAndRid(self, reqId, purchaseDate, rid):
        result = dummyDB
        return result

    def getPurchaseByReqidAndPurchasedateAndUid(self, reqId, purchaseDate, uid):
        result = dummyDB
        return result

    def getPurchaseByReqidAndPurchasedate(self, reqId, purchaseDate):
        result = dummyDB
        return result

    def getPurchaseByReqidAndPtqy(self, reqId, ptqy):
        result = dummyDB
        return result

    def getPurchaseByReqidAndRid(self, reqId, rid):
        result = dummyDB
        return result

    def getPurchaseByReqidAndUid(self, reqId, uid):
        result = dummyDB
        return result

    def getPurchaseByReqid(self, reqId):
        result = dummyDB
        return result

    def getPurchaseByPurchasedate(self, purchaseDate):
        result = dummyDB
        return result

    def getPurchaseByPtqy(self, ptqy):
        result = dummyDB
        return result

    def getPurchaseByRid(self, rid):
        result = dummyDB
        return result

    def getPurchaseByPid(self, pid):
        result = ["1", "customer", "Jan Li", "PO BOX 231", "Mayaguez", "Mayaguez"]
        return result

    def getUserByPid(self, pid):
        result = dummyDB
        return result

