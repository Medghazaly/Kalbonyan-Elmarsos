# Debugging

for value in range(10):
    print(value)
print('All done!')

# Error Messages

temperature = 50

# if temp < 60 # should you right the right variable and in the end write colon
    # print(Bring a jacket) # The text in function print missed the quote

i = 10
while i < 0: # you should write i > 0
    i -= 1
    print(i) 

# Test Case

def check_temp(temp):
    if  temp < 15:
        print('Bring a jacket')
    elif temp > 25 and temp <= 35:
        print('Pack a jacket')
    elif temp > 35:
        print('Leave the jacket at home')

check_temp(14)
check_temp(29)
check_temp(40)
