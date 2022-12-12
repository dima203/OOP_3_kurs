#include <list>
#include <iostream>
#include <iterator>


template<class T>
void ShowList(std::list<T> list)
{
    for (T i: list) {
        std::cout << i << '\t';
    }
    std::cout << std::endl;
}


int main()
{
    std::list<int> list {1, 6, 2, 8, 2, 0};
    ShowList(list);
    list.remove(6);
    auto pos = list.begin();
    pos++;
    list.insert(pos, 7);
    for (auto i = list.begin(); i != list.end(); i++) {
        std::cout << *i << '\t';
    }
    std::cout << std::endl;
    std::list<int> list2 {15, 42, 64};
    pos = list.begin();
    std::advance(pos, 3);
    list.erase(pos, list.end());
    list.insert(list.end(), list2.begin(), list2.end());
    ShowList(list);
    ShowList(list2);
    return 0;
}
