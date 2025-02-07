from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

def fact_check_statement(statement):
    """
    This function should call a real fact-checking API.
    Right now, it uses mock data. Replace this with real data later.
    """
    fact_checks = [
        {"source": "PolitiFact", "rating": "Mostly False", "url": "https://www.politifact.com"},
        {"source": "Snopes", "rating": "False", "url": "https://www.snopes.com"},
        {"source": "FactCheck.org", "rating": "Partially True", "url": "https://www.factcheck.org"}
    ]
    return fact_checks

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fact-check', methods=['POST'])
def fact_check():
    data = request.get_json()
    statement = data.get("statement", "")
    if not statement:
        return jsonify({"error": "No statement provided"}), 400

    fact_check_results = fact_check_statement(statement)

    truth_score = 100 if any("True" in result["rating"] for result in fact_check_results) else 0
    correction = "The claim is inaccurate. Refer to sources." if truth_score == 0 else "The claim is accurate."

    return jsonify({
        "Truth Score": truth_score,
        "Analysis": "Fact-checking sources suggest this claim is " + ("true" if truth_score == 100 else "false"),
        "Correction": correction,
        "Fact-Check Sources": fact_check_results
    })

if __name__ == '__main__':
    app.run(debug=True)
