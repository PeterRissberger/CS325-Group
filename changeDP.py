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
	coins = v[amountIndex] #Set of coins used to reach target sum
	n = a[amountIndex] #Target sum for coins 
	change = [] #Array of count of each type of coin needed to reach target sum 
	coinIndex = len(coins) - 1 #Used to iterate through coin values 
	k = len(v) #size of data set
	n = len(a)
	coin = 0
	change.insert(0, 0)
	coins.insert(0, 0)
	
	#for x in range(2, n):
	for p in range(2, n):
		print "p\n"
		min = 9999999 #large number to represent infinity
		for i in range(1, k):
			print "i\n"
			if p >= coins[i]:
				print "p >= coins[i], yes"
				if (change[p - coins[i]] + 1) < min:
					print "(change[p - coins[i]] + 1) < min, yes"
					min = (change[p - coins[i]] + 1)
					coin = i
		#change[p] = min
		print "insert\n"
		change.insert(p, min)
		#coins[p] = coin
		coins.insert(p, coin)
	
	return change


#############
#MAIN PROGRAM
#############
#Read input file and display results 
scanInput()
print "Values: " 
print values
print "Amounts: "
print amounts


outfile = open('Amountchange.txt', 'w')
outfile.write("ChangeDP Algorithm Results:\n")

#Run algorithm for all amounts
for x in range(len(amounts)):
	change = changeDP(values, amounts)
	
	#File output
	outfile.write("Results for problem " + str(amountIndex) + "\nCoins: " + str(values[amountIndex]) + "\n")
	outfile.write("Amount: " + str(amounts[amountIndex]) + "\n") 
	outfile.write("Change: " + str(change) + "\n\n")
	

	amountIndex += 1
