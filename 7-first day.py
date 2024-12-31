try:
    a=int(input("Enter the Number:"))
    b=8
    print(f"the number {a} is:",isinstance(a,int))
    raise Exception()
except:
    print("there was an exeception")
finally:
        print("this runs anyways")


 