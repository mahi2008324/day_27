def M(func):
    def inner(m):  
        total = 0
        for i in range(m+1):
            if i % 4 == 0 and i % 3 == 0:
                total = total + i
        print("The sum of numbers divisible by both 3 and 4 up to", m, "is:", total)
    return inner

@M
def m1(m):
    print("The sum of numbers divisible by both 3 and 4 upto {} is {}".format(m,total))


m1(100)