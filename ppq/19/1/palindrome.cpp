#include <cstdint>
#include <iostream>
#include <stdlib.h>

#define debug(...) printf(__VA_ARGS__)

int main() {
  std::string source;
  std::cin >> source;

  if (source.length() % 2 == 0) {
    // length is even, its nice
    std::string _first_half = source.substr(0, source.length() / 2);
    int fhalf = atoi(_first_half.c_str());

    // make it palindrome
    std::string second_half =
        std::string(_first_half.rbegin(), _first_half.rend());

    std::string all_together = _first_half + second_half;
    if (atoi(all_together.c_str()) > atoi(source.c_str())) {
      // yay it work
      std::cout << all_together;
      return 0;
    }
    // it not work
    fhalf++;
    std::string first_half = std::to_string(fhalf);
    int offset = 0;
    if (first_half.length() != _first_half.length()) {
      offset = 1;
    }
    second_half = std::string(first_half.rbegin() + offset, first_half.rend());

    all_together = first_half + second_half;
    std::cout << all_together;

    return 0;
  } else {
    std::string _first_half = source.substr(0, (source.length() + 1) / 2);
    int fhalf = atoi(_first_half.c_str());

    // make it palindrome
    std::string second_half =
        std::string(_first_half.rbegin() + 1, _first_half.rend());

    std::string all_together = _first_half + second_half;
    if (atoi(all_together.c_str()) > atoi(source.c_str())) {
      // yay it work
      std::cout << all_together;
      return 0;
    }
    // it not work
    fhalf++;
    std::string first_half = std::to_string(fhalf);
    int offset = 0;
    if (first_half.length() != _first_half.length()) {
      offset = 1;
    }
    second_half =
        std::string(first_half.rbegin() + 1 + offset, first_half.rend());

    all_together = first_half + second_half;
    std::cout << all_together;

    return 0;
  }
}
