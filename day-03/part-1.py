import re
import time

start_time = time.time()

matches = []
with open("input.txt") as file:
    content = file.read()
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", content)

sum = 0
for match in matches:
    nums = match[4:-1].split(",")
    num1 = int(nums[0])
    num2 = int(nums[1])
    sum += num1 * num2

print("--- %s seconds ---" % (time.time() - start_time))
print(sum)
