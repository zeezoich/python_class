import sys

def atoi(str):
    num = 0
    mult = 1
    sign = 1
    if str[0] == '-':
        str = str[1:]
        sign = -1
        
    for c in reversed(str):
        value = ord(c) - ord('0')
        if not 0 <= value <= 9:
            raise ValueError('{!r} is not a valid digit.'.format(c))
        
        num += mult * value
        mult *= 10

    return num * sign

def __main__():
    if len(sys.argv) < 2:
        return
    
    print(atoi(sys.argv[1]))
    print(type(atoi(sys.argv[1])))


__main__()
