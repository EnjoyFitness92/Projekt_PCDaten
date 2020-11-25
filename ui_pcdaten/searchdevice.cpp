#include "searchdevice.h"
#include "ui_searchdevice.h"

searchDevice::searchDevice(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::searchDevice)
{
    ui->setupUi(this);
}

searchDevice::~searchDevice()
{
    delete ui;
}
