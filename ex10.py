def list_of_tuples(*args):
    list_of_tuples = []
    for i in range(len(args[0])):  #might not cover all cases
        list_of_tuples.append(tuple([args[j][i] for j in range(len(args))]))
    return list_of_tuples



print(list_of_tuples([1,2,3], [5,6,7], ["a", "b", "c"]))
