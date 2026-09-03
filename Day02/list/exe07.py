def compterOccurrences(elemnt,list):
    count=0
    for i in list:
        if i ==elemnt:
            count+=1

    return count

N=[23,55,76,23,33,55,43,23]
compterOccurrences(23,N)