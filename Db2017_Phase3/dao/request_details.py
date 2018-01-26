from config.db_config import db_config
import psycopg2


class requestDetailsDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host='localhost'" % (db_config['dbname'],
                                                            db_config['user'],
                                                            db_config['psswd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllRequestDetails(self):
        cursor = self.conn.cursor()
        query = "select * from request_details;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getRequestDetailsByAllAttributesExceptreqId(self, RDid, rdqty, needDate, deliveryDate, status):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s AND rdqty=%s AND need_Date=%s AND delivery_Date=%s AND status=%s;"
        cursor.execute(query, (RDid, rdqty, needDate, deliveryDate, status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByAllAttributesExceptReqStatus(self, RDid, rdqty, needDate, deliveryDate, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s AND rdqty=%s AND need_Date=%s AND delivery_Date=%s AND reqId=%s;"
        cursor.execute(query, (RDid, rdqty, needDate, deliveryDate, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByAllAttributesExceptdeliveryDate(self, RDid, rdqty, needDate, reqId, status):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s AND rdqty=%s AND need_Date=%s AND reqId=%s AND status=%s;"
        cursor.execute(query, (RDid, rdqty, needDate, reqId, status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByAllAttributesExceptneedDate(self, RDid, rdqty, status, deliveryDate, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s AND rdqty=%s AND status=%s AND delivery_Date=%s AND reqId=%s;"
        cursor.execute(query, (RDid, rdqty, status, deliveryDate, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByAllAttributesExceptrdqty(self, RDid, status, needDate, deliveryDate, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s AND status=%s AND need_Date=%s AND delivery_Date=%s AND reqId=%s;"
        cursor.execute(query, (RDid, status, needDate, deliveryDate, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByAllAttributesExceptRDid(self, status, rdqty, needDate, deliveryDate, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where status=%s AND rdqty=%s AND need_Date=%s AND delivery_Date=%s AND reqId=%s;"
        cursor.execute(query, (status, rdqty, needDate, deliveryDate, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByAllAttributesExceptReqStatusAndreqId(self, RDid, rdqty, needDate, deliveryDate):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s AND rdqty=%s AND need_Date=%s AND delivery_Date=%s;"
        cursor.execute(query, (RDid, rdqty, needDate, deliveryDate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByAllAttributesExceptReqStatusAnddeliveryDate(self, RDid, rdqty, needDate, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s AND rdqty=%s AND need_Date=%s AND reqId=%s;"
        cursor.execute(query, (RDid, rdqty, needDate, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByAllAttributesExceptReqStatusAndneedDate(self, RDid, rdqty, deliveryDate, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s AND rdqty=%s AND delivery_Date=%s AND reqId=%s;"
        cursor.execute(query, (RDid, rdqty, deliveryDate, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByAllAttributesExceptReqStatusAndrdqty(self, RDid, needDate, deliveryDate, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s AND need_Date=%s AND delivery_Date=%s AND reqId=%s;"
        cursor.execute(query, (RDid, needDate, deliveryDate, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByAllAttributesExceptReqStatusAndRDid(self, rdqty, needDate, deliveryDate, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where rdqty=%s AND need_Date=%s AND delivery_Date=%s AND reqId=%s;"
        cursor.execute(query, (rdqty, needDate, deliveryDate, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByAllAttributesExceptRDidAndrdqty(self, status, needDate, deliveryDate, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where status=%s AND need_Date=%s AND delivery_Date=%s AND reqId=%s;"
        cursor.execute(query, (status, needDate, deliveryDate, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByAllAttributesExceptRDidAndneedDate(self, status, rdqty, deliveryDate, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where status=%s AND rdqty=%s AND delivery_Date=%s AND reqId=%s;"
        cursor.execute(query, (status, rdqty, deliveryDate, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByAllAttributesExceptRDidAnddeliveryDate(self, status, rdqty, needDate, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where status=%s AND rdqty=%s AND need_Date=%s AND reqId=%s;"
        cursor.execute(query, (status, rdqty, needDate, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByAllAttributesExceptRDidAndreqId(self, status, rdqty, needDate, deliveryDate):
        cursor = self.conn.cursor()
        query = "select * from request_details where status=%s AND rdqty=%s AND need_Date=%s AND delivery_Date=%s;"
        cursor.execute(query, (status, rdqty, needDate, deliveryDate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByAllAttributesExceptreqIdAndrdqty(self, RDid, needDate, deliveryDate, status):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s AND need_Date=%s AND delivery_Date=%s AND status=%s;"
        cursor.execute(query, (RDid, needDate, deliveryDate, status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByAllAttributesExceptreqIdAndneedDate(self, RDid, rdqty, deliveryDate, status):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s AND rdqty=%s AND delivery_Date=%s AND status=%s;"
        cursor.execute(query, (RDid, rdqty, deliveryDate, status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByAllAttributesExceptreqIdAnddeliveryDate(self, RDid, rdqty, needDate, status):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s AND rdqty=%s AND need_Date=%s AND status=%s;"
        cursor.execute(query, (RDid, rdqty, needDate, status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByAllAttributesExceptrdqtyAndneedDate(self, RDid, reqId, deliveryDate, status):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s AND reqId=%s AND delivery_Date=%s AND status=%s;"
        cursor.execute(query, (RDid, reqId, deliveryDate, status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByAllAttributesExceptrdqtyAnddeliveryDate(self, reqId, needDate, status):
        cursor = self.conn.cursor()
        query = "select * from request_details where reqId=%s AND need_Date=%s AND status=%s;"
        cursor.execute(query, (reqId, needDate, status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByAllAttributesExceptneedDateAnddeliveryDate(self, RDid, reqId, rdqty, status):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s AND reqId=%s AND rdqty=%s AND status=%s;"
        cursor.execute(query, (RDid, reqId, rdqty, status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByRDidAndrdqtyAndneedDate(self, RDid, rdqty, needDate):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s AND rdqty=%s AND need_Date=%s;"
        cursor.execute(query, (RDid, rdqty, needDate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByRDidAndrdqtyAnddeliveryDate(self, RDid, rdqty, deliveryDate):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s AND rdqty=%s AND delivery_Date=%s;"
        cursor.execute(query, (RDid, rdqty, deliveryDate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByRDidAndrdqtyAndReqStatus(self, RDid, rdqty, status):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s AND rdqty=%s AND status=%s;"
        cursor.execute(query, (RDid, rdqty, status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByRDidAndrdqtyAndreqId(self, RDid, rdqty, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s AND rdqty=%s AND reqId=%s;"
        cursor.execute(query, (RDid, rdqty, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByRDidAndneedDateAnddeliveryDate(self, RDid, needDate, deliveryDate):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s AND need_Date=%s AND delivery_Date=%s;"
        cursor.execute(query, (RDid, needDate, deliveryDate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByRDidAndneedDateAndReqStatus(self, RDid, needDate, status):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s AND need_Date=%s AND status=%s;"
        cursor.execute(query, (RDid, needDate, status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByRDidAndneedDateAndreqId(self, RDid, needDate, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s AND need_Date=%s AND reqId=%s;"
        cursor.execute(query, (RDid, needDate, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByRDidAnddeliveryDateAndReqStatus(self, RDid, deliveryDate, status):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s AND delivery_Date=%s AND status=%s;"
        cursor.execute(query, (RDid, deliveryDate, status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByRDidAnddeliveryDateAndreqId(self, RDid, needDate, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s AND need_Date=%s AND reqId=%s;"
        cursor.execute(query, (RDid, needDate, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByRDidAndReqStatusAndreqId(self, RDid, status, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s AND status=%s AND reqId=%s;"
        cursor.execute(query, (RDid, status, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByrdqtyAndneedDateAnddeliveryDate(self, rdqty, needDate, deliveryDate):
        cursor = self.conn.cursor()
        query = "select * from request_details where rdqty=%s AND need_Date=%s AND delivery_Date=%s;"
        cursor.execute(query, (rdqty, needDate, deliveryDate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByrdqtyAndneedDateAndReqStatus(self, rdqty, needDate, status):
        cursor = self.conn.cursor()
        query = "select * from request_details where rdqty=%s AND need_Date=%s AND status=%s;"
        cursor.execute(query, (rdqty, needDate, status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByrdqtyAndneedDateAndreqId(self, rdqty, needDate, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where rdqty=%s AND need_Date=%s AND reqId=%s;"
        cursor.execute(query, (rdqty, needDate, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByrdqtyAnddeliveryDateAndreqId(self, rdqty, deliveryDate, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where rdqty=%s AND delivery_Date=%s AND reqId=%s;"
        cursor.execute(query, (rdqty, deliveryDate, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByrdqtyAnddeliveryDateAndReqStatus(self, rdqty, deliveryDate, status):
        cursor = self.conn.cursor()
        query = "select * from request_details where rdqty=%s AND delivery_Date=%s AND status=%s;"
        cursor.execute(query, (rdqty, deliveryDate, status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByrdqtyAnddReqStatusAndreqId(self, rdqty, status, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where rdqty=%s AND status=%s AND reqId=%s;"
        cursor.execute(query, (rdqty, status, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByneedDateAnddeliveryDateAndreqId(self, needDate, deliveryDate, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where need_Date=%s AND delivery_date=%s AND reqId=%s;"
        cursor.execute(query, (needDate, deliveryDate, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByneedDateAnddeliveryDateAndReqStatus(self, needDate, deliveryDate, status):
        cursor = self.conn.cursor()
        query = "select * from request_details where need_Date=%s AND delivery_date=%s AND status=%s;"
        cursor.execute(query, (needDate, deliveryDate, status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByneedDateAndReqStatusAndreqId(self, needDate, status, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where need_Date=%s AND status=%s AND reqId=%s;"
        cursor.execute(query, (needDate, status, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsBydeliveryDateAndReqStatusAndreqId(self, deliveryDate, status, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where delivery_Date=%s AND status=%s AND reqId=%s;"
        cursor.execute(query, ( deliveryDate, status, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByRDidAndrdqty(self, RDid, rdqty):
        cursor = self.conn.cursor()
        query = "select * from request_details where rdid=%s AND rdqty=%s;"
        cursor.execute(query, (RDid, rdqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByRDidAndneedDate(self, RDid, needDate):
        cursor = self.conn.cursor()
        query = "select * from request_details where rdid=%s AND need_date=%s;"
        cursor.execute(query, (RDid, needDate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByRDidAnddeliveryDate(self, RDid, deliveryDate):
        cursor = self.conn.cursor()
        query = "select * from request_details where rdid=%s AND delivery_date=%s;"
        cursor.execute(query, (RDid, deliveryDate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByRDidAndReqStatus(self, RDid, status):
        cursor = self.conn.cursor()
        query = "select * from request_details where rdid=%s AND status=%s;"
        cursor.execute(query, (RDid, status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByRDidAndreqId(self, RDid, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s AND reqId=%s;"
        cursor.execute(query, (RDid, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByrdqtyAndneedDate(self, rdqty, needDate):
        cursor = self.conn.cursor()
        query = "select * from request_details where rdqty=%s AND need_Date=%s;"
        cursor.execute(query, (rdqty, needDate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByrdqtyAnddeliveryDate(self, rdqty, deliveryDate):
        cursor = self.conn.cursor()
        query = "select * from request_details where rdqty=%s AND delivery_Date=%s;"
        cursor.execute(query, (rdqty, deliveryDate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByrdqtyAndReqStatus(self, rdqty, status):
        cursor = self.conn.cursor()
        query = "select * from request_details where rdqty=%s AND status=%s;"
        cursor.execute(query, (rdqty, status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByrdqtyAndreqId(self, rdqty, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where rdqty=%s AND reqId=%s;"
        cursor.execute(query, (rdqty, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByneedDateAnddeliveryDate(self, needDate, deliveryDate):
        cursor = self.conn.cursor()
        query = "select * from request_details where need_Date=%s AND delivery_date=%s;"
        cursor.execute(query, (needDate, deliveryDate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByneedDateAndReqStatus(self, needDate, status):
        cursor = self.conn.cursor()
        query = "select * from request_details where need_Date=%s AND status=%s;"
        cursor.execute(query, (needDate, status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByneedDateAndreqId(self, needDate, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where need_Date=%s AND reqId=%s;"
        cursor.execute(query, (needDate, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsBydeliveryDateAndReqStatus(self, deliveryDate, status):
        cursor = self.conn.cursor()
        query = "select * from request_details where delivery_Date=%s AND status=%s;"
        cursor.execute(query, (deliveryDate, status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsBydeliveryDateAndreqId(self, deliveryDate, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where delivery_Date=%s AND reqId=%s;"
        cursor.execute(query, ( deliveryDate, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByReqStatusAndreqId(self, status, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where status=%s AND reqId=%s;"
        cursor.execute(query, (status, reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsBydeliveryDate(self, deliveryDate):
        cursor = self.conn.cursor()
        query = "select * from request_details where delivery_Date=%s;"
        cursor.execute(query, ( deliveryDate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByReqStatus(self, status):
        cursor = self.conn.cursor()
        query = "select * from request_details where status=%s;"
        cursor.execute(query, ( status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByreqId(self, reqId):
        cursor = self.conn.cursor()
        query = "select * from request_details where reqId=%s;"
        cursor.execute(query, (reqId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByneedDate(self, needDate):
        cursor = self.conn.cursor()
        query = "select * from request_details where need_Date=%s;"
        cursor.execute(query, (needDate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByrdqty(self, rdqty):
        cursor = self.conn.cursor()
        query = "select * from request_details where rdqty=%s;"
        cursor.execute(query, (rdqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestDetailsByRDid(self, RDid):
        cursor = self.conn.cursor()
        query = "select * from request_details where RDid=%s;"
        cursor.execute(query, (RDid,))
        result = cursor.fetchone()
        return result

    def getOrderByFirstNameAndLastName(self, ufirstname, ulastname):
        cursor = self.conn.cursor()
        query = "select rdid, rname, rdqty, need_date, delivery_date, ptype from request,(request_details natural inner join resources natural inner join purchase), users where request.reqid = request_details.reqid and users.uid = request.uid and users.utype = 'client' and users.ufirstname = %s and users.ulastname = %s;"
        cursor.execute(query, (ufirstname, ulastname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderByFirstName(self, ufirstname):
        cursor = self.conn.cursor()
        query = "select rdid, rname, rdqty, need_date, delivery_date, ptype from request,(request_details natural inner join resources natural inner join purchase), users where request.reqid = request_details.reqid and users.uid = request.uid and users.utype = 'client' and users.ufirstname = %s"
        cursor.execute(query, (ufirstname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderByLastName(self, ulastname):
        cursor = self.conn.cursor()
        query = "select rdid, rname, rdqty, need_date, delivery_date, ptype from request,(request_details natural inner join resources natural inner join purchase), users where request.reqid = request_details.reqid and users.uid = request.uid and users.utype = 'client' and users.ulastname = %s;"
        cursor.execute(query, (ulastname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPaymentOfResource(self, pid):
        cursor = self.conn.cursor()
        query = "select pid, rname, pdate, pqty, (pqty*rprice) as price_paid, ccnumber from (purchase natural inner join creditcard natural inner join request_details), resources where resources.rdid = request_details.rdid and pid = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        return result

    def insert(self, rid, rdqty, need_date, reqid):
        cursor = self.conn.cursor()
        query = "insert into request_details(rid, rdqty, need_date, status, reqid) values (%s, %s, %s, 'pending', %s) returning rdid;"
        cursor.execute(query, (rid, rdqty, need_date, reqid,))
        rdid = cursor.fetchone()[0]
        self.conn.commit()
        return rdid

    # update methods
    def updatedeliveryDateAndrdqtyAndstatus(self, rdid, deliverydate, rdqty, status):
        cursor = self.conn.cursor()
        query = "update request_details set delivery_date= %s, rdqty=%s, status=%s where rdid=%s returning need_date, reqid, rid;"
        cursor.execute(query, (deliverydate, rdqty, status, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def updatedeliveryDateAndstatus(self, rdid, deliverydate, status):
        cursor = self.conn.cursor()
        query = "update request_details set delivery_date= %s, status=%s where rdid=%s returning need_date, reqid, rid, rdqty;"
        cursor.execute(query, (deliverydate, status, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def updaterdqty(self, rdid, rdqty):
        cursor = self.conn.cursor()
        query = "update request_details set rdqty=%s where rdid=%s returning need_date, reqid, rid, delivery_date, status;"
        cursor.execute(query, (rdqty, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def updatestatus(self, rdid, status):
        cursor = self.conn.cursor()
        query = "update request_details set status=%s where rdid=%s returning need_date, reqid, rid, delivery_date, rdqty;"
        cursor.execute(query, (status, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def updatedeliverydate(self, rdid, deliverydate):
        cursor = self.conn.cursor()
        query = "update request_details set delivery_date=%s where rdid=%s returning need_date, reqid, rid, rdqty, status ;"
        cursor.execute(query, (deliverydate, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result