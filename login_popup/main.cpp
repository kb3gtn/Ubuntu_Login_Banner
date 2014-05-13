#include "loginbanner.hpp"
#include <QApplication>
#include <QDesktopWidget>
#include <iostream>

int main(int argc, char *argv[])
{
    int ret;
    QApplication a(argc, argv);
    LoginBanner w;
    w.adjustSize();
    w.move( QApplication::desktop()->screen()->rect().center() - w.rect().center() );
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
