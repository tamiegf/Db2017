from flask import jsonify
from dao.creditCard import CreditCardDAO

class creditCardHandler:

    # Create a dictionary of category
    def build_creditCard_dict(self, row):
        result = {}
        result['ccNumber'] = row[0]
        result['cvv'] = row[1]
        result['ccExpirationDate'] = row[2]
        return result


    def getAllCategory(self):
        dao = CreditCardDAO()
        creditCard_list = dao.getAllCategory()
        results_list = []
        for row in creditCard_list:
            result = self.build_creditCard_dict(row)
            results_list.append(result)
        return jsonify(CreditCard=results_list)

    def searchCategory(self, args):
        ccNumber = args.get("ccNumber")
        cvv = args.get("cvv")
        ccExpirationDate = args.get("ccExpirationDate")
        dao = CreditCardDAO()
        creditCard_list = []
        if (len(args) == 3) and ccNumber and cvv and ccExpirationDate:
            creditCard_list = dao.getCreditCardWithAllAttributes(ccNumber,cvv,ccExpirationDate )
        elif (len(args) == 2) and ccNumber and cvv:
            creditCard_list = dao.getCreditCardByAllAttributesExceptExpirationDate(ccNumber, cvv)
        elif (len(args) == 2) and ccNumber and ccExpirationDate:
            creditCard_list = dao.getCreditCardByAllAttributesExceptCVV(ccNumber, ccExpirationDate)
        elif (len(args) == 2) and cvv and ccExpirationDate:
            creditCard_list = dao.getCreditCardByAllAttributesExceptccNumber(cvv, ccExpirationDate)
        elif (len(args) == 1) and ccNumber:
            creditCard_list = dao.getCreditCardByccNumber(ccNumber)
        elif (len(args) == 1) and cvv:
            creditCard_list = dao.getCreditCardBycvv(cvv)
        elif (len(args) == 1) and ccExpirationDate:
            creditCard_list = dao.getCreditCardByExpirationDate(ccExpirationDate)

        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in creditCard_list:
            result = self.build_creditCArddict(row)
            result_list.append(result)
        return jsonify(CreditCard=result_list)

        def getCreditCardByccNumber(self, ccNumber):
        dao = creditCardDAO()
        row = dao.getCreditCardByccNumber(ccNumber)
           if not row:
              return jsonify(Error="Credit Card Not Found"), 404
            else:
               print(row)
               creditCard = self.build_creditCard_dict(row)
              return jsonify(creditCard=creditCard)