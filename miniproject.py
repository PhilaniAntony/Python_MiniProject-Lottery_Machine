#Name : P.A Dlamini
#Project : Mini Project 1
import  random
def lottery_picker() :
    #Create two empty list
    userNumbers = []
    lotteryNumbers = []
    
    #Add numbers from userNumbers to list
    print('**************For this lottery, please enter six unique numbers and must be between 1 and 49**************')
    for userNumber in range(6) :
        
        userNumber = int(input('Please enter your lotto numbers : '))
        
        #Check if a userNumber is in the list already
        while userNumber in userNumbers :
            userNumber = int(input('Please re-enter a unique number'))
            
        #Check if the userNumber is in the range 1-49
        if userNumber > 0 and  userNumber < 50 :
            userNumbers.append(userNumber)
            userNumbers.sort()#Sorting the numbers
        #Create a variable that hold len(userNumbers)
        userNumbersLen = len(userNumbers)
    print(f'Your numbers today are {userNumbers}')
        
    '''    #Check if legth of list is eqaul to six
        if userNumbersLen < 6 :
            print(f'Your list has {userNumbersLen} item, please renter numbers between 1 and 49')
            numDiffernce = 6 - userNumbersLen
            for num in range(numDiffernce):
                num = int(input('Please re-enter  unique numbers'))    
    '''
    #Add numbers to the lotteryNumbers list
    for lotteryNumber in range(6):
        
        #Generate a random integer in  range 1-50
        lotteryNumber = random.randint(1,50)
        
        #Check if number is not in the lotteryNumbers list
        while lotteryNumber in lotteryNumbers :
            lotteryNumber = random.randint(1,50) 
        #Append number to a list
        lotteryNumbers.append(lotteryNumber)
        lotteryNumbers.sort()#Sorting the numbers
        48
    print(f'The lottery numbers today are {lotteryNumbers}')
    
    #Create a new list on the fly using list comprehension 
    winningNumbers = [userNumber for userNumber in userNumbers if userNumber in lotteryNumbers] 
        
    #Create a new variable winningLen that will hold the legnth of winningNumbers
    winningLen = len(winningNumbers)
    
    print(f'You have {winningLen} winning number(s) {winningNumbers}')
    
    #Create Logic for Winning
    if winningLen == 6 :
        print(f'You have 6 winning numbers and you won R10 000 000')
        
    elif  winningLen == 5 :
        print(f'You have 5 winning numbers and you won R8 584.00')
        
    elif  winningLen == 4 :
        print(f'You have 4 winning numbers and you won R2 384.00')
        
    elif  winningLen == 3 :
        print(f'You have 3 winning numbers and you won R100.50')
        
    elif  winningLen == 2 :
        print(f'You have 2 winning numbers and you won R20.00')
        
    elif  winningLen <= 1 :
        print(f'Try hard next time')

lottery_picker()
