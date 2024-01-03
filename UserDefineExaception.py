class Invalid_Password(Exception):
    pass


def varifyPass(p):
    if str(p)!="abc":
        raise Invalid_Password
    else:
        print("valid password")

varifyPass("abc")
varifyPass("xyz")