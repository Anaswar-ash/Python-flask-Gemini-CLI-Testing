from flask import Flask, jsonify
from database import get_sorted_data

app = Flask(__name__)

@app.route('/data')
def sorted_data():
    """
    Endpoint to get the database content sorted by ID.
    """
    data = get_sorted_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
