
def zbroj_prvih_n_prirodnih_brojeva(n):

    br = 0
    for i in range(1,n+1):
        br+=i
        
    return br
print(zbroj_prvih_n_prirodnih_brojeva(100))