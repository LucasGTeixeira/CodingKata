def reverseStringSlicing(string:str):
    print(f'{string[::-1]}') 

def reverseStringManual(string:str):
    str = ''
    for i in string:
        str = i + str
    print(str)


def reverseRecusivo(string):
    if len(string) == 0:
        return string
    else:
        return reverseRecusivo(string[1:]) + string[0]

reverseStringSlicing("abaco")
reverseStringManual("abaco")
print(reverseRecusivo("abaco"))