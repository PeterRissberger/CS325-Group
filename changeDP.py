#Alex C. Way
#5/10/15
#ChangeDP
#CS 325

import sys

#Global Vars
values = []	#Array of of coin sets (array of arrays)
amounts = []	#Array of target sums associated with coin sets
amountIndex = 0 #Number of amounts scanned so far 

#Scans 'Amount.txt' and creates an array of the coin sets as well as their target amounts
def scanInput():
	global values
	global amounts

	infile = open('Amount.txt', 'r')	#File containing all arrays to be tested
	outfile = open('Amountchange.txt', 'w')	#Outfile used as a temp file for arrays

	#Cleanup junk brackets and commas from file 
	string = infile.read()
	string = string.translate(None, '[],') 	#Clean up junk commas and brackets from input
	outfile.write(string)
	outfile.seek(0)
		
	#Make array of arrays contained in infile
	with open('Amountchange.txt') as f: 
		index = 0	#Use to iterate through lines in input file 
		
		#Append every other line to values, every other *other* line to amounts
		for line in f: 
			if index % 2 == 0:
				line = line.split() 
				line = [int(i) for i in line]
				values.append(line)
			else: 
				line = int(line)
				amounts.append(line)
			index += 1

	#Clean up outfile used as temp work file
	outfile.truncate(0)
	outfile.close()

def changeDP(v, a):
	global amountIndex
	V = v[amountIndex] # coinValueList: Set of coins used to reach target sum
	A = a[amountIndex] # change: Target sum for coins 
	T = [] # coinsUsed: Table of minimum number of coins for v
	C = [] # minCoins: Array of count of each type of coin needed to reach target sum 
	
	for i in range(A+1): #was for v in range(2, A):
		coinCount = i
		newCoin = V[0]
		for j in [n for n in V if n <= i]:
			if C[i-j] + 1 < coinCount:
				coinCount = C[i-j] + 1
				newCoin = j
		C.insert(i, coinCount)
		T.insert(i, newCoin)
	print "C[i] = ", C[i]
	newC = convertChange(A, T)
	return newC


#takes the set of values found in changeDP() and extracts the answer
def convertChange(A, T):
	newC = []
	i = 0
	coin = A
	while coin > 0:
		print "size of T:", len(T)
		print "coin = ", coin
		thisCoin = T[coin]
		print "thisCoin = ", thisCoin
		newC.insert(i, thisCoin)
		coin = coin - thisCoin
		print "coin2 = ", coin
		i = i + 1
	print "returning ", newC
	return newC


#############
#MAIN PROGRAM
#############
#Read input file and display results 
scanInput()
print "Values: " 
print values
print "Amounts: "
print amounts


outfile = open('AmountchangeDP.txt', 'w')
outfile.write("ChangeDP Algorithm Results:\n")

#Run algorithm for all amounts
for x in range(len(amounts)):
	change = changeDP(values, amounts)
	
	#File output
	outfile.write("Results for problem " + str(amountIndex) + "\nCoins: " + str(values[amountIndex]) + "\n")
	outfile.write("Amount: " + str(amounts[amountIndex]) + "\n") 
	outfile.write("Change: " + str(change) + "\n\n")
	

	amountIndex += 1
