from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fact-check', methods=['POST'])
def fact_check():
    data = request.get_json()
    statement = data.get("statement", "")

    # Mock fact-checking logic (replace this with real API)
    fact_check_results = [
        {"source": "PolitiFact", "rating": "Mostly False", "url": "https://www.politifact.com"},
        {"source": "Snopes", "rating": "False", "url": "https://www.snopes.com"},
        {"source": "FactCheck.org", "rating": "Partially True", "url": "https://www.factcheck.org"}
    ]

    truth_score = 100 if "True" in [res["rating"] for res in fact_check_results] else 0
    correction = "The claim is inaccurate. Refer to sources." if truth_score == 0 else "The claim is accurate."

    return jsonify({
        "Truth Score": truth_score,
        "Analysis": f"Fact-checking sources suggest this claim is {'true' if truth_score == 100 else 'false'}",
        "Correction": correction,
        "Fact-Check Sources": fact_check_results
    })

if __name__ == '__main__':
    app.run(debug=True)
