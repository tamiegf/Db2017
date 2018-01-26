from config.db_config import db_config
import psycopg2

class userLoginDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (db_config['dbname'],
                                                            db_config['user'],
                                                            db_config['psswd'])
        self.conn = psycopg2._connect(connection_url)

    ##################### GET METHODS ##########################################

    def getAllUserLogin(self):
        cursor = self.conn.cursor()
        query = "select * from user_login;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserLoginByNameAndPassword(self, user_name, user_password):
        cursor = self.conn.cursor()
        query = "select * from user_login where user_name=%s and user_password=%s;"
        cursor.execute(query, (user_name, user_password, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserLoginByName(self, user_name):
        cursor = self.conn.cursor()
        query = "select * from user_login where user_name=%s;"
        cursor.execute(query, (user_name, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserLoginByPassword(self, user_password):
        cursor = self.conn.cursor()
        query = "select * from user_login where user_password=%s;"
        cursor.execute(query, (user_password,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserLoginByUid(self, uid):
        cursor = self.conn.cursor()
        query = "select * from user_login where uid=%s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result;