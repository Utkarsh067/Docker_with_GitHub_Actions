from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, I am Utkarsh Jain, I made flask app, dockerised it and implemented CI/CD using GitHub Actions and deploying locally with Minikube"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

