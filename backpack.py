def backpack():
        print('Price of gem:')
        price = [int(x) for x in input().split(" ")]
        print('Weight of gem:')
        weight = [int(x) for x in input().split(" ")]
        print('Backpack capacity:')
        capacity = int(input())+1 # add 1 becuse list start 0
        price.insert(0,0) #initial price list
        weight.insert(0,0)#initial weight list
        num = len(weight) #number of gem
        c = [[0]*(capacity) for i in range(num)] #dynamic matrix
        for x in range(1,num): #The number of gem available
                for y in range(1,capacity):#Backpack capacity
                        if weight[x]<=y:
                                c[x][y] = max(c[x-1][y],price[x]+c[x-1][y-weight[x]])
                        else :
                                c[x][y] = c[x-1][y]
        print("Maximum of price in backpack =>",c[num-1][capacity-1])
backpack()
