import MyModule

while True:
    print("VALIK:")
    print("1. Registreerimine")
    print("2. Sisse logimine")
    print("3. Parooli muutmine")
    print("4. Parooli taastamine")
    print("5. Välja logimine")
    print("6. Lõpp")
    
    if MyModule.sees:
        print(f"Tere, {MyModule.user}!")
    
    v=input("Valik: ")
    
    if v=="1":
        MyModule.reg()
    elif v=="2":
        MyModule.login()
    elif v=="3":
        MyModule.parool()
    elif v=="4":
        MyModule.taasta()
    elif v=="5":
        MyModule.logout()
        break
    else:
        print("Vale valik")
