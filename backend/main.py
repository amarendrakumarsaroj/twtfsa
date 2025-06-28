from flask import request, jsonify
from config import app,db
from models import Contact


@app.route("/contacts", methods=["GET"])
def get_contacts(): #Valid any function name
    contacts = Contact.query.all() # query.all but logically you can filter when specific data only
    json_contacts = list(map(lambda x: x.to_json(), contacts)) # lambda function भनेको shortcut तरिकाले function लेख्ने हो :
                                                               #  x variable ma contact list aucha, x.to_json() function चल्छ then contacts bhanne naya list ma data pathaidincha
    return jsonify({"contacts": json_contacts})

@app.route("/contacts", methods=["POST"])
def create_contacts():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")
    if not first_name or not last_name or not email:
        return (
            jsonify({"message": "You must include a first name , last name or email"}), 400,
        )
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)   
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    return jsonify({"message": "User Created!"}), 201 

 # Update a contact
@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    contact_to_update = Contact.query.get(user_id)
    
    if not contact_to_update:
        return jsonify({"message": "User Not Found"}), 404
    data = request.json
    contact_to_update.first_name = data.get("firstName", contact_to_update.first_name)
    contact_to_update.last_name = data.get("lastName", contact_to_update.last_name)
    contact_to_update.email = data.get("email", contact_to_update.email)
    db.session.commit()
    return jsonify({
        "message": "User Updated"
    }), 200

@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    contact_to_delete = Contact.query.get(user_id)
    if not contact_to_delete:
        return jsonify({
            "error":"User Not Found"
        }), 404
    db.session.delete(contact_to_delete)
    db.session.commit()
    return jsonify({"message":"User Deleted!"}),200    
        

if __name__=="__main__":
    #create all tables
    with app.app_context():
        db.create_all()
    
    #then run app     
    app.run(debug=True)
    
    