def roman_to_int(s):
    total = 0 
    # is a list of chars seperated
    #check for special instances first
    if 'IV' in s:
        total += 4
        s= s.replace('IV','')
    if 'IX' in s:
        total += 9 
        s = s.replace('IX', '')
    if 'XL' in s:
        total += 40 
        s = s.replace('XL', '')
    if 'XC' in s:
        total += 90 
        s = s.replace('XC','')
    if 'CD' in s:
        total += 400 
        s = s.replace('CD','')
    if 'CM' in s:
        total += 900 
        s= s.replace('CM','')
    char = [c for c in s]
    print(char)
    # make sure only roman chars are in there  
    for c in char:
        if c == 'I':
            total += 1
        if c == 'V':
            total += 5 
        if c == 'X':
            total += 10
        if c == 'L':
            total += 50 
        if c == 'C':
            total += 100 
        if c == 'D':
            total += 500 
        if c == 'M':
            total += 1000
    return total 

