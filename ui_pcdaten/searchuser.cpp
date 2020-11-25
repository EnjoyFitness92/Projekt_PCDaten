#include "searchuser.h"
#include "ui_searchuser.h"

searchUser::searchUser(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::searchUser)
{
    ui->setupUi(this);
}

searchUser::~searchUser()
{
    delete ui;
}
