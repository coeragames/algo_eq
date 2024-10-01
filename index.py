from math import *

def sed(a, b, c):
    de = (b**2) - 4*a*c
    if de < 0:
        return "Pas de solution à cette équation"
    elif de == 0:
        l = -b / (2*a)
        return l
    else:
        n = (-b - sqrt(de)) / (2*a)
        m = (-b + sqrt(de)) / (2*a)
        return n, m

def trd(a, b, c, d):
    for root in range(-abs(int(d)), abs(int(d)) + 1):
        if root != 0 and a * root**3 + b * root**2 + c * root + d == 0:
            break
    else:
        return "Pas de solution particulière trouvée"
    
    nv_a = a
    nv_b = b + a * root
    nv_c = c + nv_b * root
    
    a_roots = sed(nv_a, nv_b, nv_c)
    
    return root, a_roots

def bic(a, b, c):
    roots = sed(a,b,c)
    n_roots = []
    for root in roots:
        if(root>=0):
            n_roots.extend([sqrt(root), -sqrt(root)])
    
    if(n_roots == []):
        return "Pas de solution à cette équation"
    
    return n_roots       
    
try:
    n = int(input("degré (2 ou 3 ou 4 (bicarré)) :\n"))
    a = float(input("a :\n"))
    b = float(input("b :\n"))
    c = float(input("c :\n"))

    if n == 2:
        print("Solution(s): ",sed(a, b, c))
    elif n == 3:
        d = float(input("d :\n"))
        print("Solution(s): ",trd(a, b, c, d))
    elif n == 4:
        print("Solution(s): ",bic(a, b, c))
    else:
        print("Degré non valide")
except:
    print("Erreur lors de l'execution du code")