def validate_pin(pin):
    s = str(pin)
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    if len(s)!=4 and len(s)!=6:
        return False
    else:
        for i in s:
            if i in numbers:
                continue
            else:
                return False
        return True