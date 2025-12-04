if __name__ == '__main__':
    f = open('./data/input3.txt')
    lines = f.readlines()
    accum_jolt = 0
    for line in lines:
        nums = [int(i) for i in line.replace('\n', '')]
        jolt = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] * 10 + nums[j] > jolt:
                    jolt = nums[i] * 10 + nums[j]
        accum_jolt += jolt

    print(accum_jolt)