def getname():
    while True:
        name=input(question)
        if name.isnumeric() ==False:
            if len(name)>=1:
                return name
            print("not a good name")



def getnumber(question,low,high):
    while True:
        number=input(question)
        if number.isnumeric():
            number=int(number)
            if number >=low and number <=high:
                return number
            print("not a good number")

def familysetup():
    fam_list=[]
    wagonleader=getname("whats the name of your leader")
    num = getnumber("how many in fam",2,5)
    for i in range(num):
        name=getname("whats the fam member name")
        fam_list.append(name)
        return wagonleader,fam_list




x,y = familysetup()
print(x,y)

    
            
