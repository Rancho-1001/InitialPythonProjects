# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 07:10:14 2023

@author: user
"""

#Constants for the calculation given

#Loop over some values
#   collect some inputs
#       location
#       square footage
#       maximum monthly payments
#       expected down payments
#       Annual APR
#
#   process inputs
#   
#   Branch to different cases
#       have square footage, no max monthly payment
#       have max monthly payment, no square footage
#       have both 
#       have neither 
#   
#   Ask for monthly payment schedule(Y or N)
#
#   ask to go again



NUMBER_OF_PAYMENTS = 360    # 30-year fixed rate mortgage, 30 years * 12 monthly payments 
SEATTLE_PROPERTY_TAX_RATE = 0.0092
SAN_FRANCISCO_PROPERTY_TAX_RATE = 0.0074
AUSTIN_PROPERTY_TAX_RATE = 0.0181
EAST_LANSING_PROPERTY_TAX_RATE = 0.0162
AVERAGE_NATIONAL_PROPERTY_TAX_RATE = 0.011
SEATTLE_PRICE_PER_SQ_FOOT = 499.0
SAN_FRANCISCO_PRICE_PER_SQ_FOOT = 1000.0
AUSTIN_PRICE_PER_SQ_FOOT = 349.0
EAST_LANSING_PRICE_PER_SQ_FOOT = 170.0
AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT = 244.0
APR_2023 = 0.0668



print("\nMORTGAGE PLANNING CALCULATOR\n============================ ")   
 #Print welcome message 
user_input_lower = 'y'

while user_input_lower == "y":
    print("\nEnter a value for each of the following items or type 'NA' if unknown ")
    location = input("\nWhere is the house you are considering (Seattle, San Francisco, Austin, East Lansing)? ") #Ask user for location
    location_lower = location.lower()
    if location_lower == "seattle": 
        Tax_Rate = SEATTLE_PROPERTY_TAX_RATE
        Price_per_sq_foot = SEATTLE_PRICE_PER_SQ_FOOT
    elif location_lower == "san francisco":
        Tax_Rate = SAN_FRANCISCO_PROPERTY_TAX_RATE
        Price_per_sq_foot = SAN_FRANCISCO_PRICE_PER_SQ_FOOT
    elif location_lower == "austin":
        Tax_Rate = AUSTIN_PROPERTY_TAX_RATE
        Price_per_sq_foot = AUSTIN_PRICE_PER_SQ_FOOT
    elif location_lower == "east lansing":
        Tax_Rate = EAST_LANSING_PROPERTY_TAX_RATE
        Price_per_sq_foot = EAST_LANSING_PRICE_PER_SQ_FOOT
    else:
        Tax_Rate = AVERAGE_NATIONAL_PROPERTY_TAX_RATE
        Price_per_sq_foot = AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT
        location = "the average U.S. housing market"  
     
    
    desired_sq_ft = input("\nWhat is the maximum square footage you are considering? ")  #Ask user for maximum square feet
    if desired_sq_ft != "NA":
        desired_sq_ft_float = float(desired_sq_ft)
        
    #else:
        #statement1 = ("\nIn {}, a maximum monthly payment of ${:.2f} allows the purchase of a house of {:.0f} sq.feets for ${:.0f}\n\t"
                    # "assuming a 30-year fixed rate mortgage with a ${} down payment at {:.1f}% APR.")
        #print(statement1.format(location, max_monthly_pt, desired_sq_ft, Total_cost_of_home, down_payment, current_APR ))
        
    max_monthly_pt = input("\nWhat is the maximum monthly payment you can afford? ") #Ask user for maximum monthly payment
    if max_monthly_pt != "NA":
        max_monthly_payment_float = float(max_monthly_pt)
    #else:
        #maximum_monthly_payment
        
    if desired_sq_ft == "NA" and max_monthly_pt == "NA":  #Checks to see if user enterred values if not break out of the loop
        print("\nYou must either supply a desired square footage or a maximum monthly payment. Please try again.")
        break
      
    down_payment = input("\nHow much money can you put down as a down payment? ") #Ask user for down payment
    if down_payment != "NA":
        down_payment_float = float(down_payment)
    else:
        down_payment_float = 0
        
        
    APR = input("\nWhat is the current annual percentage rate? ")   #Ask User for APR

    if location == "the average U.S. housing market":
        print("\nUnknown location. Using national averages for price per square foot and tax rate.")
    
    if APR.isalpha():
        APR_float = APR_2023
        Interest_rate = APR_float / 12
             
    else:
        APR_float = float(APR) / 100
        Interest_rate = APR_float / 12 
        
    if desired_sq_ft != "NA":
        desired_sq_ft_float = float(desired_sq_ft)
        Total_cost_of_home = desired_sq_ft_float * Price_per_sq_foot     #calculates total cost for a home
        Principal_loan = Total_cost_of_home - down_payment_float 
        I = Interest_rate
        P = Principal_loan
        N = NUMBER_OF_PAYMENTS
        
        A = (P * I) * (1 + I)**N
        B = (1 + I)**N - 1
        
        Monthly_Mortgage_payment = A / B 
        
        Monthly_Tax_Payment = (Tax_Rate * Total_cost_of_home) / 12
        
        Estimated_Monthly_Payment = Monthly_Mortgage_payment + Monthly_Tax_Payment
        
        statement = ("\n\nIn {}, an average {:.0f} sq. foot house would cost ${:.0f}.\n"
                     "A 30-year fixed rate mortgage with a down payment of ${:.0f} at {:.1f}% APR results\n"
                     "\tin an expected monthly payment of ${:.2f} (taxes) + ${:.2f} (mortgage payment) = ${:.2f}")
        print(statement.format(location, desired_sq_ft_float, Total_cost_of_home, down_payment_float, APR_float * 100, Monthly_Tax_Payment, Monthly_Mortgage_payment, Estimated_Monthly_Payment))
        
        
        
        if max_monthly_pt != "NA" and desired_sq_ft != "NA":
            if max_monthly_payment_float > Estimated_Monthly_Payment:
                print("Based on your maximum monthly payment of ${:.2f} you can afford this house.".format(max_monthly_payment_float))
            else:
                print("Based on your maximum monthly payment of ${:.2f} you cannot afford this house.".format(max_monthly_payment_float))
                
        prompt_user_for_amortization = input("\nWould you like to print the monthly payment schedule (Y or N)? ")
        prompt_user_lower = prompt_user_for_amortization.lower()
        
        if prompt_user_lower == "y":
            print("\n{:^7}|  {:^9} |  {:^10} | {:^11}  ".format("Month", "Interest", "Principal", "Balance"))
            print("="*48)
            remaining_loan_amount = P 
            i = 1
            while remaining_loan_amount > 0: 
                payment_to_interest = remaining_loan_amount * I 
                print("{:^7d}| ${:>9.2f} | ${:>10.2f} | ${:>11.2f}".format(i, payment_to_interest,Monthly_Mortgage_payment - payment_to_interest, remaining_loan_amount))  
                payment_to_loan = Monthly_Mortgage_payment - payment_to_interest
                remaining_loan_amount -= payment_to_loan
                # print("{:^7}|${:^8.2f}|${:^9.2f}|${:^10.2f}".format(i, payment_to_interest, P, remaining_loan_amount))   
                i += 1
    else:
        I = Interest_rate
        N = NUMBER_OF_PAYMENTS
        A = I * (1 + I)**N
        B = (1 + I)**N - 1 
        desired_sq_ft_float = ((max_monthly_payment_float * B)/A + down_payment_float)/ Price_per_sq_foot
        Total_cost_of_home = Price_per_sq_foot * desired_sq_ft_float
        statement = ("\nIn {}, a maximum monthly payment of ${:.2f} allows the purchase of a house of {:.0f} sq.feets for ${:.0f}\n\t"
                     "assuming a 30-year fixed rate mortgage with a ${} down payment at {:.1f}% APR.")
        print(statement.format(location, max_monthly_payment_float , desired_sq_ft_float, Total_cost_of_home, down_payment_float, APR_float *100 ))
            
        
    
   
    
            '''
   #  #Calculations involving data collected above begins from here    
   
   # # Total_cost_of_home = desired_sq_ft_float * Price_per_sq_foot     #calculates total cost for a home
   #  Principal_loan = Total_cost_of_home - down_payment_float         #Calculates the principal loan 
    
   #  #Converts the variables and constants into simpler variables to make the equation readable
   #  I = Interest_rate
   #  P = Principal_loan
   #  N = NUMBER_OF_PAYMENTS
    
    
    
   #  #print(I)
    
   #  A = (P * I) * (1 + I)**N
   #  B = (1 + I)**N - 1
    
   #  Monthly_Mortgage_payment = A / B 
    
   #  Monthly_Tax_Payment = (Tax_Rate * Total_cost_of_home) / 12
    
   #  Estimated_Monthly_Payment = Monthly_Mortgage_payment + Monthly_Tax_Payment
    
   #  #print("\nIn {}, an average {} sq. foot house would cost ${}.".format(location, desired_sq_ft, Total_cost_of_home))
   #  #print("\nA 30-year fixed rate mortgage with a down payment of ${} at {}% APR results \n\t in an expected monthly payment of ${:.2f} (taxes) + ${:.2f} (mortgage payment) = ${:.2f}".format(down_payment,current_APR,Monthly_Tax_Payment,Monthly_Mortgage_payment,Estimated_Monthly_Payment))
    
   
    

   #  prompt_user_for_amortization = input("\nWould you like to print the monthly payment schedule (Y or N)? ")
   #  prompt_user_lower = prompt_user_for_amortization.lower()
    
   #  if prompt_user_lower == "y":
   #      print("\n{:^7}|{:^9}|{:^10}|{:^11}".format("Month", "Interest", "Principal", "Balance"))
   #      print("-"*47)
   #      remaining_loan_amount = P - Estimated_Monthly_Payment
   #      for i in range(1,N+1):
   #          payment_to_interest = remaining_loan_amount * I 
   #          payment_to_loan = Estimated_Monthly_Payment - payment_to_interest
   #          remaining_loan_amount -= payment_to_loan
   #          print("{:^7}|${:^8.2f}|${:^9.2f}|${:^10.2f}".format(i, payment_to_interest, P, remaining_loan_amount))
        
   #  else:
    #user_input = input("\nWould you like to make another attempt (Y or N)? ")
    #user_input_lower = user_input.lower() '''
