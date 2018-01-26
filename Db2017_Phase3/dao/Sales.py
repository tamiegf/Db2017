from config.db_config import db_config
import psycopg2



class SalesDAO:
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

    def getAllSales(self):
        cursor = self.conn.cursor()
        query = "select * from Sales;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSalesBysid(self, sid):
        cursor = self.conn.cursor()
        query = "select * from Sales where sid =%s;"
        cursor.execute(query, (sid,) )
        result = []
        for row in cursor:
            result.append(row)
        return result
