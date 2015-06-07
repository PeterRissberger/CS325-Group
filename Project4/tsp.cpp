//CS 325 Project 4: TSP
//Alex Way, Kristin Swanson, Peter Rissberger
//Build with: g++ -std=c++0x -g -o tsp tsp.cpp
//Run with: tsp inFile.txt

#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

//Global vars
ifstream inFile;
ofstream outFile;

//Reads file, counts input, returns arrays to main
int lineCount(char *infileName)
{
	int lineCount = 0;

  //Create/open in/outFile
  inFile.open(infileName);

  string outfileName = infileName;
  outfileName += ".tour";
  outFile.open(outfileName);

	//Count lines in file
	for (string line; getline(inFile, line); ++lineCount);
	//cout << "Lines in file: " << lineCount << endl;
	inFile.clear();
	inFile.seekg(0, ios::beg);
	//cout << "Lines: " << lineCount << endl;
	return lineCount;
}

//Populate Names, Xs, and Ys of arrays with inFile data
int populateArrays(string names[], int xs[], int ys[], int lines)
{

	string str;
	int i = 0;
	//cout << sizeof(xs);
	while (i < lines)
	{
		//cout << "Populating index " << i << endl;

		//Input city name
		inFile >> str;
		//cout << "Name = " << str << endl;
		names[i] = str;

		//Input city's x coordinate
		inFile >> str;
		//cout << "X = " << str << endl;
		xs[i] = stoi(str);

		//Input city's y coordinate
		inFile >> str;
		//cout << "Y = " << str << endl;
		ys[i] = stoi(str);

		i++;
	}
}

// Return true if test in arr
bool isIn(int arr[], int test, int length){
  for (int i = 0; i < length; i++) {
    if (arr[i] == test) return true;
  }
  return false;
}

// Returns distance between two points to the nearest integer
int distance(float x1, float y1, float x2, float y2) {
  return (int) (sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)) + .5);
}

unsigned int long tourLength(int xs[], int ys[], int order[], int points) {
  unsigned int long length = 0;

  for (int i = 0; i < points - 1; i++) {
    length += distance(xs[order[i]], ys[order[i]], xs[order[i+1]], ys[order[i+1]]);
  }
  length += distance(xs[order[points - 1]], ys[order[points - 1]], xs[order[0]], ys[order[0]]);

  return length;
}

// Greedy algorithm for initial tour, returns the tour length
unsigned int long greedyTour(int xs[], int ys[], int order[], int points)
{
  unsigned int long length = 0, current, bestPoint = 0, bestDist, nextDist;
  bool firstDist;

  // For each point, compare it to each of the other points that have not
  // yet been done, picking the point with the smallest distance to be next
  // in order
  for (int i = 0; i < points; i++) {
    current = bestPoint;
    order[i] = current;
    firstDist = true;
    bestDist = 0;
    //cout << "i = " << i << "\n";
    for (int j = 0; j < points; j++) {
        //cout << "j = " << j << "\n";
      if (isIn(order, j, points)) continue;
      nextDist = distance(xs[current], ys[current], xs[j], ys[j]);
      if (nextDist < bestDist || firstDist) {
	bestDist = nextDist;
	bestPoint = j;
	firstDist = false;
      }
    }
      length += bestDist;
  }
  // Add the connection from the last point to the first
  length += distance(xs[order[points - 1]], ys[order[points - 1]], xs[order[0]], ys[order[0]]);
  //cout << "Greedy tour total: " << length << endl;
  return length;
}

// 2-otp improvement from initial tour (as giving by order)
int opt2Tour(int xs[], int ys[], int order[], int points)
{
  int length = 0, bestPointIdx, bestDist, nextDist;
  bool isChange;

  /*cout << "Previous order: " << endl;
  for (int i = 0; i < points; i++) {
    cout << order[i] << endl;
  }*/

  // For each point, consider switching it with each other point, storing the
  // best solution until you have compared it to each point.  Once a point
  // is considered for all, it does not need to be considered again.
  for (int i = 0; i < points - 1; i++) {
    // Set best to the current distance and point
    bestDist = tourLength(xs, ys, order, points);
    bestPointIdx = i;
    for (int j = i+1; j < points; j++) {
      // Get the tour distance if we swapped order[i] with order[j]
      swap(order[i], order[j]);
      nextDist = tourLength(xs, ys, order, points);
      swap(order[i], order[j]);

      // if the new tour is shorter, store the point index j and the distance
      // of its tour as best option so far
      if (nextDist < bestDist) {
  	bestDist = nextDist;
	bestPointIdx = j;
      }
    }
    // Swap points if a better tour was found
    if (bestPointIdx != i) {
      swap(order[i], order[bestPointIdx]);
      isChange = true;
    }
  }
  length = tourLength(xs, ys, order, points);
  /*cout << "Improved length: " << length << endl;

  cout << "Improved order: " << endl;
  for (int i = 0; i < points; i++) {
    cout << order[i] << endl;
  }*/

 return length;
}

// 2-otp/3-opt improvement from initial tour (as giving by order)
int opt3Tour(int xs[], int ys[], int order[], int points, string names[])
{
  unsigned int long length = 0, bestPointIdx, bestPointIdx2, bestDist, nextDist;
  bool isChange; //TODO Use to re-run the entire algorithm if any swap was made

  /*cout << "Previous order: " << endl;
  for (int i = 0; i < points; i++) {
    cout << "a" << i << " " << order[i] << endl;
  }*/

  // For each point, consider switching it with each other point, storing the
  // best solution until you have compared it to each point.  Once a point
  // is considered for all, it does not need to be considered again.
  for (int i = 0; i < points - 1; i++) {
        //cout << "i = " << i << "\n";
    // Set best to the current distance and point
    bestDist = tourLength(xs, ys, order, points);
    bestPointIdx = i;
    bestPointIdx2 = i;
    for (int j = i+1; j < points; j++) {
        //cout << "j = " << j << "\n";
      // Get the tour distance if we swapped order[i] with order[j]
      swap(order[i], order[j]);
      nextDist = tourLength(xs, ys, order, points);
      swap(order[i], order[j]);

      // if the new tour is shorter, store the point index j and the distance
      // of its tour as best option so far
      if (nextDist < bestDist) {
  	bestDist = nextDist;
	bestPointIdx = j;
        bestPointIdx2 = i;
      }
      //cout << "entering k \n";
      for (int k = j+1; k < points; k++) {
        //cout << "k = " << k << "\n";

      // Get the tour distance if we swapped 123 to 231
      swap(order[i], order[j]); //213
      swap(order[j], order[k]); //231
      nextDist = tourLength(xs, ys, order, points);
      swap(order[j], order[k]);
      swap(order[i], order[j]);

      // if the new tour is shorter, store the points to swap in order
      if (nextDist < bestDist) {
  	bestDist = nextDist;
	bestPointIdx = j;
	bestPointIdx2 = k;
      }
      // Get the tour distance if we swapped 123 to 312
      swap(order[i], order[k]); //321
      swap(order[j], order[k]); //312
      nextDist = tourLength(xs, ys, order, points);
      swap(order[j], order[k]);
      swap(order[i], order[k]);

      // if the new tour is shorter, store the points to swap in order
      if (nextDist < bestDist) {
  	bestDist = nextDist;
	bestPointIdx = k;
	bestPointIdx2 = j;
      }
      }
    }
    // Swap points if a better tour was found
    if (bestPointIdx != i) {
      if (bestPointIdx2 != i) {
	swap(order[i], order[bestPointIdx]);
	swap(order[bestPointIdx], order[bestPointIdx2]);
      //cout << "Swapped 3 edges" << endl;
      } else {
        swap(order[i], order[bestPointIdx]);
	//cout << "Swapped 2 edges" << endl;
      }
      isChange = true;
    }
    //cout << "Current tour length: " << tourLength(xs, ys, order, points) << endl;

  }

  /*cout << "Improved order: " << endl;
  for (int i = 0; i < points; i++) {
    cout << "b" << i << " "  << order[i] << endl;
  }*/

  length = tourLength(xs, ys, order, points);
  //cout << "Improved length: " << length << endl;

  //Modified to output to Outfile
  //outFile << "Length: " << length;

  /*for (int i = 0; i < points; i++) {
    string identifier = names[order[i]];
    outFile << endl << identifier;
  }*/

 return length;
}

int main(int argc, char *argv[])
{
	//Count lines in input file
	int lines = lineCount(argv[1]);

	//Populate arrays with cities and coordinates
	string names[lines];
	int xs[lines];
	int ys[lines];
	int order[lines];
  	for (int i = 0; i < lines; i++) order[i] = -1;
	populateArrays(names, xs, ys, lines);

	int totalDist = greedyTour(xs, ys, order, lines);

    if(lines < 250)
    {
        //cout << "If";
        //opt2Tour(xs, ys, order, lines);
        //opt3Tour(xs, ys, order, lines, names);
        totalDist = opt3Tour(xs, ys, order, lines, names);
        totalDist = opt3Tour(xs, ys, order, lines, names);
    }

    outFile << "Length: " << totalDist;

  for (int i = 0; i < lines; i++) {
    string identifier = names[order[i]];
    outFile << endl << identifier;
  }

	return 0;
}
