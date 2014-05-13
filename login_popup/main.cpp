#include "loginbanner.hpp"
#include <QApplication>
#include <iostream>

int main(int argc, char *argv[])
{
    int ret;
    QApplication a(argc, argv);
    LoginBanner w;
    w.show();
    a.exec();
    ret = w.result();
    if (ret == 1 ) {
        std::cout << "accepted.." << std::endl;
        return 0;
    } else {
        std::cout << "rejected.." << std::endl;
        return -1;
     }
}
