import re

# Updated skill percentages combining Automation, C++, and AI
skills = {
    "PLC_Programming": 85,
    "C++": 85,
    "Python": 80,
    "AutoCAD": 80,
    "OpenCV": 75,
    "Arduino": 75
}

# Read README.md
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Update Shields.io badges in README
for skill, percent in skills.items():
    pattern = rf"!\[{skill}\]\(https://img\.shields\.io/badge/{skill}-\d+%25-[a-z]+\)"
    replacement = f"![{skill}](https://img.shields.io/badge/{skill}-{percent}%25-brightgreen)"
    content = re.sub(pattern, replacement, content)

# Write updated README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

print("README.md multi-disciplinary engineering skill badges updated!")
