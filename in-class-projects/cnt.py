def is_valid_string(s):
    if not s or s[0] != 'a':
        return False
    
    cnta = 0
    cntb = 0
    for char in s:
        if char == 'a':
            cnta += 1
        elif char == 'b':
            cntb += 1
        else:
            return False
        
        if cntb > 0 and cnta == 0:
            return False
    
    return cnta == cntb

print(is_valid_string("aaabbb"))