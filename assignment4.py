def Cube_volume(x):
    float(x)
    result = float(3*x)
    return result

def Average_element(list):
    i=0
    result=0
    for i in list:
        result += float(i)
    result = result/len(list)
    return result

def Name_generator(first,last):
    full_name = str(first + " " + last)
    return full_name

