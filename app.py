from flask import Flask, Response
import os
import json

app = Flask(__name__)

def load_appsettings():
    env = os.getenv('FLASK_ENV', 'prod')
    if env == 'prod':
        config_file = 'appsettings-prod.json'
    else:
        config_file = 'appsettings-dev.json'

    with open(config_file) as f:
        app.config.update(json.load(f))

@app.route('/')
def home():
    return f"Flask Sample App - Environment: {app.config.get('env')}"

@app.route('/healthcheck')
def health_check():
    return Response("Healthy", status=200)

@app.route('/exit')
def exit_app():
    os._exit(0)

if __name__ == "__main__":
    load_appsettings()
    app.run(host='0.0.0.0', port=80)