from flask import request, jsonify
from config import app,db
from models import Contact


@app.route("/contacts", methods=["GET"])
def get_contacts(): #Valid any function name
    contacts = Contact.query.all() # query.all but logically you can filter when specific data only
    json_contacts = map(lambda x: x.to_json(), contacts) # lambda function भनेको shortcut तरिकाले function लेख्ने हो :
                                                         #  x variable ma contact list aucha, x.to_json() function चल्छ then contacts bhanne naya list ma data pathaidincha
    return jsonify({"contacts": json_contacts})





if __name__=="__main__":
    #create all tables
    with app.app_context():
        db.create_all()
    
    #then run app     
    app.run(debug=True)
    
    