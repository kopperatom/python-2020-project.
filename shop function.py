def shop(money):
    ammo = 0
    food = 0
    clothes = 0
    ox = 0
    parts = []
    bill = 0
    items = ["Oxen", "food", "ammo",
             "clothes", "waggon parts",
             "check out"]
    spent_on_items = [0.00,0.00,0.00,0.00,0.00,bill]
    print("before leaving independence you should buy equipment and supplies.")
    print(str.format("you have{} in cash to make this trip",money))
    print("remember you can buy supplies along the way so you dont have to spend it all now")
    print()
    print()
    input("press any key to continue")
    while True:
        spent_on_items[len(spent_on_items)-1] = bill
        print("welcome to the generel shop")
        print("here is a list of things you can buy")
        print()
        print("============================================")
        for i in range(len(items)):
            print(str.format("\t{}:    {:20}    ${:.2f}",i+1,items[i],spent_on_items[i]))
        print("============================================")
        print()
        print(str.format("total bill so far:      ${:.2f}",bill))
        print(str.format("total funds avalable:   ${:.2f}",money-bill))
        choice = int(input("what do you want to buy"))#use get_number function not input
        if choice == 1:
            print("""
            there are 2 oxen in a yoke;
            i recomend at least 3 yokes.
            i charge $40 a yoke""")
            print(str.format("total bill so far:        ${:.2f}",bill))
            answer = int(input("how many yoke do you want"))
            cost = answer*40
            bill += cost
            ox = answer * 2
            spent_on_items[0] = cost
            
        if choice == 2:
            print("""
            i recomend 200 pounds of food
            pure person.
            i charge .20 a pound""")
            print(str.format("total bill so far:       ${:.2f}",bill))
            answer = int(input("how much food do you want"))
            cost = answer*.2
            bill += cost
            food = answer * 1
            spent_on_items[1] = cost
            
        if choice == 3:
            print("""
            1 box equals 20 bullets.
            1 box is 2.00 a box""")
            print(str.format("total bill so far:       ${:.2f}",bill))
            answer = int(input("how much boxes of ammo would you like"))
            cost = answer*2.00
            bill += cost
            ammo = answer * 1
            spent_on_items[2] = cost
            
        if choice == 4:
            print("""
            1 set of clothes is 10.00.
            i recomend 2 sets a person""")
            print(str.format("total bill so far:       ${:.2f}",bill))
            answer = int(input("how much clothing do you want"))
            cost = answer*10.00
            bill += cost
            clothes = answer * 1
            spent_on_items[3] = cost
        if choice == 5:
            pass
        if choice == 6:
            pass

money = 2000
shop(money)    
