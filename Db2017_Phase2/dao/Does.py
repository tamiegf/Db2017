from Db2017_Phase2.config.db_config import db_config
import psycopg2



class DoesDAO:

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
    def getAllDoes(self):
        cursor = self.conn.cursor()
        query = "select * from Does;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getDoesByisCustomer(self, isCustomer):
        cursor = self.conn.cursor()
        query = "select * from Does where isCustomer = %s;"
        cursor.execute(query, (isCustomer,))
        result = []
        for row in cursor:
            result.append(row)
        return result
