#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # create hash table (cache)
    cache = {}

    #starting locations
    route = []

    # find all tickets and store them
    for i in tickets:
        cache[i.source] = i.destination
    
    # first ticket/flight starts at None
    flight_one = cache["NONE"]

    # add each destination stop to cache
    while flight_one != "NONE":
        route.append(flight_one)
        flight_one = cache[flight_one]
    route.append("NONE")

    return route
