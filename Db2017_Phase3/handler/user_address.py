from flask import jsonify
from dao.user_address import userAddressDAO

class userAddressHandler:

    # Create a dictionary of users
    def build_userAddress_dict(self, row):
        result = {}
        result['uaId'] = row[0]
        result['uaCity'] = row[1]
        result['uaRegion'] = row[2]
        result['uaZipCode'] = row[3]
        result['gpsLat'] = row[4]
        result['gpsLong'] = row[5]
        return result

    #################### GET METHODS #############################################
    def getAllUserAddress(self):
        dao = userAddressDAO()
        userAddress_list = dao.getAllUserAddress()
        results_list = []
        for row in userAddress_list:
            result = self.build_userAddress_dict(row)
            results_list.append(result)
        return jsonify(User_Address=results_list)

    def searchUserAddress(self, args):
        uaid = args.get("uaid")
        uacity = args.get("uacity")
        uaregion = args.get("uaregion")
        uazipcode = args.get("uazipcode")
        gpsLat = args.get("gpsLat")
        gpsLong = args.get("gpsLong")
        dao = userAddressDAO()
        user_address_list = []
        if (len(args) == 5) and (uacity or uaregion or uazipcode or gpsLat or gpsLong):
            user_address_list = dao.getUserAddressWithAllAttributes(uacity, uaregion, uazipcode, gpsLat, gpsLong)
        elif (len(args) == 4) and (uacity or uaregion or uazipcode or gpsLat):
            user_address_list = dao.getUserAddressWithAllAtributesExceptGpsLong(uacity, uaregion, uazipcode, gpsLat)
        elif (len(args) == 4) and (uacity or uaregion or uazipcode or gpsLong):
            user_address_list = dao.getUserAddressWithAllAtributesExceptGpsLat(uacity, uaregion, uazipcode, gpsLong)
        elif (len(args) == 3) and (uacity or uaregion or uazipcode):
            user_address_list = dao.getUserAddressByCityAndRegionAndZipcode(uacity, uaregion, uazipcode)
        elif (len(args) == 3) and (uacity or uaregion or gpsLat):
            user_address_list = dao.getUserAddressByCityAndRegionAndGpsLat(uacity, uaregion, gpsLat)
        elif (len(args) == 3) and (uacity or uaregion or gpsLong):
            user_address_list = dao.getUserAddressByCityAndRegionAndGpsLong(uacity, uaregion, gpsLong)
        elif (len(args) == 2) and (uacity or uaregion):
            user_address_list = dao.getUserAddressByCityAndRegion(uacity, uaregion)
        elif (len(args) == 2) and (uacity or uazipcode):
            user_address_list = dao.getUserAddressByCityAndZipCode(uacity, uazipcode)
        elif (len(args) == 2) and (uacity or gpsLat):
            user_address_list = dao.getUserAddressByCityAndGpsLat(uacity, gpsLat)
        elif (len(args) == 2) and (uacity or gpsLong):
            user_address_list = dao.getUserAddressByCityAndGpsLong(uacity, gpsLong)
        elif (len(args) == 1) and uacity:
            user_address_list = dao.getUserAddressByCity(uacity)
        elif (len(args) == 1) and uaregion:
            user_address_list = dao.getUserAddressByRegion(uaregion)
        elif (len(args) == 1) and uazipcode:
            user_address_list = dao.getUserAddressByZipCode(uazipcode)
        elif (len(args) == 1) and gpsLat:
            user_address_list = dao.getUserAddressByGpsLat(gpsLat)
        elif (len(args) == 1) and gpsLong:
            user_address_list = dao.getUserAddressByGpsLong(gpsLong)
        else:
            return jsonify(Error = "Malformed query string"), 400
        results_list = []
        for row in user_address_list:
            result = self.build_userAddress_dict(row)
            results_list.append(result)
        return jsonify(User_Address = results_list)

    def getUserAddressById(self, uaid):
        dao = userAddressDAO()
        row = dao.getUserAddressById(uaid)
        if not row:
            return jsonify(Error = "User Address not found."), 404
        else:
            userAddress = self.build_userAddress_dict(row)
            return jsonify(User = userAddress)

    #################### POST METHODS #############################################
    def insertUserAddress(self, form):
        # No hay que hacerlo para esta fase
        pass