# from config.dbconfig import pg_config
# import psycopg2

# dummyDB is a dummy array that simulates a database. This is for Phase1 purposes.
dummyDB = [["1", "customer", "Jan Li", "PO BOX 231", "Mayaguez", "Mayaguez", "00680", "-14.45", "26.23", "1"]]

class userDAO:

    # This is an implementation for a future phase of the project
    # def __init__(self):
    #     connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
    #                                                         pg_config['user'],
    #                                                         pg_config['psswd'])
    #     self.conn = psycopg2._connect(connection_url)

    def getAllUsers(self):
        result = dummyDB
        return result

    def getUserWithAllAttributes(self, type, uName, address, city, county, zipcode, gpsLat, gpsLong, uid):
        result = dummyDB
        return result

    def getUserByAllAttributesExceptGpsLong(self, type, uName, address, city, county, zipcode, gpsLat, uid):
        result = dummyDB
        return result

    def getUserWithAllAttributesExceptUid(self, utype, uName, address, city, region, zipcode, gpsLat, gpsLong):
        result = dummyDB
        return result

    def getUserByAllAttributesExceptGpsLat(self, type, uName, address, city, county, zipcode, gpsLong):
        result = dummyDB
        return result

    def getUserWithAllAttributesExceptGpsLong(self, utype, uName, address, city, region, zipcode, gpsLat, gpsLong):
        result = dummyDB
        return result

    def getUserByAllAttributesExceptUid(self, utype, uName, address, city, region, zipcode, uid):
        result = dummyDB
        return result

    def getUserByAllAttributesExceptGpsLongAndGpsLat(self, type, uName, address, city, county, zipcode):
        result = dummyDB
        return result

    def getUserByAllAttributesExceptZipcodeAndGpsLat(self, type, uName, address, city, county, gpsLong):
        result = dummyDB
        return result

    def getUserByAllAttributesExceptGpsLongAndZipcode(self, type, uName, address, city, county, gpsLat):
        result = dummyDB
        return result

    def getUserByAllAttributesExceptGpsLongAndUid(self, utype, uName, address, city, region, uid):
        result = dummyDB
        return result

    def getUserByAllAttributesExceptGpsLongAndGpsLatAndZipcode(self, type, uName, address, city, county):
        result = dummyDB
        return result

    def getUserByAllAttributesExceptGpsLongAndCountyAndZipcode(self, type, uName, address, city, gpsLat):
        result = dummyDB
        return result

    def getUserByAllAttributesExceptGpsLatAndCountyAndZipcode(self, type, uName, address, city, gpsLong):
        result = dummyDB
        return result

    def getUserByAllAttributesExceptGpsLongAndCountyAndGpsLat(self, type, uName, address, city, zipcode):
        result = dummyDB
        return result

    def getUserByAllAttributesExceptGpsLongAndCountyAndUid(self, utype, uName, address, city, uid):
        result = dummyDB
        return result

    def getUserBytypeAndUnameAndAddressAndCity(self, type, uName, address, city):
        result = dummyDB
        return result

    def getUserBytypeAndUnameAndAddressAndZipcode(self, type, uName, address, zipcode):
        result = dummyDB
        return result

    def getUserBytypeAndUnameAndAddressAndCounty(self, type, uName, address, county):
        result = dummyDB
        return result

    def getUserBytypeAndUnameAndAddressAndGpsLat(self, type, uName, address, gpsLat):
        result = dummyDB
        return result

    def getUserBytypeAndUnameAndAddressAndgpsLong(self, utype, uName, address, gpsLong):
        result = dummyDB
        return result

    def getUserBytypeAndUnameAndAddressAndUid(self, utype, uName, address, uid):
        result = dummyDB
        return result

    def getUserBytypeAndUnameAndAddress(self, type, uName, address):
        result = dummyDB
        return result

    def getUserBytypeAndUnameAndCity(self, type, uName, city):
        result = dummyDB
        return result

    def getUserBytypeAndUnameAndZipcode(self, type, uName, zipcode):
        result = dummyDB
        return result

    def getUserBytypeAndUnameAndGpsLat(self, type, uName, gpsLat):
        result = dummyDB
        return result

    def getUserBytypeAndUnameAndGpsLong(self, type, uName, gpsLong):
        result = dummyDB
        return result

    def getUserBytypeAndUnameAndUid(self, utype, uName, uid):
        result = dummyDB
        return result

    def getUserBytypeAndUid(self, utype, uid):
        result = dummyDB
        return result

    def getUserBytypeAndUname(self, type, uName):
        result = dummyDB
        return result

    def getUserBytypeAndAddress(self, type, address):
        result = dummyDB
        return result

    def getUserBytypeAndCity(self, type, city):
        result = dummyDB
        return result

    def getUserBytypeAndCounty(self, type, county):
        result = dummyDB
        return result

    def getUserBytypeandZipcode(self, type, zipcode):
        result = dummyDB
        return result

    def getUserBytypeAndGpsLat(self, type, gpsLat):
        result = dummyDB
        return result

    def getUserBytypeAndGpsLong(self, type, gpsLong):
        result = dummyDB
        return result

    def getUserByType(self, type):
        result = dummyDB
        return result

    def getUserByUname(self, uName):
        result = dummyDB
        return result

    def getUserByAdress(self, address):
        result = dummyDB
        return result

    def getUserByCity(self, city):
        result = dummyDB
        return result

    def getUserByCounty(self, county):
        result = dummyDB
        return result

    def getUserByZipcode(self, zipcode):
        result = dummyDB
        return result

    def getUserByGpsLat(self, gpsLat):
        result = dummyDB
        return result

    def getUserByGpsLong(self, gpsLong):
        result = dummyDB
        return result

    def getUserByUid(self, uId):
        result = ["1", "customer", "Jan Li", "PO BOX 231", "Mayaguez", "Mayaguez", "00680", "-14.45", "26.23"]
        return result

    def getRequestByUserId(self, uId):
        result = dummyDB
        return result

    def getPurchaseByUserId(self, uId):
        result = dummyDB
        return result

    def getResourcesByUserId(self, uId):
        result = dummyDB
        return result