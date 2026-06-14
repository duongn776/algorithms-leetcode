import os

difficulties = {
    "Easy": "🟢 Easy",
    "Medium": "🟡 Medium", 
    "Hard": "🔴 Hard"
}

sections = {"Easy": [], "Medium": [], "Hard": []}

# Scan folder LeetCode/Easy, LeetCode/Medium, LeetCode/Hard
for diff in difficulties:
    path = f"./LeetCode/{diff}"
    if os.path.exists(path):
        for problem in sorted(os.listdir(path)):
            if os.path.isdir(f"{path}/{problem}"):
                sections[diff].append(problem)

content = "# LeetCode Solutions\n\n"
content += f"![Easy](https://img.shields.io/badge/Easy-{len(sections['Easy'])}-green) "
content += f"![Medium](https://img.shields.io/badge/Medium-{len(sections['Medium'])}-yellow) "
content += f"![Hard](https://img.shields.io/badge/Hard-{len(sections['Hard'])}-red)\n\n"

for diff, label in difficulties.items():
    if sections[diff]:
        content += f"## {label}\n\n"
        content += "| Problem | Difficulty |\n|---|---|\n"
        for problem in sections[diff]:
            content += f"| [{problem}](./LeetCode/{diff}/{problem}) | {label} |\n"
        content += "\n"

with open("README.md", "w") as f:
    f.write(content)

print("README updated!")
