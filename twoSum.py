"""
a list and a target number, return indices of the two numbers such that they add up to target.
give list = [list],
target = target value
initial state of the dict = {} (empty dict)
formula  = target - current_number
iteration:
    Index = index value
    current = value of the current index
    result = target - current 
    Check:
    Is result in dictionary?
    if No: 
        Store:
        {value: index }
    else:
        return [dictionary[result], index]
"""
def two_sum(nums:list[int], target:int) -> list[int]:
    mydict = {}
    #mydict[key] = value
    for index in range(len(nums)):
        complement = target - nums[index] # 3 -1 =2, 3-2 =1
        if complement in mydict:
            return [mydict[complement],index] #[1,0]
        else:
            mydict[nums[index]] = index 

two_sum([1,2,3,4], 3)