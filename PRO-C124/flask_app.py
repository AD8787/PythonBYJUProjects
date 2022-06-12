from flask import Flask, jsonify, request

app = Flask(__name_)

contact_list = [
    {
        "ID": "1",
        "Name": "Raju",
        "Contact": "9987644456",
        "Done": False
    },

    {
        "ID": "2",
        "Name": "Rahul",
        "Contact": "9876543222",
        "Done": False
    }
]

@app.route("/")
@app.route("/add_data", method = "POST")

def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data"
        }, 400)

    contact = {
        "ID": tasks[-1]["ID"] + 1,
        "Name": request.json["Name"],
        "Contact": request.json.get("Contact", ""),
        "Done": False
    }

    contact_list.append(contact)
    return jsonify({
        "status": "success",
        "message": "Contact added"
    })

@app.route("/get-data")

def get_task():
    return jsonify({
        "data" : contact_list
    }) 

if (__name__ == "__main__"):
    app.run(debug = True)