from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json()
    query = req.get("text", "").strip()

    # This is a simplified version; use this if CX is calling without tag
    if query == "Connect":
        return jsonify({
            "fulfillment_response": {
                "messages": [{
                    "text": {
                        "text": ["To Make an Appointment go here: https://apply.wagner.nyu.edu/portal/admission_appointments?_gl=1*50yj5*_gcl_au*NDU3MTU2MDY2LjE3NTA0MjU3ODM.*_ga*MTAzNTI5MzgyMy4xNzUwNDI1Nzgz*_ga_2TJ7LPP22J*czE3NTE1Njg4NDQkbzEwJGcxJHQxNzUxNTY4ODg5JGoxNSRsMCRoMA.."]
                    }
                }]
            }
        })
    else:
        return jsonify({
            "fulfillment_response": {
                "messages": [{
                    "text": {
                        "text": ["unhandled"]
                    }
                }]
            }
        })
    
@app.route("/appointment", methods=["POST"])
def appointment():
    return jsonify({
        "fulfillment_response": {
            "messages": [{
                "text": {
                    "text": ["To Make an Appointment go here: https://apply.wagner.nyu.edu/portal/admission_appointments?_gl=1*50yj5*_gcl_au*NDU3MTU2MDY2LjE3NTA0MjU3ODM.*_ga*MTAzNTI5MzgyMy4xNzUwNDI1Nzgz*_ga_2TJ7LPP22J*czE3NTE1Njg4NDQkbzEwJGcxJHQxNzUxNTY4ODg5JGoxNSRsMCRoMA.."]
                }
            }]
        }
    })
    
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "Connection Valid"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)