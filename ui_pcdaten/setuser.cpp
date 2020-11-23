#include "setuser.h"
#include "ui_setuser.h"

setUser::setUser(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::setUser)
{
    ui->setupUi(this);
}

setUser::~setUser()
{
    delete ui;
}
