#include <string>
#include <sstream>
#include <iostream>
#include <list>
#include <set>
#include <algorithm>


class Point
{
    template<int x_min, int x_max, int y_min, int y_max>
    friend bool IsPointInRange(Point);
private:
    double _x, _y;
public:
    Point(double x, double y)
    {
        _x = x;
        _y = y;
    }

    std::string ToString() const
    {
        std::stringstream ss;
        ss << "Point(" << _x << ", " << _y << ")";
        return ss.str();
    }

    bool operator==(const Point other) const
    {
        return (_x == other._x && _y == other._y);
    }

    bool operator>(const Point other) const
    {
        return (_x * _x + _y * _y > other._x * other._x + other._y * other._y);
    }

    bool operator<(const Point other) const
    {
        return (_x * _x + _y * _y < other._x * other._x + other._y * other._y);
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


template<class T>
void ShowSet(std::set<T> set)
{
    for (T i: set) {
        std::cout << i.ToString() << '\t';
    }
    std::cout << std::endl;
}


template<int x_min, int x_max, int y_min, int y_max>
bool IsPointInRange(Point point)
{
    return (point._x >= x_min && point._x <= x_max && point._y >= y_min && point._y <= y_max);
}


int main()
{
    std::list<Point> list {Point(1, 3), Point(2, 4), Point(1, 1), Point(7, 4), Point(4, 9)};
    list.sort();
    list.reverse();
    ShowList(list);

    auto element = std::find_if(list.begin(), list.end(), IsPointInRange<2, 5, 3, 10>);
    std::cout << element->ToString() << std::endl;

    std::set<Point> set;
    for (auto it = std::find_if(list.begin(), list.end(), IsPointInRange<2, 5, 3, 10>);
     it != list.end();
     it = std::find_if(++it, list.end(), IsPointInRange<2, 5, 3, 10>)) {
        set.insert(*it);
    }
    ShowSet(set);

    list.sort();
    ShowList(list);
    ShowSet(set);

    std::list<Point> new_list;
    new_list.insert(new_list.end(), list.begin(), list.end());
    new_list.insert(new_list.end(), set.begin(), set.end());
    ShowList(new_list);

    int count = 0;
    for (auto it = std::find_if(new_list.begin(), new_list.end(), IsPointInRange<2, 5, 3, 10>);
     it != new_list.end();
     it = std::find_if(++it, new_list.end(), IsPointInRange<2, 5, 3, 10>)) {
        count++;
    }
    std::cout << count << std::endl;

    std::cout << (std::find_if(new_list.begin(), new_list.end(), IsPointInRange<3, 8, 1, 5>) != new_list.end()) << std::endl;
    return 0;
}
