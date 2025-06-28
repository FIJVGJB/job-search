from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def search_jobs(query):
    # (Your same existing job scraping logic here)
    ...

@app.route("/")
def home():
    return "✅ Job Bot API is running."

@app.route("/search")
def search():
    query = request.args.get("query")
    if not query:
        return jsonify({"error": "No query provided."}), 400

    jobs = search_jobs(query)
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(debug=True)
