from flask import Flask, render_template, request
import requests
import json
import os

# Find the directory of this file (even if compiled)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Go up one level (from __pycache__ to /app) and set templates folder
TEMPLATES_DIR = os.path.join(os.path.dirname(BASE_DIR), "templates")

app = Flask(__name__, template_folder=TEMPLATES_DIR)

API_URL = "https://patientsafe.global-value-web.in:8048/PQCS"

@app.route("/", methods=["GET", "POST"])
def index():
    output = None
    input_text = ""

    if request.method == "POST":
        input_text = request.form.get("text_input")
        if input_text.strip():
            try:
                payload = {"text": input_text}
                headers = {"Content-Type": "application/json"}

                # Call the API
                response = requests.post(API_URL, data=json.dumps(payload), headers=headers, verify=False)

                if response.status_code == 200:
                    output = response.json()
                else:
                    output = {"error": f"API returned status {response.status_code}"}
            except Exception as e:
                output = {"error": str(e)}

    return render_template("index.html", input_text=input_text, output=output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5700, debug=True)
