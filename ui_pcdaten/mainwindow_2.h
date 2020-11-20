#ifndef MAINWINDOW_2_H
#define MAINWINDOW_2_H

#include <QDialog>

namespace Ui {
class mainwindow_2;
}

class mainwindow_2 : public QDialog
{
    Q_OBJECT

public:
    explicit mainwindow_2(QWidget *parent = nullptr);
    ~mainwindow_2();

private:
    Ui::mainwindow_2 *ui;
};

#endif // MAINWINDOW_2_H
