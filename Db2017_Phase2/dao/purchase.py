from Db2017_Phase2.config.db_config import db_config
import psycopg2


class purchaseDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (db_config['dbname'],
                                                            db_config['user'],
                                                            db_config['psswd'])
        self.conn = psycopg2._connect(connection_url)

    ##################### POST METHODS ##########################################
    def insert(self):
        # No hay que hacer esta parte para esta fase
        pass

    #############################################################################

    #################### GET METHODS ############################################
    def getAllPurchases(self):
        cursor = self.conn.cursor()
        query = "select * from purchase;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchaseById(self, pid):
        cursor = self.conn.cursor()
        query = "select * from purchase where pid = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        return result

    def getPurchaseByDateAndQty(self, pdate, pqty):
        cursor = self.conn.cursor()
        query = "select * from purchase where pdate = %s and pqty = %s;"
        cursor.execute(query, (pdate, pqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchaseByDate(self, pdate):
        cursor = self.conn.cursor()
        query = "select * from purchase where pdate = %s;"
        cursor.execute(query, (pdate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchaseByQty(self, pqty):
        cursor = self.conn.cursor()
        query = "select * from purchase where pqty = %s;"
        cursor.execute(query, (pqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchaseByDateAndQtyAndType(self, pdate, pqty, ptype):
        cursor = self.conn.cursor()
        query = "select * from purchase where pdate = %s and pqty = %s and ptype = %s;"
        cursor.execute(query, (pdate, pqty, ptype, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchaseByDateAndType(self, pdate, ptype):
        cursor = self.conn.cursor()
        query = "select * from purchase where pdate = %s and ptype = %s;"
        cursor.execute(query, (pdate, ptype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchaseByType(self, ptype):
        cursor = self.conn.cursor()
        query = "select * from purchase where ptype = %s;"
        cursor.execute(query, (ptype,))
        result = []
        for row in cursor:
            result.append(row)
        return result


