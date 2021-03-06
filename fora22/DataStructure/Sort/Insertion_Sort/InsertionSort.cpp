#include <iostream>
#include <random>
#include <vector>

using namespace std;

vector<int> getRandomArray(const int randomNumberCount)
{
	int temp, x, y;
	random_device rd;
	mt19937 gen(rd());

	uniform_int_distribution<int> dis(0, randomNumberCount - 1);

	vector<int> randomArray(randomNumberCount);

	for (int i = 0; i < randomNumberCount; i++)
	{
		randomArray[i] = i + 1;
	}

	for (int i = 0; i < randomNumberCount; i++)
	{
		x = dis(gen);
		y = dis(gen);
		if (x != y)
		{
			temp = randomArray[x];
			randomArray[x] = randomArray[y];
			randomArray[y] = temp;
		}
	}

	return randomArray;
}

int main(void) 
{
	const int randNumberLength = 100;
	vector<int> randArray = getRandomArray(randNumberLength);

	int temp;
	for (int i = 1; i < randArray.size(); i++)
	{
		for (int j = i; j > 0; j--)
		{
			if (randArray[j] < randArray[j - 1])
			{
				temp = randArray[j];
				randArray[j] = randArray[j - 1];
				randArray[j - 1] = temp;
			}
			else
			{
				break;
			}
		}
	}
    
	for (int i = 0; i < randArray.size(); i++)	{
		cout << randArray[i] << " ";
	}

	return 0;
}