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
        for i in range(1,len(pattern)):
            if shift + i < len(string):
                break
            is_equal = is_equal and (pattern[i] == string[shift + i])
        if is_equal:
            match_list.append(shift)
    return match_list

#print(get_shifts(string, pattern))
print(matches(string, pattern))