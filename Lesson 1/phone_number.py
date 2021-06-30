nums = [input(), input(), input(), input()]
def phone(nums):
    # remove the first digit of the number
    nums = [num[1:] if num[0] == '8' else num for num in nums]
    nums = [num[2:] if num[:2] == '+7' else num for num in nums]
    # remove the brackets
    nums = [''.join(num.split(')')) if ')' in num else num for num in nums]
    nums = [''.join(num.split('(')) if '(' in num else num for num in nums]
    # remove dash
    nums = [''.join(num.split('-')) if '-' in num else num for num in nums]
    if nums[0][0:3] == '495' or len(nums[0]) == 7:
        nums = [num.replace('495', '') if '495' in num else num for num in nums]
    for i in range(1, len(nums)):
        if nums[0] == nums[i]:
            yield 'YES'
        else:
            yield 'NO'
phones = phone(nums)
print(next(phones))
print(next(phones))
print(next(phones))