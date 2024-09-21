from demo import print1
import getpass
from demo import again
cardno=(12341,12342,12343,12344,12345,12346,12347,12348,12349,123410)
name=('SANKET PADAVALE','SOHAM SHETE','PRANISH PATIL','ANUJ VEER',' VIRAJAS NAIK','KEDAR DODE','ADITYA SULE','PRANAV NIKAM','RAVIRAJ RAJE','SHRIKANT SATPUTE')
pinno=[12341,12342,12343,12344,12345,12346,12347,12348,12349,123410]
amounts = [1000, 2000, 3000,4000,5000,6000,7000,8000,9000,10000]

a=0
def print1(j):
    global a
    a=j
    return(a)
    
def again():
    cno=int(input("\n PLEASE ENTER YOUR CARD NUMBER"))
    if cno in cardno:
        for i in cardno:
            j=cardno.index(i)
            b=print1(j)
            #print(b)
            if(cno==i):
                print("\n WELCOME ",name[j])
                print('\n*******************************')
                pin=int(input("\n PLEASE ENTER YOUR PIN NUMBER \n"))
                if pin in pinno:
                    for i in pinno:
                        print(name[j],"Login Sucessfully....!")
                        #print(b)
                        return(b)
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
again()
j=a
             
#print(j)
print('\n----------ATM SYSTEM-----------')
# Main menu
while True:
	#os.system('clear')
	
	print('\n *******************************')
	response = input('\n SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \nLodgement__(L)  \nChange PIN_(P)  \nQuit_______(Q) \n: ').lower()
	print('\n*******************************')
	
	valid_responses = ['s', 'w', 'l', 'p', 'q']
	response = response.lower()
	if response == 's':
		
		print('\n *********************************************')
		print(str.capitalize(name[j]), 'YOU HAVE ', amounts[j],'RUPEES ON YOUR ACCOUNT.')
		print('\n *********************************************')
		
		
	elif response == 'w':
		
		print('\n *********************************************')
		cash_out = int(input('\n ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
		print('\n *********************************************')
		
		if cash_out%10 != 0:
			
			print('\n ******************************************************')
			print('\n AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH MULTIPLES OF 100')
			print('\n ******************************************************')
			
		elif cash_out > amounts[j]:
			
			print('\n *****************************')
			print('\n YOU HAVE INSUFFICIENT BALANCE')
			print('\n *****************************')
			
		else:
			amounts[j] = amounts[j] - cash_out
			
			print('\n ***********************************')
			print('\n YOUR NEW BALANCE IS: ', amounts[j], 'EURO')
			print('\n ***********************************')
			
			
	elif response == 'l':
		
		print('\n *********************************************')
		cash_in = int(input('\n ENTER AMOUNT YOU WANT TO LODGE: '))
		print('\n *********************************************')
		
		if cash_in%10 != 0:
			
			print('\n ****************************************************')
			print('\n AMOUNT YOU WANT TO LODGE MUST TO MATCH 100 RS NOTES')
			print('\n ****************************************************')
			
		else:
			amounts[j] = amounts[j] + cash_in
			
			print('\n ****************************************')
			print('\n YOUR NEW BALANCE IS: ', amounts[j], 'RUPEES')
			print('\n ****************************************')
			
	elif response == 'p':
		
		print('\n *****************************')
		new_pin = str(getpass.getpass('\n ENTER A NEW PIN: '))
		print('\n *****************************')
		
		if new_pin.isdigit() and new_pin != pinno[j] and len(new_pin) == 4:
			
			print('\n ******************')
			new_ppin = str(getpass.getpass('\n CONFIRM NEW PIN: '))
			print('\n *******************')
			
			if new_ppin != new_pin:
				
				print('\n ************')
				print('\n PIN MISMATCH')
				print('\n ************')
				
			else:
				pinno[j] = new_pin
				print('\n NEW PIN SAVED')
		else:
			
			print('\n *************************************')
			print('  \n  NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
			print('\n *************************************')
			
	elif response == 'q':
		exit()
	else:
		print('\n ------------------')
		print('\n ******************')
		print('\n RESPONSE NOT VALID')
		print('\n ******************')
		print('\n ------------------')

