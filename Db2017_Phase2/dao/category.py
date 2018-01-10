from Db2017_Phase2.config.db_config import db_config
import psycopg2


class categoryDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host='localhost'" % (db_config['dbname'],
                                                            db_config['user'],
                                                            db_config['psswd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllCategory(self):
        cursor = self.conn.cursor()
        query = "select * from resource_category;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

#    def getCategoryWithAllAttributes(self, cName, cid, rid, description):
#        result = dummyDB
#        return result

    def getCategoryByAllAttributesExceptDescription(self, cid, cName, rid):
        cursor = self.conn.cursor()
        query = "select * from resource_category where cid=%s AND cname=%s AND rid=%s;"
        cursor.execute(query, (cid, cName, rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoryByAllAttributesExceptrid(self, cName, cid, cdescription):
        cursor = self.conn.cursor()
        query = "select * from resource_category where cName=%s AND cid=%s AND cdescription=%s;"
        cursor.execute(query, (cName, cid, cdescription,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoryByAllAttributesExceptcidAndcName(self, rid, cdescription):
        cursor = self.conn.cursor()
        query = "select * from resource_category where rid=%s AND cdescription=%s;"
        cursor.execute(query, (rid, cdescription,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoryByAllAttributesExceptdescriptionAndcName(self, cid, rid):
        cursor = self.conn.cursor()
        query = "select * from resource_category where cid=%s AND rid=%s;"
        cursor.execute(query, (cid, rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoryByAllAttributesExceptridAndcName(self, cid, cdescription):
        cursor = self.conn.cursor()
        query = "select * from resource_category where cid=%s AND cdescription=%s;"
        cursor.execute(query, (cid, cdescription,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoryByAllAttributesExceptridAndcid(self, cName, cdescription):
        cursor = self.conn.cursor()
        query = "select * from resource_category where cName=%s AND cdescription=%s;"
        cursor.execute(query, (cName, cdescription,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoryByAllAttributesExceptcidAndDescritption(self, cName, rid):
        cursor = self.conn.cursor()
        query = "select * from resource_category where cName=%s AND rid=%s;"
        cursor.execute(query, (cName, rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoryByAllAttributesExceptridAndDescritption(self, cName, cid):
        cursor = self.conn.cursor()
        query = "select * from resource_category where cName=%s AND cid=%s;"
        cursor.execute(query, (cName, cid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoryByAllAttributesExceptcName(self, cid, rid, cdescription):
        cursor = self.conn.cursor()
        query = "select * from resource_category where cid=%s AND rid=%s AND cdescription=%s;"
        cursor.execute(query, (cid, rid, cdescription,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoryByAllAttributesExceptcid(self, cName, rid, cdescription):
        cursor = self.conn.cursor()
        query = "select * from resource_category where cName=%s AND rid=%s AND cdescription=%s;"
        cursor.execute(query, (cName, rid, cdescription,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoryBycName(self, cName):
        cursor = self.conn.cursor()
        query = "select * from resource_category where cName=%s;"
        cursor.execute(query, (cName,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoryByrid(self, rid):
        cursor = self.conn.cursor()
        query = "select * from resource_category where rid=%s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoryBycid(self, cid):
        cursor = self.conn.cursor()
        query = "select * from resource_category where cid=%s;"
        cursor.execute(query, (cid,))
        result = cursor.fetchone()
        return result

    def getCategoryByDescription(self, cdescription):
        cursor = self.conn.cursor()
        query = "select * from resource_category where cdescription=%s;"
        cursor.execute(query, (cdescription,))
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