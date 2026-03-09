# Badge Maker for [problem-solving](https://github.com/Anshul-Padiyar/problem-solving) Repository

[![Python](https://img.shields.io/badge/Python-3.12.8-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Shields.io](https://img.shields.io/badge/Shields.io-badges-green?logo=shields.io&logoColor=white)](https://shields.io/)

A Python script that automates the creation of markdown badges and table entries for problem-solving's readme.md

### Features

- Generates platform-specific badges
- Creates difficulty level badges
- Supports multiple programming platform's URL:
  - GeeksForGeeks
  - LeetCode
  - HackerRank
  - CodeChef
- Creates formatted table rows for main README

### Platforms Badges

| Platform | Platform Badge | Problem Badge |
|---|---|---|
| LeetCode | [![LeetCode](https://img.shields.io/badge/LeetCode-000?style=flat&logo=leetcode&logoColor=FFA116)](#) | [![LeetCode](https://img.shields.io/badge/LeetCode-Problem_Title-ffa116?logo=leetcode)](#) |
| GeeksForGeeks | [![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-000?style=flat&logo=geeksforgeeks&logoColor)](#) | [![GFG](https://img.shields.io/badge/GeeksforGeeks-Problem_Title-388e3c?logo=geeksforgeeks)](#) |
| HackerRank | [![HackerRank](https://img.shields.io/badge/HackerRank-000?logo=hackerrank&logoColor)](#) | [![HackerRank](https://img.shields.io/badge/HackerRank-Problem_Title-00c698?logo=hackerrank&logoColor)](#) |
| CodeChef | [![CodeChef](https://img.shields.io/badge/CodeChef-000?style=flat&logo=codechef&logoColor=white)](#) | [![CodeChef](https://img.shields.io/badge/CodeChef-Problem_Title-5B4638?style=flat&logo=codechef&logoColor=white)](#) |

### Difficulty Level Badges

| Level | Simple Difficulty | Difficulty Badges |
|---|---|---|
| Basic | ![](https://img.shields.io/badge/Basic-lightgrey) | ![Difficulty: Basic](https://img.shields.io/badge/Difficulty-Basic-lightgrey) |
| Easy | ![](https://img.shields.io/badge/Easy-green) | ![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-green) |
| Medium | ![](https://img.shields.io/badge/Medium-yellow) | ![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-yellow) |
| Hard | ![](https://img.shields.io/badge/Hard-red) | ![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red) |

## How to use?

1. Run the script:
   ```bash
   python main.py
   ```

2. Enter the required information:
   - Problem name
   - Problem URL
   - Solution URL
   - Difficulty level
   - Problem tags (space-separated)

3. The script will generate:
   - A markdown file with badges
   - A table row for your main problem list

## Example Output

### *ScreenShot : Terminal View*
![Terminal Screenshot](ScreenShots/ScreenShot01.png)

### *ScreenShot : Generated File*
![Generated File Screenshot](ScreenShots/ScreenShot02.png)
