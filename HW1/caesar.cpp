#include <iostream>
#include <string>

using namespace std;

int main()
{
	string cipher;
	int length;
	char c;

	cout << "Enter the ciphertext: ";
	cin >> cipher;
	length = cipher.length();

	for(int k=1; k<26; k++)
	{
		string * plain  = NULL;
		plain  = new string;
		*plain = cipher;

		for(int i=0; i<length; i++)
		{
			c = cipher[i];
			if(c - k < 65)
			{
				c = 26 + c - k;
			}
			else
			{
				c = c - k;
			}
			(*plain)[i] = c;
		}
		cout << *plain << '\t' << "Shift: " << k << endl;
		delete plain;
	}

	cin.get();
	cin.ignore();
	return 0;
}