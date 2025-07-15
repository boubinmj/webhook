from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])

## Webhook Payload Test
## Only works with GoogleDialogflowCX Playbook Structure
def webhook():
    req = request.get_json()
    query = req.get("text", "").strip()

    # This is a simplified version; use this if CX is calling without tag
    if query == "Connect":
        return jsonify({
            "fulfillment_response": {
                "messages": [{
                    "text": {
                        "text": [
                                "To make an appointment, visit: <a href='https://apply.wagner.nyu.edu/portal/admission_appointments?...'>this link</a>"
                            ]
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

##############################################
######### CONNECT WITH US ####################
##############################################
# https://wagner.nyu.edu/admissions/connect-with-us

## Speak to an admissions counselor
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

## Connect with Students and Alumni
@app.route("/studentAlumni", methods=["POST"])
def studentAlumni():
    return jsonify({
        "fulfillment_response": {
            "messages": [{
                "text": {
                    "text": ["Connect with Students and Alumni: https://wagner.nyu.edu/admissions/visit-us/connections"]
                }
            }]
        }
    })

## Tour Campus
@app.route("/tour", methods=["POST"])
def tour():
    return jsonify({
        "fulfillment_response": {
            "messages": [{
                "text": {
                    "text": ["Schedule a Campus Tour: https://connect.nyu.edu/portal/grad_tours"]
                }
            }]
        }
    })

## Attend a Campus Event
@app.route("/event", methods=["POST"])
def event():
    return jsonify({
        "fulfillment_response": {
            "messages": [{
                "text": {
                    "text": ["Attend an Admissions Event: https://apply.wagner.nyu.edu/portal/admission-events?_gl=1*9fyl4r*_gcl_au*MTYxMTAyMjMzOS4xNzUxNzE2OTg3*_ga*NDMwNzc0Nzg3LjE3Mjc5OTkwOTk.*_ga_2TJ7LPP22J*czE3NTI1NDE1MDgkbzE0JGcxJHQxNzUyNTQxNzI4JGo3JGwwJGgw\n\nEvent Recordings: [https://wagner.nyu.edu/admissions/connect-with-us/admissions-events-recordings]"]
                }
            }]
        }
    })

##############################################
######### VISA PAGE ##########################
##############################################
# https://wagner.nyu.edu/portal/students/incoming/getting-started/international/visa-requirements

## Understand your visa requirements
@app.route("/requirementsVisa", methods=["POST"])
def requirementsVisa():
    return jsonify({
        "fulfillment_response": {
            "messages": [{
                "text": {
                    "text": ["Office of Global Services: https://www.nyu.edu/students/student-information-and-resources/student-visa-and-immigration.html"]
                }
            }]
        }
    })

## Change Your Enrollment Status
@app.route("/enrollmentStatus", methods=["POST"])
def enrollmentStatus():
    return jsonify({
        "fulfillment_response": {
            "messages": [{
                "text": {
                    "text": ["Change your Enrollment Status: https://wagner.nyu.edu/portal/students/academics/registration/ft-or-pt"]
                }
            }]
        }
    })

## Understand your visa requirements
@app.route("/visaStatus", methods=["POST"])
def visaStatus():
    return jsonify({
        "fulfillment_response": {
            "messages": [{
                "text": {
                    "text": ["Visa Status: https://www.nyu.edu/students/student-information-and-resources/student-visa-and-immigration/current-students/visa-and-academic-changes.html"]
                }
            }]
        }
    })

## Understand your visa requirements
@app.route("/digitalPrivacy", methods=["POST"])
def digitalPrivacy():
    return jsonify({
        "fulfillment_response": {
            "messages": [{
                "text": {
                    "text": ["Know your rights: https://www.nyu.edu/students/student-information-and-resources/student-visa-and-immigration/current-students/know-your-rights.html"]
                }
            }]
        }
    })


##############################################
######### HEALTH #############################
##############################################

## HealthCheck
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "Connection Valid"}), 200

## Main Method
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)