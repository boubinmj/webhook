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
                                "To make an appointment, visit the: <a href='https://apply.wagner.nyu.edu/portal/admission_appointments?...'>Appointment Portal</a>"
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
                   "text": [
                                "To make an appointment, visit the <a href='https://apply.wagner.nyu.edu/portal/admission_appointments?...'>Admissions Appointmnet Portal</a>"
                            ]
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
                    "text": ["Visit the Wagner website to make an <a href='https://wagner.nyu.edu/admissions/visit-us/connections'>appointment with Students and Alumni</a>"]
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
                    "text": ["Schedule a <a href='https://connect.nyu.edu/portal/grad_tours'>Campus Tour</a>"]
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
                    "text": ["Attend an Admissions Event \
                              <a href='https://apply.wagner.nyu.edu/portal/admission-events?_gl=1*9fyl4r*_gcl_au*MTYxMTAyMjMzOS4xNzUxNzE2OTg3*_ga*NDMwNzc0Nzg3LjE3Mjc5OTkwOTk.*_ga_2TJ7LPP22J*czE3NTI1NDE1MDgkbzE0JGcxJHQxNzUyNTQxNzI4JGo3JGwwJGgw'>Admissions Event</a> \
                             \n\nView <a href='https://wagner.nyu.edu/admissions/connect-with-us/admissions-events-recordings'>Event Recordings</a>"]
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
                    "text": ["To understand visa requirements please visit the "
                    "<a href='https://www.nyu.edu/students/student-information-and-resources/student-visa-and-immigration.html'>Office of Global Services</a>"]
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
                    "text": ["View or change your \
                              <a href='https://wagner.nyu.edu/portal/students/academics/registration/ft-or-pt'>Enrollment Status</a>"]
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
                    "text": ["Check your \
                             <a href='https://www.nyu.edu/students/student-information-and-resources/student-visa-and-immigration/current-students/visa-and-academic-changes.html'>Visa Status</a>"]
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
                    "text": ["US International Students - "
                    "<a href='https://www.nyu.edu/students/student-information-and-resources/student-visa-and-immigration/current-students/know-your-rights.html'>Know Your Rights</a>"]
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