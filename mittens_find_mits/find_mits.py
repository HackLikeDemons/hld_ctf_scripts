# use case: CTF https://acmcyber.com/challenges#mittens

solution_lines = []
allowed_chars = ["\\","`","/","_","\n"," ",","]

for i in range(1,7):
    file_name = f"mits{i}.txt"
    file = open(file_name, "r")
    file_lines = file.readlines()
    file.close()
    for line in file_lines:
        if "/" in line:
            if "_" in line:                
                    line = ''.join(c for c in line if c in allowed_chars)
                    solution_lines.append(line)

print("".join(solution_lines))
