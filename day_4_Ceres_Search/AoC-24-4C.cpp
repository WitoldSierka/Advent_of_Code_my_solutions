#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

int find_horizontal(const std::string& s) {
    int result = 0;

    for (size_t i = 0; i < s.size() -3; i++) {
        if (s.at(i) == 'X') {
            if (s.at(i + 1) == 'M' && s.at(i + 2) == 'A' && s.at(i + 3) == 'S') {
                result++;
            }
        }
        if (s.at(i) == 'S') {
            if (s.at(i + 1) == 'A' && s.at(i + 2) == 'M' && s.at(i + 3) == 'X') {
                result++;
            }
        }
    }

    return result;
}

int find_vertical(const std::vector<std::string>& vec) {
    int result = 0;
    
    for (size_t i = 0; i < vec.at(0).size(); i++) {// inputs are always rectangular
        for (size_t j = 0; j < vec.size() - 3; j++) {
            if (vec.at(j).at(i) == 'X') {
                if (vec.at(j + 1).at(i) == 'M' && vec.at(j + 2).at(i) == 'A' && vec.at(j + 3).at(i) == 'S') {
                    result++;
                }
            }
            if (vec.at(j).at(i) == 'S') {
                if (vec.at(j + 1).at(i) == 'A' && vec.at(j + 2).at(i) == 'M' && vec.at(j + 3).at(i) == 'X') {
                    result++;
                }
            }
        }
    }

    return result;
}

int find_diagonal(const std::vector<std::string>& vec) {
    int result = 0;

    for (size_t i = 0; i < vec.at(0).size() - 3; i++) {
        for (size_t j = 0; j < vec.size(); j++) {
            if (j < vec.size() - 3) {//check down-right
                if (vec.at(j).at(i) == 'X') {
                    if (vec.at(j + 1).at(i + 1) == 'M' && vec.at(j + 2).at(i + 2) == 'A' && vec.at(j + 3).at(i + 3) == 'S') {
                        result++;
                    }
                }
                if (vec.at(j).at(i) == 'S') {
                    if (vec.at(j + 1).at(i + 1) == 'A' && vec.at(j + 2).at(i + 2) == 'M' && vec.at(j + 3).at(i + 3) == 'X') {
                        result++;
                    }
                }
            }
            if (j >= 3) {//check up-right
                if (vec.at(j).at(i) == 'X') {
                    if (vec.at(j - 1).at(i + 1) == 'M' && vec.at(j - 2).at(i + 2) == 'A' && vec.at(j - 3).at(i + 3) == 'S') {
                        result++;
                    }
                }
                if (vec.at(j).at(i) == 'S') {
                    if (vec.at(j - 1).at(i + 1) == 'A' && vec.at(j - 2).at(i + 2) == 'M' && vec.at(j - 3).at(i + 3) == 'X') {
                        result++;
                    }
                }
            }
        }
    }

    return result;
}

int find_XMAS(const std::vector<std::string>& vec) {
    int result = 0;

    for (size_t i = 1; i < vec.at(0).size() - 1; i++) {
        for (size_t j = 1; j < vec.size() - 1; j++) {
            if (!(vec.at(j).at(i) == 'A')) { continue; }
            if (vec.at(j - 1).at(i - 1) == 'M' && vec.at(j + 1).at(i + 1) == 'S') {
                if (vec.at(j + 1).at(i - 1) == 'M' && vec.at(j - 1).at(i + 1) == 'S') {
                    result++;
                } else if (vec.at(j + 1).at(i - 1) == 'S' && vec.at(j - 1).at(i + 1) == 'M') {
                    result++;
                }
            } else if (vec.at(j - 1).at(i - 1) == 'S' && vec.at(j + 1).at(i + 1) == 'M') {
                if (vec.at(j + 1).at(i - 1) == 'M' && vec.at(j - 1).at(i + 1) == 'S') {
                    result++;
                } else if (vec.at(j + 1).at(i - 1) == 'S' && vec.at(j - 1).at(i + 1) == 'M') {
                    result++;
                }
            }
        }
    }

    return result;
}

int main(){
    //std::ifstream data{ "test.txt" };
    std::ifstream data{ "input.txt" };
    std::vector<std::string> puzzle;

    if (!data) {
        std::cerr << "Problem opening input file" << std::endl;
    } else {
        std::string line;
        while(getline(data, line)) {
            puzzle.push_back(line);
        }
    }
    int total = 0;
    for (const auto& row : puzzle) {
        total += find_horizontal(row);
    }
    total += find_vertical(puzzle);
    total += find_diagonal(puzzle);

    int total2 = find_XMAS(puzzle);

    std::cout << "XMAS appears exactly " << total << " times.\n";
    std::cout << "An X-MAS appears exactly " << total2 << " times." << std::endl;

    return 0;
}
