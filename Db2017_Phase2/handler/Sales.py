from flask import jsonify

from Db2017_Phase2.dao.Sales import SalesDAO


class SalesHandler:
    # Create a dictionary of category
    def build_Sales_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['pid'] = row[1]

        return result

    def getAllSales(self):
        dao = SalesDAO()
        Sales_list = dao.getAllSales()
        results_list = []
        for row in Sales_list:
            result = self.build_Sales_dict(row)
            results_list.append(result)
        return jsonify(Sales=results_list)

    def searchSales(self, args):
        sid = args.get("sid")

        dao = SalesDAO()
        Sales_list = []


        if (len(args) == 1) and sid:
            Sales_list = dao.getSalesBysid(sid)
        else:
            return jsonify(Error="Malformed query string"), 400
            result_list = []
        for row in Sales_list:
         result = self.build_Sales_dict(row)
         result_list.append(result)
        return jsonify(Sales=result_list)




    def getSalesBysid(self, sid):
        dao = SalesDAO()
        row = dao.getSalesBysid(sid)
        if not row:
         return jsonify(Error=" Sale Not Found"), 404
        else:
           print(row)
           Sales = self.build_Sales_dict(row)
        return jsonify(Sales=Sales)