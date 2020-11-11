
def get_menu_choice () :
    options = ["Burgers, fries, soda","Chicken salad, iced tea","pizza, soda"]
    cost = [6.99, 10.50, 5.72]

    print("your menu choices are:")
    for i in range(len(options)):
        print(str.format("{} - ${:5.2f} : {}",i,cost[i],options[i]))

    choice = ask_number("what will you have?",0,3)
    order = options[choice]
    price = cost[choice]
    tax = .075
    total = (price*tax) + price

    print(str.format("ok, you have ordered ----- {}",order))
    print(str.format("out the door you are looking at ----- ${:5.2f}",total))


def ask_number(question,low,high):
    """Ask for a number within a range. """
    response = None
    while response not in range(low,high):
        response = int(input(question))
    return response
            


    
running = "y"        
while running == "y":
    get_menu_choice()
    running = ask_yes_no("do you want to order more")
    
  
