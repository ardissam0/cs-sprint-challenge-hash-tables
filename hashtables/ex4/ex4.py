def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # create hash table (cache)
    # create empty array as result
    cache = {}
    result = []

    #loop through array
    #add nums to cache
    #uses absolute value
    for num in a:
        num = abs(num)
        if cache.get(num) is None:
            cache[num] = "Added to cache"

        #already in cache
        else:
            result.append(num)
 
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
