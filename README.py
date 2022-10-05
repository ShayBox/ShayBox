from collections import OrderedDict

import requests

sections = {}

for repo in requests.get("https://api.github.com/users/shaybox/repos?per_page=100").json():
    language = repo["language"]
    if (language is None or repo["name"] == "ShayBox"):
        continue

    section = sections.get(language) or []
    section.append(f"- [{repo['name']}]({repo['html_url']}) - {repo['description']}  ")
    sections[language] = section

sections = OrderedDict(sorted(sections.items(), key=lambda x: len(x[1]), reverse=True))
markdown = ["# Projects"]

for section in sections:
    markdown.append(f"\n### {section}")
    for repo in sections[section]:
        markdown.append(repo)

with open("README.md", "w") as f:
    f.write("\n".join(markdown))