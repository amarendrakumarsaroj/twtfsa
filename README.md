This is Tech With Tim Full stack App


npm create vite@latest frontend -- --template react --> select React --> Javascript
cd frontend
npm install 



cd backend
pip install Flask, Flask-SQLAlchemy, flask-cors


@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify("contacts":json_contacts)


@app.route("/contacts", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName"),
    last_name = request.json.get("lastName"),
    email = request.json.get("email")

    #check if कुनै entry garena bhane
    if not first_name or not last_name or not email:
        return (
            jsonify({"message":"firstname or lastname or email not entered"}), 400
        )
    
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)

    #try-catch block
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    #सबै कुरा ठिक हुँदा चाहिं
    return jsonify({"message":"User Created!"}), 201
    
    # you can check on postman

