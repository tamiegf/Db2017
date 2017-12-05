from flask import jsonify
from dao.resources import resourcesDAO

class resourcesHandler:

    # Create a dictionary of resources
    def build_resources_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rName'] = row[1]
        result['rQty'] = row[2]
        result['cid'] = row[3]
        result['price'] = row[4]
        result['RDid'] = row[5]
        return result

    # Create a dictionary of users
    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['utype'] = row[1]
        result['uName'] = row[2]
        result['address'] = row[3]
        result['city'] = row[4]
        result['county'] = row[5]
        result['zipCode'] = row[6]
        result['gpsLat'] = row[7]
        result['gpsLong'] = row[8]
        return result


    def getAllResources(self):
        dao = resourcesDAO()
        resources_list = dao.getAllResources()
        results_list = []
        for row in resources_list:
            result = self.build_resources_dict(row)
            results_list.append(result)
        return jsonify(Resources=results_list)

    def searchResources(self, args):
        rName = args.get("rName")
        rQty = args.get("rQty")
        cid = args.get("cid")
        price = args.get("price")
        RDid = args.get("RDid")
        dao = resourcesDAO()
        resource_list = []
        if (len(args) == 5) and (rName or rQty or cid or price or RDid):
            resource_list = dao.getResourceWithAllAttributes(rName, rQty, cid, price, RDid)
        elif (len(args) == 4) and (rName or rQty or cid or price):
            resource_list = dao.getResourceByRnameAndRqtyAndCidAndPrice(rName, rQty, cid, price)
        elif (len(args) == 4) and (rName or rQty or cid or RDid):
            resource_list = dao.getResourceByRnameAndRqtyAndCidAndRdid(rName, rQty, cid, RDid)
        elif (len(args) == 3) and (rName or rQty or cid):
            resource_list = dao.getResourceByRnameAndRqtyAndCid(rName, rQty, cid)
        elif (len(args) == 3) and (rName or rQty or price):
            resource_list = dao.getResourceByRnameAndRqtyAndPrice(rName, rQty, price)
        elif (len(args) == 3) and (rName or rQty or RDid):
            resource_list = dao.getResourceByRnameAndRqtyAndRdid(rName, rQty, RDid)
        elif (len(args) == 2) and (rName or rQty):
            resource_list = dao.getResourceByRnameAndRqty(rName, rQty)
        elif (len(args) == 2) and (rName or cid):
            resource_list = dao.getResourceByRnameAndCid(rName, cid)
        elif (len(args) == 2) and (rName or price):
            resource_list = dao.getResourceByRnameAndPrice(rName, price)
        elif (len(args) == 2) and (rName or RDid):
            resource_list = dao.getResourceByRnameAndRid(rName, RDid)
        elif (len(args) == 1) and rName:
            resource_list = dao.getResourceByRname(rName)
        elif (len(args) == 1) and rQty:
            resource_list = dao.getResourceByRqty(rQty)
        elif (len(args) == 1) and cid:
            resource_list = dao.getResourceByCid(cid)
        elif (len(args) == 1) and price:
            resource_list = dao.getResourceByPrice(price)
        elif (len(args) == 1) and RDid:
            resource_list = dao.getResourceByRdid(RDid)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in resource_list:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)


    def getResourcesByRid(self, rid):
        dao = resourcesDAO()
        row = dao.getResourcesByRid(rid)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            resource = self.build_resources_dict(row)
            return jsonify(Resource=resource)

    def getUserByRid(self, rid):
        dao = resourcesDAO()
        if not dao.getResourcesByRid(rid):
            return jsonify(Error="Part Not Found"), 404
        request_list = dao.getUserByRid(rid)
        result_list = []
        for row in request_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(User=result_list)

    def getCategoryByRid(self, rid):
        dao = resourcesDAO()
        if not dao.getResourcesByRid(rid):
            return jsonify(Error="Part Not Found"), 404
        request_list = dao.getCategoryByRid(rid)
        result_list = []
        for row in request_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Category=result_list)

    def getReqDetailByRid(self, rid):
        dao = resourcesDAO()
        if not dao.getResourcesByRid(rid):
            return jsonify(Error="Part Not Found"), 404
        request_list = dao.getReqDetailByRid(rid)
        result_list = []
        for row in request_list:
            result = self.build_ReqDetail_dict(row)
            result_list.append(result)
        return jsonify(RequestDeatils=result_list)

