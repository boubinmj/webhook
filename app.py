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
                                "To make an appointment with our admissions officers, please visit the <a href='https://apply.wagner.nyu.edu/portal/admission_appointments?...'><strong>Admissions Appointmnet Portal</strong></a>"
                            ]
                }
            }]
        }
    })

## Visit A Class
@app.route("/visitClass", methods=["POST"])
def visitClass():
    return jsonify({
        "fulfillment_response": {
            "messages": [{
                "text": {
                   "text": [
                                "Sit in on a course to experience the classroom, meet current students, and learn from NYU Wagner's dynamic faculty. \
                                      Most classes are conveniently offered in the evening. Class visits are subject to availability and offered on a first-come, first-served basis. \
                                      Prospective students can register for up to two class visits per semester.Class visits will resume in the Fall."
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
                    "text": ["To hear first-hand about the NYU Wagner student experience and the value of our graduate degrees from current students or one of our over 15,000 alumni throughout the United States and around the world.  \
                             Visit the Wagner website to make an <a href='https://wagner.nyu.edu/admissions/visit-us/connections'><strong>Appointment with Students and Alumni</strong></a>."]
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
                    "text": ["See what it's like to study in our unique urban setting! The university offers tours of the Washington Square campus to prospective graduate and professional school students throughout the year.  \
                             Visit the <a href='https://connect.nyu.edu/portal/grad_tours'><strong>graduate admissions portal</strong></a> to schedule a campus tour!"]
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
                    "text": ["Check out our events page for a listing of our upcoming public admissions events on the \
                              <a href='https://apply.wagner.nyu.edu/portal/admission-events?_gl=1*9fyl4r*_gcl_au*MTYxMTAyMjMzOS4xNzUxNzE2OTg3*_ga*NDMwNzc0Nzg3LjE3Mjc5OTkwOTk.*_ga_2TJ7LPP22J*czE3NTI1NDE1MDgkbzE0JGcxJHQxNzUyNTQxNzI4JGo3JGwwJGgw'><strong>Wagner Events Page</strong></a>! \
                             \n\nOr to access content any time, check out <a href='https://wagner.nyu.edu/admissions/connect-with-us/admissions-events-recordings'><strong>event recordings</strong></a> of past admissions events."]
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
                    "<a href='https://www.nyu.edu/students/student-information-and-resources/student-visa-and-immigration.html'><strong>Office of Global Services</strong></a>."]
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
                    "text": ["To view or change your enrollment status please visit the \
                              <a href='https://wagner.nyu.edu/portal/students/academics/registration/ft-or-pt'><strong>Wagner Registration Portal</strong></a>."]
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
                    "text": ["To check or update your visa status, please use the resources provided by the \
                             <a href='https://www.nyu.edu/students/student-information-and-resources/student-visa-and-immigration/current-students/visa-and-academic-changes.html'><strong>Office of Global Services</strong></a>."]
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
                    "text": ["For information privacy guidance as it relates to US International Students, please refer to the "
                    "<a href='https://www.nyu.edu/students/student-information-and-resources/student-visa-and-immigration/current-students/know-your-rights.html'><strong>Current Students Resources Page</strong></a>."]
                }
            }]
        }
    })

#####################################
######## webpage replacement ########
#####################################
## Dual Degree
@app.route("/dualDegree", methods=["POST"])
def dualDegree():
    return jsonify({
        "fulfillment_response": {
            "messages": [{
                "text": {
                    "text": ["Check out the NYU Wagner Website to learn about "
                    "<a href='https://wagner.nyu.edu/education/degrees/dual-degree-program'><strong>Dual Degree Programs</strong></a>."]
                }
            }]
        }
    })
## Student Groups
@app.route("/studentGroups", methods=["POST"])
def studentGroups():
    return jsonify({
        "fulfillment_response": {
            "messages": [{
                "text": {
                    "text": ["All Wagner <a href='https://wagner.nyu.edu/education/degrees/dual-degree-program'><strong>Student Groups</strong></a> and Organizations are open to any interested Wagner student."]
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