def f(x):
    return ((3.5*10**7) + (0.401*((1000/x)**2))) * (x - (1000*42.7*10**-6)) - ((1.3806503*10**-23)*1000*300)
def fp(a,b):    
    c = 1   
    n = 0
    X = []
    Y = []
    while (f(c) > 10**-12) or (f(c) < -(10**-12)):        
        c = b - ((f(b)*(b-a))/(f(b)- f(a)))
        n += 1
        X.append(n)
        Y.append(c)
        if c==a or c==b:
            return c, n, X, Y
        if f(c)*f(a) < 0:            
            b = c
        elif f(c)*f(b) < 0:            
            a = c          
    return c, n, X, Y

a,n,x,y = fp(-0.5,1)
print(a,n)

%matplotlib inline
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 10))
plt.style.use('fivethirtyeight')
plt.axis([-100, x[len(x)-1]+100, min(y)-0.1, max(y)+0.1])
plt.plot(x,y, '-b', color='green')
plt.show()