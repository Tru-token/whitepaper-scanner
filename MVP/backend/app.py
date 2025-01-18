
from flask import Flask, request, jsonify
from ai_analysis import analyze_whitepaper
from risk_scoring import calculate_risk_score

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "version": "MVP v1.0"}), 200

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    whitepaper_text = data.get('whitepaper_text', '')
    analysis_result = analyze_whitepaper(whitepaper_text)
    risk_score = calculate_risk_score(analysis_result)
    return jsonify({'analysis': analysis_result, 'risk_score': risk_score})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
