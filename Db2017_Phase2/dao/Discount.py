from config.db_config import db_config
import psycopg2



class DiscountDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host = 'localhost'" % (db_config['dbname'],
                                                                               db_config['user'],
                                                                               db_config['psswd'])
        self.conn = psycopg2._connect(connection_url)

    ##################### POST METHODS ##########################################
    def insert(self):
        # No hay que hacer esta parte para esta fase
        pass

    ############################################################################

    ##################### GET METHODS ##########################################

    def getAllDiscount(self):
        cursor = self.conn.cursor()
        query = "select * from Discount;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getDiscountWithAllAttributes(self, did, dPercent, stackable):
        cursor = self.conn.cursor()
        query = "select * from Discount where did=%s and stackable=%s and dPercent=%s;"
        cursor.execute(query, (did, dPercent, stackable,))
        result = cursor.fetchone()
        return result

    def getDiscountByAllAttributesExceptdid(self, dPercent, stackable):
        cursor = self.conn.cursor()
        query = "select * from Discount where stackable=%s and dPercent=%s;"
        cursor.execute(query, (dPercent, stackable,))
        result = cursor.fetchone()
        return result


    def getDiscountByAllAttributesExceptdPercent(self, did, stackable):
        cursor = self.conn.cursor()
        query = "select * from Discount where did=%s and stackable=%s;"
        cursor.execute(query, (did, stackable,))
        result = cursor.fetchone()
        return result

    def getDiscountByAllAttributesExceptStackable(self, did, dPercent):
        cursor = self.conn.cursor()
        query = "select * from Discount where did=%s and dPercent=%s;"
        cursor.execute(query, (did, dPercent,))
        result = cursor.fetchone()
        return result

    def getDiscountBydid(self, did):
        cursor = self.conn.cursor()
        query = "select * from Discount where did=%s;"
        cursor.execute(query, (did,))
        result = cursor.fetchone()
        return result

    def getDiscountBydPercent(self, dPercent):
        cursor = self.conn.cursor()
        query = "select * from Discount where dPercent=%s;"
        cursor.execute(query, (dPercent,))
        result = cursor.fetchone()
        return result

    def getDiscountByStackable(self, stackable):
        cursor = self.conn.cursor()
        query = "select * from Discount where stackable=%s;"
        cursor.execute(query, (stackable,))
        result = cursor.fetchone()
        return result

