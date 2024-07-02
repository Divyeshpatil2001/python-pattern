def greet(fx):
    def mfx(*args,**kwargs):
        print("good morning!")
        fx(*args,**kwargs)
        print("thanks you for visit")
    return mfx
@greet
def showme():
    print("hello")
showme()

@greet
def sum(a,b):
    print(a+b)
sum(1,2)
