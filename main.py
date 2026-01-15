nomer = input("Telfon raqam kiriting: +998")

if len(nomer) >= 9:
    if nomer.startswith('90') or nomer.startswith('91'):
        print("Beeline")
    elif nomer.startswith('93') or nomer.startswith('94'):
        print("ucel")
    elif nomer.startswith('95') or nomer.startswith('99'):
        print("uzmobile")
    elif nomer.startswith('97'):
        print("mobiuz")
else:
    print("raqam 9 ta son bolishi kerak")
