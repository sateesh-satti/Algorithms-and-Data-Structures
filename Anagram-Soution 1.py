def check_anagram(a,b):
    anagram = True
    if len(a) != len(b):
        anagram = False
    blist = list(b)
    p1 = 0
    while p1 < len(a) and anagram:
        p2=0
        found=False
        while p2 < len(blist) and not found:
            if a[p1] == blist[p2]:
                found = True
            else:
                p2 = p2+1

        if found:
            blist[p2] = None
        else:
            anagram = False

        p1 = p1 + 1
    return anagram

check_anagram("heart","earth")
