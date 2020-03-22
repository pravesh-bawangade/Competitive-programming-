#include <iostream>
#include <vector>
using namespace std;
int main() {
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
	// we use 'cas' because 'case' is a keyword
	int N, K, L;

	// allocate more than necessary
	// note that phrases[i] is a vector of strings.
	vector < string > phrase[55];

	//array of forgotten words
	string forgotten[109];

	cin >> N >> K;
	for (int i = 0; i < N; i++) {
	    cin >> forgotten[i];
	}

	for (int i = 0; i < K; i++) {
	    cin >> L;
	    for (int j = 0; j < L; j++) {
	        string S;
	        cin >> S;
	        phrase[i].push_back(S);
	    }
	}

	for (int i = 0; i < N; i++){
	    string answer = "NO";

	    //traverse over all phrases
	    for(int j = 0; j < K; j++){

	        //traverse over phrase[j]
	        for(int k = 0; k < phrase[j].size(); k++){
	            if(phrase[j][k] == forgotten[i])
	                answer = "YES";
	        }
	    }

	    cout << answer << (i==N-1 ? "\n" : " ");
	}
    }
}