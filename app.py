import os
from flask import Flask

app = Flask(__name__)

pod_name = os.getenv('POD_NAME', 'Unknown Pod')
node_name = os.getenv('NODE_NAME', 'Unknown Node')
pod_namespace = os.getenv('POD_NAMESPACE', 'Unknown Namespace')

@app.route("/")
def index():
    return " Container EDU | POD Working : " + pod_name + " | nodename : " +  node_name +  " | namespace : " +  pod_namespace + "\n"

if __name__ == '__main__':
    app.run(host= '0.0.0.0',port=5000,debug=True)
