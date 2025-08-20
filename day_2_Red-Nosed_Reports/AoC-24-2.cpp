#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

bool is_increasing_or_decreasing(const std::vector<int> &vec) {
    bool dec_flag = false;
    bool inc_flag = false;
    for (size_t i = 1; i < vec.size(); i++) {
        if (vec.at(i - 1) == vec.at(i)) { return false; }
        if (vec.at(i - 1) < vec.at(i)) { 
            if (dec_flag) { return false; }
            inc_flag = true;
            continue;
        }
        if (vec.at(i - 1) > vec.at(i)) { 
            if (inc_flag) { return false; }
            dec_flag = true; 
        }
    }
    return (dec_flag || inc_flag);
}

bool difference_check(const std::vector<int>& vec) {
    bool is_safe = false;
    for (size_t i = 1; i < vec.size(); i++) {
            int diff = vec.at(i - 1) - vec.at(i);
            if (diff < 0) { diff = -diff; }
            if (1 <= diff && diff <= 3) { 
                is_safe = true;
            } else {
                is_safe = false;
                break;
            }
        }
    return is_safe;
}

bool problem_dampener(const std::vector<int>& vec) {
    bool is_safe = false;
    std::vector<int> temp;

    for (size_t i = 0; i < vec.size(); i++) {
        temp = vec;
        temp.erase(temp.begin() + i);
        is_safe = is_increasing_or_decreasing(temp);
        if (!is_safe) { continue; }
        is_safe = difference_check(temp);
        if (is_safe) { return true; }
    }

    return false;
}

int main(){
    //std::ifstream data{"test.txt"};
    std::ifstream data{"input.txt"};
    int total = 0;
    //int dampened_total = 0;
    std::vector<std::vector<int>> reports;
    
    if (!data) {
        std::cerr << "Problem opening input file" << std::endl;
    } else {
        std::string line;
        while (getline(data, line)) {
            std::istringstream inbuf(line);
            int temp = 0;
            reports.push_back({});
            while (!inbuf.eof()) {
                inbuf >> temp;
                reports.at(reports.size()-1).push_back(temp);
            }
        }
    }
    
    bool is_safe = false;
    bool dampened = false;
    for (const auto& report : reports) {
        dampened = false;
        is_safe = false;
        is_safe = is_increasing_or_decreasing(report);
        if (!is_safe) {
            dampened = true;
            is_safe = problem_dampener(report);
            if (!is_safe) { continue; }
            total++;
            continue;
        }
        is_safe = difference_check(report);
        if (!is_safe) {
            if (dampened) {
                continue;
            }
            dampened = true;
            is_safe = problem_dampener(report);
        }
        if (is_safe) { total++; }
    }
    
    std::cout << "With Problem Dampener in use, there are exactly " << total << " safe reports." << std::endl;
    //std::cout << "With Problem Dampener in use, there are exactly " << dampened_total << " safe reports." << std::endl;
    return 0;
}