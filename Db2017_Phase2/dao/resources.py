from Db2017_Phase2.config.db_config import db_config
import psycopg2


class resourcesDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host='localhost'" % (db_config['dbname'],
                                                            db_config['user'],
                                                            db_config['psswd'])
        self.conn = psycopg2._connect(connection_url)


    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "select * from resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
#
    def getResourceByRidAndRnameAndrqtyAndrpriceAnduid(self, rid, rName, rqty, rprice, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where rid=%s AND rName=%s AND rqty=%s AND rprice=%s AND uid=%s;"
        cursor.execute(query, (rid, rName, rqty, rprice, uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
#
    def getResourceByRidAndRnameAndRqtyAndrPriceAndrid(self, rid, rName, rqty, rprice, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rid=%s AND rName=%s AND rqty=%s AND rprice=%s AND rdid=%s;"
        cursor.execute(query, (rid, rName, rqty, rprice, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
#
    def getResourceByRidAndRnameAndRqtyAnduidAndrdid(self, rid, rName, rqty, uid, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rid=%s AND rName=%s AND rqty=%s AND uid=%s AND rdid=%s;"
        cursor.execute(query, (rid, rName, rqty, uid, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
#
    def getResourceByRidAndRnameAndrPriceAnduidAndrdid(self, rid, rName, rprice, uid, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rid=%s AND rName=%s AND rprice=%s AND uid=%s AND rdid=%s;"
        cursor.execute(query, (rid, rName, rprice, uid, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
#
    def getResourceByRidAndRqtyAndrPriceAnduidAndrdid(self, rid, rqty, rprice, uid, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rid=%s AND rqty=%s AND rprice=%s AND uid=%s AND rdid=%s;"
        cursor.execute(query, (rid, rqty, rprice, uid, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
#
    def getResourceByRnameAndRqtyAndrPriceAnduidAndrdid(self, rName, rqty, rprice, uid, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rName=%s AND rqty=%s AND rprice=%s AND uid=%s AND rdid=%s;"
        cursor.execute(query, (rName, rqty, rprice, uid, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
#
    def getResourceByRidAndRnameAndRqtyAndrPrice(self, rid, rName, rqty, rprice):
        cursor = self.conn.cursor()
        query = "select * from resources where rid=%s AND rName=%s AND rqty=%s AND rprice=%s;"
        cursor.execute(query, (rid, rName, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result
#
    def getResourceByRidAndRnameAndRqtyAnduid(self, rid, rName, rqty, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where rid=%s AND rName=%s AND rqty=%s AND uid=%s;"
        cursor.execute(query, (rid, rName, rqty, uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
#
    def getResourceByRidAndRnameAndrPriceAnduid(self, rid, rName, rprice, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where rid=%s AND rName=%s AND rprice=%s AND uid=%s;"
        cursor.execute(query, (rid, rName, rprice, uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
#
    def getResourceByRidAndRnameAndRqtyAndrPriceAnduidAndrdid(self, rid, rqty, rprice, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where rid=%s AND rqty=%s AND rprice=%s AND uid=%s;"
        cursor.execute(query, (rid, rqty, rprice, uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
#
    def getResourceByRnameAndrqtyAndrpriceAnduid(self, rName, rqty, rprice, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where rName=%s AND rqty=%s AND rprice=%s AND uid=%s;"
        cursor.execute(query, ( rName, rqty, rprice, uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getResourceByRnameAndrqtyAnduidAndrdid(self, rName, rqty, uid, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rName=%s AND rqty=%s AND uid=%s AND rdid=%s;"
        cursor.execute(query, (rName, rqty, uid, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByRnameAndRqtyAnduid(self, rName, rqty, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where rName=%s AND rqty=%s AND uid=%s;"
        cursor.execute(query, (rName, rqty, uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByRnameAndrqtyAndrprice(self, rName, rqty, rprice):
        cursor = self.conn.cursor()
        query = "select * from resources where rName=%s AND rqty=%s AND rprice=%s;"
        cursor.execute(query, (rName, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByRnameAndrqtyAndrdid(self, rName, rqty, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rName=%s AND rqty=%s ANd rdid=%s;"
        cursor.execute(query, (rName, rqty, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByRnameAndrqty(self, rName, rqty):
        cursor = self.conn.cursor()
        query = "select * from resources where rName=%s AND rqty=%s;"
        cursor.execute(query, (rName, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByRnameAnduid(self, rName, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where rName=%s AND uid=%s;"
        cursor.execute(query, (rName, uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByRnameAndrprice(self, rName, rprice):
        cursor = self.conn.cursor()
        query = "select * from resources where rName=%s AND rprice=%s;"
        cursor.execute(query, (rName, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByRnameAndrdid(self, rName, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rName=%s AND rdid=%s;"
        cursor.execute(query, (rName, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByRname(self, rName):
        cursor = self.conn.cursor()
        query = "select * from resources where rName=%s;"
        cursor.execute(query, (rName,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByrqty(self, rqty):
        cursor = self.conn.cursor()
        query = "select * from resources where rqty=%s;"
        cursor.execute(query, (rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByuid(self, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where uid=%s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByrprice(self, rprice):
        cursor = self.conn.cursor()
        query = "select * from resources where rprice=%s;"
        cursor.execute(query, (rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByrdid(self, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid=%s;"
        cursor.execute(query, (rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRid(self,rid):
        cursor = self.conn.cursor()
        query = "select * from resources where rid=%s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result


    def getSuplierByResourceId(self, rid):
        cursor = self.conn.cursor()
        query = "select uid,uaid,utype,ufirstname,ulastname from users natural inner join resources where rid=%s ;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByCategoryNameAndDescription(self, cname, cdescription):
        cursor = self.conn.cursor()
        query = "select uid,uaid,utype,ufirstname,ulastname from users natural inner join resources natural inner join resource_category where cname=%s and cdescription=%s ;"
        cursor.execute(query, (cname, cdescription,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByCategoryName(self, cname):
        cursor = self.conn.cursor()
        query = "select uid,uaid,utype,ufirstname,ulastname from users natural inner join resources natural inner join resource_category where cname=%s;"
        cursor.execute(query, (cname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByCategoryDescription(self, cdescription):
        cursor = self.conn.cursor()
        query = "select uid,uaid,utype,ufirstname,ulastname from users natural inner join resources natural inner join resource_category where cdescription=%s ;"
        cursor.execute(query, (cdescription,))
        result = []
        for row in cursor:
            result.append(row)

    def getOrderBySupplierFirstNameAndLastName(self, ufirstname, ulastname):
        cursor = self.conn.cursor()
        query = "select rdid, rname, ufirstname, ulastname, rdqty from users natural inner join resources natural inner join request_details where utype = 'supplier' and ufirstname = %s and ulastname = %s;"
        cursor.execute(query, (ufirstname, ulastname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderBySupplierFirstName(self, ufirstname):
        cursor = self.conn.cursor()
        query = "select rdid, rname, ufirstname, ulastname, rdqty from users natural inner join resources natural inner join request_details where utype = 'supplier' and ufirstname = %s;"
        cursor.execute(query, (ufirstname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderBySupplierLastName(self, ulastname):
        cursor = self.conn.cursor()
        query = "select rdid, rname, ufirstname, ulastname, rdqty from users natural inner join resources natural inner join request_details where utype = 'supplier' and ulastname = %s;"
        cursor.execute(query, (ulastname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrderBySupplier(self):
        cursor = self.conn.cursor()
        query = "select rdid, rname, ufirstname, ulastname, rdqty from users natural inner join resources natural inner join request_details where utype = 'supplier';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllResourcesOrderByName(self):
        cursor = self.conn.cursor()
        query = "select * from resources where rqty>0 order by rname;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByRidAndRnameAndrPriceAnduidAndrdidOrderByName(self, rid, rName, rprice, uid, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rid=%s AND rName=%s AND rprice=%s AND uid=%s AND rdid=%s AND rqty>0 order by rname;"
        cursor.execute(query, (rid, rName, rprice, uid, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByRidAndRnameAndrPriceAnduidOrderByName(self, rid, rName, rprice, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where rid=%s AND rName=%s AND rprice=%s AND uid=%s AND rqty>0 order by rname;"
        cursor.execute(query, (rid, rName, rprice, uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getResourceByRnameAnduidOrderByName(self, rName, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where rName=%s AND uid=%s AND rqty>0 order by rname;"
        cursor.execute(query, (rName, uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByRnameAndrpriceOrderByName(self, rName, rprice):
        cursor = self.conn.cursor()
        query = "select * from resources where rName=%s AND rprice=%s AND rqty>0 order by rname;"
        cursor.execute(query, (rName, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByRnameAndrdidOrderByName(self, rName, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rName=%s AND rdid=%s AND rqty>0 order by rname;"
        cursor.execute(query, (rName, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByRnameOrderByName(self, rName):
        cursor = self.conn.cursor()
        query = "select * from resources where rName=%s AND rqty>0 order by rname;"
        cursor.execute(query, (rName,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getResourceByuidOrderByName(self, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where uid=%s AND rqty>0 order by rname;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByrpriceOrderByName(self, rprice):
        cursor = self.conn.cursor()
        query = "select * from resources where rprice=%s AND rqty>0 order by rname;"
        cursor.execute(query, (rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByrdidOrderByName(self, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid=%s AND rqty>0 order by rname;"
        cursor.execute(query, (rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRidOrderByName(self, rid):
        cursor = self.conn.cursor()
        query = "select * from resources where rid=%s AND rqty>0 order by rname;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getResourceByRnameAndRdidAndrpriceAnduidOrderByName(self, rid, rName, rprice, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rid=%s AND rName=%s AND rprice=%s AND rdid=%s AND rqty>0 order by rname;"
        cursor.execute(query, (rid, rName, rprice, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByRidAndRNameAndRpriceOrderByRname(self, rid, rName, rprice):
        cursor = self.conn.cursor()
        query = "select * from resources where rid=%s AND rName=%s AND rprice=%s AND rqty>0 order by rname;"
        cursor.execute(query, (rid, rName, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByRidAndRNameAndRpriceOrderByRdid(self, rid, rName, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rid=%s AND rName=%s AND rdid=%s AND rqty>0 order by rname;"
        cursor.execute(query, (rid, rName, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByRidAndRNameAndRpriceOrderByUid(self, rid, rName, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where rid=%s AND rName=%s AND rprice=%s AND uid=%s AND rqty>0 order by rname;"
        cursor.execute(query, (rid, rName, uid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllResourcesAvailable(self):
        cursor = self.conn.cursor()
        query = "select * from resources where rqty>0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

#############

    def getAllResourcesRequestedOrderByName(self):
        cursor = self.conn.cursor()
        query = "select * from resources  where rdid IS NOT NULL order by rname;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #
    def getResourceRequestedByRidAndRnameAndrqtyAndrpriceAnduidOrderByName(self, rid, rName, rqty, rprice, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rid=%s AND rName=%s AND rqty=%s AND rprice=%s AND uid=%s order by rname;"
        cursor.execute(query, (rid, rName, rqty, rprice, uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #
    def getResourceRequestedByRidAndRnameAndRqtyAndrPriceAndridOrderByName(self, rid, rName, rqty, rprice, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rid=%s AND rName=%s AND rqty=%s AND rprice=%s AND rdid=%s order by rname;"
        cursor.execute(query, (rid, rName, rqty, rprice, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #
    def getResourceRequestedByRidAndRnameAndRqtyAnduidAndrdidOrderByName(self, rid, rName, rqty, uid, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rid=%s AND rName=%s AND rqty=%s AND uid=%s AND rdid=%s order by rname;"
        cursor.execute(query, (rid, rName, rqty, uid, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #
    def getResourceRequestedByRidAndRnameAndrPriceAnduidAndrdidOrderByName(self, rid, rName, rprice, uid, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rid=%s AND rName=%s AND rprice=%s AND uid=%s AND rdid=%s order by rname;"
        cursor.execute(query, (rid, rName, rprice, uid, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #
    def getResourceRequestedByRidAndRqtyAndrPriceAnduidAndrdidOrderByName(self, rid, rqty, rprice, uid, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rid=%s AND rqty=%s AND rprice=%s AND uid=%s AND rdid=%s orderby rname;"
        cursor.execute(query, (rid, rqty, rprice, uid, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #
    def getResourceRequestedByRnameAndRqtyAndrPriceAnduidAndrdidOrderByName(self, rName, rqty, rprice, uid, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rName=%s AND rqty=%s AND rprice=%s AND uid=%s AND rdid=%s order by rname;"
        cursor.execute(query, (rName, rqty, rprice, uid, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRidAndRnameAndRqtyAndrPriceAnduidAndrdidOrderByName(self, rid, rqty, rprice, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rid=%s AND rqty=%s AND rprice=%s AND uid=%s order by name;"
        cursor.execute(query, (rid, rprice, rqty, uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRidAndRnameAndrPriceAnduidOrderByName(self, rid, rName, rprice, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rid=%s AND rName=%s AND rprice=%s AND uid=%s order by rname;"
        cursor.execute(query, (rid, rName, rprice, uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRidAndRnameAndRqtyAnduidOrderByName(self, rid, rName, rqty, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rid=%s AND rName=%s AND rqty=%s AND uid=%s order by rname;"
        cursor.execute(query, (rid, rName, rqty, uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRidAndRnameAndRqtyAndrPriceOrderByName(self, rid, rName, rqty, rprice):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rid=%s AND rName=%s AND rqty=%s AND rprice=%s order by rname;"
        cursor.execute(query, (rid, rName, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRnameAndrqtyAnduidAndrdidOrderByName(self, rName, rqty, uid, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rName=%s AND rqty=%s AND uid=%s AND rdid=%s order by rname;"
        cursor.execute(query, (rName, rqty, uid, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRnameAndRqtyAnduidOrderByName(self, rName, rqty, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rName=%s AND rqty=%s AND uid=%s order by rname;"
        cursor.execute(query, (rName, rqty, uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRnameAndrqtyAndrpriceOrderByName(self, rName, rqty, rprice):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rName=%s AND rqty=%s AND rprice=%s order by rname;"
        cursor.execute(query, (rName, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRnameAndrqtyAndrdidOrderByName(self, rName, rqty, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rName=%s AND rqty=%s ANd rdid=%s order by rname;"
        cursor.execute(query, (rName, rqty, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRnameAndrqtyOrderByName(self, rName, rqty):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rName=%s AND rqty=%s order by rname;"
        cursor.execute(query, (rName, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRnameAnduidOrderByName(self, rName, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rName=%s AND uid=%s order by rname;"
        cursor.execute(query, (rName, uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRnameAndrpriceOrderByName(self, rName, rprice):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rName=%s AND rprice=%s order by rname;"
        cursor.execute(query, (rName, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRnameAndrdidOrderByName(self, rName, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rName=%s AND rdid=%s order by rname;"
        cursor.execute(query, (rName, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRnameOrderByName(self, rName):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rName=%s order by rname;"
        cursor.execute(query, (rName,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByrqtyOrderByName(self, rqty):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rqty=%s order by rname;"
        cursor.execute(query, (rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByuidOrderByName(self, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and uid=%s order by rname;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByrpriceOrderByName(self, rprice):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rprice=%s order by rname;"
        cursor.execute(query, (rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByrdidOrderByName(self, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rdid=%s order by rname;"
        cursor.execute(query, (rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRidOrderByName(self, rid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL AND rid=%s order by rname;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    ########
    ########

    def getAllResourcesRequested(self):
        cursor = self.conn.cursor()
        query = "select * from resources  where rdid IS NOT NULL;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #
    def getResourceRequestedByRidAndRnameAndrqtyAndrpriceAnduid(self, rid, rName, rqty, rprice, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rid=%s AND rName=%s AND rqty=%s AND rprice=%s AND uid=%s ;"
        cursor.execute(query, (rid, rName, rqty, rprice, uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #
    def getResourceRequestedByRidAndRnameAndRqtyAndrPriceAndrid(self, rid, rName, rqty, rprice, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rid=%s AND rName=%s AND rqty=%s AND rprice=%s AND rdid=%s;"
        cursor.execute(query, (rid, rName, rqty, rprice, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #
    def getResourceRequestedByRidAndRnameAndRqtyAnduidAndrdid(self, rid, rName, rqty, uid, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rid=%s AND rName=%s AND rqty=%s AND uid=%s AND rdid=%s;"
        cursor.execute(query, (rid, rName, rqty, uid, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #
    def getResourceRequestedByRidAndRnameAndrPriceAnduidAndrdid(self, rid, rName, rprice, uid, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rid=%s AND rName=%s AND rprice=%s AND uid=%s AND rdid=%s;"
        cursor.execute(query, (rid, rName, rprice, uid, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #
    def getResourceRequestedByRidAndRqtyAndrPriceAnduidAndrdid(self, rid, rqty, rprice, uid, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rid=%s AND rqty=%s AND rprice=%s AND uid=%s AND rdid=%s;"
        cursor.execute(query, (rid, rqty, rprice, uid, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #
    def getResourceRequestedByRnameAndRqtyAndrPriceAnduidAndrdid(self, rName, rqty, rprice, uid, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rName=%s AND rqty=%s AND rprice=%s AND uid=%s AND rdid=%s;"
        cursor.execute(query, (rName, rqty, rprice, uid, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRidAndRnameAndRqtyAndrPriceAnduidAndrdid(self, rid, rqty, rprice, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rid=%s AND rqty=%s AND rprice=%s AND uid=%s;"
        cursor.execute(query, (rid, rprice, rqty, uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRidAndRnameAndrPriceAnduid(self, rid, rName, rprice, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rid=%s AND rName=%s AND rprice=%s AND uid=%s;"
        cursor.execute(query, (rid, rName, rprice, uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRidAndRnameAndRqtyAnduid(self, rid, rName, rqty, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rid=%s AND rName=%s AND rqty=%s AND uid=%s;"
        cursor.execute(query, (rid, rName, rqty, uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRidAndRnameAndRqtyAndrPrice(self, rid, rName, rqty, rprice):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rid=%s AND rName=%s AND rqty=%s AND rprice=%s;"
        cursor.execute(query, (rid, rName, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRnameAndrqtyAnduidAndrdid(self, rName, rqty, uid, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rName=%s AND rqty=%s AND uid=%s AND rdid=%s ;"
        cursor.execute(query, (rName, rqty, uid, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRnameAndRqtyAnduid(self, rName, rqty, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rName=%s AND rqty=%s AND uid=%s;"
        cursor.execute(query, (rName, rqty, uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRnameAndrqtyAndrprice(self, rName, rqty, rprice):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rName=%s AND rqty=%s AND rprice=%s;"
        cursor.execute(query, (rName, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRnameAndrqtyAndrdid(self, rName, rqty, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rName=%s AND rqty=%s ANd rdid=%s;"
        cursor.execute(query, (rName, rqty, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRnameAndrqty(self, rName, rqty):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rName=%s AND rqty=%s;"
        cursor.execute(query, (rName, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRnameAnduid(self, rName, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rName=%s AND uid=%s;"
        cursor.execute(query, (rName, uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRnameAndrprice(self, rName, rprice):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rName=%s AND rprice=%s;"
        cursor.execute(query, (rName, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRnameAndrdid(self, rName, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rName=%s AND rdid=%s;"
        cursor.execute(query, (rName, rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByRname(self, rName):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rName=%s;"
        cursor.execute(query, (rName,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByrqty(self, rqty):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rqty=%s;"
        cursor.execute(query, (rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByuid(self, uid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and uid=%s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByrprice(self, rprice):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rprice=%s;"
        cursor.execute(query, (rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByrdid(self, rdid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL and rdid=%s;"
        cursor.execute(query, (rdid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRid(self, rid):
        cursor = self.conn.cursor()
        query = "select * from resources where rdid IS NOT NULL AND rid=%s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

