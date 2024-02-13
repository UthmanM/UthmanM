#constants
while True:
    balance = float (200000)
    print ("ATM")
    print ('''
    1) Balance
    2) Withdraw
    3) Deposit
    4)Quit
    ''')
#first condition, error report for ivalid entry (anything outside of  1,2,3,4)
    try:
        Option = (int (input ("Enter Option:")))
        
    except ValueError:
        print ("Enter Valid Option")
        
    except Exception:
        Option!= 1 or 2 or 3 or 4
        print ("Enter Valid Option")
        continue 

#If customer enters options 1  (Result in one condtion which is just to show the balance)   
    if Option ==1:
        print ("Balance N:",  balance) 
        
#if cutomer enters option 2, (Results in many condition, first, customer might enter less than 500 which is unwithrawable,
# the second condition is if the amount of money to be withdrawn is less than or equals to the balance, which is valid and 
#will in return show the current balance. The third and final possibilities is that the amount entered for withdrawal is 
#more than balance)     
    if Option==2:
        print ("Balance N:",  balance)
        
        def Withdraw(Amount= float (input("Enter Amount N:  "))):
            Mount = balance-Amount
           
            return Mount
        
        if Withdraw < 500:  
            print ("Enter Valid Amount")
            
        if Withdraw>500:
           def  Current_Balance():
               (balance-Withdraw)
               print ("Current Balance N", Current_Balance)
      
        if Withdraw > balance:
            print ("Insufficient Funds")
    
        else:
            print ("NO WITDRAWAL MADE")
            
            
    if Option == 3:
        print ("Balance $:",  balance)
        
        def Deposit  (Amount = float (input("Enter Amount N:  "))):
            Amount +0
        
        def  Current_Balance_():
            ( balance + Deposit)
          
                   
            
            if Deposit <=0:
                print ("Enter Valid Amount")
    
        if Deposit >0:
           
            print ("Current Balance N",  Current_Balance_())
       
        else:
            print ("NO DEPOSIT MADE")
            
    if Option== 4:
        exit ()
    
        print ("Thank you for banking with us")
    else:
          break


