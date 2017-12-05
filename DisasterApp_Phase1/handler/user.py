from flask import jsonify
from dao.user import userDAO

class userHandler:

    # Create a dictionary of users
    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['type'] = row[1]
        result['uName'] = row[2]
        result['address'] = row[3]
        result['city'] = row[4]
        result['county'] = row[5]
        result['zipCode'] = row[6]
        result['gpsLat'] = row[7]
        result['gpsLong'] = row[8]
        return result

    # Create a dictionary of request
    def build_purchase_dict(self, row):
        result = {}
        result['pid'] = row[0]
        result['reqId'] = row[1]
        result['purchaseDate'] = row[2]
        result['pqty'] = row[3]
        result['rid'] = row[4]
        result['uid'] = row[5]
        return result

    # Create a dictionary of request
    def build_resources_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rName'] = row[1]
        result['rQty'] = row[2]
        result['cid'] = row[3]
        result['price'] = row[4]
        result['RDid'] = row[5]
        return result

    def getAllUsers(self):
        dao = userDAO()
        users_list = dao.getAllUsers()
        results_list = []
        for row in users_list:
            result = self.build_user_dict(row)
            results_list.append(result)
        return jsonify(Users=results_list)

    def searchUsers(self, args):
        utype = args.get("utype")
        uName = args.get("uName")
        address = args.get("address")
        city = args.get("city")
        region = args.get("region")
        zipcode = args.get("zipcode")
        gpsLat = args.get("gpsLat")
        gpsLong = args.get("gpsLong")
        dao = userDAO()
        user_list = []
        if (len(args) == 8) and (utype or uName or address or city or region or zipcode or gpsLat or gpsLong):
            user_list = dao.getUserWithAllAttributes(utype, uName, address, city, region, zipcode, gpsLat, gpsLong)
        elif (len(args) == 7) and (utype or uName or address or city or region or zipcode or gpsLat):
            user_list = dao.getUserByAllAttributesExceptGpsLong(utype, uName, address, city, region, zipcode, gpsLat)
        elif (len(args) == 7) and (utype or uName or address or city or region or zipcode or gpsLong):
            user_list = dao.getUserByAllAttributesExceptGpsLat(utype, uName, address, city, region, zipcode, gpsLong)
        elif (len(args) == 6) and (utype or uName or address or city or region or zipcode):
            user_list = dao.getUserByAllAttributesExceptGpsLongAndGpsLat(utype, uName, address, city, region, zipcode)
        elif (len(args) == 6) and (utype or uName or address or city or region or gpsLong):
            user_list = dao.getUserByAllAttributesExceptZipcodeAndGpsLat(utype, uName, address, city, region, gpsLong)
        elif (len(args) == 6) and (utype or uName or address or city or region or gpsLat):
            user_list = dao.getUserByAllAttributesExceptGpsLongAndZipcode(utype, uName, address, city, region, gpsLat)
        elif (len(args) == 5) and (utype or uName or address or city or region):
            user_list = dao.getUserByAllAttributesExceptGpsLongAndGpsLatAndZipcode(utype, uName, address, city, region)
        elif (len(args) == 5) and (utype or uName or address or city or gpsLat):
            user_list = dao.getUserByAllAttributesExceptGpsLongAndCountyAndZipcode(utype, uName, address, city, gpsLat)
        elif (len(args) == 5) and (utype or uName or address or city or gpsLong):
            user_list = dao.getUserByAllAttributesExceptGpsLatAndCountyAndZipcode(utype, uName, address, city, gpsLong)
        elif (len(args) == 5) and (utype or uName or address or city or zipcode):
            user_list = dao.getUserByAllAttributesExceptGpsLongAndCountyAndGpsLat(utype, uName, address, city, zipcode)
        elif (len(args) == 4) and (utype or uName or address or city):
            user_list = dao.getUserBytypeAndUnameAndAddressAndCity(utype, uName, address, city)
        elif (len(args) == 4) and (utype or uName or address or zipcode):
            user_list = dao.getUserBytypeAndUnameAndAddressAndZipcode(utype, uName, address, zipcode)
        elif (len(args) == 4) and (utype or uName or address or region):
            user_list = dao.getUserBytypeAndUnameAndAddressAndCounty(utype, uName, address, region)
        elif (len(args) == 4) and (utype or uName or address or gpsLat):
            user_list = dao.getUserBytypeAndUnameAndAddressAndGpsLat(utype, uName, address, gpsLat)
        elif (len(args) == 4) and (utype or uName or address or gpsLong):
            user_list = dao.getUserBytypeAndUnameAndAddressAndCity(utype, uName, address, gpsLong)
        elif (len(args) == 3) and (utype or uName or address):
            user_list = dao.getUserBytypeAndUnameAndAddress(utype, uName, address)
        elif (len(args) == 3) and (utype or uName or city):
            user_list = dao.getUserBytypeAndUnameAndCity(utype, uName, city)
        elif (len(args) == 3) and (utype or uName or region):
            user_list = dao.getUserBytypeAndUnameAndAddress(utype, uName, region)
        elif (len(args) == 3) and (utype or uName or zipcode):
            user_list = dao.getUserBytypeAndUnameAndZipcode(utype, uName, zipcode)
        elif (len(args) == 3) and (utype or uName or gpsLat):
            user_list = dao.getUserBytypeAndUnameAndGpsLat(utype, uName, gpsLat)
        elif (len(args) == 3) and (utype or uName or gpsLong):
            user_list = dao.getUserBytypeAndUnameAndGpsLong(utype, uName, gpsLong)
        elif (len(args) == 2) and (utype or uName):
            user_list = dao.getUserBytypeAndUname(utype, uName)
        elif (len(args) == 2) and (utype or address):
            user_list = dao.getUserBytypeAndAddress(utype, address)
        elif (len(args) == 2) and (utype or city):
            user_list = dao.getUserBytypeAndCity(utype, city)
        elif (len(args) == 2) and (utype or region):
            user_list = dao.getUserBytypeAndCounty(utype, region)
        elif (len(args) == 2) and (utype or zipcode):
            user_list = dao.getUserBytypeandZipcode(utype, zipcode)
        elif (len(args) == 2) and (utype or gpsLat):
            user_list = dao.getUserBytypeAndGpsLat(utype, gpsLat)
        elif (len(args) == 2) and (utype or gpsLong):
            user_list = dao.getUserBytypeAndGpsLong(utype, gpsLong)
        elif (len(args) == 1) and utype:
            user_list = dao.getUserByType(utype)
        elif (len(args) == 1) and uName:
            user_list = dao.getUserByUname(uName)
        elif (len(args) == 1) and address:
            user_list = dao.getUserByAdress(address)
        elif (len(args) == 1) and city:
            user_list = dao.getUserByCity(city)
        elif (len(args) == 1) and region:
            user_list = dao.getUserByCounty(region)
        elif (len(args) == 1) and zipcode:
            user_list = dao.getUserByZipcode(zipcode)
        elif (len(args) == 1) and gpsLat:
            user_list = dao.getUserByGpsLat(gpsLat)
        elif (len(args) == 1) and gpsLong:
            user_list = dao.getUserByGpsLong(gpsLong)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in user_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(User=result_list)

    def getUserByUid(self, uId):
        dao = userDAO()
        row = dao.getUserByUid(uId)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User=user)

    def getRequestByUserId(self, uId):
        dao = userDAO()
        if not dao.getUserByUid(uId):
            return jsonify(Error="Part Not Found"), 404
        request_list = dao.getRequestByUserId(uId)
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Request=result_list)

    def getPurchaseByUserId(self, uId):
        dao = userDAO()
        if not dao.getUserByUid(uId):
            return jsonify(Error="Part Not Found"), 404
        request_list = dao.getPurchaseByUserId(uId)
        result_list = []
        for row in request_list:
            result = self.build_purchase_dict(row)
            result_list.append(result)
        return jsonify(Request=result_list)

    def getResourcesByUserId(self, uId):
        dao = userDAO()
        if not dao.getUserByUid(uId):
            return jsonify(Error="Part Not Found"), 404
        request_list = dao.getResourcesByUserId(uId)
        result_list = []
        for row in request_list:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Request=result_list)


