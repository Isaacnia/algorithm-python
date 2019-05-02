import pandas as pa
def coin_change(coins,cap):
	M = cap
	coins.insert(0,0)#initial
	count = [[0]*(M+1) for x in range(len(coins))]
	for i in range(len(coins)):
		for j in range(1,M+1):
			if i==1 and j<coins[i]:
				count[i][j] = 1000
			elif i==1:
				count[i][j] = 1+count[1][j-coins[1]]
			elif j<coins[i]:
				count[i][j] = count[i-1][j]
			else :
				count[i][j] = min(1+count[i][j-coins[i]],count[i-1][j]) 
	print(pa.DataFrame(count))#ans == count[len(coins)-1][M]
