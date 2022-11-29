# this script will find diffs in two textfiles and concatenate them into a single string
# use case: CTF challenge https://acmcyber.com/challenges#lawsOfAviation

import difflib

first_file = "script1.txt"
second_file = "script2.txt"

file = open(first_file, "r")
first_file_lines = file.readlines()
file.close()

file = open(second_file, "r")
second_file_lines = file.readlines()
file.close()

i = 0
output_list = []

while i < len(first_file_lines):
    string_1 = first_file_lines[i]
    string_2 = second_file_lines[i]
    i += 1

    diff_list = difflib.ndiff(string_1, string_2)
    
    for li in diff_list:
        if li[0] != ' ':
            output_list.append(li)

print("".join(output_list).replace("+","").replace(" ", ""))