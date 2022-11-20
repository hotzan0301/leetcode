def removeDuplicates(nums):
    index = 0
    cursor = 0
    qty = 0
    current = nums[0]
    init_len = len(nums)
    while (index < len(nums)):
        value = nums[index]
        if current == value:
            qty += 1
            index += 1
        else:
            for i in range(qty - 1):
                nums.pop(cursor)
            qty = 1
            cursor += 1
            index = cursor + 1
            current = value
    for i in range(qty - 1):
        nums.pop(len(nums)-1)
    current_len = len(nums)
    for i in range(init_len - current_len):
        nums.append("_")
    return current_len

def removeDuplicates2(nums):
        n=len(nums)
        if n == 0 or n == 1:
            return n
        j = 1
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                print(nums)
                j += 1
        return j

if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates2(nums))
    print(nums)
    

    
    
    