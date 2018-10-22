def flatten(list):
    final = []
    for item in list:
        final += item

    return final

def flattenN(list):
    if type(list[0]) != type([]):
        return list
    return flattenN(flatten(list))
    

list = [[[1,2],[3,4]],[[3,4],["hello","there"]]]
result = flattenN(list)
print(result)
