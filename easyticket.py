#Philani Antony Dalmini : Class 2
#Create a class that calculates prices of a ticket given the amount for category, number of tickets

class clsTicketSale :
    #Capture class variables 
    soccer = 40 
    movie = 75 
    theatre =100
    #capture instance variable via __init__()
    def __init__(self ,cell_number, ticket_price, number_of_tickets) :
        self.cell_number = cell_number
        self.ticket_price = ticket_price
        self.number_of_tickets = number_of_tickets
        
        #Capture the variables dynamically
        cell_number = input('Please provide your cellnumber\n')
        ticket_price = input('Please provide your category of choice\n')
        number_of_tickets = input('How many tckets are you purchasing \n')
        
    #Create a method that calculates the price of the ticket
    def calcPrepayment(self):
        if len(ticket_price) == len('soccer'):
            tic_total = clsTicketSale.soccer * number_of_tickets
            price_of_ticket = tic_total + (tic_total*0.15)
            price_of_ticket
            return price_of_ticket   
        elif len(ticket_price) == len('movie') :
            tic_total = clsTicketSale.movie * number_of_tickets
            price_of_ticket = tic_total + (tic_total*0.15)
            price_of_ticket
            return price_of_ticket
               
        elif len(ticket_price) == len('theatre') :
            tic_total = clsTicketSale.theatre * number_of_tickets
            price_of_ticket = tic_total + (tic_total*0.15)
            price_of_ticket
            return price_of_ticket
            
        else:
            print('The category you opted for is not yet available')
                
    print(f'Amout payable : {price_of_ticket}')
    print(f'Reservation for {ticket_price} for {number_of_tickets}')
    print(f'for {cell_number}')
