with open("input.txt", "r") as f:
    nums = f.read().split("\n")[:-1]
nums = [int(x) for x in nums]
nums.sort()

s = set()

for i in range(len(nums)):
    temp = 2020 - nums[i]
    if temp in s:
        print(temp * nums[i])
    else:        
        s.add(nums[i])    