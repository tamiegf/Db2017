from flask import jsonify

from dao.creditCard import CreditCardDAO


class creditCardHandler:

    # Create a dictionary of category
    def build_creditCard_dict(self, row):
        result = {}
        result['ccid'] = row[0]
        result['ccNumber'] = row[2]
        result['cvv'] = row[3]
        result['ccExpirationDate']= row[4]
        return result

    def build_paymentinfo_dict2(self, uid, ccNumber, cvv, ccExpirationDate):
        result = {}
        result['uid'] = uid
        result['ccNumber'] = ccNumber
        result['cvv'] = cvv
        result['ccExpirationDate'] = ccExpirationDate
        return result

    #################### POST METHODS #############################################

    def insertCreditCard(self, form):
        dao = CreditCardDAO()
        if len(form) != 4:
            return jsonify(Error="Malformed query string"), 400
        else:
            uid = form['uid']
            ccNumber = form['ccNumber']
            cvv = form['cvv']
            ccExpirationDate = form['ccExpirationDate']
            if uid and ccNumber and cvv and ccExpirationDate:
                dao.insert(uid, ccNumber, cvv, ccExpirationDate)
                result = self.build_paymentinfo_dict2(uid, ccNumber, cvv, ccExpirationDate)
                return jsonify(User=result), 201
            else:
                return jsonify(Error="Unable to insert"), 400
    ######################################################################################

    ###################### UPDATE METHODS ################################################
    def updateCreditCard(self, uid, form):
        dao = CreditCardDAO()
        if not dao.getCreditCardByUid(uid):
            return jsonify(Error="Malformed query string"), 400
        else:
            if len(form) != 3:
                return jsonify(Error="Malformed update request"), 400
            else:
                ccNumber = form['ccNumber']
                cvv = form['cvv']
                ccExpirationDate = form['ccExpirationDate']
                if ccNumber and cvv and ccExpirationDate:
                    dao.update(uid, ccNumber, cvv, ccExpirationDate)
                    result = self.build_paymentinfo_dict2(uid, ccNumber, cvv, ccExpirationDate)
                    return jsonify(CreditCard=result), 201
                else:
                    return jsonify(Error="Unable to update credit card details"), 400

        ###############################################################################

        #################### POST METHODS #############################################


    def getAllCreditCard(self):
        dao = CreditCardDAO()
        creditCard_list = dao.getAllCategory()
        results_list = []
        for row in creditCard_list:
            result = self.build_creditCard_dict(row)
            results_list.append(result)
        return jsonify(CreditCard=results_list)

    def searchCreditCard(self, args):
        ccNumber = args.get("ccNumber")
        cvv = args.get("cvv")
        ccExpirationDate = args.get("ccExpirationDate")
        ccid=args.get("ccid")
        dao = CreditCardDAO()
        creditCard_list = []
        if (len(args) == 3) and ccNumber and cvv and ccExpirationDate:
            creditCard_list = dao.getCreditCardWithAllAttributes(ccNumber,cvv,ccExpirationDate )
        elif (len(args) == 1) and ccNumber:
            creditCard_list = dao.getCreditCardByccNumber(ccNumber)
        elif (len(args) == 1) and cvv:
            creditCard_list = dao.getCreditCardBycvv(cvv)
        elif (len(args) == 1) and ccExpirationDate:
            creditCard_list = dao.getCreditCardByExpirationDate(ccExpirationDate)
        elif (len(args)==1) and ccid:
            creditCard_list = dao.getCreditCardByCCID(ccid)

        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in creditCard_list:
            result = self.build_creditCard_dict(row)
            result_list.append(result)
        return jsonify(CreditCard=result_list)

    def getCreditCardByccNumber(self, ccNumber):
        dao = CreditCardDAO()
        row = dao.getCreditCardByccNumber(ccNumber)
        if not row:
          return jsonify(Error="Credit Card Not Found"), 404
        else:
           creditCard = self.build_creditCard_dict(row)
        return jsonify(creditCard=creditCard)

    def getCreditCardByCCID(self, ccid):
        dao = CreditCardDAO()
        row = dao.getCreditCardByCCID(ccid)
        if not row:
            return jsonify(Error="Credit Card Not Found"), 404
        else:
            creditCard = self.build_creditCard_dict(row)
        return jsonify(creditCard=creditCard)

    def getCreditCardByExpirationDate(self, ccExpirationDate):
        dao = CreditCardDAO()
        row = dao.getCreditCardByExpirationDate(ccExpirationDate)
        if not row:
            return jsonify(Error="Credit Card Not Found"), 404
        else:
            creditCard = self.build_creditCard_dict(row)
        return jsonify(creditCard=creditCard)