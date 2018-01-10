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

    #################### POST METHODS #############################################

    def insertPurchase(self, form):
        # No hay que hacerlo para esta fase
        pass

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