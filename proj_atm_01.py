import os.path #lbr read & write files
import csv #import & export format for CSV files
from datetime import datetime #lbr to set time and date 

file = 'history.txt'                                     # define the file 
masterlist = []                                          # create an array master list to  
masterhist = []                  # create an array master list to record transacctions 
error_msg1 = 'Unable to dispense full amount requested at this time'  # declare errors
error_msg2 = 'Unable to process your withdrawal at this time'
Insufficient_funds = 'You have been charged an overdraft fee of $5.'

# List date time 
def transc_append(x,y,z):
    record = []
    overdraft = []
    now = datetime.now()            # get date_time
    date = now.strftime('%Y-%m-%d') # get date 
    time = now.strftime('%H:%M:%S') # get time

    balance = x
    over =  y
    amount = z

    if over == 0:
        record.extend((date, time, amount, balance))
        masterhist.append(record)
    elif over == -5:
        record.extend((date, time, amount, balance))
        overdraft.extend((date, time, over, balance+over))
        masterhist.append(record)
        masterhist.append(overdraft)

    print(masterhist)




# GET CURRENT BALANCE FUNCTION
def current_balance(): 
    if os.path.getsize(file) == 0:   # check and set the file to 0
        return 500                   # add 500 to balance
    else:
        n = float(masterlist[-1][-1])
        return n

def transc_history():
    with open(file, 'r') as data:   # call history file  
        reader = csv.reader(data)   # read data in the file 
        for row in reader:          # iterate over the reader and add elements in a row 
            masterlist.append(row)
  


#   MAIN FUNCTION WITH FIVE ATM COMMANDS
def main():
    acc_reserve =  current_balance()    # define ATM balance
    atm_reserve = float(10000)          # add 10000 to the ATM balance
    print("**********\t\tBoston Regional ATM\t\t**********\n")
    print("Type 'help' to display the command list\n") #display ATM menu by typing list 
    command = input('>>> ')            
    command.lower()                     #take lowercase characters 

    while command != 'end':
        if command == 'help':                                                # display all the options avaiable for the ATM 
            print("\nwithdraw <value>\t\t\t-Withdraw money from account-\n") 
            print("deposit <value>\t\t\t\t-Deposit money to account-\n")
            print("balace\t\t\t\t\t-Print account balance-\n")
            print("history\t\t\t\t\t-Print transaction history-\n")
            print("end\t\t\t\t\t-Finish ATM transactions-\n")
            command = input('>>> ')

        # WITHDRAW FROM ACCOUNT
        elif 'withdraw' in command:         
            if command == 'withdraw':
                print('\nAmount not specified. Please try again.\n') # errors when not input int amount (Any integer)
                command = input('>>> ')                              # take any int value after typing withdraw
            else:
                brk = command.split()                                # split command 
                n = brk[-1]                                          
                amount = float(n)                                    # define variable that can take int decimals  
                if amount > acc_reserve:                             # if the user account is less than ATM balance 
                    acc_reserve -= amount                            # subtract amount from ATM balance 
                    print('Amount dispensed: $', amount,'\n')        # print the amount dispensed
                    fmt = "{:.2f}".format(acc_reserve)               
                    acc_over = acc_reserve - 5                       # initialize overwithdraw subtracting 5 from ATM balance
                    print(Insufficient_funds, ' Current balance: $', fmt,'\n') # display user's negative balance
                    #transc_append(acc_reserve, acc_over)
                    command = input('>>> ')                          
                elif amount > atm_reserve:                          # display error when the amount is greater than atm _reserve
                    print('\n'+error_msg1+'\n')                     
                    print('Please try a different amount\n')
                    command = input('>>> ')                         # input amount to withdraw 
                elif amount > 0:                                    
                    acc_reserve -= amount                           # subtract the amount from ATM if its less than the ATM balance
                    acc_over = 0                                    # define to 0
                    print('\nAmount dispensed: $', amount)
                    print('Current balance:', acc_reserve, '\n')
                     #transc_append(acc_reserve, acc_over, amount)
                    command = input('>>> ')
                else:
                    print('\nAmount not valid. Please try again.\n')  # error if any int is input
                    command = input('>>> ')
                    
        # DEPOSIT TO ACCOUNT
        elif 'deposit' in command:
            if command == 'deposit':
                print('\nAmount not specified. Please try again.\n') # enter int values 
                command = input('>>> ')                              
            else:
                brk = command.split()                               # separate the values
                n = brk[-1]
                amount = float(n)                                   # set them to float to take int 
                acc_reserve += amount                               # add amount to acc_reserve 
                acc_over =0                                      
                print('\nCurrent balance: $', acc_reserve,'\n')     # display acc_reserve 
                transc_append(acc_reserve, acc_over, amount)
                print()
                command = input('>>> ')

        # CHECK ACCOUNT BALANCE
        elif command == 'balance':
            print('\nCurrent balance: $', acc_reserve,'\n')
            command = input('>>> ')

        # DISPLAY ACCOUNT TRANSACTION HISTORY
        elif command == 'history': # Move this to a funtion 
            record = ""
            print("\n\t\t\tACCOUNT TRANSACTION HISTORY\n")      
            print("Date\t\t\tTime\t\t\tAmount\t\tBalance\n")    

            for i in masterlist:                            # iterate over the masterlist 
                for x in i:                                 # check for all the value in the masterlist and add spaces
                    record += x + "\t\t"                    
                record+="\n"
            print(record)
            command = input('>>> ')                         


        else:
            print("\nCommand not valid. Type 'help' to dispay the command list\n")
            command = input('>>> ')


transc_history()
#main()
#print("\n**********\t\tThanks for using Boston Regional ATM\t\t**********\n")
#print('\n',masterlist,'\n')        

transc_append(-60, -5, -560)
