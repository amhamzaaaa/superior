from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.form["msg"]
    return jsonify({'response': generate_response(user_input)})

def generate_response(message):
    msg = message.lower()
    if "admission" in msg:
        return "Admissions open from July 15th. Apply online at our portal."
    elif "fee" in msg:
        return "Tuition fees vary by program. For CS, it's $5,000 per semester."
    elif "deadline" in msg:
        return "Application deadline is August 30th."
    elif "eligibility" in msg:
        return "Minimum 60% in high school with Math for CS program."
    elif "apply" in msg:
        return "You can apply through our website. Need help with steps?"
    else:
        return "I'm not sure about that. Ask me about admissions, fees, or deadlines."

if __name__ == "__main__":
    app.run(debug=True)
