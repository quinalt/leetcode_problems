def half_string(s):
    half_length = len(s) / 2 
    s1 = s[0:int(half_length)]
    s2 = s[int(half_length):]
    vowels = 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'
    # get the vowel count 
    s1_char = [char for char in s1]
    s2_char = [char for char in s2]
    s1_count = 0 
    s2_count = 0 

    for i in s1_char:
        if i in vowels:
            s1_count += 1
    for i in s2_char:
        if i in vowels:
            s2_count += 1
    
    if s1_count == s2_count:
        return True
    if s1_count != s2_count:
        return False
