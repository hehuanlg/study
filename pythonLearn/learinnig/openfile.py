with open('c:\pi.txt') as file_object:
    lines = file_object.readlines()
pi_str = ''
for line in lines:
    pi_str += line.strip()
print(pi_str[0:10])

