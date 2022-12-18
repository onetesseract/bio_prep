#include <cstdint>
#include <iostream>
#include <stdint.h>
#include <string>
#include <vector>

#define debug(...) /*printf(__VA_ARGS__)*/

std::vector<int> str_contains_less_than(std::string str, uint16_t cutoff,
                                        char c) {
  std::vector<int> indexes;
  for (int i = cutoff - 1; i != -1; i--) {
    if (str[i] < c)
      indexes.push_back(i);
  }
  return indexes;
}

int str_contains(std::string str, char c) {
  for (int i = 0; i < str.length(); i++) {
    if (str[i] == c)
      return i;
  }
  return -1;
}

int blockchain_variants(std::string start, uint16_t alphabet_length) {
  // for it to be valid, it must not pick a letter such that the letter picked
  // is alphabetically after a letter alphabetically after another one previous.
  // save my soul from the O(n^2)
  std::vector<char> valid_opts;
  int total = 0;
  for (char c = 'a'; c != ('a' + alphabet_length); c++) {
    if (str_contains(start, c) != -1) {
      debug("Disregarding %c as %s contains it\n", c, start.c_str());
      continue;
    }
    int valid = true;
    std::vector<int> str_less_indexes =
        str_contains_less_than(start, start.length(), c);
    for (int index : str_less_indexes) {
      if (str_contains_less_than(start, index, start[index]).size() !=
          0) { // bad bad
        debug("Adding %c to %s isnt valid\n", c, start.c_str());
        valid = false;
        break;
      }
    }
    if (valid) {
      debug("%c is a valid option for %s\n", c, start.c_str());
      valid_opts.push_back(c);
    }
  }

  /*
  for (int i = start.length() - 1; i != -1; i -= 1) {
    printf("looping %c\n", start[i]);
    if (start[i] == 'a')
      continue;
    int index = str_contains(start, )
  }*/

  if (valid_opts.size() < 2 && (start.length() + 1) == alphabet_length) {
    return valid_opts.size();
  }

  start.push_back('a');

  for (char c : valid_opts) {
    start[start.size() - 1] = c;
    total += blockchain_variants(start, alphabet_length);
  }

  return total;
}

int main() {
  uint16_t alphabet_length;
  std::string start_str;
  std::cin >> alphabet_length >> start_str;

  int count = blockchain_variants(start_str, alphabet_length);

  std::cout << count << std::endl;

  return 0;
}
