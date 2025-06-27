import requests

USERNAME = "oniwasgone"
README_FILE = "README.md"
START = "<!-- START PROJECT LINKS -->"
END = "<!-- END PROJECT LINKS -->"

def fetch_repos():
    url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100&sort=updated"
    response = requests.get(url)
    return response.json()

def format_table(repos):
    table = "| Project | Description | Link |\n|--------|-------------|------|\n"
    for repo in repos:
        table += f"| 🔹 **{repo['name']}** | {repo['description'] or 'No description'} | [View](https://github.com/{USERNAME}/{repo['name']}) |\n"
    return table

def update_readme():
    repos = fetch_repos()
    table_md = format_table(repos)
    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    updated = content.split(START)[0] + START + "\n" + table_md + "\n" + END + content.split(END)[1]
    
    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(updated)

if __name__ == "__main__":
    update_readme()
