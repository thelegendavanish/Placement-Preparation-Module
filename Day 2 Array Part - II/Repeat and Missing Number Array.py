class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        s = sum(A)
        s2 = 0  #for sum of squares
        for i in A:
            s2 += i*i

        k = n*(n+1)//2 - s  #Value of B-A
        l = ((n*(n+1)*(2*n+1))//6 - s2)//k      #Value of (B^2-A^2)/(B-A) == B+A
        b = (k+l)//2        #missing
        a = (l-k)//2        #repeated

        return [a,b]