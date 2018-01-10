from flask import jsonify
from dao.resource_location import resourceLocationDAO

class resourceLocationHandler:

    # Create a dictionary of users
    def build_resource_location_dict(self, row):
        result = {}
        result['rlid'] = row[0]
        result['rcity'] = row[1]
        result['rregion'] = row[2]
        result['rid'] = row[3]
        return result

    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['rqty'] = row[2]
        result['rprice'] = row[3]
        return result

    #################### POST METHODS #############################################
    def insertResourceLocation(self, form):
        # No hay que hacerlo para esta fase
        pass

    ###############################################################################

    #################### GET METHODS #############################################
    def getAllResourceLocation(self):
        dao = resourceLocationDAO()
        rlocation_list = dao.getAllResourceLocation()
        results_list = []
        for row in rlocation_list:
            result = self.build_resource_location_dict(row)
            results_list.append(result)
        return jsonify(Users=results_list)

    def searchResourceLocation(self, args):
        rlid = args.get("rlid")
        rcity = args.get("rcity")
        rregion = args.get("rregion")
        rid = args.get("rid")
        dao = resourceLocationDAO()
        user_list = []
        if(len(args) == 2) and (rcity or rregion):
            user_list = dao.getRLWithAllAttributes(rcity, rregion)
        elif(len(args) == 1) and rcity:
            user_list = dao.getRLByCity(rcity)
        elif(len(args) == 1) and rregion:
            user_list = dao.getRLByRegion(rregion)
        else:
            return jsonify(Error = "Malformed query string"), 400
        results_list = []
        for row in user_list:
            result = self.build_resource_location_dict(row)
            results_list.append(result)
        return jsonify(User = results_list)

    def getResourceLocationById(self, rlid):
        dao = resourceLocationDAO()
        row = dao.getResourceLocationById(rlid)
        if not row:
            return jsonify(Error="User not found."), 404
        else:
            user = self.build_resource_location_dict(row)
            return jsonify(User=user)

    def getresourceByResourceLocationSearch(self, args):
        rcity = args.get("rcity")
        rregion = args.get("rregion")
        dao = resourceLocationDAO()
        user_list = []
        if (len(args) == 2) and (rcity or rregion):
            user_list = dao.getResourceByResourceLocationAndCity(rcity, rregion)
        elif (len(args) == 1) and rcity:
            user_list = dao.getResourceByResourceCity(rcity)
        elif (len(args) == 1) and rregion:
            user_list = dao.getResourceByResourceregion(rregion)
        else:
            return jsonify(Error="Malformed query string"), 400
        results_list = []
        for row in user_list:
            result = self.build_resource_dict(row)
            results_list.append(result)
        return jsonify(User=results_list)


