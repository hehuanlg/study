height = 1.75
weight = 80.5
bmi = 80.5/(1.75**2)
if 18.5<=bmi<=25:
    print('正常')
elif bmi<18.5:
    print('过轻')
elif 25<bmi<=28:
    print('过重')
