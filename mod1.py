from random import randint
def generate(n):
    str=[]
    for i in range(n):
        str.append(chr(randint(48,118)))
    return ''.join(str)