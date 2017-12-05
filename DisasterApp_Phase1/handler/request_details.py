from flask import jsonify
from dao.request_details import requestDetailsDAO

class requestDetailsHandler:

    # Create a dictionary of request
    def build_request_details_dict(self, row):
        result = {}
        result['RDid'] = row[0]
        result['qtyNeeded'] = row[1]
        result['needDate'] = row[2]
        result['deliveryDate'] = row[3]
        result['ReqStatus'] = row[4]
        result['reqId'] = row[5]
        return result


    def getAllRequestDetails(self):
        dao = requestDetailsDAO()
        request_details_list = dao.getAllRequestDetails()
        results_list = []
        for row in request_details_list:
            result = self.build_request_details_dict(row)
            results_list.append(result)
        return jsonify(Request_Details=results_list)

    def searchRequestDetails(self, args):
        RDid = args.get("RDid")
        qtyNeeded = args.get("qtyNeeded")
        needDate = args.get("needDate")
        deliveryDate = args.get("deliveryDate")
        ReqStatus = args.get("ReqStatus")
        reqId = args.get("reqId")
        dao = requestDetailsDAO()
        request_details_list = []
        if (len(args) == 6) and RDid and qtyNeeded and needDate and deliveryDate and ReqStatus and reqId:
            request_details_list = dao.getRequestDetailsWithAllAttributes(RDid, qtyNeeded, needDate, deliveryDate, ReqStatus, reqId)
        elif (len(args) == 5) and RDid and qtyNeeded and needDate and deliveryDate and ReqStatus:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptreqId(RDid, qtyNeeded, needDate, deliveryDate, ReqStatus)
        elif (len(args) == 5) and RDid and qtyNeeded and needDate and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptReqStatus(RDid, qtyNeeded, needDate, deliveryDate, reqId)
        elif (len(args) == 5) and RDid and qtyNeeded and needDate and reqId and ReqStatus:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptdeliveryDate(RDid, qtyNeeded, needDate, reqId, ReqStatus)
        elif (len(args) == 5) and RDid and qtyNeeded and ReqStatus and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptneedDate(RDid, qtyNeeded, ReqStatus, deliveryDate, reqId)
        elif (len(args) == 5) and RDid and ReqStatus and needDate and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptqtyNeeded(RDid, ReqStatus, needDate, deliveryDate, reqId)
        elif (len(args) == 5) and ReqStatus and qtyNeeded and needDate and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptRDid(ReqStatus, qtyNeeded, needDate, deliveryDate, reqId)
        elif (len(args) == 4) and RDid and qtyNeeded and needDate and deliveryDate:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptReqStatusAndreqId(RDid, qtyNeeded, needDate, deliveryDate)
        elif (len(args) == 4) and RDid and qtyNeeded and needDate and reqId:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptReqStatusAnddeliveryDate(RDid, qtyNeeded, needDate, reqId)
        elif (len(args) == 4) and RDid and qtyNeeded and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptReqStatusAndneedDate(RDid, qtyNeeded, deliveryDate, reqId)
        elif (len(args) == 4) and RDid and needDate and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptReqStatusAndqtyNeeded(RDid, needDate, deliveryDate, reqId)
        elif (len(args) == 4) and qtyNeeded and needDate and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptReqStatusAndRDid(qtyNeeded, needDate, deliveryDate, reqId)
        elif (len(args) == 4) and ReqStatus and needDate and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptRDidAndqtyNeeded(ReqStatus, needDate, deliveryDate, reqId)
        elif (len(args) == 4) and ReqStatus and qtyNeeded and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptRDidAndneedDate(ReqStatus, qtyNeeded, deliveryDate, reqId)
        elif (len(args) == 4) and ReqStatus and qtyNeeded and needDate and reqId:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptRDidAnddeliveryDate(ReqStatus, qtyNeeded, needDate, reqId)
        elif (len(args) == 4) and ReqStatus and qtyNeeded and needDate and deliveryDate:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptRDidAndreqId(ReqStatus, qtyNeeded, needDate, deliveryDate)
        elif (len(args) == 4) and RDid and needDate and deliveryDate and ReqStatus:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptreqIdAndqtyNeeded(RDid, needDate, deliveryDate, ReqStatus)
        elif (len(args) == 4) and RDid and qtyNeeded and deliveryDate and ReqStatus:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptreqIdAndneedDate(RDid, qtyNeeded, deliveryDate, ReqStatus)
        elif (len(args) == 4) and RDid and qtyNeeded and needDate and ReqStatus:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptreqIdAnddeliveryDate(RDid, qtyNeeded, needDate, ReqStatus)
        elif (len(args) == 4) and RDid and reqId and deliveryDate and ReqStatus:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptqtyNeededAndneedDate(RDid, reqId, deliveryDate, ReqStatus)
        elif (len(args) == 4) and RDid and reqId and needDate and ReqStatus:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptqtyNeededAnddeliveryDate(RDid, reqId, needDate, ReqStatus)
        elif (len(args) == 4) and RDid and reqId and qtyNeeded and ReqStatus:
            request_details_list = dao.getRequestDetailsByAllAttributesExceptneedDateAnddeliveryDate(RDid, reqId, qtyNeeded, ReqStatus)
        elif (len(args) == 3)and RDid and qtyNeeded and needDate:
            request_details_list = dao.getRequestDetailsByRDidAndqtyNeededAndneedDate(RDid, qtyNeeded, needDate)
        elif (len(args) == 3) and RDid and qtyNeeded and deliveryDate:
            request_details_list = dao.getRequestDetailsByRDidAndqtyNeededAnddeliveryDate(RDid, qtyNeeded, deliveryDate)
        elif (len(args) == 3) and RDid and qtyNeeded and ReqStatus:
            request_details_list = dao.getRequestDetailsByRDidAndqtyNeededAndReqStatus(RDid, qtyNeeded, ReqStatus)
        elif (len(args) == 3) and RDid and qtyNeeded and reqId:
            request_details_list = dao.getRequestDetailsByRDidAndqtyNeededAndreqId(RDid, qtyNeeded, reqId)
        elif (len(args) == 3) and RDid and needDate and deliveryDate:
            request_details_list = dao.getRequestDetailsByRDidAndneedDateAnddeliveryDate(RDid, needDate, deliveryDate)
        elif (len(args) == 3) and RDid and needDate and ReqStatus:
            request_details_list = dao.getRequestDetailsByRDidAndneedDateAndReqStatus(RDid, needDate, ReqStatus)
        elif (len(args) == 3) and RDid and needDate and reqId:
            request_details_list = dao.getRequestDetailsByRDidAndneedDateAndreqId(RDid, needDate, reqId)
        elif (len(args) == 3)and RDid and deliveryDate and ReqStatus:
            request_details_list = dao.getRequestDetailsByRDidAnddeliveryDateAndReqStatus(RDid, deliveryDate, ReqStatus)
        elif (len(args) == 3)and RDid and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsByRDidAnddeliveryDateAndreqId(RDid, needDate, reqId)
        elif (len(args) == 3)and RDid and ReqStatus and reqId:
            request_details_list = dao.getRequestDetailsByRDidAndReqStatusAndreqId(RDid, ReqStatus, reqId)
        elif (len(args) == 3)and qtyNeeded and needDate and deliveryDate:
            request_details_list = dao.getRequestDetailsByqtyNeededAndneedDateAnddeliveryDate(qtyNeeded, needDate, deliveryDate)
        elif (len(args) == 3)and qtyNeeded and needDate and ReqStatus:
            request_details_list = dao.getRequestDetailsByqtyNeededAndneedDateAndReqStatus(qtyNeeded, needDate, ReqStatus)
        elif (len(args) == 3)and qtyNeeded and needDate and reqId:
            request_details_list = dao.getRequestDetailsByqtyNeededAndneedDateAndreqId(qtyNeeded, needDate, reqId)
        elif (len(args) == 3)and qtyNeeded and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsByqtyNeededAnddeliveryDateAndreqId(qtyNeeded, deliveryDate, reqId)
        elif (len(args) == 3)and qtyNeeded and deliveryDate and ReqStatus:
            request_details_list = dao.getRequestDetailsByqtyNeededAnddeliveryDateAndReqStatus(qtyNeeded, deliveryDate, ReqStatus)
        elif (len(args) == 3)and qtyNeeded and ReqStatus and reqId:
            request_details_list = dao.getRequestDetailsByqtyNeededAnddReqStatusAndreqId(qtyNeeded, ReqStatus, reqId)
        elif (len(args) == 3)and needDate and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsByneedDateAnddeliveryDateAndreqId(needDate, deliveryDate, reqId)
        elif (len(args) == 3)and needDate and deliveryDate and ReqStatus:
            request_details_list = dao.getRequestDetailsByneedDateAnddeliveryDateAndReqStatus(needDate, deliveryDate, ReqStatus)
        elif (len(args) == 3)and needDate and ReqStatus and reqId:
            request_details_list = dao.getRequestDetailsByneedDateAndReqStatusAndreqId(needDate, ReqStatus, reqId)
        elif (len(args) == 3)and deliveryDate and ReqStatus and reqId:
            request_details_list = dao.getRequestDetailsBydeliveryDateAndReqStatusAndreqId(deliveryDate, ReqStatus, reqId)
        elif (len(args) == 2)and RDid and qtyNeeded:
            request_details_list = dao.getRequestDetailsByRDidAndqtyNeeded(RDid, qtyNeeded)
        elif (len(args) == 2)and RDid and needDate:
            request_details_list = dao.getRequestDetailsByRDidAndneedDate(RDid, needDate)
        elif (len(args) == 2)and RDid and deliveryDate:
            request_details_list = dao.getRequestDetailsByRDidAnddeliveryDate(RDid, deliveryDate)
        elif (len(args) == 2)and RDid and ReqStatus:
            request_details_list = dao.getRequestDetailsByRDidAndReqStatus(RDid, ReqStatus)
        elif (len(args) == 2)and RDid and reqId:
            request_details_list = dao.getRequestDetailsByRDidAndreqId(RDid, reqId)
        elif (len(args) == 2)and qtyNeeded and needDate:
            request_details_list = dao.getRequestDetailsByqtyNeededAndneedDate(qtyNeeded, needDate)
        elif (len(args) == 2)and qtyNeeded and deliveryDate:
            request_details_list = dao.getRequestDetailsByqtyNeededAnddeliveryDate(qtyNeeded, deliveryDate)
        elif (len(args) == 2) and qtyNeeded and ReqStatus:
            request_details_list = dao.getRequestDetailsByqtyNeededAndReqStatus(qtyNeeded, ReqStatus)
        elif (len(args) == 2) and qtyNeeded and reqId:
            request_details_list = dao.getRequestDetailsByqtyNeededAndreqId(qtyNeeded, reqId)
        elif (len(args) == 2)and needDate and deliveryDate:
            request_details_list = dao.getRequestDetailsByneedDateAnddeliveryDate(needDate, deliveryDate)
        elif (len(args) == 2) and needDate and ReqStatus:
            request_details_list = dao.getRequestDetailsByneedDateAndReqStatus(needDate, ReqStatus)
        elif (len(args) == 2) and needDate and reqId:
            request_details_list = dao.getRequestDetailsByneedDateAndreqId(needDate, reqId)
        elif (len(args) == 2) and deliveryDate and ReqStatus:
            request_details_list = dao.getRequestDetailsBydeliveryDateAndReqStatus(deliveryDate, ReqStatus)
        elif (len(args) == 2) and deliveryDate and reqId:
            request_details_list = dao.getRequestDetailsBydeliveryDateAndreqId(deliveryDate, reqId)
        elif (len(args) == 2) and ReqStatus and reqId:
            request_details_list = dao.getRequestDetailsByReqStatusAndreqId(ReqStatus, reqId)
        elif (len(args) == 1) and deliveryDate:
            request_details_list = dao.getRequestDetailsBydeliveryDate(deliveryDate)
        elif (len(args) == 1) and ReqStatus:
            request_details_list = dao.getRequestDetailsByReqStatus(ReqStatus)
        elif (len(args) == 1) and reqId:
            request_details_list = dao.getRequestDetailsByreqId(reqId)
        elif (len(args) == 1) and needDate:
            request_details_list = dao.getRequestDetailsByneedDate(needDate)
        elif (len(args) == 1) and qtyNeeded:
            request_details_list = dao.getRequestDetailsByqtyNeeded(qtyNeeded)
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