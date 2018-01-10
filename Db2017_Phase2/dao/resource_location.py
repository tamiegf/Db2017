from Db2017_Phase2.config.db_config import db_config
import psycopg2

class resourceLocationDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (db_config['dbname'],
                                                            db_config['user'],
                                                            db_config['psswd'])
        self.conn = psycopg2._connect(connection_url)

    ##################### POST METHODS ##########################################
    def insert(self):
        # No hay que hacer esta parte para esta fase
        pass

    ############################################################################

    ##################### GET METHODS ##########################################
    def getAllResourceLocation(self):
        cursor = self.conn.cursor()
        query = "select * from resource_location;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRLWithAllAttributes(self, rcity, rregion):
        cursor = self.conn.cursor()
        query = "select * from resource_location where rcity = %s and rregion =%s;"
        cursor.execute(query, (rcity, rregion,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRLByCity(self, rcity):
        cursor = self.conn.cursor()
        query = "select * from resource_location where rcity = %s;"
        cursor.execute(query, (rcity,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRLByRegion(self, rregion):
        cursor = self.conn.cursor()
        query = "select * from resource_location where rregion = %s;"
        cursor.execute(query, (rregion,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceLocationById(self, rlid):
        cursor = self.conn.cursor()
        query = "select * from resource_location where rlid = %s;"
        cursor.execute(query, (rlid,))
        result = cursor.fetchone()
        return result

    def getResourceByResourceLocationAndCity(self, rcity, rregion):
        cursor = self.conn.cursor()
        query = "select rid,rname,rqty,rprice from resources natural inner join resource_location where rcity = %s and rregion = %s;"
        cursor.execute(query, (rcity, rregion, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByResourceCity(self, rcity):
        cursor = self.conn.cursor()
        query = "select rid,rname,rqty,rprice from resources natural inner join resource_location where rcity = %s;"
        cursor.execute(query, (rcity,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByResourceregion(self, rregion):
        cursor = self.conn.cursor()
        query = "select rid,rname,rqty,rprice from resources natural inner join resource_location where rregion = %s;"
        cursor.execute(query, (rregion,))
        result = []
        for row in cursor:
            result.append(row)
        return result