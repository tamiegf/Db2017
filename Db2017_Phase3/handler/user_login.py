from flask import jsonify
from dao.user_login import userLoginDAO

class userLoginHandler:

    # Create a dictionary of user_logins
    def build_userLogin_dict(self, row):
        result = {}
        result['lid'] = row[0]
        result['user_name'] = row[1]
        result['user_password'] = row[2]
        result['uid'] = row[3]
        return result

    def getAllUserLogin(self):
        dao = userLoginDAO()
        userLogin_list = dao.getAllUserLogin()
        results_list = []
        for row in userLogin_list:
            result = self.build_userLogin_dict(row)
            results_list.append(result)
        return jsonify(User_Login=results_list)

    def searchUserLogin(self, args):
        user_name = args.get('user_name')
        user_password = args.get('user_password')
        dao = userLoginDAO()
        results_list = []
        if(len(args) == 2) and (user_name or user_password):
            results_list = dao.getUserLoginByNameAndPassword(user_name, user_password)
        elif(len(args) == 1) and user_name:
            results_list = dao.getUserLoginByName(user_name)
        elif(len(args) == 1) and user_password:
            results_list = dao.getUserLoginByPassword(user_password)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in results_list:
            result = self.build_userLogin_dict(row)
            result_list.append(result)
        return jsonify(User_Login=result_list)

    def getUserLoginByUid(self, uid):
        dao = userLoginDAO()
        row = dao.getUserLoginByUid(uid)
        if not row:
            return jsonify(Error="User_Login not found."), 404
        else:
            result = self.build_userLogin_dict(row)
            return jsonify(User_Login=result)
