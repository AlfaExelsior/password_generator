from flask import Flask, jsonify, send_from_directory
import os
import random
import string

app = Flask(__name__, static_folder='../frontend')

# Define sets of characters
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
all_chars = letters + digits + symbols  # Define all_chars here

@app.route('/generate_password/<int:length>')
def generate_password(length):
    password = "".join(random.choice(all_chars) for i in range(length))
    return jsonify({"password": password})

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    app.run(debug=False)