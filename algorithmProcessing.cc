// NOT IMPLEMENTATED

#include <iostream>
#include <vector>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>


using namespace std;




struct Data {
	int tests;
	int N;
	int M;
	int Q;
	vector<int> mVector;
	vector<int> qVector;
};

Data test1;
vector<int> paginasLeidas;

int calcularPaginasLeidas() {
	int pagina = 0;
	bool paginaArrancada = false;
	int paginasLeidas = 0;
	vector<int> resultsVector;
	for (int j = 0; j < test1.Q +1; j++) {
		for (int i = 0; i == test1.N; i++) {
			pagina = test1.qVector[j] * i;
			if (pagina > test1.N) break;
			for (int j = 0; j < test1.M; j++) {
				if (pagina == test1.mVector[j]) {
					paginaArrancada = true;
				}
			}
			if (paginaArrancada == false) {
				paginasLeidas++;
			}
			else {
				paginaArrancada = false;
			}
		}
		resultsVector.push_back(paginasLeidas);
		paginasLeidas = 0;
	}
	return paginasLeidas;
}

int main(int argc, char const* argv[]) {
	bool inputExit = false;
	string s;
	vector<string> stringVector;
	while (inputExit == false) {
		getline(cin, s);
		stringVector.push_back(s);
		if (s.size() == 0) {
			inputExit = true;
		}
		s.clear();
	}

	test1.tests = 1;
	test1.N = 11;
	test1.M = 1;
	test1.Q = 2;
	test1.mVector = { 8 };
	test1.qVector = { 2,3 };


	paginasLeidas[0] = calcularPaginasLeidas();
}
