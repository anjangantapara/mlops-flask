from flask import Flask
from pprint import pprint
import os
from redis import Redis

app = Flask(__name__)
r = Redis(host=os.enviro.get, port=6379, db=0', decode_responses=True)
REDIS_NAMES_KEY = "names"


#names = set()

@app.route("/names")
def list_names():
    names = r.smembers(REDIS_NAMES_KEY)
    return {"names": list(names)}


@app.route("/names/<name>", methods=["POST"])
def post_names(name):
    new = r.sadd(REDIS_NAMES_KEY, name)
    if not new:
        return "already exists", 208
    
    #names.add(name)
    return "ok", 201

@app.route("/names/<name>", methods=["GET"])
def get_name(name):
    #if name not in names:
    if not name in r.smembers(REDIS_NAMES_KEY):
        abort(404)
    return f"hello {name}!"
    