#include <list>
#include <iostream>
#include <iterator>
#include <string>
#include <sstream>


class Point
{
private:
    double _x, _y;
public:
    Point(double x, double y)
    {
        _x = x;
        _y = y;
    }

    std::string ToString()
    {
        std::stringstream ss;
        ss << "Point(" << _x << ", " << _y << ")";
        return ss.str();
    }

    bool operator==(Point other)
    {
        return (_x == other._x && _y == other._y);
    }

    bool operator>(Point other)
    {
        return (_x * _x + _y * _y > other._x * other._x + other._y * other._y);
    }
};


template<class T>
void ShowList(std::list<T> list)
{
    for (T i: list) {
        std::cout << i.ToString() << '\t';
    }
    std::cout << std::endl;
}


int main()
{
    std::list<Point> list {Point(1, 2), Point(5, 3), Point(1, 0), Point(6, 9), Point(7, 2), Point(0, -5)};
    ShowList(list);
    list.erase(++list.begin());
    auto pos = list.begin();
    pos++;
    list.insert(pos, Point(8, 4));
    for (auto i = list.begin(); i != list.end(); i++) {
        std::cout << i->ToString() << '\t';
    }
    std::cout << std::endl;
    std::list<Point> list2 {Point(15, 76), Point(54, 90), Point(43, 85)};
    pos = list.begin();
    std::advance(pos, 3);
    list.erase(pos, list.end());
    list.insert(list.end(), list2.begin(), list2.end());
    ShowList(list);
    ShowList(list2);
    return 0;
}
