from flask import jsonify
from dao.user import userDAO

class userHandler:

    # Create a dictionary of users
    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['uaid'] = row[1]
        result['utype'] = row[2]
        result['ufirstname'] = row[3]
        result['ulastname'] = row[4]
        return result

    def build_userAddress_dict(self, row):
        result = {}
        result['uaId'] = row[0]
        result['uaCity'] = row[1]
        result['uaRegion'] = row[2]
        result['uaZipCode'] = row[3]
        result['gpsLat'] = row[4]
        result['gpsLong'] = row[5]
        return result

    def build_resources_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['rqty'] = row[2]
        result['rprice'] = row[3]
        result['uid'] = row[4]
        result['rdid'] = row[5]
        return result

    def build_order_dict(self,row):
        result = {}
        result['rdid'] = row[0]  #request_details
        result['rname'] = row[1] #resources
        result['rdqty'] = row[2] #request_details
        result['need_date'] = row[3] #request_details
        result['delivery_date'] = row[4]#request_details
        result['ptype'] = row[5] #purchase
        return result

    def build_supplier_order_dict(self, row):
        result = {}
        result['rdid'] = row[0]
        result['rname'] = row[1]
        result['ufirstname'] = row[2]
        result['ulastname'] = row[3]
        result['rdpqty'] = row[4]
        return result

    def build_user_attributes(self, uid, utype, ufirstname, ulastname, user_name, user_password, uacity, uaregion, uazipcode, gpslat, gpslong):
        result = {}
        result['uid'] = uid
        result['utype'] = utype
        result['ufirstname'] = ufirstname
        result['ulastname'] = ulastname
        result['user_name'] = user_name
        result['user_password'] = user_password
        result['uacity'] = uacity
        result['uaregion'] = uaregion
        result['uazipcode'] = uazipcode
        result['gpslat'] = gpslat
        result['gpslong'] = gpslong
        return result


    #################### POST METHODS #############################################
    def insertUser(self, form):
        if len(form) != 10:
            return jsonify(Error = "Malformed post request"), 400
        else:
            utype = form['utype']
            ufirstname = form['ufirstname']
            ulastname = form['ulastname']
            user_name = form['user_name']
            user_password = form['user_password']
            uacity = form['uacity']
            uaregion = form['uaregion']
            uazipcode = form['uazipcode']
            gpslat = form['gpslat']
            gpslong = form['gpslong']
            if utype and ufirstname and ulastname and user_name and user_password and uacity and uaregion and uazipcode and gpslat and gpslong:
                dao = userDAO()
                uid = dao.insert(utype, ufirstname, ulastname, user_name, user_password, uacity, uaregion, uazipcode, gpslat, gpslong)
                result = self.build_user_attributes(uid, utype, ufirstname, ulastname, user_name, user_password, uacity, uaregion, uazipcode, gpslat, gpslong)
                return jsonify(User=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    ###############################################################################

    #################### GET METHODS #############################################
    def getAllUsers(self):
        dao = userDAO()
        users_list = dao.getAllUsers()
        results_list = []
        for row in users_list:
            result = self.build_user_dict(row)
            results_list.append(result)
        return jsonify(Users=results_list)

    def searchUsers(self, args):
        uid = args.get("uid")
        utype = args.get("utype")
        ufirstname = args.get("ufirstname")
        ulastname = args.get("ulastname")
        dao = userDAO()
        user_list = []
        if (len(args) == 3) and (utype or ufirstname or ulastname):
            user_list = dao.getUsersWithAllAttributes(utype, ufirstname, ulastname)
        elif (len(args) == 2) and (utype or ufirstname):
            user_list = dao.getUserByTypeAndName(utype, ufirstname)
        elif (len(args) == 2) and (utype or ulastname):
            user_list = dao.getUserByTypeAndLastName(utype, ulastname)
        elif (len(args) == 1)and utype:
            user_list = dao.getUserByType(utype)
        elif (len(args) == 1) and ufirstname:
            user_list = dao.getUserByName(ufirstname)
        elif (len(args) == 1) and ulastname:
            user_list = dao.getUserByLastName(ulastname)
        else:
            return jsonify(Error = "Malformed query string"), 400
        results_list = []
        for row in user_list:
            result = self.build_user_dict(row)
            results_list.append(result)
        return jsonify(User = results_list)

    def getUserById(self, uid):
        dao = userDAO()
        row = dao.getUserById(uid)
        if not row:
            return jsonify(Error = "User not found."), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User = user)

    def getUserAddressByUid(self, uid):
        dao = userDAO()
        if not dao.getUserById(uid):
            return jsonify(Error="Part Not Found"), 404
        suppliers_list = dao.getUserAddressByUid(uid)
        result_list = []
        for row in suppliers_list:
            result = self.build_userAddress_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getResourcesByUserSearch(self, args):
        ufirstname = args.get("ufirstname")
        ulastname = args.get("ulastname")
        dao = userDAO()
        user_list = []
        if (len(args) == 2) and (ufirstname or ulastname):
            user_list = dao.getResourceByUserFirstNameAndLastName(ufirstname, ulastname)
        elif (len(args) == 1) and ufirstname:
            user_list = dao.getResourceByUserFirstName(ufirstname)
        elif (len(args) == 1) and ulastname:
            user_list = dao.getResourceByUserLastName(ulastname)
        else:
            return jsonify(Error = "Malformed query string"), 400
        results_list = []
        for row in user_list:
            result = self.build_resources_dict(row)
            results_list.append(result)
        return jsonify(User = results_list)

    def getResourcesByUserId(self, uid):
        dao = userDAO()
        if not dao.getUserById(uid):
            return jsonify(Error="User Not Found"), 404
        suppliers_list = dao.getResourcesByUserId(uid)
        result_list = []
        for row in suppliers_list:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)


