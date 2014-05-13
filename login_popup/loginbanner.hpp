#ifndef LOGINBANNER_HPP
#define LOGINBANNER_HPP

#include <QDialog>

namespace Ui {
class LoginBanner;
}

class LoginBanner : public QDialog
{
    Q_OBJECT

public:
    explicit LoginBanner(QWidget *parent = 0);
    ~LoginBanner();

private:
    Ui::LoginBanner *ui;
};

#endif // LOGINBANNER_HPP
