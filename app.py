from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Harsh Agrawal</h1>
    <a href="/static/Resume-HarshAgrawal.pdf" target="_blank">View My Resume</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
