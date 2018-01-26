from flask import jsonify
from dao.category import categoryDAO

class categoryHandler:

    # Create a dictionary of category
    def build_category_dict(self, row):
        result = {}
        result['cid'] = row[0]
        result['cName'] = row[1]
        result['rid'] = row[3]
        result['cdescription'] = row[2]
        return result

    # Create a dictionary of users
    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['uaid'] = row[1]
        result['utype'] = row[2]
        result['ufirstname'] = row[3]
        result['ulastname'] = row[4]
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
        cdescription = args.get("cdescription")
        dao = categoryDAO()
        category_list = []
        if (len(args) == 3) and cName and cid and rid:
            category_list = dao.getCategoryByAllAttributesExceptDescription(cName, cid, rid)
        elif (len(args) == 3) and cName and cid and cdescription:
            category_list = dao.getCategoryByAllAttributesExceptrid(cName, cid, cdescription)
        elif (len(args) == 3) and cName and rid and cdescription:
            category_list = dao.getCategoryByAllAttributesExceptcid(cName, rid, cdescription)
        elif (len(args) == 3) and cid and rid and cdescription:
            category_list = dao.getCategoryByAllAttributesExceptcName(cid, rid, cdescription)
        elif (len(args) == 2) and cName and cid:
            category_list = dao.getCategoryByAllAttributesExceptridAndDescritption(cName, cid)
        elif (len(args) == 2) and cName and rid:
            category_list = dao.getCategoryByAllAttributesExceptcidAndDescritption(cName, rid)
        elif (len(args) == 2) and cName and cdescription:
            category_list = dao.getCategoryByAllAttributesExceptridAndcid(cName, cdescription)
        elif (len(args) == 2) and cid and cdescription:
            category_list = dao.getCategoryByAllAttributesExceptridAndcName(cid, cdescription)
        elif (len(args) == 2) and cid and rid:
            category_list = dao.getCategoryByAllAttributesExceptdescriptionAndcName(cid, rid)
        elif (len(args) == 2) and cdescription and rid:
            category_list = dao.getCategoryByAllAttributesExceptcidAndcName(rid, cdescription)
        elif (len(args) == 1) and rid:
            category_list = dao.getCategoryByrid(rid)
        elif (len(args) == 1) and cName:
            category_list = dao.getCategoryBycName(cName)
        elif (len(args) == 1) and cid:
            category_list = dao.getCategoryBycid(cid)
        elif (len(args) == 1) and cdescription:
            category_list = dao.getCategoryByDescription(cdescription)
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
            category = self.build_category_dict(row)
            return jsonify(Category=category)


    def getSupplierByCategorySearch(self, args):
        cname = args.get("cname")
        cdescription = args.get("cdescription")
        dao = categoryDAO()
        user_list = []
        if (len(args) == 2) and (cname or cdescription):
            user_list = dao.getSupplierByCategoryNameAndDescription(cname, cdescription)
        elif (len(args) == 1) and cname:
            user_list = dao.getSupplierByCategoryName(cname)
        elif (len(args) == 1) and cdescription:
            user_list = dao.getSupplierByCategoryDescription(cdescription)
        else:
            return jsonify(Error="Malformed query string"), 400
        results_list = []
        for row in user_list:
            result = self.build_user_dict(row)
            results_list.append(result)
        return jsonify(User=results_list)