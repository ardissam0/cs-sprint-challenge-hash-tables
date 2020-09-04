def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # create has table (cache)
    cache = {}

    #create cases
    #if length is less than or equal to 1
    #its too short
    if length <=1:
        print("To short")
        return None

    #for i in the range of the length
    #set the current weight
    #if the current weight is in the cache
    # previous equals the current
    # otherwise cache the limit minus the weight as i
    # find the limit
    for i in range(length):
        cur = weights[i]

        if cur in cache:

            previous = cache[cur]

            return(i, previous)

        cache[limit - weights[i]] = i
    return None
