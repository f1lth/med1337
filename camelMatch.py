def camelMatch(queries, pattern):
    """
    :type queries: List[str]
    :type pattern: str
    :rtype: List[bool]
    """
    out = list()

    def getPattern(pat):
        '''isolate the pattern regardless of format'''
        p = list()
        if len(pat) == 2:
            p.append(pat[0])
            p.append(pat[1])
            return p
        for i in range(len(pat)):
            if pat[i].isupper():
                for j in range(i+1, len(pat)):
                    if pat[j].isupper() and len(pat) != 2:
                        p.append(pat[i:j])
                        break
                    elif j == (len(pat)-1) and len(pat) != 2:
                        p.append(pat[i:j+1])
        return p

    pat = getPattern(pattern)

    def check(a, b):
        '''compare if pattern - b holds true for a list of strings - a'''
        # if they have unequal lengths it cannot be true
        if len(a) != len(b):
            return False
        # for any given pattern check if its in the query
        for i, query in enumerate(a):
            for x in range(len(b[i])):
                if b[i][x] != query[x]:
                    return False
        return True

    # loop through and append bools to the output list
    for query in queries:
        e = list()
        for i in range(len(query)):
            if query[i].isupper():
                for j in range(i+1, len(query)):
                    if query[j].isupper():
                        e.append(query[i:j])
                        break
                    elif j == (len(query)-1):
                        e.append(query[i:j+1])
        out.append(check(e,pat))
    return out

def main():
    queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
    pattern = "FB"

    queries1 = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
    pattern1 = "FoBaT"

    queries3 = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
    pattern3 = "FoBa"
    
    print(camelMatch(queries, pattern))
    print(camelMatch(queries1, pattern1))
    print(camelMatch(queries3, pattern3))


main()                
            
        