import requests

def search_jobs(query):
    url = "https://jsearch.p.rapidapi.com/search"

    headers = {
        "X-RapidAPI-Key": "80be7f8251msh1363265404d3c26p16700bjsn414dbdb600f5",
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    params = {
        "query": query,
        "page": "1",
        "num_pages": "1"
    }

    print("🔍 Searching jobs...")
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print(f"❌ API Error: {response.status_code}")
        return []

    data = response.json()
    jobs = data.get("data", [])

    job_list = []
    for job in jobs[:5]:  # Limit to 5 jobs
        job_info = {
            "title": job.get("job_title", "N/A"),
            "company": job.get("employer_name", "N/A"),
            "location": job.get("job_city", "N/A"),
            "description": job.get("job_description", "N/A")[:200] + "...",
            "apply_link": job.get("job_apply_link", "N/A")
        }
        job_list.append(job_info)

    return job_list


# --- MAIN ---
query = input("🔎 Enter job title to search: ")
jobs = search_jobs(query)

if jobs:
    print(f"\n📋 Found {len(jobs)} jobs:\n")
    for i, job in enumerate(jobs, 1):
        print(f"{i}. {job['title']} ({job['location']})")
        print(f"   Company: {job['company']}")
        print(f"   Description: {job['description']}")
        print(f"   Apply: {job['apply_link']}\n")
else:
    print("❌ No jobs found.")
