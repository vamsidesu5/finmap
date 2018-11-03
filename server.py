from flask import Flask, request, jsonify, render_template, send_from_directory, send_file
from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId
import pymongo
import os
import nessie

application = Flask(__name__)
client = MongoClient("ds151383.mlab.com:51383",51383)
db = client["finmap"]
db.authenticate("admin","finmap123");
# static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'public')

@application.route('/accounts/{id}/purchases', methods=['GET'])
def purchases():
    user_info = request.form.to_dict();
    
    })
})






@application.route('/analytics', methods=['GET'])
def analytics():
    # print(static_file_dir)
    print("hi")
    return render_template("analytics.html")
@application.route('/getappointment', methods=['GET'])
def get_appointment():
    lst = []
    for a in db.appointments.find({}):
        print(a["_id"])
        lst.append({
            "name" : db.users.find_one({"_id":ObjectId(a["user-id"])})["name"],
            "operations" : a["operations"],
            "start_time": a["start_time"],
            "end_time": a["end_time"],
        })
    return jsonify(lst)
@application.route('/makeuser', methods=['POST'])
def make_user():
    user_info = request.form.to_dict()
    db.users.insert_one({
        "name" : user_info["name"],
        "dob" : user_info["dob"],
        "email" : user_info["email"],
        "number" : user_info["number"]
    })
    return jsonify("Success!")
@application.route('/users', methods=['GET'])
def users():
    users = db.users.find({})
    u = []
    for user in users:
        u.append({
            "name" : user["name"],
            "dob" : user["dob"],
            "email" : user["email"],
            "number" : user["number"]
        })
    return jsonify(u)
@application.route('/makeappointment', methods=['POST'])
def make_appointment():
    appointment_info = request.form.to_dict()
    print(appointment_info)
    print(appointment_info["name"])
    user_id = db.users.find_one({"name":appointment_info["name"]})
    print("OK",user_id)
    if(user_id == None):
        usr = db.users.insert_one({
            "name" : appointment_info["name"],
            "dob" : appointment_info["dob"],
            "email" : appointment_info["email"],
            "number" : appointment_info["number"]
        })
        print(usr)
        user_id = db.users.find_one({"name" : appointment_info["name"]})["_id"]
    else:
        user_id = user_id["_id"]
    print(user_id)
    db.appointments.insert_one({
        "user-id" : user_id,
        "operations" : appointment_info["operations"],
        "start_time": appointment_info["start_time"],
        "end_time": appointment_info["end_time"],
    })
    return jsonify(appointment_info)
 # @application.route('/getwaittime', methods=['POST'])
 # def make_waittime():
 #     waittimedetails = request.form.to_dict()
 #     user_id = db.appointments.find_one("name":appointment_info["name"]})["_id"]
 #     db.appointments.insert_one({
 #         "waittime" : waittimedetails,
 #         "operations" : appointment_info["operations"],
 #         "start_time": appointment_info["operations"]
 #     })
 #     return jsonify(appointment_info)
@application.route('/tardies', methods=['POST'])
def list_tardies():
    tardy_info = request.form.to_dict()
    user_id = db.users.find_one({"name":tardy_info["name"]})
    db.usrs.update({"username":user_id},{"$inc":{
        "tardies":{ quantity: 1}
    }})
    return jsonify(tardy_info)


if __name__ == '__main__':
    application.run(host='0.0.0.0',debug=True)
