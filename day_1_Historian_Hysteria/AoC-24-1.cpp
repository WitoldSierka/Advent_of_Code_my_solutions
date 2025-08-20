#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

int main() {
    //read input
    std::ifstream ids{"input.txt"};
    //std::ifstream ids{ "test.txt" };
    std::vector<int> left_list;
    std::vector<int> right_list;
    int total = 0;

    if (!ids) {
        std::cerr << "Problem opening input file" << std::endl;
    } else {
        std::string line;

        while(getline(ids, line)) {
            std::istringstream inbuf(line);
            int left_id = 0;
            int right_id = 0;
            inbuf >> left_id >> right_id;
            left_list.push_back(left_id);
            right_list.push_back(right_id);
        }
    }

    std::sort(left_list.begin(), left_list.end());
    std::sort(right_list.begin(), right_list.end());
    int temp = 0;
    //std::vector<int>::size_type;
    for (size_t i = 0; i < left_list.size(); i++) {
        temp = left_list.at(i) - right_list.at(i);
        if (temp < 0) { temp = -temp; }
        total += temp;
    }
    std::cout << "Total distance between lists is: " << total << std::endl;

    int similarity_score = 0;
    for (const auto& left_id : left_list) {
        int count = 0;
        for (const auto& right_id : right_list) {
            if (left_id == right_id) {
                count++;
            }
        }
        similarity_score += left_id * count;
    }

    std::cout << "Total similarity score is: " << similarity_score << std::endl;

    return 0;
}