all: 
	@echo "***** Brute Force Resuls *****" > temp
	python bruteForce.py
	cat Amountchange.txt >> temp

	@echo "***** Change Greedy Results *****" >> temp
	python changegreedy.py
	cat Amountchange.txt >> temp
	
	@echo "***** Change DP Results *****" >> temp
	python changeDP.py
	cat Amountchange.txt >> temp

	cat temp > Amountchange.txt
