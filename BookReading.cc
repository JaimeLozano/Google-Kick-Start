#include <iostream>
#include <vector>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>

using namespace std;

/* Supervin librarian 
	Ancient book
	- N pages from book --> 1 to N
	- M pages torn out --> P1, P2, ..., Pm

	- Q lazy Readers --> Not necesarily read all pages.
		Qi Reader only read pages multiples of Ri and not torn out

	Result --> pages read by each reader.

	INPUT
	First stringVector[i] --> number of tests cases, T.
	 three integers N, M, and Q, 
	 - the number of pages in the book, N
	 - the number of torn out pages in the book, M
	 - and the number of readers, Q
	
	 The second stringVector[i] contains M integers, the i-th of which is Pi. 
	 The third stringVector[i] contains Q integers, the i-th of which is Ri. 


*/

struct Data {
	int tests;
	int N;
	int M;
	int Q;
	vector<int> mVector;
	vector<int> qVector;	
}; 


bool tornOutPageComprobation(int page, vector<int> mVector) {
	bool Out = false;

	for(unsigned int i=0; i<mVector.size(); i++) { 
		if(page == mVector[i]) { // Case page torned out
			Out = true;
			break;
		}
	}

	return Out;
}

int ReadedPagesCalculator(Data test) {
	unsigned int page, readedPages = 0;
	bool pageTornedOut = false;

	for(unsigned int i=0; i<test.qVector.size(); i++) { // Lazy Reader Level
		for(unsigned int j=1; j < (unsigned)test.N+1; j++) { // Page from Book Level
			page = test.qVector[i]*j;	// Index * j number			
			if(page > (unsigned)test.N) { 								
				break;
			}
			pageTornedOut = tornOutPageComprobation(page, test.mVector); // Torned out pages level
			if(!pageTornedOut) {
				readedPages++;
			}
		}
	}

	return readedPages;
}

vector<Data> InputValues(vector<string> stringVector) {	

	string var;
	Data d;
	vector<Data> dataVector;
	d.tests = stoi(stringVector[0]); // Save tests

	for(unsigned int i=1, process = 0; i<stringVector.size(); i++) {
		if(process == 0) {
			// PROCESS 1 --> NMQ
			for(unsigned int j=0, internProcess=0; j<stringVector[i].size(); j++) {
				if(stringVector[i][j] != ' ') { // Add values to var string
					var += stringVector[i][j];
				} else {
					if(internProcess == 0) { // Save N
						d.N = atoi(var.c_str());
					} else if(internProcess == 1) { // Save M
						d.M = atoi(var.c_str());
					} 
					var.clear();
					internProcess++;
				}
			}
			d.Q = atoi(var.c_str());	// Save Q
			var.clear();
		} else if(process == 1) {
			// PROCESS 1 --> mVector
			for(unsigned int j=0; j<stringVector[i].size(); j++) {
				if(stringVector[i][j] != ' ') {
					var += stringVector[i][j];
				} else {
					d.mVector.push_back(atoi(var.c_str())); // Save M values
					var.clear();
				}
			}
			d.mVector.push_back(atoi(var.c_str()));
			var.clear();

		} else if(process == 2) {
			// PROCESS 2 --> qVector
			for(unsigned int j=0; j<stringVector[i].size(); j++) {
				if(stringVector[i][j] != ' ') {
					var += stringVector[i][j];      
				} else {
					d.qVector.push_back(atoi(var.c_str())); // Save Q values
					var.clear();      
				}
			}
			d.qVector.push_back(atoi(var.c_str()));
			var.clear(); 
		}
		if(process < 2) {
			process++;
		} else { // Value Reset and Back to process 0
			dataVector.push_back(d);
			d.M = -1;
			d.N = -1;
			d.Q = -1;
			d.mVector.clear();
			d.qVector.clear();
			process = 0;
		}
	}

	return dataVector;
}

void resultOutPut(vector<int> resultsVector) {

	for(unsigned int i=1; i<resultsVector.size()+1; i++) {
		cout<<"Case #"<<i<<": "<< resultsVector[i-1] << endl; // Case#i: number --> Format
	}
}

int main(int argc, char const *argv[]) {
	if(argc == 1) {
		bool inputExit = false;
		string s;
		vector<string> stringVector;


		while(inputExit == false) { // Pass input to string vector
			getline(cin, s);
			stringVector.push_back(s);
			if(s.size() == 0) {
				inputExit = true;
			}
			s.clear();
		}

		
		vector<Data> dataVector = InputValues(stringVector); // Pass string to values
		vector<int> resultsVector;

		for(unsigned int i=0, result = 0; i<dataVector.size(); i++) { // Calculate and save result values
			result = ReadedPagesCalculator(dataVector[i]);
			resultsVector.push_back(result);
		}

		resultOutPut(resultsVector);
		
	} else {
		perror("ERROR: Incorrect arguments input");
	}
}