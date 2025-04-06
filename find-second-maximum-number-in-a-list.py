if __name__ == '__main__':
    n = int(input())
    nums = list(set(map(int, input().split())))
    nums.sort()
    n = len(nums)
    print(nums[n-2] if len(nums) >= 2 else None)
