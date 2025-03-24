nimi=["admin"]
salas=["admin123"]
sees=False
user=""

def kontroll(p: str) -> bool:
    """
    Kontrollib parooli
    """
    s=0
    n=0
    e=0
    
    for t in p:
        if t.isupper():
            s+=1
        if t.isdigit():
            n+=1
        if not t.isalpha() and not t.isdigit():
            e+=1
    
    if len(p)>=8 and s>=1 and e>=1:
        return True
    return False

def reg():
    """
    Registreerimine
    """
    n=input("Nimi: ")
    if n in nimi:
        print("Nimi on olemas")
        return
    
    v=input("Ise või genereerida (i/g)? ")
    if v=="i":
        p=input("Parool: ")
        if kontroll(p):
            nimi.append(n)
            salas.append(p)
            print("Registreeritud")
        else:
            print("Parool on nõrk")
    elif v=="g":
        import random
        p=""
        while not kontroll(p):
            s1=".,:;!_*-+()/#¤%&"
            s2="0123456789"
            s3="qwertyuiopasdfghjklzxcvbnm"
            s4=s3.upper()
            s5=s1+s2+s3+s4
            ls=list(s5)
            random.shuffle(ls)
            p=''.join([random.choice(ls) for x in range(12)])
        print("Sinu parool on", p)
        nimi.append(n)
        salas.append(p)
        print("Registreeritud")

def login():
    """
    Autoriseerimine
    """
    global sees, user
    n=input("Nimi: ")
    p=input("Parool: ")
    
    if n in nimi:
        i=nimi.index(n)
        if salas[i]==p:
            sees=True
            user=n
            print("Logitud")
        else:
            print("Vale parool")
    else:
        print("Kasutaja puudub")

def parool():
    """
    Parooli muutmine
    """
    if not sees:
        print("Logi sisse")
        return
    
    p=input("Uus parool: ")
    if kontroll(p):
        i=nimi.index(user)
        salas[i]=p
        print("Parool muudetud")
    else:
        print("Parool on nõrk")

def taasta():
    """
    Parooli taastamine
    """
    n=input("Nimi: ")
    if n in nimi:
        import random
        p=""
        while not kontroll(p):
            s1=".,:;!_*-+()/#¤%&"
            s2="0123456789"
            s3="qwertyuiopasdfghjklzxcvbnm"
            s4=s3.upper()
            s5=s1+s2+s3+s4
            ls=list(s5)
            random.shuffle(ls)
            p=''.join([random.choice(ls) for x in range(12)])
        print("Uus parool on", p)
        i=nimi.index(n)
        salas[i]=p
    else:
        print("Kasutaja puudub")

def logout():
    """
    Väljalogimine
    """
    global sees, user
    if sees:
        sees=False
        user=""
        print("Välja logitud")
    else:
        print("Pole sisse logitud")
