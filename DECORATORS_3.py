def M(func):
    def inner(m):  
        total = 0
        for i in range(m):
            if i % 2 != 0:
                total = total + i
        print("The sum of odd numbers up to", m, "is:", total)
    return inner

@M
def m1(m):
    print("The sum of odd numbers upto {} is {}".format(m,total))


m1(101)
