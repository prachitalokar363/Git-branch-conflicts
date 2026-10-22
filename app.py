from flask import Flask
import linux os

app = Flask(__name__)

@app.route("/")
def hello():
    return "ghhhb"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5003))
    app.run(host="0.0.0.0", port=port, debug=False)
