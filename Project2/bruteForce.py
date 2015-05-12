import sys

#Global Vars
values = []     #Array of of coin sets (array of arrays)
amounts = []    #Array of target sums associated with coin sets
amountIndex = 0 #Number of amounts scanned so far 
sys.setrecursionlimit(5000)

def scanInput():
    global values
    global amounts

    infile = open('Amount.txt', 'r')    #File containing all arrays to be tested
    outfile = open('Amountchange.txt', 'w') #Outfile used as a temp file for arrays

    #Cleanup junk brackets and commas from file 
    string = infile.read()
    string = string.translate(None, '[],')  #Clean up junk commas and brackets from input
    outfile.write(string)
    outfile.seek(0)
        
    #Make array of arrays contained in infile
    with open('Amountchange.txt') as f: 
        index = 0   #Use to iterate through lines in input file 
        
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


def change(n, coins_available, coins_so_far):
	
    if sum(coins_so_far) == n:
        yield coins_so_far
    elif sum(coins_so_far) > n:
        pass
    elif coins_available == []:
        pass
    else:
        #print coins_so_far+[coins_available[0]];
        #print coins_available[:];
        for c in change(n, coins_available[:], coins_so_far+[coins_available[0]]):
            yield c
			
        for c in change(n, coins_available[1:], coins_so_far):
            yield c
def setup():			
    n = amounts[amountIndex]
    coins = values[amountIndex]

    solutions = [s for s in change(n, coins, [])]


    optimalSolution  = min(solutions, key=len)
    for op, val in enumerate(optimalSolution):
    #    print 'optimal solution:', op
         #print 'value:', val
         pass

    finalChange = [0] * len(coins)

    for c, coinsVal in enumerate(coins):
       for d, opVal in enumerate(optimalSolution):
            if coinsVal == opVal:
                finalChange[c] = finalChange[c]+1
    #print 'optimal solution:', optimalSolution

    #finalChangeCounter = 0
    #for n in finalChange:
        #print 'final change array:', n
           
    #print 'finalChangeCounter', sum(finalChange)

    return finalChange

#############
#MAIN PROGRAM
#############
scanInput()

outfile = open('Amountchange.txt', 'w')
outfile.write("Brute Force Algorithm Resutls:\n")

#Run algorithm for all amounts
for x in range(len(amounts)):
    terminalChange = setup()
    
    #File output
    outfile.write("Results for problem " + str(amountIndex) + "\nCoins: " + str(values[amountIndex]) + "\n")
    outfile.write("Amount: " + str(amounts[amountIndex]) + "\n") 
    outfile.write("Change: " + str(terminalChange) + "\n")

    # #Calculate minimum number of required coins
    minimum = 0
    for x in terminalChange: 
        minimum += x
    outfile.write("Minumum: " + str(minimum) + "\n\n")  
    
    amountIndex += 1
