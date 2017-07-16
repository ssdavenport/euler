# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
# multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

multiples = [x for x in range(1000) if (x%3==0 or x %5 ==0)]

print(sum(int(x) for x in multiples))


# 3 repeats 10 times in 30
#sum30 = 1000 %

divisibles_by_3 = int((1000-1) / 3)
divisibles_by_5 = int((1000-1) / 5)
divisibles_by_15 = int((1000-1) / 15)

d3 = 3*divisibles_by_3*(1+divisibles_by_3) / 2
d5 = 5*divisibles_by_5*(1+divisibles_by_5) / 2
d15 = 15*divisibles_by_15*(1+divisibles_by_15) / 2

print(d3)
print(d5)
print(d3 + d5-d15)