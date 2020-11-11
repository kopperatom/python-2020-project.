##star wars the old republic MMO
##guild wars 2 MMO
##fortnite
##marvel avengers endgame
##captain america civil war
##iron man 3
##thor ragnorok
##star wars attack of the clones
##star wars a new hope
##indiana jones raiders of the last arch
##cobra kai series
##call of duty modern warfare 2020
##call of duty warzone
##fortnite save the world
##captain marvel
##karate kid 1984
##avatar
##jurassic park 
##war thunder
##kotor 1 star wars  knights of the old republic  1
##kotor 2 starwars knights of the old republic
##marvel vs capcom
##zelda breath of the wild
##rocket league
##minecraft



#lists and loops

top_games = ["star wars the old republic MMO",  #0
"guild wars 2 MMO",  #1
"fortnite",#2
"captain america civil war",#3
"iron man 3",#4
"thor ragnorok",#5
"star wars attack of the clones",#6
"star wars a new hope",#7
"indiana jones raiders of the last arch",#8
"cobra kai series",#9
"call of duty modern warfare 2020",#10
"all of duty warzone",#11
"fortnite save the world",#12
"captain marvel",#13
"karate kid 1984",#14
"avatar",#15
"jurassic park",#16
"war thunder",#17
"kotor 1 star wars  knights of the old republic  1",#18
"kotor 2 starwars knights of the old republic",#19
"marvel vs capcom",#20
"World of warcraft",#21
"Zelda link to the past",#22
"minecraft"#23
"overwatch"           
             ]#24

top_games.append("World of warcraft")
top_games.sort()
top_games.reverse()
top_games.insert(0,"Zelda link to the past")
top_games.insert(6,"Zelda link to the past")
#print(topGames.count("Zelda link to the past"))
#print(topGames.count("World of warcraft"))
num = top_games.index("Zelda link to the past",True)
game = top_games.pop(int(num))
#print(game)
num = top_games.index("Zelda link to the past",True)
game = top_games.pop(int(num))
#print(game)
#print(topGames.count("Zelda link to the past"))
newlist = top_games.copy()
top_games.clear()
#print(topGames)
#print(newlist)


points = 0
if len(top_games) >= 25 :
    points+=25
else:
        points -=25
if not top_games:
    points +=10
else:
    points-=25
    
if "World of warcraft" in newlist:
    points+=10
else:
    points-=10
if newlist.count("Zelda link to the past") > 1:
    points-=5
else:
    points+=5
if newlist.index("Zelda link to the past") == 0:
    points+=25
else:
    points-=25
if newlist.count("World of warcraft") > 1:
    points+=25
else:
    points-=25

for i in newlist:
    if "Pokemon" in i or "pokemon" in i:
        points-=100
    if "Halo" in i or "halo" in i:
        points-=100

    if "fortnite" in i or "Fortnite" in i:
        points-=1000000000000000000

    if "smash" in i:
        points-=50

highscore = [443, 950, 1000, 410, 875, 600, 550,500, 395, 308]

#print(top_games)
#print(len(top_games))

name = "kian"
#print(len(top_games))
x=0
while x != len(highscore)  :
   # print ("looping" ,x)
    highscore [x] +=1000
    x+=1
    
    y=0
while True:
    #print(y)
    y+=1

print (points)


##topGames.remove("Zelda link to the past")
##print(topGames.count("Zelda link to the past"))
##topGames.remove("Zelda link to the past")
##topGames.remove("World of warcraft")
##print(topGames.count("Zelda link to the past"))
##print(topGames.count("World of warcraft"))

##print(len(topGames))

##numbers = []
##x = 0
##while x != 100:
##    numbers.append(random.randint(1000,10000))
##    x+=1
##print(numbers)
##numbers.sort()
##print(numbers)
##numbers.reverse()
##print(numbers)


