# from config.dbconfig import pg_config
# import psycopg2


# dummyDB is a dummy array that simulates a database. This is for Phase1 purposes.
dummyDB = [["1", "gas", "12", "Combustion"]]

class categoryDAO:

    # This is an implementation for a future phase of the project
    # def __init__(self):
    #     connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
    #                                                         pg_config['user'],
    #                                                         pg_config['psswd'])
    #     self.conn = psycopg2._connect(connection_url)

    def getAllCategory(self):
        result = dummyDB
        return result

    def getCategoryWithAllAttributes(self, cName, cid, rid, description):
        result = dummyDB
        return result

    def getCategoryByAllAttributesExceptDescription(self, cid, cName, rid):
        result = dummyDB
        return result

    def getCategoryByAllAttributesExceptrid(self, cName, cid, description):
        result = dummyDB
        return result

    def getCategoryByAllAttributesExceptcidAndcName(self, rid, description):
        result = dummyDB
        return result

    def getCategoryByAllAttributesExceptdescriptionAndcName(self, cid, rid):
        result = dummyDB
        return result

    def getCategoryByAllAttributesExceptridAndcName(self, cid, description):
        result = dummyDB
        return result

    def getCategoryByAllAttributesExceptridAndcid(self, cName, description):
        result = dummyDB
        return result

    def getCategoryByAllAttributesExceptcidAndDescritption(self, cName, rid):
        result= dummyDB
        return result

    def getCategoryByAllAttributesExceptridAndDescritption(self, cName, cid):
        result = dummyDB
        return result

    def getCategoryByAllAttributesExceptcName(self, cid, rid, description):
        result= dummyDB
        return result

    def getCategoryByAllAttributesExceptcid(self, cName, rid, description):
        result = dummyDB
        return result

    def getCategoryBycName(self, cName):
        result = dummyDB
        return result

    def getCategoryByrid(self, rid):
        result = dummyDB
        return result

    def getCategoryBycid(self, cid):
        result = dummyDB
        return result

    def getCategoryByDescription(self, description):
        result = dummyDB
        return result