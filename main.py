import os
import requests
from string import Template

def get_stats():
    headers = {"Authorization": f"token {os.environ['GHT']}"}
    # CHANGE 1: We force the username to be thw01f (or whatever your handle is)
    response = requests.get("https://api.github.com/users/thw01f", headers=headers)
    data = response.json()
    
    # CHANGE 2: Force the display name to "w01f"
    name = "w01f" 
    
    return {
        "name": name,
        "public_repos": data.get("public_repos", 0),
        "followers": data.get("followers", 0),
        "following": data.get("following", 0),
    }

def make_svg(data):
    # CHANGE 3: The Hacker Red Theme
    # Background: #0D1117 (GitHub Dark)
    # Text/Border: #FF0000 (Red)
    
    svg = f"""
    <svg width="400" height="200" viewBox="0 0 400 200" fill="none" xmlns="http://www.w3.org/2000/svg">
    <style>
    .header {{ font: 600 18px 'Courier New', monospace; fill: #FF0000; }}
    .stat {{ font: 400 14px 'Courier New', monospace; fill: #FF0000; }}
    </style>
    <rect width="100%" height="100%" rx="10" fill="#0D1117" stroke="#FF0000" stroke-width="2"/>
    
    <text x="20" y="35" class="header">root@w01f:~# ./status</text>
    
    <text x="20" y="80" class="stat">User: {data['name']}</text>
    <text x="20" y="110" class="stat">Repos: {data['public_repos']}</text>
    <text x="20" y="140" class="stat">Followers: {data['followers']}</text>
    <text x="20" y="170" class="stat">Following: {data['following']}</text>
    
    <rect x="20" y="180" width="10" height="2" fill="#FF0000">
      <animate attributeName="opacity" values="0;1;0" dur="1s" repeatCount="indefinite" />
    </rect>
    </svg>
    """
    return svg

def main():
    data = get_stats()
    svg = make_svg(data)
    with open("github_stats.svg", "w") as f:
        f.write(svg)

if __name__ == "__main__":
    main()
