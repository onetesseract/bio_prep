#include <iostream>

char max_alpha_char(std::string &string, int start, int end) {
  char max = 0;
  for (int i = start; i < end; i++) {
    if (string[i] > max)
      max = string[i];
  }
  return max;
}

char min_alpha_char(std::string &string, int start, int end) {
  char min = 127;
  for (int i = start; i < end; i++) {
    if (string[i] < min)
      min = string[i];
  }
  return min;
}

bool is_pat(std::string &pat, int start, int end, bool reverse) {
  if (end - start == 1)
    return true;
  for (int i = start + 1; i < end - 1; i++) {
    if (!reverse) {
      if (min_alpha_char(pat, start, i) > max_alpha_char(pat, i, end)) {
        if (is_pat(pat, start, i, !reverse) && is_pat(pat, i, end, !reverse))
          return true;
      }
    } else {
      if (max_alpha_char(pat, start, i) < min_alpha_char(pat, i, end)) {
        if (is_pat(pat, start, i, !reverse) && is_pat(pat, i, end, !reverse))
          return true;
      }
    }
  }
  return false;
}

int main() {
  std::string pat;
  std::cin >> pat;
  std::cout << (is_pat(pat, 0, pat.length() - 1, false) ? "YES" : "NO")
            << std::endl;
}
