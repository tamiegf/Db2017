from flask import Flask, jsonify, request

from handler.resources import resourcesHandler
from handler.category import categoryHandler
from handler.user import userHandler
from handler.request import requestHandler
from handler.request_details import requestDetailsHandler
from handler.purchase import purchaseHandler


app = Flask(__name__)

# Initial page to display when app starts
@app.route('/')
def greeting():
    return 'Hello! This is the Phase 1 for the Disaster project for ICOM5016'


# All Possibilities for users entity
# Get all users
@app.route('/DisasterApp/users')
def getAllUsers():
    if not request.args:
        return userHandler().getAllUsers()
    else:
        return userHandler().searchUsers(request.args)

# Get user by uid
@app.route('/DisasterApp/users/<int:uId>')
def getUserByUid(uId):
    return userHandler().getUserByUid(uId)

@app.route('/DisasterApp/users/<int:uId>/request')
def getRequestByUserId(uId):
    return userHandler().getRequestByUserId(uId)

@app.route('/DisasterApp/users/<int:uId>/purchase')
def getPurchaseByUserId(uId):
    return userHandler().getPurchaseByUserId(uId)

@app.route('/DisasterApp/users/<int:uId>/resources')
def getResourcesByUserId(uId):
    return userHandler().getResourcesByUserId(uId)


#########################################
# All possibilities for resources entity
@app.route('/DisasterApp/resources')
def getAllResources():
    if not request.args:
        return resourcesHandler().getAllResources()
    else:
        return resourcesHandler().searchResources(request.args)

@app.route('/DisasterApp/resources/<int:rid>')
def getResourcesByRid(rid):
    return resourcesHandler().getResourcesByRid(rid)

@app.route('/DisasterApp/resources/<int:rid>/users')
def getUserByRid(rid):
    return resourcesHandler().getUserByRid(rid)

@app.route('/DisasterApp/resources/<int:rid>/category')
def getCategoryByRid(rid):
    return resourcesHandler().getCategoryByRid(rid)

@app.route('/DisasterApp/resources/<int:rid>/request_details')
def getReqDetailByRid(rid):
    return resourcesHandler().getReqDetailByRid(rid)

##########################################
# All possibilities for purchase entity
@app.route('/DisasterApp/purchase')
def getAllPurchase():
    if not request.args:
        return purchaseHandler().getAllPurchase()
    else:
        return purchaseHandler().searchPurchase(request.args)

@app.route('/DisasterApp/purchase/<int:pid>')
def getPurchaseByPid(pid):
    return purchaseHandler().getPurchaseByPid(pid)

@app.route('/DisasterApp/purchase/<int:pid>/user')
def getUserByPid(pid):
    return purchaseHandler().getUserByPid(pid)




##########################################
# All possibilities for category entity
@app.route('/DisasterApp/category')
def getAllCategory():
    if not request.args:
        return categoryHandler().getAllCategory()
    else:
        return categoryHandler().searchCategory(request.args)

# Get category by cid
# Not Enabled in phase 1
@app.route('/DisasterApp/category/<int:cid>')
def getCategoryBycid(cid):
    return categoryHandler().getCategoryBycid(cid)


###############################################
# All possibilities for request entity
@app.route('/DisasterApp/request')
def getAllRequest():
    if not request.args:
        return requestHandler().getAllRequest()
    else:
        return requestHandler().searchRequest(request.args)


# Get request by reqId
@app.route('/DisasterApp/request/<int:reqId>')
def getRequestByreqId(reqId):
    return requestHandler().getRequestByreqId(reqId)



###############################################
# All possibilities for request details entity
@app.route('/DisasterApp/request_details')
def getAllRequestDetails():
    if not request.args:
        return requestDetailsHandler().getAllRequestDetails()
    else:
        return requestDetailsHandler().searchRequestDetails(request.args)

# Get request details by RDid
#Not enabled on phase 1
@app.route('/DisasterApp/request_details/<int:RDid>')
def getRequestDetailsByreqId(RDid):
    return requestDetailsHandler().getRequestDetailsByRDid(RDid)


# Run the app
if __name__ == '__main__':
    app.run()