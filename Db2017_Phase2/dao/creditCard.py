from config.db_config import db_config
import psycopg2

class CreditCardDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host = 'localhost'" % (db_config['dbname'],
                                                                               db_config['user'],
                                                                               db_config['psswd'])
        self.conn = psycopg2._connect(connection_url)


################################POST METHODS###########################################
    def insert(self):
        # No hay que hacer esta parte para esta fase
        pass
######################################################################################

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
    #def getCreditCardByAllAttributesExceptCCID(self, ccNumber, cvv, ccExpirationDate):
      #  result = dummyDB
       # return result

   # def getCreditCardByAllAttributesExceptExpirationDate(self,ccid, ccNumber, cvv):
      #  result = dummyDB
       # return result

   # def getCreditCardByAllAttributesExceptCVV(self, ccid, ccNumber, ccExpirationDate):
    #    result = dummyDB
     #   return result

   # def getCreditCardByAllAttributesExceptccNumber(self, ccid, cvv, ccExpirationDate):
    #    result = dummyDB
      #  return result

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


