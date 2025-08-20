#include <fstream>
#include <iostream>
#include <sstream>

bool check_for_string(std::stringstream& stream, std::string s) {
    char c;
    int counter = 0;
    bool flag = true;
    for (size_t i = 0; i < s.size(); i++) {
        c = stream.peek();
        if (!(c == s.at(i))) {
            flag = false;
            break;
        }
        counter++;
        stream.get(c);
    }
    for (int i = 0; i < counter; i++) {
        stream.unget();
    }

    return flag;
}


int main() {
    //std::ifstream data{ "test.txt" };
    //std::ifstream data{ "test2.txt" };
    std::ifstream data{ "input.txt" };

    long total = 0;
    std::string enabled = "o()";
    std::string disabled = "on't()";
    std::string mul = "ul(";
    bool enabled_flag = true;

    if (!data) {
        std::cerr << "Problem opening input file" << std::endl;
    } else {
        std::string line;
        while (getline(data, line)) {
            std::stringstream inbuf(line);
            
            char c;

            while (!inbuf.eof()) {
                inbuf.get(c);

                if (c == 'm' && enabled_flag) {
                    if (check_for_string(inbuf, mul)) {
                        char temp[4];
                        inbuf.get(temp, 4);
                        int n1 = 0;
                        inbuf >> n1;
                        inbuf.get(c);
                        if (c == ',') {
                            int n2 = 0;
                            inbuf >> n2;
                            inbuf.get(c);
                            if (c == ')') {
                                long mul = n1 * n2;
                                total += mul;
                            }
                        }
                    }
                } else if (c == 'd') {
                    if (check_for_string(inbuf, disabled)) {
                        enabled_flag = false;
                    } else if (check_for_string(inbuf, enabled)) {
                        enabled_flag = true;
                    }
                }
            }
        }
    }

    std::cout << "Sum of all of the results of the multiplications is " << total << std::endl;

    return 0;
}
