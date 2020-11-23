#include "setdevice.h"
#include "ui_setdevice.h"

setDevice::setDevice(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::setDevice)
{
    ui->setupUi(this);
}

setDevice::~setDevice()
{
    delete ui;
}
