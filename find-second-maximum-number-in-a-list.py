if __name__ == '__main__':
    n = int(input())
    nums = list(set(map(int, input().split())))
    n = len(nums)
    for i in range(n):
        swap = 0
        for j in range(i, n-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swap += 1
        if swap == 0:
            break
    print(nums[n-2] if len(nums) > 2 else None)
