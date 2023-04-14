import re
x="89e9jcd^o38829@3%3,/mkl$w1"
numbers=re.sub("[^0-9]","", x )
print(numbers)
