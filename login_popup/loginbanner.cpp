#include "loginbanner.hpp"
#include "ui_loginbanner.h"

LoginBanner::LoginBanner(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::LoginBanner)
{
    ui->setupUi(this);
}

LoginBanner::~LoginBanner()
{
    delete ui;
}
