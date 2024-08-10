itr = 1
while True:
    print(f"\n--------------------------------\n\tAttempt No. {itr}\n")
    val1= eval(input("Enter Value 1 : "))
    val2= eval(input("Enter Value 1 : "))
    opr= str(input("Enter Operation (+,-,*,/) (Y to exit) : "))
    if opr == "+":
        print(val1+val2)
    if opr == "-":
        print(val1-val2)
    if opr == "*":
        print(val1*val2)
    if opr == "/":
        print(val1*val2)
    if opr not in ["+","-","*","/"]:
        print("Enter Valid Input")
    if opr == "Y":
        break
    itr += 1