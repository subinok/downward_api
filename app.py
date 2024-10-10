from flask import Flask
app = Flask(__name__)

@app.route("/")
def getInfo():
    pod_name = os.getenv('POD_NAME', 'Unknown Pod')
    node_name = os.getenv('NODE_NAME', 'Unknown Node')
    pod_namespace = os.getenv('POD_NAMESPACE', 'Unknown Namespace')
    
    return f'Pod Name: {pod_name}, Node Name: {node_name}, Pod Namespace: {pod_namespace}'

if __name__ == '__main__':
    app.run(host= '0.0.0.0',port=8080,debug=True)
