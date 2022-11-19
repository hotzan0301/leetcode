def twoSum(nums, target):
    result = dict()
    for index, value in enumerate(nums):
        result[target - value] = index
    result_list = list()
    print(result)
    for index, value in enumerate(nums):
        x = result.get(value)
        if x != None and x != index:
            result_list.append(index)
            result_list.append(x)
            break
    return result_list
