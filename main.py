string = "algoritmo aguacate albacora algoritmica algoritmo"
pattern = "algoritmo"


def get_shifts(string: str, pattern:str) -> list:
    x_0 = 0
    x_1 = len(pattern)

    concurr = []
    while x_1 < len(string):
        for i in range(len(string[x_0:x_1])):
            i += x_0
            if string[i] == pattern[0] and string[i+1] == pattern[1]:
                concurr.append(i)
        x_0 = x_1
        x_1 += len(pattern) 
    return concurr

def matches(string:str, pattern:str) -> list:
    shifts = get_shifts(string, pattern)
    match_list = []
    for shift in shifts:
        is_equal = True
        for i in range(2,len(pattern)):
            is_equal = is_equal and (pattern[i] == string[shift + i])
        if is_equal:
            match_list.append(shift)
    return match_list

print(get_shifts(string, pattern))
print(matches(string, pattern))