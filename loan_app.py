from flask import Flask,request
import pickle

app = Flask(__name__)

loan_pickle = open("./loan_classifier.pkl", "rb")
loan_clf = pickle.load(loan_pickle)

@app.route("/")
def hello_world():
    return """<p>Hello, this is the Loan Classifying App main page!
                 Use /predict next to the url to use the app</p>"""

@app.route("/ping", methods = ['GET'])
def pinger():
    return "<p>Hello I am Batman</p>"

@app.route("/json_check", methods = ['GET'])
def json():
    return {"message": "Hi I am JSON"}

@app.route("/predict", methods = ['POST'])
def prediction():
    loan_req = request.get_json()

    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1
    if loan_req['Married'] == "Yes":
        Married = 1
    else:
        Married = 0

    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']
    Credit_History = loan_req['Credit_History']

    result = loan_clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

    if result == 0:
        pred = "Rejected"
    else:
        pred = "Approved"

    return {"loan approval status: ": pred}

