from flask import jsonify

from dao.Does import DoesDAO


class DoesHandler:

    # Create a dictionary of category
    def build_Does_dict(self, row):
        result = {}
        result['isCustomer'] = row[0]
      
        return result


    def getAllDoes(self):
        dao = DoesDAO()
        Does_list = dao.getAllDoes()
        results_list = []
        for row in Does_list:
            result = self.build_Does_dict(row)
            results_list.append(result)
        return jsonify(Does=results_list)

    def searchDoes(self, args):
        isCustomer = args.get("isCustomer")
        dao = DoesDAO()
        Does_list = []
        if (len(args) == 1) and isCustomer:
            Does_list = dao.getDoesByisCustomer(isCustomer)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in Does_list:
            result = self.build_Does_dict(row)
            result_list.append(result)
        return jsonify(Does=result_list)

    def getDoesByisCustomer(self, isCustomer):
        dao = DoesDAO()
        row = dao.getDoesByisCustomer(isCustomer)
        if not row:
          return jsonify(Error="Not Found"), 404
        else:
            Does = self.build_Does_dict(row)
        return jsonify(Does=Does)