from flask import jsonify
from dao.category import categoryDAO

class categoryHandler:

    # Create a dictionary of category
    def build_category_dict(self, row):
        result = {}
        result['cid'] = row[0]
        result['cName'] = row[1]
        result['rid'] = row[2]
        result['description'] = row[3]
        return result


    def getAllCategory(self):
        dao = categoryDAO()
        category_list = dao.getAllCategory()
        results_list = []
        for row in category_list:
            result = self.build_category_dict(row)
            results_list.append(result)
        return jsonify(Category=results_list)

    def searchCategory(self, args):
        cName = args.get("cName")
        cid = args.get("cid")
        rid = args.get("rid")
        description = args.get("description")
        dao = categoryDAO()
        category_list = []
        if (len(args) == 4) and cName and cid and rid and description:
            category_list = dao.getCategoryWithAllAttributes(cName, cid, rid, description)
        elif (len(args) == 3) and cName and cid and rid:
            category_list = dao.getCategoryByAllAttributesExceptDescription(cName, cid, rid)
        elif (len(args) == 3) and cName and cid and description:
            category_list = dao.getCategoryByAllAttributesExceptrid(cName, cid, description)
        elif (len(args) == 3) and cName and rid and description:
            category_list = dao.getCategoryByAllAttributesExceptcid(cName, rid, description)
        elif (len(args) == 3) and cid and rid and description:
            category_list = dao.getCategoryByAllAttributesExceptcName(cid, rid, description)
        elif (len(args) == 2) and cName and cid:
            category_list = dao.getCategoryByAllAttributesExceptridAndDescritption(cName, cid)
        elif (len(args) == 2) and cName and rid:
            category_list = dao.getCategoryByAllAttributesExceptcidAndDescritption(cName, rid)
        elif (len(args) == 2) and cName and description:
            category_list = dao.getCategoryByAllAttributesExceptridAndcid(cName, description)
        elif (len(args) == 2) and cid and description:
            category_list = dao.getCategoryByAllAttributesExceptridAndcName(cid, description)
        elif (len(args) == 2) and cid and rid:
            category_list = dao.getCategoryByAllAttributesExceptdescriptionAndcName(cid, rid)
        elif (len(args) == 2) and description and rid:
            category_list = dao.getCategoryByAllAttributesExceptcidAndcName(rid, description)
        elif (len(args) == 1) and rid:
            category_list = dao.getCategoryByrid(rid)
        elif (len(args) == 1) and cName:
            category_list = dao.getCategoryBycName(cName)
        elif (len(args) == 1) and cid:
            category_list = dao.getCategoryBycid(cid)
        elif (len(args) == 1) and description:
            category_list = dao.getCategoryByDescription(description)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in category_list:
            result = self.build_category_dict(row)
            result_list.append(result)
        return jsonify(Category=result_list)

    def getCategoryBycid(self, cid):
        dao = categoryDAO()
        row = dao.getCategoryBycid(cid)
        if not row:
            return jsonify(Error="Category Not Found"), 404
        else:
            print(row)
            category = self.build_category_dict(row)
            return jsonify(Category=category)