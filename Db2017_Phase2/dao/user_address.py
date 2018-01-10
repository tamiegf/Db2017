from Db2017_Phase2.config.db_config import db_config
import psycopg2

class userAddressDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host='localhost'" % (db_config['dbname'],
                                                            db_config['user'],
                                                            db_config['psswd'])
        self.conn = psycopg2._connect(connection_url)

    ##################### POST METHODS ##########################################
    def insert(self):
        # No hay que hacer esta parte para esta fase
        pass

    ##################### GET METHODS ##########################################
    def getAllUserAddress(self):
        cursor = self.conn.cursor()
        query = "select * from user_address;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserAddressById(self, uaid):
        cursor = self.conn.cursor()
        query = "select * from user_address where uaid = %s;"
        cursor.execute(query, (uaid,))
        result = cursor.fetchone()
        return result

    def getUserAddressWithAllAttributes(self, uacity, uaregion, uazipcode, gpsLat, gpsLong):
        cursor = self.conn.cursor()
        query = "select * from user_address where uacity=%s and uaregion=%s and uazipcode=%s and gpsLat=%s and gpsLong=%s;"
        cursor.execute(query, (uacity, uaregion, uazipcode, gpsLat, gpsLong,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserAddressWithAllAtributesExceptGpsLong(self, uacity, uaregion, uazipcode, gpsLat):
        cursor = self.conn.cursor()
        query = "select * from user_address where uacity=%s and uaregion=%s and uazipcode=%s and gpsLat=%s;"
        cursor.execute(query, (uacity, uaregion, uazipcode, gpsLat,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserAddressWithAllAtributesExceptGpsLat(self, uacity, uaregion, uazipcode, gpsLong):
        cursor = self.conn.cursor()
        query = "select * from user_address where uacity=%s and uaregion=%s and uazipcode=%s and gpsLong=%s;"
        cursor.execute(query, (uacity, uaregion, uazipcode, gpsLong,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserAddressByCityAndRegionAndZipcode(self, uacity, uaregion, uazipcode):
        cursor = self.conn.cursor()
        query = "select * from user_address where uacity=%s and uaregion=%s and uazipcode=%s;"
        cursor.execute(query, (uacity, uaregion, uazipcode,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserAddressByCityAndRegionAndGpsLat(self, uacity, uaregion, gpsLat):
        cursor = self.conn.cursor()
        query = "select * from user_address where uacity=%s and uaregion=%s and gpsLat=%s;"
        cursor.execute(query, (uacity, uaregion, gpsLat,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserAddressByCityAndRegionAndGpsLong(self, uacity, uaregion, gpsLong):
        cursor = self.conn.cursor()
        query = "select * from user_address where uacity=%s and uaregion=%s and gpsLong=%s;"
        cursor.execute(query, (uacity, uaregion, gpsLong,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserAddressByCityAndRegion(self, uacity, uaregion):
        cursor = self.conn.cursor()
        query = "select * from user_address where uacity=%s and uaregion=%s;"
        cursor.execute(query, (uacity, uaregion,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserAddressByCityAndZipCode(self, uacity, uazipcode):
        cursor = self.conn.cursor()
        query = "select * from user_address where uacity=%s and uazipcode=%s;"
        cursor.execute(query, (uacity, uazipcode,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserAddressByCityAndGpsLat(self, uacity, gpsLat):
        cursor = self.conn.cursor()
        query = "select * from user_address where uacity=%s and gpsLat=%s;"
        cursor.execute(query, (uacity, gpsLat,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserAddressByCityAndGpsLong(self, uacity, gpsLong):
        cursor = self.conn.cursor()
        query = "select * from user_address where uacity=%s and gpsLong=%s;"
        cursor.execute(query, (uacity, gpsLong,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserAddressByCity(self, uacity):
        cursor = self.conn.cursor()
        query = "select * from user_address where uacity=%s;"
        cursor.execute(query, (uacity,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserAddressByRegion(self, uaregion):
        cursor = self.conn.cursor()
        query = "select * from user_address where uaregion=%s;"
        cursor.execute(query, (uaregion,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserAddressByZipCode(self, uazipcode):
        cursor = self.conn.cursor()
        query = "select * from user_address where uazipcode=%s;"
        cursor.execute(query, (uazipcode,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserAddressByGpsLat(self, gpsLat):
        cursor = self.conn.cursor()
        query = "select * from user_address where gpsLat=%s;"
        cursor.execute(query, (gpsLat,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserAddressByGpsLong(self, gpsLong):
        cursor = self.conn.cursor()
        query = "select * from user_address where gpsLong=%s;"
        cursor.execute(query, (gpsLong,))
        result = []
        for row in cursor:
            result.append(row)
        return result


