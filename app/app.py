from flask import Flask
import redis
import os

app = Flask(__name__)

rh = os.getenv("REDIS_HOST", "localhost")
rc = redis.Redis(host=rh, port=6379, decode_responses=True)
rc.set('count', '0')

@app.route("/ping")
def ping():
    return {"status": "ok"}

@app.route("/count")
def count():
    rc.incr("count")
    return {"count": rc.get('count')}
    

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 5000)
