
#settings
com_base = 9.95
com_per = 1.00

def total_cost_of_trade(price, num_of_contracts):         #For options trading 
    cost = (price*num_of_contracts*100)+ com_base + (com_per*num_of_contracts)
    return cost                     #x = price of contract y=number of contracts
#to be continued: create algorithm for desired profits, what price to sell at,
#predicting future stock prices

def return_cost(x,y):
    ret = (x*y*100) - com_base - (com_per*y)
    return ret

def profit_prediction(x, y, z):   #z= current price of contract
    profit = ((z-x)*y*100)-com_base-(y*com_per)
    return profit

def contractcom(f):
    com = com_base+ (f * com_per)
    return float(com)

if __name__=='__main__':

    count = 0
    tries = 10000
    
    print("""pd = Price difference. PP = Profit predicter. type "exit" to go back """)
    while count < tries:
        setting = input('enter pd or pp ')
        while setting.lower() == 'pd':
            p1 = input('What is the price of the option? ')
            if p1 == 'exit':
                break
            p2 = input('What is the price you want to get out ')
            numcon = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for i in numcon:
                price1 = total_cost_of_trade((float(p1)), (float(i)))
                price2 = return_cost((float(p2)), (float(i)))
                print("%0.1f" %(i), " contract. Profit", "%.2f" %(price2 - price1), " buy cost: ", price1, "Sell Cost: ", "%.2f" %(price2))

            
        while setting.lower() == 'pp':
            
            potential = input\
        ('What is the price of the trade ')
            if potential == 'exit':
                break
            des = input('How much money do you want to make? ')
            numcon = input('How many contracts?')
            profit_goals = [25, 50, 75, 100]

            p = total_cost_of_trade((float(potential)), (float(numcon)))
            beven = (float(p)+ contractcom(float(numcon)))/(float(numcon)*100)
            desi = (float(p) + float(des) + contractcom(float(numcon)))/ (float(numcon)* 100)

            print ("The cost of this trade is",(p))
            print ("To break even, sell at this price", "%.3f" %(beven))
            print ("Sell at", "%.2f" % (desi), "to make", (des))

            for i in profit_goals:
                scenario_profit = (float(p)+ float(i) + contractcom(float(numcon)))/ (float(numcon)* 100)
                print("Sell at", "%.2f" % (scenario_profit), "to make", i)
            
            

            
     
