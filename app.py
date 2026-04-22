from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Flask is running"

@app.route('/result', methods=['POST'])
def result():
    data = request.json

    try:
        name = data.get('name')
        mark1 = int(data.get('mark1'))
        mark2 = int(data.get('mark2'))
        mark3 = int(data.get('mark3'))

        total = mark1 + mark2 + mark3
        average = total / 3

        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 50:
            grade = "C"
        else:
            grade = "Fail"

        return jsonify({
            "name": name,
            "total": total,
            "average": round(average, 2),
            "grade": grade
        })

    except Exception:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(debug=True)