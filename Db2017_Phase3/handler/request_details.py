from flask import jsonify
from dao.request_details import requestDetailsDAO

class requestDetailsHandler:

    # Create a dictionary of request
    def build_request_details_dict(self, row):
        result = {}
        result['RDid'] = row[0]
        result['rdqty'] = row[1]
        result['needDate'] = row[2]
        result['deliveryDate'] = row[3]
        result['status'] = row[4]
        result['reqId'] = row[5]
        return result

    def build_order_dict(self, row):
        result ={}
        result['RDid'] = row[0]
        result['rname'] = row[1]
        result['rdqty'] = row[2]
        result['need_date'] = row[3]
        result['delivery_date'] = row[4]
        result['ptype'] = row[5]
        return result

    def build_payment_dict(self, row):
        result = {}
        result['pid'] = row[0]
        result['rname'] = row[1]
        result['pdate'] = row[2]
        result['pqty'] = row[3]
        result['price_paid'] = row[4]
        result['ccnumber'] = row[5]
        return result

    def build_request_details_attributes(self, rdid, rdqty, need_date, delivery_date, status, reqid, rid):
        result = {}
        result['RDid'] = rdid
        result['rdqty'] = rdqty
        result['need_date'] = need_date
        result['delivery_date'] = delivery_date
        result['status'] = status
        result['reqid'] = reqid
        result['rid'] = rid
        return result


    def getAllRequestDetails(self):
        dao = requestDetailsDAO()
        request_details_list = dao.getAllRequestDetails()
        results_list = []
        for row in request_details_list:
            result = self.build_request_details_dict(row)
            results_list.append(result)
        return jsonify(Request_Details=results_list)

    def updateRequestDetails(self, rdid, form):
        dao = requestDetailsDAO()
        if not dao.getRequestDetailsByRDid(rdid):
            return jsonify(Error="Request Details not found."), 404
        else:
            if len(form) > 3:
                return jsonify(Error="Malformed update request"), 400
            else:
                if (len(form) == 3):
                    rdqty = form['rdqty']
                    status = form['status']
                    deliverydate = form['delivery_date']
                    if rdqty and status and deliverydate:
                        dao = requestDetailsDAO()
                        attlist = dao.updatedeliveryDateAndrdqtyAndstatus(rdid, deliverydate, rdqty, status)
                        res = attlist.pop(0)
                        needdate = res[0]
                        reqid = res[1]
                        rid = res[2]
                        result = self.build_request_details_attributes(rdid, rdqty, needdate, deliverydate, status,
                                                                       reqid, rid)
                        return jsonify(RequestDetails=result), 200
                    else:
                        return jsonify(Error="Unexpected attributes in update request"), 400
                elif len(form) == 2:
                    if ('delivery_date' in form) and ('status' in form):
                        deliverydate = form['delivery_date']
                        status = form['status']
                        if status and deliverydate:
                            dao = requestDetailsDAO()
                            attlist = dao.updatedeliveryDateAndstatus(rdid, deliverydate, status)
                            res = attlist.pop(0)
                            needdate = res[0]
                            reqid = res[1]
                            rid = res[2]
                            rdqty = res[3]
                            result = self.build_request_details_attributes(rdid, rdqty, needdate, deliverydate, status,
                                                                           reqid, rid)
                            return jsonify(RequestDetails=result), 200
                    else:
                        return jsonify(Error="Unexpected attributes in update request"), 400
                elif len(form) == 1:
                    if 'rdqty' in form:
                        rdqty = form['rdqty']
                        if rdqty:
                            dao = requestDetailsDAO()
                            attlist = dao.updaterdqty(rdid, rdqty)
                            res = attlist.pop(0)
                            needdate = res[0]
                            reqid = res[1]
                            rid = res[2]
                            deliverydate = res[3]
                            status = res[4]
                            result = self.build_request_details_attributes(rdid, rdqty, needdate, deliverydate, status,
                                                                           reqid, rid)
                            return jsonify(RequestDetails=result), 200
                    elif 'status' in form:
                        status = form['status']
                        if status:
                            dao = requestDetailsDAO()
                            attlist = dao.updatestatus(rdid, status)
                            res = attlist.pop(0)
                            needdate = res[0]
                            reqid = res[1]
                            rid = res[2]
                            deliverydate = res[3]
                            rdqty = res[4]
                            result = self.build_request_details_attributes(rdid, rdqty, needdate, deliverydate, status,
                                                                           reqid, rid)
                            return jsonify(RequestDetails=result), 200
                    elif 'delivery_date' in form:
                        deliverydate = form['delivery_date']
                        if deliverydate:
                            dao = requestDetailsDAO()
                            attlist = dao.updatedeliverydate(rdid, deliverydate)
                            res = attlist.pop(0)
                            needdate = res[0]
                            reqid = res[1]
                            rid = res[2]
                            rdqty = res[3]
                            status = res[4]
                            result = self.build_request_details_attributes(rdid, rdqty, needdate, deliverydate, status,
                                                                           reqid, rid)
                            return jsonify(RequestDetails=result), 200
                    else:
                        return jsonify(Error="Unexpected attributes in update request"), 400

    def searchRequestDetails(self, args):
        RDid = args.get("RDid")
        rdqty = args.get("rdqty")
        needDate = args.get("needDate")
        deliveryDate = args.get("deliveryDate")
        status = args.get("status")
        reqId = args.get("reqId")
        dao = requestDetailsDAO()
        request_details_list = []
        if (len(args) == 5) and RDid and rdqty and needDate and deliveryDate and status:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptreqId(RDid, rdqty, needDate, deliveryDate, status)
        elif (len(args) == 5) and RDid and rdqty and needDate and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptReqStatus(RDid, rdqty, needDate, deliveryDate, reqId)
        elif (len(args) == 5) and RDid and rdqty and needDate and reqId and status:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptdeliveryDate(RDid, rdqty, needDate, reqId, status)
        elif (len(args) == 5) and RDid and rdqty and status and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptneedDate(RDid, rdqty, status, deliveryDate, reqId)
        elif (len(args) == 5) and RDid and status and needDate and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptrdqty(RDid, status, needDate, deliveryDate, reqId)
        elif (len(args) == 5) and status and rdqty and needDate and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptRDid(status, rdqty, needDate, deliveryDate, reqId)
        elif (len(args) == 4) and RDid and rdqty and needDate and deliveryDate:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptReqStatusAndreqId(RDid, rdqty, needDate, deliveryDate)
        elif (len(args) == 4) and RDid and rdqty and needDate and reqId:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptReqStatusAnddeliveryDate(RDid, rdqty, needDate, reqId)
        elif (len(args) == 4) and RDid and rdqty and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptReqStatusAndneedDate(RDid, rdqty, deliveryDate, reqId)
        elif (len(args) == 4) and RDid and needDate and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptReqStatusAndrdqty(RDid, needDate, deliveryDate, reqId)
        elif (len(args) == 4) and rdqty and needDate and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptReqStatusAndRDid(rdqty, needDate, deliveryDate, reqId)
        elif (len(args) == 4) and status and needDate and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptRDidAndrdqty(status, needDate, deliveryDate, reqId)
        elif (len(args) == 4) and status and rdqty and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptRDidAndneedDate(status, rdqty, deliveryDate, reqId)
        elif (len(args) == 4) and status and rdqty and needDate and reqId:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptRDidAnddeliveryDate(status, rdqty, needDate, reqId)
        elif (len(args) == 4) and status and rdqty and needDate and deliveryDate:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptRDidAndreqId(status, rdqty, needDate, deliveryDate)
        elif (len(args) == 4) and RDid and needDate and deliveryDate and status:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptreqIdAndrdqty(RDid, needDate, deliveryDate, status)
        elif (len(args) == 4) and RDid and rdqty and deliveryDate and status:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptreqIdAndneedDate(RDid, rdqty, deliveryDate, status)
        elif (len(args) == 4) and RDid and rdqty and needDate and status:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptreqIdAnddeliveryDate(RDid, rdqty, needDate, status)
        elif (len(args) == 4) and RDid and reqId and deliveryDate and status:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptrdqtyAndneedDate(RDid, reqId, deliveryDate, status)
        elif (len(args) == 4) and RDid and reqId and needDate and status:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptrdqtyAnddeliveryDate(RDid, reqId, needDate, status)
        elif (len(args) == 4) and RDid and reqId and rdqty and status:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptneedDateAnddeliveryDate(RDid, reqId, rdqty, status)
        elif (len(args) == 3)and RDid and rdqty and needDate:
            request_details_list = dao.getRequestDetailsByRDidAndrdqtyAndneedDate(RDid, rdqty, needDate)
        elif (len(args) == 3) and RDid and rdqty and deliveryDate:
            request_details_list = dao.getRequestDetailsByRDidAndrdqtyAnddeliveryDate(RDid, rdqty, deliveryDate)
        elif (len(args) == 3) and RDid and rdqty and status:
            request_details_list = dao.getRequestDetailsByRDidAndrdqtyAndReqStatus(RDid, rdqty, status)
        elif (len(args) == 3) and RDid and rdqty and reqId:
            request_details_list = dao.getRequestDetailsByRDidAndrdqtyAndreqId(RDid, rdqty, reqId)
        elif (len(args) == 3) and RDid and needDate and deliveryDate:
            request_details_list = dao.getRequestDetailsByRDidAndneedDateAnddeliveryDate(RDid, needDate, deliveryDate)
        elif (len(args) == 3) and RDid and needDate and status:
            request_details_list = dao.getRequestDetailsByRDidAndneedDateAndReqStatus(RDid, needDate, status)
        elif (len(args) == 3) and RDid and needDate and reqId:
            request_details_list = dao.getRequestDetailsByRDidAndneedDateAndreqId(RDid, needDate, reqId)
        elif (len(args) == 3)and RDid and deliveryDate and status:
            request_details_list = dao.getRequestDetailsByRDidAnddeliveryDateAndReqStatus(RDid, deliveryDate, status)
        elif (len(args) == 3)and RDid and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsByRDidAnddeliveryDateAndreqId(RDid, needDate, reqId)
        elif (len(args) == 3)and RDid and status and reqId:
            request_details_list = dao.getRequestDetailsByRDidAndReqStatusAndreqId(RDid, status, reqId)
        elif (len(args) == 3)and rdqty and needDate and deliveryDate:
            request_details_list = dao.getRequestDetailsByrdqtyAndneedDateAnddeliveryDate(rdqty, needDate, deliveryDate)
        elif (len(args) == 3)and rdqty and needDate and status:
            request_details_list = dao.getRequestDetailsByrdqtyAndneedDateAndReqStatus(rdqty, needDate, status)
        elif (len(args) == 3)and rdqty and needDate and reqId:
            request_details_list = dao.getRequestDetailsByrdqtyAndneedDateAndreqId(rdqty, needDate, reqId)
        elif (len(args) == 3)and rdqty and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsByrdqtyAnddeliveryDateAndreqId(rdqty, deliveryDate, reqId)
        elif (len(args) == 3)and rdqty and deliveryDate and status:
            request_details_list = dao.getRequestDetailsByrdqtyAnddeliveryDateAndReqStatus(rdqty, deliveryDate, status)
        elif (len(args) == 3)and rdqty and status and reqId:
            request_details_list = dao.getRequestDetailsByrdqtyAnddReqStatusAndreqId(rdqty, status, reqId)
        elif (len(args) == 3)and needDate and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsByneedDateAnddeliveryDateAndreqId(needDate, deliveryDate, reqId)
        elif (len(args) == 3)and needDate and deliveryDate and status:
            request_details_list = dao.getRequestDetailsByneedDateAnddeliveryDateAndReqStatus(needDate, deliveryDate, status)
        elif (len(args) == 3)and needDate and status and reqId:
            request_details_list = dao.getRequestDetailsByneedDateAndReqStatusAndreqId(needDate, status, reqId)
        elif (len(args) == 3)and deliveryDate and status and reqId:
            request_details_list = dao.getRequestDetailsBydeliveryDateAndReqStatusAndreqId(deliveryDate, status, reqId)
        elif (len(args) == 2)and RDid and rdqty:
            request_details_list = dao.getRequestDetailsByRDidAndrdqty(RDid, rdqty)
        elif (len(args) == 2)and RDid and needDate:
            request_details_list = dao.getRequestDetailsByRDidAndneedDate(RDid, needDate)
        elif (len(args) == 2)and RDid and deliveryDate:
            request_details_list = dao.getRequestDetailsByRDidAnddeliveryDate(RDid, deliveryDate)
        elif (len(args) == 2)and RDid and status:
            request_details_list = dao.getRequestDetailsByRDidAndReqStatus(RDid, status)
        elif (len(args) == 2)and RDid and reqId:
            request_details_list = dao.getRequestDetailsByRDidAndreqId(RDid, reqId)
        elif (len(args) == 2)and rdqty and needDate:
            request_details_list = dao.getRequestDetailsByrdqtyAndneedDate(rdqty, needDate)
        elif (len(args) == 2)and rdqty and deliveryDate:
            request_details_list = dao.getRequestDetailsByrdqtyAnddeliveryDate(rdqty, deliveryDate)
        elif (len(args) == 2) and rdqty and status:
            request_details_list = dao.getRequestDetailsByrdqtyAndReqStatus(rdqty, status)
        elif (len(args) == 2) and rdqty and reqId:
            request_details_list = dao.getRequestDetailsByrdqtyAndreqId(rdqty, reqId)
        elif (len(args) == 2)and needDate and deliveryDate:
            request_details_list = dao.getRequestDetailsByneedDateAnddeliveryDate(needDate, deliveryDate)
        elif (len(args) == 2) and needDate and status:
            request_details_list = dao.getRequestDetailsByneedDateAndReqStatus(needDate, status)
        elif (len(args) == 2) and needDate and reqId:
            request_details_list = dao.getRequestDetailsByneedDateAndreqId(needDate, reqId)
        elif (len(args) == 2) and deliveryDate and status:
            request_details_list = dao.getRequestDetailsBydeliveryDateAndReqStatus(deliveryDate, status)
        elif (len(args) == 2) and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsBydeliveryDateAndreqId(deliveryDate, reqId)
        elif (len(args) == 2) and status and reqId:
            request_details_list = dao.getRequestDetailsByReqStatusAndreqId(status, reqId)
        elif (len(args) == 1) and deliveryDate:
            request_details_list = dao.getRequestDetailsBydeliveryDate(deliveryDate)
        elif (len(args) == 1) and status:
            request_details_list = dao.getRequestDetailsByReqStatus(status)
        elif (len(args) == 1) and reqId:
            request_details_list = dao.getRequestDetailsByreqId(reqId)
        elif (len(args) == 1) and needDate:
            request_details_list = dao.getRequestDetailsByneedDate(needDate)
        elif (len(args) == 1) and rdqty:
            request_details_list = dao.getRequestDetailsByrdqty(rdqty)
        elif (len(args) == 1) and RDid:
            request_details_list = dao.getRequestDetailsByRDid(RDid)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in request_details_list:
            result = self.build_request_details_dict(row)
            result_list.append(result)
        return jsonify(Request_Details=result_list)

    def getRequestDetailsByRDid(self, RDid):
        dao = requestDetailsDAO()
        row = dao.getRequestDetailsByRDid(RDid)
        if not row:
            return jsonify(Error="Request Details Not Found"), 404
        else:
            print(row)
            reqDetails = self.build_request_details_dict(row)
            return jsonify(Request_Details=reqDetails)

    def getOrderByClientSearch(self, args):
        ufirstname = args.get("ufirstname")
        ulastname = args.get("ulastname")
        dao = requestDetailsDAO()
        user_list = []
        if (len(args) == 2) and (ufirstname or ulastname):
            user_list = dao.getOrderByFirstNameAndLastName(ufirstname, ulastname)
        elif (len(args) == 1) and ufirstname:
            user_list = dao.getOrderByFirstName(ufirstname)
        elif (len(args) == 1) and ulastname:
            user_list = dao.getOrderByLastName(ulastname)
        else:
            return jsonify(Error="Malformed query string"), 400
        results_list = []
        for row in user_list:
            result = self.build_order_dict(row)
            results_list.append(result)
        return jsonify(User=results_list)

    def getPaymentOfResource(self, pid):
        dao = requestDetailsDAO()
        row = dao.getPaymentOfResource(pid)
        if not row:
            return jsonify(Error="Request Details Not Found"), 404
        else:
            reqDetails = self.build_payment_dict(row)
            return jsonify(Request_Details=reqDetails)