'''
Given a number N, find all factors of N.

Example:

N = 6 
factors = {1, 2, 3, 6}
Make sure the returned array is sorted.

Problem Approach:

Complete code in the hint.
'''


import math as m

class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        res = []
        add = []
        for i in range(1, int(m.sqrt(A)+1)):
            if A%i == 0:
                res.append(i)
                if i != (A/i):
                    add.append(int(A/i))
                    
        for i in range(len(add)):
            res.append(add[-1-i])
        return res
    
    # ----------------------- is N prime?
     def isPrime(self, A):
        res = []
        for i in range(1, int(m.sqrt(A) + 1)):
            if A % i == 0:
                res.append(i)
            if len(res) >= 2:
                return 0

        if A != 1:
            return 1
        else:
            return 0

        
    #--------------------------- list of prime numbers
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        if A == 1:
            res = []
            return res
        elif A == 2:
            res = [2]
            return res
        elif A == 3 or A == 4:
            res = [2, 3]
            return res
        elif A == 5:
            res = [2, 3, 5]
            return res

        res = [2]
        n = A
        k = 0

        while res[k] <= res[-1]:

            i = k + 1
            while i < n:
                if res[k] == 2:
                    if i % res[k] != 0 and i != 1:
                        res.append(i)
                        if i == (n - 2) and (i % res[k]) != 0:
                            res.append(i+2)
                elif res[k] != 2:
                    if (res[i] % res[k]) == 0:
                        try:
                            res.remove(res[i])
                            i -= 1
                        except:
                            pass
                    n = len(res)

                i += 1
            k += 1
            if k == n:
                break

        return res
