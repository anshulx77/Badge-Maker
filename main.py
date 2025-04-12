
# Badge Maker for github.com/Anshul-Padiyar/problem-solving
# Started: 2025, 12 April, 22:14

from datetime import date
date = date.today()

problem_name = input(f"Enter the problem name here : ")
problem_url = input("Enter the problem url here : ")
solution_url = input("Enter the solution url here : ")
difficulty = input("Enter the difficulty level here : ")
problem_tags = input("Enter problem tags here (sperate them by \" \" (space)) : ")

# Generates problem name for url
def generate_title_for_url (problem_name) :
    title_for_url = problem_name.replace("-", "--")
    title_for_url = title_for_url.replace("_", "__")
    title_for_url = "_".join(title_for_url.split())
    return title_for_url

# function call to generates problem name for url
title_for_url = generate_title_for_url(problem_name)

# Generates file name
def create_markdown_filename(problem_name) :
    file_name = problem_name.replace("-", " ")
    file_name = f"{"-".join(file_name.split())}.md"
    print(f"\nFile name : {file_name}")
    return file_name

# Fuction call to generate file name
file_name = create_markdown_filename(problem_name)

# makeing problem_tags for README file
def make_tag_badges(problem_tags):
    if problem_tags == "" :
        return " "
    else :
        problem_tags = " ".join(problem_tags.split())
        tag_string = str()
        for tag in problem_tags :
            tag_string = f"{tag_string} ![Tag: {tag.capitalize()}](https://img.shields.io/badge/{tag.capitalize()}-grey)"
        return tag_string

# Creates badges for problem's README file
def generate_badges_for_problem_readme(file_name, problem_url, title_for_url, level) : 
    level = level.lower()
    difficulty_levels_pr = {
        "basic" : "![Difficulty: Basic](https://img.shields.io/badge/Difficulty-Basic-lightgrey)\n",
        "easy" : "![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-green)\n",
        "medium" : "![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)\n",
        "hard" : "![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)\n"
    }
    # for GeeksForGeeks
    if problem_url.startswith("https://www.geeksforgeeks.org") :
        with open(file_name, "w+") as f :
            f.writelines(
                [
                    f"<!-- Badges Section for Problem's README File -->\n",
                    f"[![GFG](https://img.shields.io/badge/GeeksforGeeks-{title_for_url}-388e3c?logo=geeksforgeeks)]({problem_url})\n\n",
                    f"<!-- Difficulty Level Badges for Problem README -->\n",
                    f"{difficulty_levels_pr.get(level)}\n"
                ]
            )
    # for LeetCode
    elif problem_url.startswith("https://leetcode.com") :
        with open(file_name, "w+") as f :
            f.writelines(
                [
                    f"<!-- Badges Section for Problem's README File -->\n",
                    f"[![LeetCode](https://img.shields.io/badge/LeetCode-{title_for_url}-ffa116?logo=leetcode)]({problem_url}))\n\n",
                    f"<!-- Difficulty Level Badges for Problem README -->\n",
                    f"{difficulty_levels_pr.get(level)}\n"
                ]
            )
    # for HackerRank
    elif problem_url.startswith("https://www.hackerrank.com") :
        with open(file_name, "w+") as f :
            f.writelines(
                [
                    f"<!-- Badges Section for Problem's README File -->\n",
                    f"[[![HackerRank](https://img.shields.io/badge/HackerRank-{title_for_url}-00c698?logo=hackerrank&logoColor)]({problem_url}))\n\n",
                    f"<!-- Difficulty Level Badges for Problem README -->\n",
                    f"{difficulty_levels_pr.get(level)}\n"
                ]
            )
    # for CodeChef
    elif problem_url.startswith("https://www.codechef.com") :
        with open(file_name, "w+") as f :
            f.writelines(
                [
                    f"<!-- Badges Section for Problem's README File -->\n",
                    f"[![CodeChef](https://img.shields.io/badge/CodeChef-{title_for_url}-5B4638?style=flat&logo=codechef&logoColor=white)]({problem_url}))\n\n",
                    f"<!-- Difficulty Level Badges for Problem README -->\n",
                    f"{difficulty_levels_pr.get(level)}\n"
                ]
            )
    else :
        print("Invalid Problem url")
    # success msg
    print("\nPlatform name badge created successfully ...")

# Funtion call for badges for problem's README file
generate_badges_for_problem_readme(file_name, problem_url, title_for_url, difficulty)

# Creates table rows for Main README
def  generate_table_row(file_name, problem_name, problem_url, solution_url, level, date, problem_tags) :  
    level = level.lower()   
    difficulty_levels_main = {
        "basic" : "![Difficulty: Basic](https://img.shields.io/badge/Basic-lightgrey)\n",
        "easy" : "![Difficulty: Easy](https://img.shields.io/badge/Easy-green)\n",
        "medium" : "![Difficulty: Medium](https://img.shields.io/badge/Medium-yellow)\n",
        "hard" : "![Difficulty: Hard](https://img.shields.io/badge/Hard-red)\n"
    }
    # for GeeksForGeeks
    if problem_url.startswith("https://www.geeksforgeeks.org") :
        with open(file_name, "a+") as f :
            f.write(f"| sr_number | [{problem_name}]({problem_url}) | [![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-000?style=flat&logo=geeksforgeeks&logoColor)]({problem_url}) | [Solution]({solution_url}) | {difficulty_levels_main.get(level)} | {date} | {make_tag_badges(problem_tags)} |")
    # for LeetCode
    elif problem_url.startswith("https://leetcode.com") :
        with open(file_name, "a+") as f :
            f.write(f"| sr_number | [{problem_name}]({problem_url}) | [![LeetCode](https://img.shields.io/badge/LeetCode-000?style=flat&logo=leetcode&logoColor=FFA116)]({problem_url}) | [Solution]({solution_url}) | {difficulty_levels_main.get(level)} | {date} | {make_tag_badges(problem_tags)} |")
    # for HackerRank
    elif problem_url.startswith("https://www.hackerrank.com") :
        with open(file_name, "a+") as f :
            f.write(f"| sr_number | [{problem_name}]({problem_url}) | [![HackerRank](https://img.shields.io/badge/HackerRank-000?logo=hackerrank&logoColor)]({problem_url}) | [Solution]({solution_url}) | {difficulty_levels_main.get(level)} | {date} | {make_tag_badges(problem_tags)} |")
    # for CodeChef
    elif problem_url.startswith("https://www.codechef.com") :
        with open(file_name, "a+") as f :
            f.write(f"| sr_number | [{problem_name}]({problem_url}) | [![CodeChef](https://img.shields.io/badge/CodeChef-000?style=flat&logo=codechef&logoColor=white)]({problem_url}) | [Solution]({solution_url}) | {difficulty_levels_main.get(level)} | {date} | {make_tag_badges(problem_tags)} |")
    else :
        print("Invalid Problem url")
    # success msg
    print("\nTable row created successfully ...")

# Fuction call to generate table row
generate_table_row(file_name, problem_name, problem_url, solution_url, difficulty, date, problem_tags)