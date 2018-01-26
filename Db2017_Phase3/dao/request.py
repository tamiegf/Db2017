from config.db_config import db_config
import psycopg2

class requestDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host='localhost'" % (db_config['dbname'],
                                                            db_config['user'],
                                                            db_config['psswd'])
        self.conn = psycopg2._connect(connection_url)


    def getAllRequest(self):
        cursor = self.conn.cursor()
        query = "select * from request;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getRequestWithAllAttributesExceptreqDate(self, reqId, uid):
        cursor = self.conn.cursor()
        query = "select * from request where reqId=%s AND uid=%s;"
        cursor.execute(query, (reqId, uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestWithAllAttributesExceptuid(self, reqId, reqDate):
        cursor = self.conn.cursor()
        query = "select * from request where reqId=%s AND reqDate=%s;"
        cursor.execute(query, (reqId, reqDate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestWithAllAttributesExceptreqId(self, uid, reqDate):
        cursor = self.conn.cursor()
        query = "select * from request where uid=%s AND reqDate=%s;"
        cursor.execute(query, (uid, reqDate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByreqId(self, reqId):
        cursor = self.conn.cursor()
        query = "select * from request where reqId=%s;"
        cursor.execute(query, (reqId,))
        result = cursor.fetchone()
        return result

    def getRequestByuid(self, uid):
        cursor = self.conn.cursor()
        query = "select * from request where uid=%s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByreqDate(self, reqDate):
        cursor = self.conn.cursor()
        query = "select * from request where reqDate=%s;"
        cursor.execute(query, (reqDate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, reqdate, uid):
        cursor = self.conn.cursor()
        query = "insert into request(reqdate, uid) values (%s, %s) returning reqid;"
        cursor.execute(query, (reqdate, uid,))
        reqid = cursor.fetchone()[0]
        self.conn.commit()
        return reqid