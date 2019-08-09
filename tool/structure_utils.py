def make_spaces(n):
    strr = ""
    for i in range(n):
        strr += " "
    return strr


def deduce_structure(x, spaces="", depth=0, preceding_spaces=True, max_depth = 4):
    deep = depth < max_depth
    type_x = type(x)
    if type_x is dict:
        print ((spaces if preceding_spaces else "")+'{}')
        if not deep:
            return
        print (spaces+make_spaces(4)+'{')
        for key in x.keys():
            print (spaces+make_spaces(8), ((key if len(key) < 20 else key[:20] + "......")), ' : ', end = '')
            deduce_structure(x[key], spaces+make_spaces(8+min(20, len(key))), depth+1, False, max_depth)
        print (spaces+make_spaces(4) +'}')
    elif type_x is list:
        print ((spaces if preceding_spaces else "")+'[ ' + str(len(x)) + ' ]')
        if not deep:
            return
        print (spaces+make_spaces(4)+'[')
        for elem in x:
            deduce_structure(elem, spaces+make_spaces(8), depth+1, max_depth=max_depth)
        print (spaces+make_spaces(4)+']')
    elif type_x is tuple:
        print ((spaces if preceding_spaces else "")+'( ' + str(len(x)) + ' )')
        if not deep:
            return
        print (spaces+make_spaces(4)+'(')
        for elem in x:
            deduce_structure(elem, spaces+make_spaces(8), depth+1, max_depth=max_depth)
        print (spaces+make_spaces(4)+')')
    elif  type_x is str:
        print ((spaces if preceding_spaces else ""), end='')
        print (x if len(x) < 50 else x[:20] + "......")
    else :
        print ((spaces if preceding_spaces else ""), end='')
        print (x)

