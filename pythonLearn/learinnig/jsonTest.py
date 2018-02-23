import json
'''numbers = [2,3,5,7,9,10]
with open('c:\\numbers.json','w') as files:
    json.dump(numbers,files)
'''

def new_number():
    number = input('your favorite number? \n')
    with open('c:\\numbers.json','w') as f_number:
        numbers = json.dump(number,f_number)
        return numbers
def old_number():
    with open('c:\\numbers.json') as r_number:
        re_number = json.load(r_number)
    #read_number = renumber.read()
        return print("i know your favorite number! it's:" + re_number)
