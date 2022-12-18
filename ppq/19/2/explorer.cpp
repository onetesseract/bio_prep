#include <iostream>
#include <stdlib.h>
#include <unordered_map>

#define debug(...) /*printf(__VA_ARGS__)*/

struct Coord {
  int x;
  int y;

  Coord(int _x, int _y) : x{_x}, y{_y} {}
  Coord() : x{0}, y{0} {}
};

Coord get_square(Coord _origin, int rotation) {
  Coord origin = _origin;
  switch (rotation) {
  case 0:
    origin.y++;
    break;
  case 1:
    origin.x++;
    break;
  case 2:
    origin.y--;
    break;
  case 3:
    origin.x--;
    break;
  }
  return origin;
}

class coord_array {
  std::unordered_map<int, std::unordered_map<int, int>> content;

public:
  bool contains(Coord pos) {
    if (content.count(pos.x) != 0) {
      if (content[pos.x].count(pos.y) != 0) {
        return true;
      }
    }
    return false;
  }
  int get(Coord pos) { return content[pos.x][pos.y]; }

  void set(Coord pos, int val) {
    if (content.count(pos.x) == 0) {
      content[pos.x] = std::unordered_map<int, int>();
    }
    content[pos.x][pos.y] = val;
  }
};

int main() {
  std::string instructions;
  int trail_decay_length;
  int moves;
  std::cin >> trail_decay_length >> instructions >> moves;

  // debug("Trail: %i, instructions: %s, moves: %i\n", trail_decay_length,
  //       instructions.c_str(), moves);

  coord_array grid;
  Coord explorer_pos = {0, 0};
  int explorer_rot = 0; // 0 = up, 1 = right, 2 = down, 3 = left

  for (int i = 0; i < moves; i++) {
    char instruction = instructions[i % instructions.size()];
    debug("Performing instruction %c at position %i:%i with rotation %i\n",
          instruction, explorer_pos.x, explorer_pos.y, explorer_rot);
    switch (instruction) {
    case 'F': {
      break;
    }
    case 'R':
      explorer_rot = (explorer_rot + 1) % 4;
      break;
    case 'L':
      explorer_rot = (explorer_rot + 3) % 4;
      break;
    default:
      printf("Invalid instruction %c", instruction);
      exit(1);
      break;
    }
    bool valid = false;
    for (int j = 0; j < 4; j++) {
      Coord target = get_square(explorer_pos, explorer_rot);
      if (grid.contains(target)) {
        if (grid.get(target) > (i - trail_decay_length)) {
          explorer_rot = (explorer_rot + 1) % 4;
          continue;
        }
      }
      grid.set(explorer_pos, i);
      explorer_pos = target;
      valid = true;
      break;
    }
    if (!valid) {
      break;
    }
  }

  printf("(%i,%i)\n", explorer_pos.x, explorer_pos.y);
  return 0;
}
