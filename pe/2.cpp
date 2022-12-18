#include <iostream>

int main() {
  long int a = 1;
  long int b = 1;
  long int last = 0;
  long int val = 0;
  long long int total = 0;

  while (true) {
    val = a + b;
    if (val > 4000000) {
      break;
    }
    if ((val % 2) == 0) {
      total += val;
      std::cout << total << " " << val << '\n';
    }
    if (last) {
      a = val;
    } else {
      b = val;
    }
    last = !last;
  }

  std::cout << total << std::endl;
}
