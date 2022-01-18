from crypt import methods

from flask import jsonify
from app import create_app

app = create_app()

@app.route('/',methods=['GET'])
def index():
    return jsonify({'Message':'Welcome to API REST Python'})

if __name__ == "__main__":
    app.run(debug=True)