# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 18:27:48 2024

@author: HP
"""



#dictionaries
Menu={'Latte': 
      {'ingredients': {
          "water":200,
          "milk":150,
          "coffee":20,
          },
          "cost":150
       },
      "Cuppuccino": 
            {'ingredients': {
                "water":100,
                "milk":250,
                "coffee":24,
                },
                "cost":100
             },
        "Espresso": 
              {'ingredients': {
                  "water":200,
                  "milk":0,
                  "coffee":100,
                  },
                  "cost":100
      
       
       }
      
      }
    
    
    
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print("sorry no enough resources")
            return False
    return True
    


def coin_process():
    print("please insert coin")
    total=0
    #coffee machine accepts only 5 , 10 , 20 coins
    coins_five=int(input("How many 5 $ ?"))
    coins_ten=int(input("How many 10 $ ?"))
    coins_twenty=int(input("How many 20 $ ?"))
    total=coins_five*5 + coins_ten*10 + coins_twenty*20
    return total


def is_payment_successful(money_received , coffe_cost):
    if money_received >= coffe_cost:
        global profit
        profit+=coffe_cost
        change=money_received-coffe_cost
        print(f"you have change: {change}")
        return True
    else:
        money_received<coffe_cost
        print("no suffecient money")
        return False
    
def make_coffee(coffe_name, coffe_ingredients):
    for item in coffe_ingredients:
        resources[item]-=coffe_ingredients[item]
    print(f"you selected {coffe_name}..Enjoy!!")
    
profit=0
resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100
}
is_on = True

while is_on:
    choice = input('What would you like to have? (Latte/Cuppucino/Espresso): ')
    
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        # Corrected the key usage in the print statement
        print(f"Water = {resources['water']} ml")
        print(f"Milk = {resources['milk']} ml")
        print(f"Coffee = {resources['coffee']} g")
        print(f"Money={profit}")
    else:
      coffe_type= Menu[choice]
      print(coffe_type)
      if check_resources(coffe_type['ingredients']):
         payment=coin_process()
         if is_payment_successful(payment, coffe_type['cost']):
            make_coffee(choice,coffe_type['ingredients'])

     
     
 

    