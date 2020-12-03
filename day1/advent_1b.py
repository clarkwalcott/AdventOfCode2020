with open("input.txt", "r") as f:
    nums = f.read().split("\n")[:-1]
nums = [int(x) for x in nums]
nums.sort()

nums = [x for x in nums if (x + nums[0] + nums[1]) < 2020]
print(nums)

for i in range(len(nums)-2):
    for j in range(1, len(nums)-1):
        for k in range(2, len(nums)):
            if(nums[i] + nums[j] + nums[k] == 2020):
                print(nums[i]*nums[j]*nums[k])