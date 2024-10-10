import sys

def min_steps_to_equalize(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    steps = 0
    for num in nums:
        steps += abs(num - median)
    return steps

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py input_file")
        sys.exit(1)

    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        nums = [int(line.strip()) for line in f.readlines()]

    result = min_steps_to_equalize(nums)
    print(result)