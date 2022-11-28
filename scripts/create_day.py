import requests
import sys
import os

DAY = 1

FORMATTED_DAY = f"0{DAY}" if DAY < 10 else str(DAY)


def get_session_cookie():
    if sys.argv[1] is None:
        raise Exception('Missing session cookie, please provide it as a command line argument')
    session_cookie = sys.argv[1]
    return session_cookie


def fetch_input():
    url = f"https://adventofcode.com/2021/day/{DAY}/input"
    response = requests.post(url, cookies={'session': get_session_cookie()})
    if response.status_code != 200:
        raise Exception(f"Error code {response.status_code} while fetching {url}: {response.text}")
    return response.text


def save_input(input_string):
    folder_path = f'../day{FORMATTED_DAY}'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    with open(f'../day{FORMATTED_DAY}/input.txt', 'w') as file:
        file.write(input_string)


def save_template(template_string):
    folder_path = f'../day{FORMATTED_DAY}'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    with open(f'../day{FORMATTED_DAY}/day{FORMATTED_DAY}.py', 'w') as file:
        file.write(template_string)


def get_solution_template():
    return f"""# https://adventofcode.com/2022/day/{DAY}

with open('input.txt', 'r') as file:
    input = file.read()
    lines = file.read().splitlines()
    
# --- Part 1 --- #
print(input)
"""


if __name__ == '__main__':
    input_string = fetch_input()
    template = get_solution_template()

    save_input(input_string)
    save_template(template)
