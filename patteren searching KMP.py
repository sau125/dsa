def computelps(lps,m,ptr):
    lps[0]=0
    i=0
    j=1
    while j<m:
        if lps[j]==lps[i]:
            i+=1
            lps[j]=i
            j+=1
        else:
            if i!=0:
                i=lps[i-1]
            else:
                lps[j]=0
                j+=1
def kmp(txt,ptr):
    n=len(txt)
    m=len(ptr)
    lps=[0]*m
    r=[]
    computelps(lps,m,ptr)
    i=0
    j=0
    while i<n:
        if txt[i]==ptr[j]:
            i+=1
            j+=1
            if j==m:
                r.append(j)
        elif j<m and  txt[i]!=ptr[j]:
            if j!=0:
                j=lps[j-1]
            else:
                
                i+=1
                

