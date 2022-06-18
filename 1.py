var_int = 1235
sum_even = 0
x1 = var_int%10
var_int //= 10

x2 = var_int%10
var_int //= 10

x3 = var_int%10
var_int //= 10

x4 = var_int%10
s1 = x1%2
s2 = x2%2
s3 = x3%2
s4 = x4%2
b1 = s1 * x1
b2 = s2 * x2
b3 = s3 * x3
b4 = s4 * x4
y = b1 + b2 + b3 + b4
print(y)