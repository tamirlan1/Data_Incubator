
import numpy as np
def partition(m,n):
    if n==1:
        if m >6:
            return None
        return [m]
    result = []
    maxvalue = min(6, m-n+1)
    for i in range(1, maxvalue+1):

        lst = partition(m-i, n-1)
        if not lst:
            continue
        for j in lst:
            if isinstance(j, int):
                a = [i,j]
            else:
                a = [i]
                a.extend(j)
            result.append(a)

    
    return result

a = partition(150, 50) #(24,8)

prod = []
for i in a:
    prod.append(np.product(i))

print 'prod len', len(prod)
print 'mean', np.mean(prod)
print 'sd', np.std(prod)
