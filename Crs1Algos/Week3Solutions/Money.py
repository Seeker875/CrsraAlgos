#python3

def MinCoins(Amount):
	temp=0

	i=0
	while temp<Amount:
		for coin in [10,5,1]:
			if temp+coin<=Amount:
				temp+=coin
				i+=1
				break
	return i

n = int(input())
print(MinCoins(n))