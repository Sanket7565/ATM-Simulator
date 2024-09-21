
cardno=[12341,12342,12343,12344,12345,12346,12347,12348,12349,123410]
name=('SANKET PADAVALE','SOHAM SHETE','PRANISH PATIL','ANUJ VEER',' VIRAJAS NAIK','KEDAR DODE','ADITYA SULE','PRANAV NIKAM','RAVIRAJ RAJE','SHRIKANT SATPUTE')
pinno=[12341,12342,12343,12344,12345,12346,12347,12348,12349,123410]
amounts = [1000, 2000, 3000,4000,5000,6000,7000,8000,9000,10000]
def print1(j):
    a=j
    print(a)
def again():
    cno=int(input("\n PLEASE ENTER YOUR CARD NUMBER"))
    if cno in cardno:
        for i in cardno:
            j=cardno.index(i)
            print1(j)
            if(cno==i):
                print("\n WELCOME ",name[j])
                print('\n*******************************')
                pin=int(input("\n PLEASE ENTER YOUR PIN NUMBER"))
            if pin in pinno:
                for i in pinno:
                    print("\n Login Sucessfully....!")
                    j=cardno.index(i)
                    print1(j)
                    return 0
                    break
            else:
                print("\n Wrong Pin Number")
                print('\n*******************************')
                again()
                break
    else:
        print("\n Wrong Card Number")
        print('\n*******************************')
        again()
        




