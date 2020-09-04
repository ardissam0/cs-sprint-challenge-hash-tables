def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # create hash table (cache)
    cache = {}
    # create empty result array
    result =[]

    # for loop iterating through array and nums in array
    #  and adding to cache
    for arr in arrays:
        for num in arr:
            if num not in cache:
                cache[num] = 1
            else:
                cache[num] += 1
    # for loop finding the intersections/same nums
        for num in cache:
            if cache[num] == len(arrays):
                result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
