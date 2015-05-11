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
	V = v[amountIndex] #Set of coins used to reach target sum
	A = a[amountIndex] #Target sum for coins 
	T = [] #Table of minimum number of coins for v
	C = [] #Array of count of each type of coin needed to reach target sum 
	#coinIndex = len(T) - 1 #Used to iterate through coin values 
	n = len(V) #size of data set
	coin = 0
	T.insert(0, 0) #large number to represent infinity
	#C.insert(0, 0)
	#print "V: %d" %V
	#print ", A: %d\n" %A
	
	for v in range(0, A): #was for v in range(2, A):
		#print "v\n"
		min = 9999999 #large number to represent infinity
		for i in range(1, n):
			#print "i\n"
			if v >= V[i]:
				#print "v >= V[i], yes"
				if (T[v - V[i]] + 1) < min:
					#print "(T[v - V[i]] + 1) < min, yes"
					min = (T[v - V[i]] + 1)
					coin = i
		#T[v] = min
		#print "insert\n"
		T.insert(v, min)
		#coins[v] = coin
		C.insert(v, coin)
	newC = convertChange(C, A, V)
	return newC


#takes the set of values found in changeDP() and extracts the answer
def convertChange(C, A, V):
	newC = []
	i = 0
	coin = A
	while coin > 0:
		print "size of C:", len(C)
		print "coin = ", coin
		thisCoin = V[C[coin-1]]
		print "thisCoin = ", thisCoin
		newC.insert(i, thisCoin)
		coin = coin - thisCoin
		i = i + 1
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
