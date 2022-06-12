import random
UPPER="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"
numbers="1234567890"
symbols="()?@#$&!{}[]"
answer=UPPER+lower+symbols+numbers
#Adjust Password Length Here
length=10
password="".join(random.sample(answer,length))
#OutPut
print(' Generated Password is ' + password)


