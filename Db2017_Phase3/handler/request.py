from flask import jsonify
from dao.request import requestDAO
from dao.request_details import requestDetailsDAO

class requestHandler:

    # Create a dictionary of request
    def build_request_dict(self, row):
        result = {}
        result['reqId'] = row[0]
        result['uid'] = row[2]
        result['reqDate'] = row[1]
        return result

    def build_request_attributes(self, reqid, reqdate, uid, rdid, rdqty, rid, need_date):
        result = {}
        result['reqId'] = reqid
        result['uid'] = uid
        result['reqDate'] = reqdate
        result['rdid'] = rdid
        result['rdqty'] = rdqty
        result['rid'] = rid
        result['need_date'] = need_date
        return result


    def getAllRequest(self):
        dao = requestDAO()
        request_list = dao.getAllRequest()
        results_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            results_list.append(result)
        return jsonify(Request=results_list)

    def searchRequest(self, args):
        reqId = args.get("reqId")
        uid = args.get("uid")
        reqDate = args.get("reqDate")
        dao = requestDAO()
        request_list = []
        if (len(args) == 2)and reqId and uid:
            request_list = dao.getRequestWithAllAttributesExceptreqDate(reqId, uid)
        elif (len(args) == 2)and reqId and reqDate:
            request_list = dao.getRequestWithAllAttributesExceptuid(reqId, reqDate)
        elif (len(args) == 2)and uid and reqDate:
            request_list = dao.getRequestWithAllAttributesExceptreqId(uid, reqDate)
        elif (len(args) == 1)and reqId:
            request_list = dao.getRequestByreqId(reqId)
        elif (len(args) == 1)and uid:
            request_list = dao.getRequestByuid(uid)
        elif (len(args) == 1)and reqDate:
            request_list = dao.getRequestByreqDate(reqDate)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Request=result_list)

    def getRequestByreqId(self, reqId):
        dao = requestDAO()
        row = dao.getRequestByreqId(reqId)
        if not row:
            return jsonify(Error="Request Not Found"), 404
        else:
            print(row)
            request = self.build_request_dict(row)
            return jsonify(Request=request)

    def insertRequest(self, form):
        if len(form) != 5:
            return jsonify(Error="Malformed post request")
        else:
            rid = form['rid']
            rdqty = form['rdqty']
            uid = form['uid']
            reqdate = form['reqdate']
            need_date = form['need_date']
            if rid and rdqty and uid and reqdate and need_date:
                dao = requestDAO()
                reqid = dao.insert(reqdate, uid)
                rdid = requestDetailsDAO().insert(rid, rdqty, need_date, reqid)
                result = self.build_request_attributes(reqid, reqdate, uid, rdid, rdqty, rid, need_date)
                return jsonify(Request=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400