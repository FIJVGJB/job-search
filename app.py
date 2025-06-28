from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your actual API key
RAPIDAPI_KEY = "80be7f8251msh1363265404d3c26p16700bjsn414dbdb600f5"

@app.route('/')
def home():
    return "✅ Job Search API is running"

@app.route('/search', methods=['GET'])
def search_jobs():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Missing 'query' parameter"}), 400

    url = "https://jsearch.p.rapidapi.com/search"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }
    params = {"query": query, "page": "1", "num_pages": "1"}

    res = requests.get(url, headers=headers, params=params)
    if res.status_code != 200:
        return jsonify({"error": "API request failed", "code": res.status_code}), 500

    jobs = res.json().get("data", [])[:5]

    result = []
    for job in jobs:
        result.append({
            "title": job.get("job_title", "N/A"),
            "company": job.get("employer_name", "N/A"),
            "location": job.get("job_city", "N/A"),
            "description": job.get("job_description", "N/A")[:200] + "...",
            "apply_link": job.get("job_apply_link", "N/A")
        })

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
