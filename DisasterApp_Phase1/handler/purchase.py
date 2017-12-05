from flask import jsonify
from dao.purchase import purchaseDAO

class purchaseHandler:

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


    def getAllPurchase(self):
        dao = purchaseDAO()
        purchase_list = dao.getAllPurchase()
        results_list = []
        for row in purchase_list:
            result = self.build_purchase_dict(row)
            results_list.append(result)
            return jsonify(Purchases=results_list)

    def searchPurchase(self, args):
        reqId = args.get("reqId")
        purchaseDate = args.get("purchaseDate")
        ptqy = args.get("pqty")
        rid = args.get("rid")
        uid = args.get("uid")
        dao = purchaseDAO()
        purchase_list = []
        if (len(args) == 5) and (reqId or purchaseDate or ptqy or rid or uid):
            purchase_list = dao.getPurchaseWithAllAttributes(reqId, purchaseDate, ptqy, uid)
        elif (len(args) == 4) and (reqId or purchaseDate or ptqy or rid):
            purchase_list = dao.getPurchaseByReqidAndPurchasedateAndPtqyAndRid(reqId, purchaseDate, ptqy, rid)
        elif (len(args) == 4) and (reqId or purchaseDate or ptqy or uid):
            purchase_list = dao.getPurchaseByReqidAndPurchasedateAndPtqyAndUid(reqId, purchaseDate, ptqy, uid)
        elif (len(args) == 3) and (reqId or purchaseDate or ptqy):
            purchase_list = dao.getPurchaseByReqidAndPurchasedateAndPtqy(reqId, purchaseDate, ptqy)
        elif (len(args) == 3) and (reqId or purchaseDate or rid):
            purchase_list = dao.getPurchaseByReqidAndPurchasedateAndRid(reqId, purchaseDate, rid)
        elif (len(args) == 3) and (reqId or purchaseDate or uid):
            purchase_list = dao.getPurchaseByReqidAndPurchasedateAndUid(reqId, purchaseDate, uid)
        elif (len(args) == 2) and (reqId or purchaseDate):
            purchase_list = dao.getPurchaseByReqidAndPurchasedate(reqId, purchaseDate)
        elif (len(args) == 2) and (reqId or ptqy):
            purchase_list = dao.getPurchaseByReqidAndPtqy(reqId, ptqy)
        elif (len(args) == 2) and (reqId or rid):
            purchase_list = dao.getPurchaseByReqidAndRid(reqId, rid)
        elif (len(args) == 2) and (reqId or uid):
            purchase_list = dao.getPurchaseByReqidAndUid(reqId, uid)
        elif (len(args) == 1) and reqId:
            purchase_list = dao.getPurchaseByReqid(reqId)
        elif (len(args) == 1) and purchaseDate:
            purchase_list = dao.getPurchaseByPurchasedate(purchaseDate)
        elif (len(args) == 1) and ptqy:
            purchase_list = dao.getPurchaseByPtqy(ptqy)
        elif (len(args) == 1) and rid:
            purchase_list = dao.getPurchaseByRid(rid)
        elif (len(args) == 1) and uid:
            purchase_list = dao.getPurchaseByReqid(uid)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in purchase_list:
            result = self.build_purchase_dict(row)
            result_list.append(result)
        return jsonify(Purchases=result_list)


    def getPurchaseByPid(self, pid):
        dao = purchaseDAO()
        row = dao.getPurchaseByPid(pid)
        if not row:
            return jsonify(Error="PURCHASE Not Found"), 404
        else:
            user = self.build_purchase_dict(row)
            return jsonify(Purchase=user)

    def getUserByPid(self, pid):
        dao = purchaseDAO()
        if not dao.getPurchaseByPid(pid):
            return jsonify(Error="User Not Found"), 404
        request_list = dao.getUserByPid(pid)
        result_list = []
        for row in request_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(User=result_list)

    def getRequestByPid(self, pid):
        dao = purchaseDAO()
        if not dao.getPurchaseByPid(pid):
            return jsonify(Error="Request Not Found"), 404
        request_list = dao.getRequestByPid(pid)
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Request=result_list)
