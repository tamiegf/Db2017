from flask import Flask, jsonify, request

from handler.user import userHandler
from handler.user_address import userAddressHandler
from handler.purchase import purchaseHandler
from handler.resource_location import resourceLocationHandler
from handler.category import categoryHandler
from handler.resources import resourcesHandler
from handler.request import requestHandler
from handler.request_details import requestDetailsHandler
from handler.creditCard import creditCardHandler
from handler.Discount import DiscountHandler
from handler.Does import DoesHandler
from handler.Sales import SalesHandler


app = Flask(__name__)

# Initial page to display when app starts
@app.route('/')
def greeting():
    return 'Hello! This is the Phase 2 for the Disaster project for ICOM5016'


#################### All Possibilities for 'users' entity #######################

# Get all users
@app.route('/DisasterApp/users', methods=['GET', 'POST'])
def getAllUsers():
    if request.method == 'POST':
        # return userHandler().insertUser(request.form)
        pass
    else:
        if not request.args:
            return userHandler().getAllUsers()
        else:
            return userHandler().searchUsers(request.args)

# Get user by uid
@app.route('/DisasterApp/users/<int:uid>')
def getUserByUid(uid):
    return userHandler().getUserById(uid)

# Get user_address by user id
@app.route('/DisasterApp/users/<int:uid>/user_address')
def getUserAddressByUid(uid):
    return userHandler().getUserAddressByUid(uid)

# Get resources by user_id
@app.route('/DisasterApp/users/<int:uid>/resources')
def getResourcesByUserId(uid):
    return userHandler().getResourcesByUserId(uid)

# Get resources by user search
@app.route('/DisasterApp/users/resources')
def getResoucesByUserSearch():
    if not request.args:
        return "Please Provide Arguments."
    else:
        return userHandler().getResourcesByUserSearch(request.args)

################################################################################

#################### All Possibilities for 'user_address' entity #######################

# Get all user address
@app.route('/DisasterApp/user_address', methods=['GET', 'POST'])
def getAllUserAddress():
    if request.method == 'POST':
        #return userAddressrHandler().insertUser(request.form)
        pass
    else:
        if not request.args:
            return userAddressHandler().getAllUserAddress()
        else:
            return userAddressHandler().searchUserAddress(request.args)

# Get user address by uaid
@app.route('/DisasterApp/user_address/<int:uaid>', methods=['GET', 'POST'])
def getUserAddressById(uaid):
    return userAddressHandler().getUserAddressById(uaid)

################################################################################

#################### All Possibilities for 'purchase' entity #######################

# Get all purchases
@app.route('/DisasterApp/purchase', methods=['GET', 'POST'])
def getAllPurchases():
    if request.method == 'POST':
        pass
    else:
        if not request.args:
            return purchaseHandler().getAllPurchases()
        else:
            return purchaseHandler().searchPurchase(request.args)

# Get purchase by pid
@app.route('/DisasterApp/purchase/<int:pid>', methods=['GET', 'POST'])
def getPurchaseById(pid):
    return purchaseHandler().getPurchaseById(pid)
################################################################################

#################### All Possibilities for 'resource_location' entity #######################

# Get all resource location
@app.route('/DisasterApp/resource_location', methods=['GET', 'POST'])
def getAllResouceLocation():
    if request.method == 'POST':
        pass
    else:
        if not request.args:
            return resourceLocationHandler().getAllResourceLocation()
        else:
            return resourceLocationHandler().searchResourceLocation(request.args)

# Get purchase by pid
@app.route('/DisasterApp/resource_location/<int:rlid>', methods=['GET', 'POST'])
def getResourceLoactionById(rlid):
    return resourceLocationHandler().getResourceLocationById(rlid)

# Get a resource based on a resource location
@app.route('/DisasterApp/resources/resource_location')
def getResourceByResourceLocationSearch():
    if not request.args:
        return "Please provide arguments."
    else:
        return resourceLocationHandler().getresourceByResourceLocationSearch(request.args)

#############################################################################################

#################### All Possibilities for 'resources' entity #######################

# Get all resources
@app.route('/DisasterApp/resources', methods=['GET', 'POST'])
def getAllResources():
    if request.method == 'POST':
        pass
    else:
        if not request.args:
            return resourcesHandler().getAllResources()
        else:
            return resourcesHandler().searchResources(request.args)


# Get resources by rid
@app.route('/DisasterApp/resources/<int:rid>', methods=['GET', 'POST'])
def getResourcesByrid(rid):
    return resourcesHandler().getResourcesByrid(rid)

# Get resources by rid
@app.route('/DisasterApp/resources/available', methods=['GET', 'POST'])
def getAllResourcesAvailable():
    return resourcesHandler().getAllResourcesAvailable()

# Get resources ordered by resource name
@app.route('/DisasterApp/resources/available/orderbyname', methods=['GET', 'POST'])
def getAllResourcesOrderByName():
    if request.method == 'POST':
        pass
    else:
        if not request.args:
            return resourcesHandler().getAllResourcesOrderedByName()
        else:
            return resourcesHandler().searchResourcesOrderedByName(request.args)

# get suppliers for given resource id
@app.route('/DisasterApp/resources/<int:rid>/users')
def getSupplierByResourceId(rid):
    return resourcesHandler().getSupplierByResourceId(rid)

@app.route('/DisasterApp/resources/request_details/users')
def getOrderBySupplierSearch():
    if not request.args:
        return resourcesHandler().getAllOrderBySupplierSearch()
    else:
        return resourcesHandler().getOrderBySupplierSearch(request.args)

# http://127.0.0.1:5000/DisasterApp/resources/requested/orderbyname?rdid=31
# Get resources requested ordered by resource name
@app.route('/DisasterApp/resources/requested/orderbyname',methods=['GET', 'POST'])
def getAllResourcesRequestedOrderByName():
    if request.method == 'POST':
        pass
    else:
        if not request.args:
            return resourcesHandler().getAllResourcesRequestedOrderedByName()
        else:
            return resourcesHandler().searchResourcesRequestedOrderedByName(request.args)


# Get resources requested
@app.route('/DisasterApp/resources/requested',methods=['GET', 'POST'])
def getAllResourcesRequested():
    if request.method == 'POST':
        pass
    else:
        if not request.args:
            return resourcesHandler().getAllResourcesRequested()
        else:
            return resourcesHandler().searchResourcesRequested(request.args)


#################### All Possibilities for 'category' entity #######################

# Get all resources category
@app.route('/DisasterApp/resource_category', methods=['GET', 'POST'])
def getAllCategory():
    if request.method == 'POST':
        pass
    else:
        if not request.args:
            return categoryHandler().getAllCategory()
        else:
            return categoryHandler().searchCategory(request.args)


# Get category by cid
@app.route('/DisasterApp/resource_category/<int:cid>', methods=['GET', 'POST'])
def getCategoryBycid(cid):
    return categoryHandler().getCategoryBycid(cid)

# Get suppliers for given category name
@app.route('/DisasterApp/resource_category/users')
def getSupplierByCategorySearch():
    return categoryHandler().getSupplierByCategorySearch(request.args)

###########################################################################################

#################### All Possibilities for 'request' entity ###############################

# Get all request
@app.route('/DisasterApp/request', methods=['GET', 'POST'])
def getAllRequest():
    if request.method == 'POST':
        pass
    else:
        if not request.args:
            return requestHandler().getAllRequest()
        else:
            return requestHandler().searchRequest(request.args)


# Get request by reqId
@app.route('/DisasterApp/request/<int:reqId>', methods=['GET', 'POST'])
def getRequestByreqId(reqId):
    return requestHandler().getRequestByreqId(reqId)

###########################################################################################


#################### All Possibilities for 'request_details' entity #######################
# Get all request details
@app.route('/DisasterApp/request_details', methods=['GET', 'POST'])
def getAllRequestDetails():
    if request.method == 'POST':
        pass
    else:
        if not request.args:
            return requestDetailsHandler().getAllRequestDetails()
        else:
            return requestDetailsHandler().searchRequestDetails(request.args)


# Get request details by rdid
@app.route('/DisasterApp/request_details/<int:RDid>', methods=['GET', 'POST'])
def getRequestDetailsByRDid(RDid):
    return requestDetailsHandler().getRequestDetailsByRDid(RDid)

@app.route('/DisasterApp/request_details/users')
def getOrderByClientSearch():
    return requestDetailsHandler().getOrderByClientSearch(request.args)
###########################################################################################

#################### All Possibilities for 'creditCard' entity #######################

# Get all credit cards
@app.route('/DisasterApp/creditCard', methods=['GET', 'POST'])
def getAllCreditCards():
    if request.method == 'POST':
        #return userAddressrHandler().insertCreditCard(request.form)
        pass
    else:
        if not request.args:
            return creditCardHandler().getAllCreditCard()
        else:
            return creditCardHandler().searchCreditCard(request.args)

# Get credit card by ccid
@app.route('/DisasterApp/creditCard/<int:ccid>', methods=['GET', 'POST'])
def getCreditCardByCCID(ccid):
    return creditCardHandler().getCreditCardByCCID(ccid)

#Get credit Card by ccNumber
@app.route('/DisasterApp/creditCard/<int:ccNumber>', methods=['GET', 'POST'])
def getCreditCardByccNumber(ccNumber):
    return creditCardHandler().getCreditCardByccNumber(ccNumber)

#Get credit card by ccExpirationDate
@app.route('/DisasterApp/creditCard/<int:ccExpirationDate>', methods=['GET', 'POST'])
def getCreditCardByExpirationDate(ccExpirationDate):
    return creditCardHandler().getCreditCardByExpirationDate(ccExpirationDate)

################################################################################

#################### All Possibilities for 'Discount' entity #######################

# Get all discounts
@app.route('/DisasterApp/Discount', methods=['GET', 'POST'])
def getAllDiscount():
    if request.method == 'POST':
        pass
    else:
        if not request.args:
            return DiscountHandler().getAllDiscount()
        else:
            return DiscountHandler().searchDiscount(request.args)

# Get discount by did
@app.route('/DisasterApp/Discount/<int:did>', methods=['GET', 'POST'])
def getDiscountById(did):
    return DiscountHandler().getDiscountBydid(did)

################################################################################

########################All possibilities for Does#############################
@app.route('/DisasterApp/Does')
def getAllDoes():
    if request.method == 'POST':
        pass
    else:
        if not request.args:
            return DoesHandler().getAllDoes()
        else:
            return DoesHandler().searchDoes(request.args)
#################################################################################

###################All possibilities for Sales######################################

@app.route('/DisasterApp/Sales', methods=['GET', 'POST'])
def getAllSales():
    if request.method == 'POST':
        pass
    else:
        if not request.args:
            return SalesHandler().getAllSales()
        else:
            return SalesHandler().searchSales(request.args)

# Get Sales by sid
@app.route('/DisasterApp/Sales/<int:sid>', methods=['GET', 'POST'])
def getSalesBysid(sid):
    return SalesHandler().getSalesBysid(sid)
#################################################################################

# Run the app
if __name__ == '__main__':
    app.run()