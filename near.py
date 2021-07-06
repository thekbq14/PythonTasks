string1 = str(input("First Word: "))
string2 = str(input("Second Word: "))
string3 = string1.replace('o', '', 1)

def near(string3, string2):
    if (string3 == string2):
     print (True)
    else:
     print (False)

near(string2, string3)