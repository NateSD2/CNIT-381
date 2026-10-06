import os
import requests

TOKEN = os.environ.get("GITHUB_TOKEN")
if not TOKEN:
    raise SystemExit("GITHUB_TOKEN is not set - see Part 1.")

USERNAME = "NateSD2"
REPO = "CNIT-381"

BASE = "https://api.github.com"
HEADER = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+jason",
    "User-Agent": USERNAME
}

def get (path, **parms):
    resp = requests.get(BASE + path, headers=HEADER, params=parms)
    resp.raise_for_status()
    return resp

resp = get(f"/repos/{USERNAME}/{REPO}")
repo = resp.json()
print("Repo:", repo["full_name"])
print("Description:", repo["description"])
print("language:", repo["language"])
print("open issues:", repo["open_issues_count"])
print("url:", repo["html_url"])
print("API calls left this hour:", resp.headers["X-RateLimit-Remaining"])
print()

try:
    get(f"/repos/{USERNAME}/this-repo-does-not-exist")
except requests.exceptions.HTTPError as e:
    print("Handled error:", e.response.status_code, "-", e.response.json().get("message"))

me = get("/user").json()
print("you are:", me["login"], "-", me.get("name"))
print(" public repos:", me["public_repos"])
print()

repos = get("/user/repos", per_page=100, sort="updated").json()
print(f"Your {len(repos)} repos (10 most recently updated):")
for r in repos[:10]:
    print(" -", r["name"])

