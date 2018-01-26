from flask import jsonify
from dao.purchase import purchaseDAO

class purchaseHandler:

    # Create a dictionary of users
    def build_purchase_dict(self, row):
        result = {}
        result['pid'] = row[0]
        result['pdate'] = row[1]
        result['pqty'] = row[2]
        result['rdid'] = row[3]
        result['ptype'] = row[4]
        return result

    def build_purchase_attributes(self, user_name, user_password, ccNumber, rdid, pdate, pqty, ptype, pid):
        result = {}
        result['user_name'] = user_name
        result['user_password'] = user_password
        result['ccNumber'] = ccNumber
        result['rdid'] = rdid
        result['pdate'] = pdate
        result['pqty'] = pqty
        result['ptype'] = ptype
        result['pid'] = pid
        return result

    #################### POST METHODS #############################################

    def insertPurchase(self, form):
        if len(form) != 7:
            return jsonify(Error = "Malformed post request"), 400
        else:
            user_name = form['user_name']
            user_password = form['user_password']
            ccNumber = form['ccNumber']
            rdid = form['rdid']
            pdate = form['pdate']
            pqty = form['pqty']
            ptype = form['ptype']
            if user_name and user_password and ccNumber and rdid and pdate and pqty and ptype:
                dao = purchaseDAO()
                pid = dao.insert(user_name, user_password, ccNumber, rdid, pdate, pqty, ptype)
                if pid == []:
                    return jsonify(Error="Unexpected Error"), 400
                else:
                    result = self.build_purchase_attributes(user_name, user_password, ccNumber, rdid, pdate, pqty, ptype, pid)
                    return jsonify(User=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    ###############################################################################

    #################### POST METHODS #############################################

    def getAllPurchases(self):
        dao = purchaseDAO()
        users_list = dao.getAllPurchases()
        results_list = []
        for row in users_list:
            result = self.build_purchase_dict(row)
            results_list.append(result)
        return jsonify(Users=results_list)

    def getPurchaseById(self, pid):
        dao = purchaseDAO()
        row = dao.getPurchaseById(pid)
        if not row:
            return jsonify(Error = "User not found."), 404
        else:
            purchase = self.build_purchase_dict(row)
            return jsonify(User = purchase)

    def searchPurchase(self, args):
        pid = args.get("pid")
        pdate = args.get("pdate")
        pqty = args.get("pqty")
        ptype = args.get("ptype")
        dao = purchaseDAO()
        purchase_list = []
        if (len(args) == 3) and (pdate or pqty or ptype):
            purchase_list = dao.getPurchaseByDateAndQtyAndType(pdate, pqty, ptype)
        elif (len(args) == 2) and (pdate or pqty):
            purchase_list = dao.getPurchaseByDateAndQty(pdate, pqty)
        elif (len(args) == 2) and (pdate and ptype):
            purchase_list = dao.getPurchaseByDateAndType(pdate, ptype)
        elif (len(args) == 1) and pdate:
            purchase_list = dao.getPurchaseByDate(pdate)
        elif (len(args) == 1) and pqty:
            purchase_list = dao.getPurchaseByQty(pqty)
        elif (len(args) == 1) and ptype:
            purchase_list = dao.getPurchaseByType(ptype)
        else:
            return jsonify(Error = "Malformed query string"), 400
        results_list = []
        for row in purchase_list:
            result = self.build_purchase_dict(row)
            results_list.append(result)
        return jsonify(Purchase = results_list)
    


    ###############################################################################
