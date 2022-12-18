#include <algorithm>
#include <iostream>
#include <math.h>
#include <vector>

std::vector<long int> largest_factor(long int val) {
  std::vector<long int> result = {};
  for (int i = val - 1; i > 0; i--) {
    float quot = float(val) / float(i);
    if (std::floor(quot) == quot) {
      std::cout << quot << " is a factor of " << val << '\n';
      result.push_back(quot);
    }
  }
  std::reverse(result.begin(), result.end());
  return result;
}

int count_factors(int number) {
  int total = 0;
  int lim = number;
  for (int i = lim; i > 0; i--) {
    float quot = lim / float(i);
    if (floor(quot) == quot) {
      total++;
    }
  }

  return total;
}

int main() {
  long long int num = 600851475143;
  for (long long int i = num; i > 0; i--) {
    float quot = num / float(i);
    std::cout << "trying " << i << '\n';
    if (floor(quot) == quot) {
      std::cout << i << " is a factor of " << num << '\n';
      if (count_factors(i) == 2) {
        std::cout << i << std::endl;
        return 0;
      }
    }
  }

  return 0;
  std::vector<long int> factors = largest_factor(num);
  long int last;
  while (factors.size() > 0) {
    last = factors[factors.size() - 1];
    factors.pop_back();
    std::vector<long int> result = largest_factor(last);
    if (result.size() == 0)
      break;
    factors.insert(factors.begin(), result.begin(), result.end());
    std::cout << "Tried " << last << ", " << factors.size() << " left. \n";
  }

  std::cout << last << std::endl;
}
