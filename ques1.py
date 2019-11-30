class MyException(Exception):
    def __init__(self,v='My Name'):
        self.v = v
    def __str__(self):
        return str(self.v)
def Xyz(n,m):
    #n = int(input())
    #m = int(input())
    c = n+m
    if c<150:
        raise MyException('Custom Exception Occured')
    else:
        return c
#raise MyException('Custom Exception Occured')
print(Xyz(200,300))
        
