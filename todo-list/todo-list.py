from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_main_page():
    #return render_template('index.html'), 200
    return "Hello World!", 200

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return error, 404

@app.errorhandler(405)
def not_allow_method(error):
    app.logger.error(error)
    return error, 405