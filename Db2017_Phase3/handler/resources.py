from flask import jsonify
from dao.resources import resourcesDAO
from dao.resource_location import resourceLocationDAO
from dao.category import categoryDAO

class resourcesHandler:

    # Create a dictionary of resources
    def build_resources_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rName'] = row[1]
        result['rqty'] = row[2]
        result['uid'] = row[4]
        result['rprice'] = row[3]
        result['rdid'] = row[5]
        return result

    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['uaid'] = row[1]
        result['utype'] = row[2]
        result['ufirstname'] = row[3]
        result['ulastname'] = row[4]
        return result

    def build_supplier_order_dict(self, row):
        result = {}
        result['rdid'] = row[0]
        result['rname'] = row[1]
        result['ufirstname'] = row[2]
        result['ulastname'] = row[3]
        result['rdpqty'] = row[4]
        return result

    def build_free_free_resource_attributes(self, user_name, user_password, rname, rqty, cname, cdescription, rid, rcity, rregion):
        result = {}
        result['user_name'] = user_name
        result['user_password'] = user_password
        result['rname'] = rname
        result['rqty'] = rqty
        result['cname'] = cname
        result['cdescription'] = cdescription
        result['rid'] = rid
        result['rcity'] = rcity
        result['rregion'] = rregion
        return result

    def build_resources_attributes(self, rid, rname, rprice, rqty, rdid, uid):
        result = {}
        result['rid'] = rid
        result['rName'] = rname
        result['rqty'] = rqty
        result['uid'] = uid
        result['rprice'] = rprice
        result['rdid'] = rdid
        return result

    def build_resources_cat_attributes(self, cid, cname, cdescription, rid):
        result = {}
        result['cid'] = cid
        result['cname'] = cname
        result['cdescription'] = cdescription
        result['rid'] = rid
        return result

    def build_resources_location_attributes(self, rlid, rcity, rregion, rid):
        result = {}
        result['rlid'] = rlid
        result['rcity'] = rcity
        result['rregion'] = rregion
        result['rid'] = rid
        return result

############################## POST METHODS ############################################################
    def insertFreeResource(self, form):
        if len(form) != 8:
            return jsonify(Error = "Malformed post request"), 400
        else:
            user_name = form['user_name']
            user_password = form['user_password']
            rname = form['rname']
            rqty = form['rqty']
            cname = form['cname']
            cdescription = form['cdescription']
            rcity = form['rcity']
            rregion = form['rregion']
            if user_name and user_password and rname and rqty and cname and cdescription and rcity and rregion:
                dao = resourcesDAO()
                rid = dao.insertFreeResource(user_name, user_password, rname, rqty, cname, cdescription, rcity, rregion)
                if not rid:
                    return jsonify(Error="Unexpected Error"), 400
                else:
                    result = self.build_free_free_resource_attributes(user_name, user_password, rname, rqty, cname, cdescription, rid, rcity, rregion)
                    return jsonify(Resource=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertResource(self, form):
        if len(form) != 9:
            return jsonify(Error="Malformed post request"), 400
        else:
            rname = form['rname']
            rprice = form['rprice']
            rqty = form['rqty']
            rdid = form['rdid']
            uid = form['uid']
            rcity = form['rcity']
            rregion = form['rregion']
            cname = form['cname']
            cdescription = form['cdescription']
            if rname and rprice and rqty and uid and rcity and rregion and cname and cdescription:
                dao = resourcesDAO()
                rid = dao.insert(rname, rqty, rprice, rdid, uid)
                rlid = resourceLocationDAO().insert(rcity, rregion, rid)
                cid = categoryDAO().insert(cname, cdescription, rid)
                result = self.build_resources_attributes(rid, rname, rprice, rqty, rdid, uid)
                res1 = self.build_resources_cat_attributes(cid, cname, cdescription, rid)
                res2 = self.build_resources_location_attributes(rlid, rcity, rregion, rid)
                return jsonify(Resource=result, Category=res1, ResourceLocation=res2), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

############################## PUT METHODS ############################################################

    def updateResource(self, rid, form):
        dao = resourcesDAO()
        if not dao.getResourcesByRid(rid):
            return jsonify(Error="Resource not found."), 404
        else:
            if len(form) > 5:
                return jsonify(Error="Malformed update request"), 400
            else:
                if (len(form) == 5):
                    rname = form['rname']
                    rprice = form['rprice']
                    rqty = form['rqty']
                    rdid = form['rdid']
                    uid = form['uid']
                    if rname and rprice and rqty and rdid and uid:
                        dao = resourcesDAO()
                        dao.updateall(rid, rname, rprice, rqty, rdid, uid)
                        result = self.build_resources_attributes(rid, rname, rprice, rqty, rdid, uid)
                        return jsonify(Resource=result), 200
                    else:
                        return jsonify(Error="Unexpected attributes in update request"), 400
                elif len(form) == 2:
                    if ('rprice' in form) and ('rqty' in form):
                        rprice = form['rprice']
                        rqty = form['rqty']
                        if rprice and rqty:
                            dao = resourcesDAO()
                            attlist = dao.updaterpriceAndrqty(rid, rprice, rqty)
                            res = attlist.pop(0)
                            rname = res[0]
                            uid = res[1]
                            rdid = res[2]
                            result = self.build_resources_attributes(rid, rname, rprice, rqty, rdid, uid)
                            return jsonify(Resource=result), 200
                    else:
                        return jsonify(Error="Unexpected attributes in update request"), 400
                elif len(form) == 1:
                    if 'rprice' in form:
                        rprice = form['rprice']
                        if rprice:
                            dao = resourcesDAO()
                            attlist = dao.updaterprice(rid, rprice)
                            res = attlist.pop(0)
                            rname = res[0]
                            uid = res[1]
                            rdid = res[2]
                            rqty = res[3]
                            result = self.build_resources_attributes(rid, rname, rprice, rqty, rdid, uid)
                            return jsonify(Resource=result), 200
                    elif 'rqty' in form:
                        rqty = form['rqty']
                        if rqty:
                            dao = resourcesDAO()
                            attlist = dao.updaterqty(rid, rqty)
                            res = attlist.pop(0)
                            rname = res[0]
                            uid = res[1]
                            rdid = res[2]
                            rprice = res[3]
                            result = self.build_resources_attributes(rid, rname, rprice, rqty, rdid, uid)
                            return jsonify(Resource=result), 200
                    elif 'rdid' in form:
                        rdid = form['rdid']
                        if rdid:
                            dao = resourcesDAO()
                            attlist = dao.updaterdid(rid, rdid)
                            res = attlist.pop(0)
                            rname = res[0]
                            uid = res[1]
                            rqty = res[2]
                            rprice = res[3]
                            result = self.build_resources_attributes(rid, rname, rprice, rqty, rdid, uid)
                            return jsonify(Resource=result), 200
                    elif 'rname' in form:
                        rname = form['rname']
                        if rname:
                            dao = resourcesDAO()
                            attlist = dao.updatername(rid, rname)
                            res = attlist.pop(0)
                            rdid = res[0]
                            uid = res[1]
                            rqty = res[2]
                            rprice = res[3]
                            result = self.build_resources_attributes(rid, rname, rprice, rqty, rdid, uid)
                            return jsonify(Resource=result), 200
                    elif 'uid' in form:
                        uid = form['uid']
                        if uid:
                            dao = resourcesDAO()
                            attlist = dao.updateuid(rid, uid)
                            res = attlist.pop(0)
                            rdid = res[0]
                            rname = res[1]
                            rqty = res[2]
                            rprice = res[3]
                            result = self.build_resources_attributes(rid, rname, rprice, rqty, rdid, uid)
                            return jsonify(Resource=result), 200
                    else:
                        return jsonify(Error="Unexpected attributes in update request"), 400

############################## DELETE METHODS ############################################################

    def deleteResource(self, rid):
        dao = resourcesDAO()
        if not dao.getResourcesByRid(rid):
            return jsonify(Error="Part not found."), 404
        else:
            dao.delete(rid)
            return jsonify(DeleteStatus="OK"), 200

############################ GET METHODS ########################################################################

    def getAllResources(self):
        dao = resourcesDAO()
        resources_list = dao.getAllResources()
        results_list = []
        for row in resources_list:
            result = self.build_resources_dict(row)
            results_list.append(result)
        return jsonify(Resources=results_list)

    def searchResources(self, args):
        rid = args.get("rid")
        rName = args.get("rName")
        rqty = args.get("rqty")
        uid = args.get("uid")
        rprice = args.get("rprice")
        rdid = args.get("rdid")
        dao = resourcesDAO()
        resource_list = []
        if (len(args) == 5) and (rid or rName or rqty or rprice or uid):
            resource_list = dao.getResourceByRidAndRnameAndrqtyAndrpriceAnduid(rid, rName, rqty, rprice, uid)
        elif(len(args) == 5) and (rid or rName or rqty or rprice or rdid):
            resource_list = dao.getResourceByRidAndRnameAndRqtyAndrPriceAndrid( rid, rName, rqty, rprice, rdid)
        elif (len(args) == 5) and (rid or rName or rqty or uid or rdid):
            resource_list = dao.getResourceByRidAndRnameAndRqtyAnduidAndrdid(rid, rName, rqty, uid, rdid)
        elif (len(args) == 5) and (rid or rName or rprice or uid or rdid):
            resource_list = dao.getResourceByRidAndRnameAndrPriceAnduidAndrdid(rid, rName, rprice, uid, rdid)
        elif (len(args) == 5) and (rid or rqty or rprice or uid or rdid):
            resource_list = dao.getResourceByRidAndRqtyAndrPriceAnduidAndrdid(rid, rqty, rprice, uid, rdid)
        elif (len(args) == 5) and (rName or rqty or rprice or uid or rdid):
            resource_list = dao.getResourceByRnameAndRqtyAndrPriceAnduidAndrdid(rName, rqty, rprice, uid, rdid)
        elif (len(args) == 4) and (rid or rqty or rprice or uid):
            resource_list = dao.getResourceByRidAndRnameAndRqtyAndrPriceAnduidAndrdid(rid, rqty, rprice, uid)
        elif (len(args) == 4) and (rid or rName or rprice or uid):
            resource_list = dao.getResourceByRidAndRnameAndrPriceAnduid(rid, rName, rprice, uid)
        elif (len(args) == 4) and (rid or rName or rqty or uid):
            resource_list = dao.getResourceByRidAndRnameAndRqtyAnduid(rid, rName, rqty, uid)
        elif (len(args) == 4) and (rid or rName or rqty or rprice):
            resource_list = dao.getResourceByRidAndRnameAndRqtyAndrPrice(rid, rName, rqty, rprice)
        elif (len(args) == 4) and (rName or rqty or rprice or uid ):
            resource_list = dao.getResourceByRnameAndrqtyAndrpriceAnduid(rName, rqty, rprice, uid)
        elif (len(args) == 4) and (rName or rqty or uid or rdid):
            resource_list = dao.getResourceByRnameAndrqtyAnduidAndrdid(rName, rqty, uid, rdid)
        elif (len(args) == 3) and (rName or rqty or uid):
            resource_list = dao.getResourceByRnameAndRqtyAnduid(rName, rqty, uid)
        elif (len(args) == 3) and (rName or rqty or rprice):
            resource_list = dao.getResourceByRnameAndrqtyAndrprice(rName, rqty, rprice)
        elif (len(args) == 3) and (rName or rqty or rdid):
            resource_list = dao.getResourceByRnameAndrqtyAndrdid(rName, rqty, rdid)
        elif (len(args) == 2) and (rName or rqty):
            resource_list = dao.getResourceByRnameAndrqty(rName, rqty)
        elif (len(args) == 2) and (rName or uid):
            resource_list = dao.getResourceByRnameAnduid(rName, uid)
        elif (len(args) == 2) and (rName or rprice):
            resource_list = dao.getResourceByRnameAndrprice(rName, rprice)
        elif (len(args) == 2) and (rName or rdid):
            resource_list = dao.getResourceByRnameAndrdid(rName, rdid)
        elif (len(args) == 1) and rName:
            resource_list = dao.getResourceByRname(rName)
        elif (len(args) == 1) and rqty:
            resource_list = dao.getResourceByrqty(rqty)
        elif (len(args) == 1) and uid:
            resource_list = dao.getResourceByuid(uid)
        elif (len(args) == 1) and rprice:
            resource_list = dao.getResourceByrprice(rprice)
        elif (len(args) == 1) and rdid:
            resource_list = dao.getResourceByrdid(rdid)
        elif (len(args) == 1) and rid:
            resource_list = dao.getResourcesByRid(rid)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in resource_list:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)


    def getResourcesByrid(self, rid):
        dao = resourcesDAO()
        row = dao.getResourcesByRid(rid)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            resource = self.build_resources_dict(row)
            return jsonify(Resource=resource)


    def getSupplierByResourceId(self, rid):
        dao = resourcesDAO()
        if not dao.getResourcesByRid(rid):
            return jsonify(Error="Resource Not Found"), 404
        suppliers_list = dao.getSuplierByResourceId(rid)
        result_list = []
        for row in suppliers_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)



    def getOrderBySupplierSearch(self, args):
        ufirstname = args.get("ufirstname")
        ulastname = args.get("ulastname")
        dao = resourcesDAO()
        user_list = []
        if (len(args) == 2) and (ufirstname or ulastname):
            user_list = dao.getOrderBySupplierFirstNameAndLastName(ufirstname, ulastname)
        elif (len(args) == 1) and ufirstname:
            user_list = dao.getOrderBySupplierFirstName(ufirstname)
        elif (len(args) == 1) and ulastname:
            user_list = dao.getOrderBySupplierLastName(ulastname)
        else:
            return jsonify(Error="Malformed query string"), 400
        results_list = []
        for row in user_list:
            result = self.build_supplier_order_dict(row)
            results_list.append(result)
        return jsonify(User=results_list)

    def getAllOrderBySupplierSearch(self):
        dao = resourcesDAO()
        resources_list = dao.getAllOrderBySupplier()
        results_list = []
        for row in resources_list:
            result = self.build_supplier_order_dict(row)
            results_list.append(result)
        return jsonify(Resources=results_list)

    def getAllResourcesOrderedByName(self):
        dao = resourcesDAO()
        resources_list = dao.getAllResourcesOrderByName()
        results_list = []
        for row in resources_list:
            result = self.build_resources_dict(row)
            results_list.append(result)
        return jsonify(Resources=results_list)

    def searchResourcesOrderedByName(self, args):
        rid = args.get("rid")
        rName = args.get("rName")
        rqty = args.get("rqty")
        uid = args.get("uid")
        rprice = args.get("rprice")
        rdid = args.get("rdid")
        dao = resourcesDAO()
        resource_list = []
        if (len(args) == 5) and (rid or rName or rprice or uid or rdid):
            resource_list = dao.getResourceByRidAndRnameAndrPriceAnduidAndrdidOrderByName(rid, rName, rprice, uid, rdid)
        elif (len(args) == 4) and (rid or rName or rprice or uid):
            resource_list = dao.getResourceByRidAndRnameAndrPriceAnduidOrderByName(rid, rName, rprice, uid)
        elif (len(args) == 4) and (rid or rName or rprice or rdid):
            resource_list = dao.getResourceByRnameAndRdidAndrpriceAnduidOrderByName(rid, rName, rprice, rdid)
        elif (len(args) == 3) and (rid or rName or rprice):
            resource_list = dao.getResourceByRidAndRNameAndRpriceOrderByRname(rid, rName, rprice)
        elif (len(args) == 3) and (rid or rName or rprice):
            resource_list = dao.getResourceByRidAndRNameAndRpriceOrderByRdid(rid, rName, rdid)
        elif (len(args) == 3) and (rid or rName or rprice):
            resource_list = dao.getResourceByRidAndRNameAndRpriceOrderByUid(rid, rName, uid)
        elif (len(args) == 2) and (rName or uid):
            resource_list = dao.getResourceByRnameAnduidOrderByName(rName, uid)
        elif (len(args) == 2) and (rName or rprice):
            resource_list = dao.getResourceByRnameAndrpriceOrderByName(rName, rprice)
        elif (len(args) == 2) and (rName or rdid):
            resource_list = dao.getResourceByRnameAndrdidOrderByName(rName, rdid)
        elif (len(args) == 1) and rName:
            resource_list = dao.getResourceByRnameOrderByName(rName)
        elif (len(args) == 1) and uid:
            resource_list = dao.getResourceByuidOrderByName(uid)
        elif (len(args) == 1) and rprice:
            resource_list = dao.getResourceByrpriceOrderByName(rprice)
        elif (len(args) == 1) and rdid:
            resource_list = dao.getResourceByrdidOrderByName(rdid)
        elif (len(args) == 1) and rid:
            resource_list = dao.getResourcesByRidOrderByName(rid)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in resource_list:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getAllResourcesAvailable(self):
        dao = resourcesDAO()
        resources_list = dao.getAllResourcesAvailable()
        results_list = []
        for row in resources_list:
            result = self.build_resources_dict(row)
            results_list.append(result)
        return jsonify(Resources=results_list)

    ##############

    def getAllResourcesRequestedOrderedByName(self):
        dao = resourcesDAO()
        resources_list = dao.getAllResourcesRequestedOrderByName()
        results_list = []
        for row in resources_list:
            result = self.build_resources_dict(row)
            results_list.append(result)
        return jsonify(Resources=results_list)

    def searchResourcesRequestedOrderedByName(self, args):
        rid = args.get("rid")
        rName = args.get("rName")
        rqty = args.get("rqty")
        uid = args.get("uid")
        rprice = args.get("rprice")
        rdid = args.get("rdid")
        dao = resourcesDAO()
        resource_list = []
        if (len(args) == 5) and (rid or rName or rqty or rprice or uid):
            resource_list = dao.getResourceRequestedByRidAndRnameAndrqtyAndrpriceAnduidOrderByName(rid,rName, rqty, rprice, uid)
        elif (len(args) == 5) and (rid or rName or rqty or rprice or rdid):
            resource_list = dao.getResourceRequestedByRidAndRnameAndRqtyAndrPriceAndridOrderByName(rid, rName, rqty, rprice, rdid)
        elif (len(args) == 5) and (rid or rName or rqty or uid or rdid):
            resource_list = dao.getResourceRequestedByRidAndRnameAndRqtyAnduidAndrdidOrderByName(rid,rName, rqty, uid, rdid)
        elif (len(args) == 5) and (rid or rName or rprice or uid or rdid):
            resource_list =dao.getResourceRequestedByRidAndRnameAndrPriceAnduidAndrdidOrderByName(rid,rName, rprice, uid, rdid)
        elif (len(args) == 5) and (rid or rqty or rprice or uid or rdid):
            resource_list =dao.getResourceRequestedByRidAndRqtyAndrPriceAnduidAndrdidOrderByName(rid,rqty, rprice, uid, rdid)
        elif (len(args) == 5) and (rName or rqty or rprice or uid or rdid):
            resource_list =dao.getResourceRequestedByRnameAndRqtyAndrPriceAnduidAndrdidOrderByName(rName,rqty, rprice, uid, rdid)
        elif (len(args) == 4) and (rid or rqty or rprice or uid):
            resource_list =dao.getResourceRequestedByRidAndRnameAndRqtyAndrPriceAnduidAndrdidOrderByName(rid,rqty, rprice, uid)
        elif (len(args) == 4) and (rid or rName or rprice or uid):
            resource_list =dao.getResourceRequestedByRidAndRnameAndrPriceAnduidOrderByName(rid,rName, rprice, uid)
        elif (len(args) == 4) and (rid or rName or rqty or uid):
            resource_list =dao.getResourceRequestedByRidAndRnameAndRqtyAnduidOrderByName(rid, rName, rqty, uid)
        elif (len(args) == 4) and (rid or rName or rqty or rprice):
            resource_list =dao.getResourceRequestedByRidAndRnameAndRqtyAndrPriceOrderByName(rid,rName, rqty, rprice)
        elif (len(args) == 4) and (rName or rqty or uid or rdid):
            resource_list =dao.getResourceRequestedByRnameAndrqtyAnduidAndrdidOrderByName(rName,rqty, uid, rdid)
        elif (len(args) == 3) and (rName or rqty or uid):
            resource_list =dao.getResourceRequestedByRnameAndRqtyAnduidOrderByName(rName, rqty, uid)
        elif (len(args) == 3) and (rName or rqty or rprice):
            resource_list =dao.getResourceRequestedByRnameAndrqtyAndrpriceOrderByName(rName,rqty, rprice)
        elif (len(args) == 3) and (rName or rqty or rdid):
            resource_list =dao.getResourceRequestedByRnameAndrqtyAndrdidOrderByName(rName, rqty,rdid)
        elif (len(args) == 2) and (rName or rqty):
            resource_list =dao.getResourceRequestedByRnameAndrqtyOrderByName(rName, rqty)
        elif (len(args) == 2) and (rName or uid):
            resource_list =dao.getResourceRequestedByRnameAnduidOrderByName(rName, uid)
        elif (len(args) == 2) and (rName or rprice):
            resource_list =dao.getResourceRequestedByRnameAndrpriceOrderByName(rName, rprice)
        elif (len(args) == 2) and (rName or rdid):
            resource_list =dao.getResourceRequestedByRnameAndrdidOrderByName(rName, rdid)
        elif (len(args) == 1) and rName:
            resource_list = dao.getResourceRequestedByRnameOrderByName(rName)
        elif (len(args) == 1) and rqty:
            resource_list = dao.getResourceRequestedByrqtyOrderByName(rqty)
        elif (len(args) == 1) and uid:
            resource_list = dao.getResourceRequestedByuidOrderByName(uid)
        elif (len(args) == 1) and rprice:
            resource_list = dao.getResourceRequestedByrpriceOrderByName(rprice)
        elif (len(args) == 1) and rdid:
            resource_list = dao.getResourceRequestedByrdidOrderByName(rdid)
        elif (len(args) == 1) and rid:
            resource_list = dao.getResourcesRequestedByRidOrderByName(rid)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in resource_list:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)


    def getAllResourcesRequested(self):
        dao = resourcesDAO()
        resources_list = dao.getAllResourcesRequested()
        results_list = []
        for row in resources_list:
            result = self.build_resources_dict(row)
            results_list.append(result)
        return jsonify(Resources=results_list)


    def searchResourcesRequested(self, args):
        rid = args.get("rid")
        rName = args.get("rName")
        rqty = args.get("rqty")
        uid = args.get("uid")
        rprice = args.get("rprice")
        rdid = args.get("rdid")
        dao = resourcesDAO()
        resource_list = []
        if (len(args) == 5) and (rid or rName or rqty or rprice or uid):
            resource_list = dao.getResourceRequestedByRidAndRnameAndrqtyAndrpriceAnduid(rid,rName, rqty, rprice, uid)
        elif (len(args) == 5) and (rid or rName or rqty or rprice or rdid):
            resource_list = dao.getResourceRequestedByRidAndRnameAndRqtyAndrPriceAndrid(rid, rName, rqty, rprice, rdid)
        elif (len(args) == 5) and (rid or rName or rqty or uid or rdid):
            resource_list = dao.getResourceRequestedByRidAndRnameAndRqtyAnduidAndrdid(rid,rName, rqty, uid, rdid)
        elif (len(args) == 5) and (rid or rName or rprice or uid or rdid):
            resource_list =dao.getResourceRequestedByRidAndRnameAndrPriceAnduidAndrdid(rid,rName, rprice, uid, rdid)
        elif (len(args) == 5) and (rid or rqty or rprice or uid or rdid):
            resource_list =dao.getResourceRequestedByRidAndRqtyAndrPriceAnduidAndrdid(rid,rqty, rprice, uid, rdid)
        elif (len(args) == 5) and (rName or rqty or rprice or uid or rdid):
            resource_list =dao.getResourceRequestedByRnameAndRqtyAndrPriceAnduidAndrdid(rName,rqty, rprice, uid, rdid)
        elif (len(args) == 4) and (rid or rqty or rprice or uid):
            resource_list =dao.getResourceRequestedByRidAndRnameAndRqtyAndrPriceAnduidAndrdid(rid,rqty, rprice, uid)
        elif (len(args) == 4) and (rid or rName or rprice or uid):
            resource_list =dao.getResourceRequestedByRidAndRnameAndrPriceAnduid(rid,rName, rprice, uid)
        elif (len(args) == 4) and (rid or rName or rqty or uid):
            resource_list =dao.getResourceRequestedByRidAndRnameAndRqtyAnduid(rid, rName, rqty, uid)
        elif (len(args) == 4) and (rid or rName or rqty or rprice):
            resource_list =dao.getResourceRequestedByRidAndRnameAndRqtyAndrPrice(rid,rName, rqty, rprice)
        elif (len(args) == 4) and (rName or rqty or uid or rdid):
            resource_list =dao.getResourceRequestedByRnameAndrqtyAnduidAndrdid(rName,rqty, uid, rdid)
        elif (len(args) == 3) and (rName or rqty or uid):
            resource_list =dao.getResourceRequestedByRnameAndRqtyAnduid(rName, rqty, uid)
        elif (len(args) == 3) and (rName or rqty or rprice):
            resource_list =dao.getResourceRequestedByRnameAndrqtyAndrprice(rName,rqty, rprice)
        elif (len(args) == 3) and (rName or rqty or rdid):
            resource_list =dao.getResourceRequestedByRnameAndrqtyAndrdid(rName, rqty,rdid)
        elif (len(args) == 2) and (rName or rqty):
            resource_list =dao.getResourceRequestedByRnameAndrqty(rName, rqty)
        elif (len(args) == 2) and (rName or uid):
            resource_list =dao.getResourceRequestedByRnameAnduid(rName, uid)
        elif (len(args) == 2) and (rName or rprice):
            resource_list =dao.getResourceRequestedByRnameAndrprice(rName, rprice)
        elif (len(args) == 2) and (rName or rdid):
            resource_list =dao.getResourceRequestedByRnameAndrdid(rName, rdid)
        elif (len(args) == 1) and rName:
            resource_list = dao.getResourceRequestedByRname(rName)
        elif (len(args) == 1) and rqty:
            resource_list = dao.getResourceRequestedByrqty(rqty)
        elif (len(args) == 1) and uid:
            resource_list = dao.getResourceRequestedByuid(uid)
        elif (len(args) == 1) and rprice:
            resource_list = dao.getResourceRequestedByrprice(rprice)
        elif (len(args) == 1) and rdid:
            resource_list = dao.getResourceRequestedByrdid(rdid)
        elif (len(args) == 1) and rid:
            resource_list = dao.getResourcesRequestedByRid(rid)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in resource_list:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)



    def searchResourceInserted(self, args):
        rid = args.get("rid")
        rName = args.get("rName")
        rqty = args.get("rqty")
        uid = args.get("uid")
        rprice = args.get("rprice")
        rdid = args.get("rdid")
        dao = resourcesDAO()
        resource_list = []
        if (len(args) == 5) and (rid or rName or rqty or rprice or uid):
            resource_list = dao.getResourceRequestedByRidAndRnameAndrqtyAndrpriceAnduid(rid, rName, rqty, rprice, uid)
        elif (len(args) == 5) and (rid or rName or rqty or rprice or rdid):
            resource_list = dao.getResourceRequestedByRidAndRnameAndRqtyAndrPriceAndrid(rid, rName, rqty, rprice, rdid)
        elif (len(args) == 5) and (rid or rName or rqty or uid or rdid):
            resource_list = dao.getResourceRequestedByRidAndRnameAndRqtyAnduidAndrdid(rid, rName, rqty, uid, rdid)
        elif (len(args) == 5) and (rid or rName or rprice or uid or rdid):
            resource_list = dao.getResourceRequestedByRidAndRnameAndrPriceAnduidAndrdid(rid, rName, rprice, uid, rdid)
        elif (len(args) == 5) and (rid or rqty or rprice or uid or rdid):
            resource_list = dao.getResourceRequestedByRidAndRqtyAndrPriceAnduidAndrdid(rid, rqty, rprice, uid, rdid)
        elif (len(args) == 4) and (rid or rqty or rprice or uid):
            resource_list = dao.getResourceRequestedByRidAndRnameAndRqtyAndrPriceAnduidAndrdid(rid, rqty, rprice, uid)
        elif (len(args) == 4) and (rid or rName or rprice or uid):
            resource_list = dao.getResourceRequestedByRidAndRnameAndrPriceAnduid(rid, rName, rprice, uid)
        elif (len(args) == 4) and (rid or rName or rqty or uid):
            resource_list = dao.getResourceRequestedByRidAndRnameAndRqtyAnduid(rid, rName, rqty, uid)
        elif (len(args) == 4) and (rid or rName or rqty or rprice):
            resource_list = dao.getResourceRequestedByRidAndRnameAndRqtyAndrPrice(rid, rName, rqty, rprice)

        elif (len(args) == 1) and rid:
            resource_list = dao.getResourcesRequestedByRid(rid)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in resource_list:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)




