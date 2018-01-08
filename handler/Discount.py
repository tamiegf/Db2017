from flask import jsonify
from dao.Discount import DiscountDAO

class DiscountHandler:
#did, dPercent, stackable
    # Create a dictionary of category
    def build_Discount_dict(self, row):
        result = {}
        result['did'] = row[0]
        result['dPercent'] = row[1]
        result['stackable'] = row[2]
        return result


    def getAllCategory(self):
        dao = DiscountDAO()
        Discount_list = dao.getAllCategory()
        results_list = []
        for row in Discount_list:
            result = self.build_Discount_dict(row)
            results_list.append(result)
        return jsonify(Discount=results_list)

    def searchCategory(self, args):
        did = args.get("did")
        dPercent = args.get("dPercent")
        stackable = args.get("stackable")
        dao = DiscountDAO()
        Discount_list = []
        if (len(args) == 3) and did and dPercent and stackable:
            Discount_list = dao.getDiscountWithAllAttributes(did,dPercent,stackable )
        elif (len(args) == 2) and did and dPercent:
            Discount_list = dao.getDiscountByAllAttributesExceptStackable(did, dPercent)
        elif (len(args) == 2) and did and stackable:
            Discount_list = dao.getDiscountByAllAttributesExceptdPercent(did, stackable)
        elif (len(args) == 2) and dPercent and stackable:
            Discount_list = dao.getDiscountByAllAttributesExceptdid(dPercent, stackable)
        elif (len(args) == 1) and did:
            Discount_list = dao.getDiscountBydid(did)
        elif (len(args) == 1) and dPercent:
            Discount_list = dao.getDiscountBydPercent(dPercent)
        elif (len(args) == 1) and stackable:
            Discount_list = dao.getDiscountByStackable(stackable)


        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in Discount_list:
            result = self.build_Discountdict(row)
            result_list.append(result)
        return jsonify(Discount=result_list)

        def getDiscountBydid(self, did):
        dao = DiscountDAO()
        row = dao.getDiscountBydid(did)
           if not row:
              return jsonify(Error="Discount Not Found"), 404
            else:
               print(row)
               Discount = self.build_Discount_dict(row)
              return jsonify(Discount=Discount)