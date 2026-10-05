from flask import Flask, request, jsonify
from google import genai
app = Flask(__name__)
API_KEY = "AQ.Ab8RN6IMRECYROJzN5mUcNDd8jd8QOse3ocBlgf4eaIUQWW7UA"
client = genai.Client(api_key=API_KEY)
@app.route('/')
def home():
    return {"status": "online"}
@app.route('/ask')
def ask():
    q = request.args.get('q','Hello')
    r = client.models.generate_content(model="gemini-2.0-flash", contents=q)
    return jsonify({"jawab": r.text})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
