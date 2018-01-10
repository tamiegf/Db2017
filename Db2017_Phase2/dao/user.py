from Db2017_Phase2.config.db_config import db_config
import psycopg2

class userDAO:

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
    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByTypeAndName(self, utype, ufirstname):
        cursor = self.conn.cursor()
        query = "select * from users where utype = %s and ufirstname = %s;"
        cursor.execute(query, (utype, ufirstname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByType(self, utype):
        cursor = self.conn.cursor()
        query = "select * from users where utype = %s;"
        cursor.execute(query, (utype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByName(self, ufirstname):
        cursor = self.conn.cursor()
        query = "select * from users where ufirstname = %s;"
        cursor.execute(query, (ufirstname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, uid):
        cursor = self.conn.cursor()
        query = "select * from users where uid = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result

    def getUsersWithAllAttributes(self, utype, ufirstname, ulastname):
        cursor = self.conn.cursor()
        query = "select * from users where utype = %s and ufirstname = %s and ulastname = %s;"
        cursor.execute(query, (utype, ufirstname, ulastname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByTypeAndLastName(self, utype, ulastname):
        cursor = self.conn.cursor()
        query = "select * from users where utype = %s and ulastname = %s;"
        cursor.execute(query, (utype, ulastname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByLastName(self, ulastname):
        cursor = self.conn.cursor()
        query = "select * from users where ulastname = %s;"
        cursor.execute(query, (ulastname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserAddressByUid(self, uid):
        cursor = self.conn.cursor()
        query = "select uaid, uacity, uaregion, uazipcode, gpslat, gpslong from user_address natural inner join users where uid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByUserFirstNameAndLastName(self, ufirstname, ulastname):
        cursor = self.conn.cursor()
        query = "select rid, rname, rqty, rprice, uid, rdid from resources natural inner join users where utype = 'supplier' and ufirstname = %s and ulastname = %s;"
        cursor.execute(query, (ufirstname, ulastname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByUserFirstName(self, ufirstname):
        cursor = self.conn.cursor()
        query = "select rid, rname, rqty, rprice, uid, rdid from resources natural inner join users where utype = 'supplier' and ufirstname = %s ;"
        cursor.execute(query, (ufirstname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByUserLastName(self, ulastname):
        cursor = self.conn.cursor()
        query = "select rid, rname, rqty, rprice, uid, rdid from resources natural inner join users where utype = 'supplier' and ulastname = %s ;"
        cursor.execute(query, (ulastname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByUserId(self, uid):
        cursor = self.conn.cursor()
        query = "select rid, rname, rqty, rprice, uid, rdid from resources natural inner join users where utype = 'supplier' and uid = %s ;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result





