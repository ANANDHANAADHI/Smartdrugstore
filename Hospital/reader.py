def rearrange_even_odd(arr):
    # sort the array in increasing order
    arr.sort()

    # create two lists for even and odd numbers
    even_nums = [num for num in arr if num % 2 == 0]
    odd_nums = [num for num in arr if num % 2 == 1]

    # merge the two lists alternatively
    res = []
    while len(even_nums) > 0 and len(odd_nums) > 0:
        res.append(even_nums.pop(0))
        res.append(odd_nums.pop(0))

    # add any remaining even or odd numbers to the end of the result
    if len(even_nums) > 0:
        res += even_nums
    if len(odd_nums) > 0:
        res += odd_nums

    # return the rearranged array as a string
    return ','.join(str(num) for num in res)
# read input array size and elements from user
n = int(input())
arr = list(map(int, input().split(',')))

# call the function to rearrange the array
result = rearrange_even_odd(arr)

# print the rearranged array
print(result)
