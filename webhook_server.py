from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/github-webhook")
async def github_webhook(request: Request):

    payload = await request.json()

    repo = payload.get("repository", {}).get("full_name", "Unknown Repo")

    commits = payload.get("commits", [])

    print("\n==============================")
    print("GITHUB PUSH RECEIVED")
    print(f"Repository: {repo}")
    print(f"Number of commits: {len(commits)}")

    for commit in commits:
        print(f"Commit: {commit['message']}")

    print("==============================\n")

    return {
        "status": "success",
        "repository": repo,
        "commits": len(commits)
    }