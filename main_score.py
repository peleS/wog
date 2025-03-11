from flask import Flask
import os

app = Flask(__name__)
SCORES_FILE_NAME = "Scores.txt"

@app.route("/")
def score_server():
    try:
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, "r") as file:
                score = file.read()
            return f"<html><head><title>Scores</title></head><body><h1>The score is: {score}</h1></body></html>"
        else:
            return "<html><head><title>Scores</title></head><body><h1>The score is: 0</h1></body></html>"
    except Exception as e:
        return f"<html><head><title>Error</title></head><body><h1>ERROR: {e}</h1></body></html>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8777)
