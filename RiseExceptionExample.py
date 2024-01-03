while True:
    try:
        a=int(input("Enter your Age ="))
        if a<18:
            raise Exception
    except Exception:
        print("Your Are Child")
    
    else:
        print("You are an Adult")
        break
    
