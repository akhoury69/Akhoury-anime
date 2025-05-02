from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    if not query:
        return jsonify({'error': 'No query provided'}), 400

    url = f"https://api.jikan.moe/v4/anime?q={query}&limit=5"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get('message')
    if 'recommend' in user_message.lower():
        reply = "I recommend 'Attack on Titan' and 'Jujutsu Kaisen'!"
    elif 'hello' in user_message.lower():
        reply = "Hello! I'm your anime assistant. Ask me anything about anime!"
    elif 'naruto' in user_message.lower():
        reply = "Naruto is a classic! A great story of perseverance and friendship."
    else:
        reply = "Sorry, I can only answer simple questions for now."
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
