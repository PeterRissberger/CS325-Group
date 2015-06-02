//CS 325 Project 4: TSP
//Alex Way, Kristin Swanson, Peter Rissberger
//Build with: g++ -std=c++0x -g -o tsp tsp.cpp
//Run with: tsp inFile.txt

#include <iostream> 
#include <fstream>
#include <string> 
using namespace std; 

//Global vars
ifstream inFile; 
ofstream outFile; 


//Reads file, counts input, returns arrays to main
int lineCount(char *infileName)
{
	int lineCount = 0; 
	inFile.open(infileName); 

	//Count lines in file 
	for (string line; getline(inFile, line); ++lineCount);
	cout << "Lines in file: " << lineCount << endl; 
	inFile.clear();
	inFile.seekg(0, ios::beg);
	cout << "Lines: " << lineCount << endl; 
	return lineCount; 
}

//Populate Names, Xs, and Ys of arrays with inFile data
int populateArrays(string names[], int xs[], int ys[], int lines)
{

	string str; 
	int i = 0; 
	cout << sizeof(xs); 
	while (i < lines)
	{
		cout << "Populating index " << i << endl; 

		//Input city name
		inFile >> str; 
		cout << "Name = " << str << endl; 
		names[i] = str; 

		//Input city's x coordinate
		inFile >> str; 
		cout << "X = " << str << endl; 
		xs[i] = stoi(str); 
		
		//Input city's y coordinate
		inFile >> str; 
		cout << "Y = " << str << endl; 
		ys[i] = stoi(str); 
				
		i++; 
	}
}

int main(int argc, char *argv[])
{
	//Count lines in input file 
	int lines = lineCount(argv[1]); 

	//Populate arrays with cities and coordinates
	string names[lines];
	int xs[lines];
	int ys[lines];
	populateArrays(names, xs, ys, lines);


	return 0;
}
