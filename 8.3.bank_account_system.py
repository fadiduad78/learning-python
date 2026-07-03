import os

while True :
    print('1.Create Account ')
    print('2.Deposit Money  ')
    print('3.Withdraw Money  ')
    print('4.Check balance ')
    print('5.View Account Details ')
    print('6.Delete Account  ')
    print('7.Exit')


    choose = input('Choose (1 - 7): ')


    if choose == '1':
        if not os.path.exists('accounts.txt'):
            open('accounts.txt','x')
            print('File Created!\n')
        else:
            print('file already exists')
        
        account_number = input('Enter Account Number = ')

        found = False

        with open('accounts.txt', 'r') as f:
            for line in f:
                if line.strip() == account_number:
                    found = True
                    break
        if found :
            print('account number already exists... Try Another onee')
        
        else :
            account_name = input('Account Name : ')
            deposit_balance = input('Enter new balance : ')

            with open('accounts.txt', 'a') as f:
                f.write(account_number +  '\n')
                f.write(account_name + '\n')
                f.write(deposit_balance + '\n')

                print('Account Created Successfully!')

    elif choose == '2':
        account_number = input('Enter your account number: ')
        deposit_amount = float(input('Enter amount to deposit: '))

        found = False

        with open('accounts.txt', 'r') as f:
         lines = f.readlines()   # FIX: readlines, not read

        for i in range(0, len(lines), 3):
            if lines[i].strip() == account_number:
                found = True

            balance = float(lines[i+2].strip())   # get old balance
            balance += deposit_amount             # add new amount

            lines[i+2] = str(balance) + "\n"      # update in list
            break

        if found:
            with open('accounts.txt', 'w') as f:
             f.writelines(lines)   # rewrite whole file
            print("Deposit successful!")
        else:
         print("Account not found!")

    elif choose == '3':
       account_number = input('Enter Account Number : ')
       withdrawal_ammount = float(input('Enter ammount you want to withdraw: '))

       found = False

       with open('accounts.txt' , 'r') as f:
          lines = f.readlines()
        #    starts , stop (go through the whole list) , step (program jumps to the account number to check because index wise 0 ,1 ,2 ,3 0 and 3 are account numbers)
          for i in range(0,len(lines), 3):
             if lines[i].strip() == account_number :
                found = True

                balance = float(lines[i+2].strip())
                if withdrawal_ammount > balance:
                    print('insufficient balance!')
                else:
                    balance -= withdrawal_ammount
                    lines[i+2] = str(balance) + '\n'
                    print('Withdrawl successfull')

                break
             
          if found :
                    with open('accounts.txt', 'w') as f:
                        f.writelines(lines)
                    
          else:
                   print("Account not found!")

    elif choose == '4':

        account_number = input('Enter Account Number to See Details : ')

        found = False

        with open('accounts.txt' , 'r') as f:
            lines =  f.readlines()

        for i in range(0 ,len(lines) , 3):
            if lines[i].strip() == account_number:
                found = True
                total_balance = float(lines[i+2].strip())
                print(f'Your Account Current balance is : {total_balance} ')
                break
        if not found:
            print('Account Number Not Found!!')
    elif choose == '5':
        account_number = input('enter youyr account number :')

        found = False
        
        with open('accounts.txt' , 'r') as f:
            lines = f.readlines()
        
        for i in range(0 , len(lines), 3):
            if lines[i].strip() == account_number:
                found = True
                account_name = lines[i+1].strip()
                account_number = lines[i].strip()
                account_balance = float(lines[i+2].strip())

                print('----------------')

                print(f"{account_number}")
                print(f"{account_name}")
                print(f"{account_balance}")
                break
        if not found:
            print('account not found')



        


        



                
                
                








    


