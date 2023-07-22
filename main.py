string = " aaa" #algoritmo aguacate albacora algoritmica algoritmo 123549 0coco 255algoritmo 55662467 
pattern = "aa"


def get_shifts(string: str, pattern:str) -> list:
    x_0 = 0
    x_1 = len(pattern)

    concurr = []
    while x_1 < len(string)+1:
        segmento = string[x_0:x_1]
        for i in range(len(pattern)):
            i += x_0
            if string[i] == pattern[0]:
                concurr.append(i)
        x_0 = x_1
        x_1 += len(pattern) 
    return concurr

def matches(string:str, pattern:str) -> list:
    shifts = get_shifts(string, pattern)
    match_list = []
    for shift in shifts:
        is_equal = True
        i = 0
        while i < len(pattern) and shift + i < len(string):
            is_equal = is_equal and (pattern[i] == string[shift + i])
            i += 1
        if is_equal and i == len(pattern):
            match_list.append(shift)
    return match_list

#print(get_shifts(string, pattern))
print(matches(string, pattern))