import re

matches = []
combined_pattern = r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))"

with open("input.txt") as file:
    content = file.read()
    matches = re.findall(combined_pattern, content)

sum = 0
enabled = True
for match in matches:
    if match.startswith("m") and enabled:
        nums = match[4:-1].split(",")
        num1 = int(nums[0])
        num2 = int(nums[1])
        sum += num1 * num2
    elif match.startswith("do()"):
        enabled = True
    else:
        enabled = False

print(sum)
