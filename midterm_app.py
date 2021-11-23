# Add to this file for the sample app lab
from flask import Flask, url_for, redirect, jsonify, request
from flask import request
from flask import render_template

webApp = Flask(__name__)

@webApp.route('/')
def main():
    # show the form, it wasn't submitted
    return render_template('login.html')

@webApp.route('/registration')
def registration():
    # show the form, it wasn't submitted
    return render_template('registration.html')

if __name__ == "__main__":
    webApp.run(host="0.0.0.0", port=5000, debug=True)