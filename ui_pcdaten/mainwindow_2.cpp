#include "mainwindow_2.h"
#include "ui_mainwindow_2.h"

mainwindow_2::mainwindow_2(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::mainwindow_2)
{
    ui->setupUi(this);
}

mainwindow_2::~mainwindow_2()
{
    delete ui;
}
