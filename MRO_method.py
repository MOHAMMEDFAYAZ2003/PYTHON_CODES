class A:pass
class  B(A):pass
class C(A):pass
class D(B,C):pass
print(A.mro())     #mro(A):A,Object
print(B.mro())     #mro(B):B,A,object
print(C.mro())     #mro(C):C,,A,Object
print(D.mro())     #mro(D):D,B,C,A,Object



class A:pass
class B:pass
class C:pass
class X(A,B):pass
class Y(B,C):pass
class P(X,Y,C):pass
print(A.mro())
print(B.mro())
print(C.mro())
print(X.mro())
print(Y.mro())
print(P.mro())


# formula:MRO(X)=X+Merge(MRO(P1),MRO(P2),..Parentlist
# mro(X):P+Merge(mro(X),mro(Y),mro(C)[XYC])
#        P+Merge(XABO,YBCO,CO)[XYC]
#        P+X+Merge(ABO,YBCO,CO)[YC]
#        P+X+A+Merge(BO,YBCO,CO)[YC]
#        P+X+A+Y+Merge(BO,BCO,CO)[C]
#        P+X+A+Y+B+Merge(O,CO,CO)[C]
#        P+X+A+Y+B+C+Merge(O,O,O)
#        P+X+A+Y+B+C+O


# mro(A):A+Merge(mro(B),mro(C),[BC])
#        A+Merge(BDEO,CDFO,BC)
#        A+B+Merge(DEO,CDFO,C)
#        A+B+C+Merge(DEO,DFO)
#        A+B+C+D+Merge(EO,FO)
#        A+B+C+D+E+Merge(O,FO)
#        A+B+C+D+E+F+Merge(O)
#        A+B+C+D+E+O+F+O

class D:pass
class E:pass
class F:pass
class B(D,F):pass
class C(D,F):pass
class A(B,C):pass
print(A.mro())


class P:
    a=10
    def __init__(self):
        print("Parent class constructer")
    @classmethod
    def m1(cls):
        print("Parent class method-1")
    @staticmethod
    def m2():
        print("Parent class method-2")
class C(P):
    a=11
    def __init__(self):
        super().__init__()
        print(super().a)
        super().m1()
        super().m2()
c=C()
print(c.a)


class TooYoungException(Exception):
    def __init__(self,arg):
        self.msg=arg
class TooOldException(Exception):
    def __init__(self,arg):
        self.msg=arg
age=int(input("Enter your age:"))
if age > 35:
    raise TooOldException("Waste of Marriage Enjoy Single Life")
elif age < 18:
    raise TooYoungException("Wait for sometime U will get a best match..")
else:
    print("You will get Match Details soon..Enjoy Pandago..")





