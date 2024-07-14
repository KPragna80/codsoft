# password generator
import random
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"
numbers="0123456789"
symbols="{}?@$!%^*+_()"
all=lower+upper+numbers+symbols
lenth=16

for i in range(5):
    password="".join(random.sample(all,lenth))
    print(password)

