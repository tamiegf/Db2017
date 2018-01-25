from Db2017_Phase2.config.db_config import db_config
import psycopg2

class CreditCardDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host = 'localhost'" % (db_config['dbname'],
                                                                               db_config['user'],
                                                                               db_config['psswd'])
        self.conn = psycopg2._connect(connection_url)

#############################GET METHODS#############################################

    def getAllCategory(self):
      #  result = dummyDB
      cursor = self.conn.cursor()
      query = "select * from creditcard;"
      cursor.execute(query)
      result = []
      for row in cursor:
          result.append(row)
      return result


    def getCreditCardWithAllAttributes(self, ccNumber, cvv, ccExpirationDate):
        cursor = self.conn.cursor()
        query = "select * from creditcard where ccNumber = %s and cvv = %s and ccExpirationDate= %s;"
        cursor.execute(query, (ccNumber, cvv, ccExpirationDate,))
        result = cursor.fetchone()
        return result

    def getCreditCardByccNumber(self, ccNumber):
        cursor = self.conn.cursor()
        query = "select * from creditcard where ccNumber = %s;"
        cursor.execute(query, (ccNumber,))
        result = cursor.fetchone()
        return result

    def getCreditCardBycvv(self, cvv):
        cursor = self.conn.cursor()
        query = "select * from creditcard where cvv = %s;"
        cursor.execute(query, (cvv,))
        result = cursor.fetchone()
        return result

    def getCreditCardByExpirationDate(self, ccExpirationDate):
        cursor = self.conn.cursor()
        query = "select * from creditcard where ccExpirationDate = %s;"
        cursor.execute(query, (ccExpirationDate,))
        result = cursor.fetchone()
        return result

    def getCreditCardByCCID(self,ccid):
        cursor = self.conn.cursor()
        query = "select * from creditcard where ccid = %s;"
        cursor.execute(query, (ccid,))
        result = cursor.fetchone()
        return result
    
    ########################################################################
    ###### Metodos de insert y Update de Credit Card#######################
    
    
    ####Insert a la tabla de CreditCard
    def insert(self, uid, ccNumber, cvv, ccExpirationDate, sale):
        cursor = self.conn.cursor ()
        query = "insert into creditCard(uid,ccNumber,ccv,ccExpirationDate,sale) values (%s, %s, %s, %s, %s);"
        cursor.execute (query,(uid, ccNumber, cvv, ccExpirationDate, sale,))
        self.conn.commit ()
        return uid  
    
   ####Update a la tabla de creditCard 
    def update(self, uid, ccNumber, cvv, ccExpirationDate, sale):
        cursor = self.conn.cursor ()
        query = "update creditCard set ccNumber = %s,cvv = %s,ccExpirationDate = %s,sale = %s where uid = %s;"
        cursor.execute (query, (ccNumber, cvv, ccExpirationDate, sale, uid,))
        self.conn.commit ()
        return uid
    
    ### Delete
    ### No es necesario implementarla pero se hizo por si acaso 
    
    def delete(self, uid):
        cursor = self.conn.cursor ()
        query = "delete from creditCard where uid = %s;"
        cursor.execute (query, (uid,))
        self.conn.commit ()
        return uid
    


