#include <iostream>
#include <string>

using namespace std;

int main()
{
    int foo [26] = { };
	string cipher;
	char maxCharacter;
	int max = 0;

	cout << "Enter ciphertext: " << endl;
	getline(cin, cipher);

    for (unsigned int i = 0; i < cipher.size(); i++)
    {
        char c = cipher[i];
		int x = c - 'A';
		foo[x]++;

		if(foo[x] > max)
		{
			max = foo[x];
			maxCharacter = x + 'A';
		}
    }

	for (unsigned int j=0; j<cipher.size(); j++)
	{
		if(cipher[j] == maxCharacter)
		{
			cipher[j] = 'O';
		}
	}
	
	cout << cipher << endl;
	
    return 0;
}
