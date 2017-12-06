# from config.dbconfig import pg_config
# import psycopg2

# dummyDB is a dummy array that simulates a database. This is for Phase1 purposes.
dummyDB = [["23456", "12", "22Jan18", "23Jan18", "Complete", "113"]]


class requestDetailsDAO:

    # This is an implementation for a future phase of the project
    # def __init__(self):
    #     connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
    #                                                         pg_config['user'],
    #                                                         pg_config['psswd'])
    #     self.conn = psycopg2._connect(connection_url)


    def getAllRequestDetails(self):
        result = dummyDB
        return result

    def getRequestDetailsWithAllAttributes(self, RDid, qtyNeeded, needDate, deliveryDate, ReqStatus, reqId):
        result = dummyDB
        return result

    def getRequestDetailsByAllAttributesExceptreqId(self, RDid, qtyNeeded, needDate, deliveryDate, ReqStatus):
        result = dummyDB
        return result

    def getRequestDetailsByAllAttributesExceptReqStatus(self, RDid, qtyNeeded, needDate, deliveryDate, reqId):
        result = dummyDB
        return result

    def getRequestDetailsByAllAttributesExceptdeliveryDate(self, RDid, qtyNeeded, needDate, reqId, ReqStatus):
        result = dummyDB
        return result

    def getRequestDetailsByAllAttributesExceptneedDate(self, RDid, qtyNeeded, ReqStatus, deliveryDate, reqId):
        result = dummyDB
        return result

    def getRequestDetailsByAllAttributesExceptqtyNeeded(self, RDid, ReqStatus, needDate, deliveryDate, reqId):
        result = dummyDB
        return result

    def getRequestDetailsByAllAttributesExceptRDid(self, ReqStatus, qtyNeeded, needDate, deliveryDate, reqId):
        result = dummyDB
        return result

    def getRequestDetailsByAllAttributesExceptReqStatusAndreqId(self, RDid, qtyNeeded, needDate, deliveryDate):
        result = dummyDB
        return result

    def getRequestDetailsByAllAttributesExceptReqStatusAnddeliveryDate(self, RDid, qtyNeeded, needDate, reqId):
        result = dummyDB
        return result

    def getRequestDetailsByAllAttributesExceptReqStatusAndneedDate(self, RDid, qtyNeeded, deliveryDate, reqId):
        result = dummyDB
        return result

    def getRequestDetailsByAllAttributesExceptReqStatusAndqtyNeeded(self, RDid, needDate, deliveryDate, reqId):
        result = dummyDB
        return result

    def getRequestDetailsByAllAttributesExceptReqStatusAndRDid(self, qtyNeeded, needDate, deliveryDate, reqId):
        result = dummyDB
        return result

    def getRequestDetailsByAllAttributesExceptRDidAndqtyNeeded(self, ReqStatus, needDate, deliveryDate, reqId):
        result = dummyDB
        return result

    def getRequestDetailsByAllAttributesExceptRDidAndneedDate(self, ReqStatus, qtyNeeded, deliveryDate, reqId):
        result = dummyDB
        return result

    def getRequestDetailsByAllAttributesExceptRDidAnddeliveryDate(self, ReqStatus, qtyNeeded, needDate, reqId):
        result = dummyDB
        return result

    def getRequestDetailsByAllAttributesExceptRDidAndreqId(self, ReqStatus, qtyNeeded, needDate, deliveryDate):
        result = dummyDB
        return result

    def getRequestDetailsByAllAttributesExceptreqIdAndqtyNeeded(self, RDid, needDate, deliveryDate, ReqStatus):
        result = dummyDB
        return result

    def getRequestDetailsByAllAttributesExceptreqIdAndneedDate(self, RDid, qtyNeeded, deliveryDate, ReqStatus):
        result = dummyDB
        return result

    def getRequestDetailsByAllAttributesExceptreqIdAnddeliveryDate(self, RDid, qtyNeeded, needDate, ReqStatus):
        result = dummyDB
        return result

    def getRequestDetailsByAllAttributesExceptqtyNeededAndneedDate(self, RDid, reqId, deliveryDate, ReqStatus):
        result = dummyDB
        return result

    def getRequestDetailsByAllAttributesExceptqtyNeededAnddeliveryDate(self, reqId, needDate, ReqStatus):
        result = dummyDB
        return result

    def getRequestDetailsByAllAttributesExceptneedDateAnddeliveryDate(self, RDid, reqId, qtyNeeded, ReqStatus):
        result = dummyDB
        return result

    def getRequestDetailsByRDidAndqtyNeededAndneedDate(self, RDid, qtyNeeded, needDate):
        result = dummyDB
        return result

    def getRequestDetailsByRDidAndqtyNeededAnddeliveryDate(self, RDid, qtyNeeded, deliveryDate):
        result = dummyDB
        return result

    def getRequestDetailsByRDidAndqtyNeededAndReqStatus(self, RDid, qtyNeeded, ReqStatus):
        result = dummyDB
        return result

    def getRequestDetailsByRDidAndqtyNeededAndreqId(self, RDid, qtyNeeded, reqId):
        result = dummyDB
        return result

    def getRequestDetailsByRDidAndneedDateAnddeliveryDate(self, RDid, needDate, deliveryDate):
        result = dummyDB
        return result

    def getRequestDetailsByRDidAndneedDateAndReqStatus(self, RDid, needDate, ReqStatus):
        result = dummyDB
        return result

    def getRequestDetailsByRDidAndneedDateAndreqId(self, RDid, needDate, reqId):
        result = dummyDB
        return result

    def getRequestDetailsByRDidAnddeliveryDateAndReqStatus(self, RDid, deliveryDate, ReqStatus):
        result = dummyDB
        return result

    def getRequestDetailsByRDidAnddeliveryDateAndreqId(self, RDid, needDate, reqId):
        result = dummyDB
        return result

    def getRequestDetailsByRDidAndReqStatusAndreqId(self, RDid, ReqStatus, reqId):
        result = dummyDB
        return result

    def getRequestDetailsByqtyNeededAndneedDateAnddeliveryDate(self, qtyNeeded, needDate, deliveryDate):
        result = dummyDB
        return result

    def getRequestDetailsByqtyNeededAndneedDateAndReqStatus(self, qtyNeeded, needDate, ReqStatus):
        result = dummyDB
        return result

    def getRequestDetailsByqtyNeededAndneedDateAndreqId(self, qtyNeeded, needDate, reqId):
        result = dummyDB
        return result

    def getRequestDetailsByqtyNeededAnddeliveryDateAndreqId(self, qtyNeeded, deliveryDate, reqId):
        result = dummyDB
        return result

    def getRequestDetailsByqtyNeededAnddeliveryDateAndReqStatus(self, qtyNeeded, deliveryDate, ReqStatus):
        result = dummyDB
        return result

    def getRequestDetailsByqtyNeededAnddReqStatusAndreqId(self, qtyNeeded, ReqStatus, reqId):
        result = dummyDB
        return result

    def getRequestDetailsByneedDateAnddeliveryDateAndreqId(self, needDate, deliveryDate, reqId):
        result = dummyDB
        return result

    def getRequestDetailsByneedDateAnddeliveryDateAndReqStatus(self, needDate, deliveryDate, ReqStatus):
        result = dummyDB
        return result

    def getRequestDetailsByneedDateAndReqStatusAndreqId(self, needDate, ReqStatus, reqId):
        result = dummyDB
        return result

    def getRequestDetailsBydeliveryDateAndReqStatusAndreqId(self, deliveryDate, ReqStatus, reqId):
        result = dummyDB
        return result

    def getRequestDetailsByRDidAndqtyNeeded(self, RDid, qtyNeeded):
        result = dummyDB
        return result

    def getRequestDetailsByRDidAndneedDate(self, RDid, needDate):
        result = dummyDB
        return result

    def getRequestDetailsByRDidAnddeliveryDate(self, RDid, deliveryDate):
        result = dummyDB
        return result

    def getRequestDetailsByRDidAndReqStatus(self, RDid, ReqStatus):
        result = dummyDB
        return result

    def getRequestDetailsByRDidAndreqId(self, RDid, reqId):
        result = dummyDB
        return result

    def getRequestDetailsByqtyNeededAndneedDate(self, qtyNeeded, needDate):
        result = dummyDB
        return result

    def getRequestDetailsByqtyNeededAnddeliveryDate(self, qtyNeeded, deliveryDate):
        result = dummyDB
        return result

    def getRequestDetailsByqtyNeededAndReqStatus(self, qtyNeeded, ReqStatus):
        result = dummyDB
        return result

    def getRequestDetailsByqtyNeededAndreqId(self, qtyNeeded, reqId):
        result = dummyDB
        return result

    def getRequestDetailsByneedDateAnddeliveryDate(self, needDate, deliveryDate):
        result = dummyDB
        return result

    def getRequestDetailsByneedDateAndReqStatus(self, needDate, ReqStatus):
        result = dummyDB
        return result

    def getRequestDetailsByneedDateAndreqId(self, needDate, reqId):
        result = dummyDB
        return result

    def getRequestDetailsBydeliveryDateAndReqStatus(self, deliveryDate, ReqStatus):
        result = dummyDB
        return result

    def getRequestDetailsBydeliveryDateAndreqId(self, deliveryDate, reqId):
        result = dummyDB
        return result

    def getRequestDetailsByReqStatusAndreqId(self, ReqStatus, reqId):
        result = dummyDB
        return result

    def getRequestDetailsBydeliveryDate(self, deliveryDate):
        result = dummyDB
        return result

    def getRequestDetailsByReqStatus(self, ReqStatus):
        result = dummyDB
        return result

    def getRequestDetailsByreqId(self, reqId):
        result = dummyDB
        return result

    def getRequestDetailsByneedDate(self, needDate):
        result = dummyDB
        return result

    def getRequestDetailsByqtyNeeded(self, qtyNeeded):
        result = dummyDB
        return result

    def getRequestDetailsByRDid(self, RDid):
        result = dummyDB
        return result