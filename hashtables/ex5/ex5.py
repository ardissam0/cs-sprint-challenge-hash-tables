# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # intialize empty array
    result = []

    # create dict
    dir = dict()

    #loop through the files
    for f in files:

        #split files at /
        s = f.split("/")
        last = s[-1]

        # create new entry into dict
        if last not in dir:
            dir[last] = []

        # add curr path to dict with last as the key
        dir[last].append(f)

    # looop through each query
    for q in queries:

        # if the file ws found, add the paths
        if q in dir:
            result.extend(dir[q])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
