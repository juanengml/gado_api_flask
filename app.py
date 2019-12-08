from flask import Flask, jsonify, make_response,request
from api import bp_api

app = Flask(__name__)
app.register_blueprint(bp_api)

@app.errorhandler(404)
def not_found(error):
   return make_response(jsonify({"error":"Not existe URL carai"}),404)
app.run(use_reloader=True)
