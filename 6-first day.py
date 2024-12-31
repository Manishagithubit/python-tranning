try:
    a=9
    b=8
    print (a+b)
    raise Exception()
    except:
        print("there was an exception")
    finally:
        print("this run anyway")