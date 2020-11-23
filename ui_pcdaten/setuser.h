#ifndef SETUSER_H
#define SETUSER_H

#include <QWidget>

namespace Ui {
class setUser;
}

class setUser : public QWidget
{
    Q_OBJECT

public:
    explicit setUser(QWidget *parent = nullptr);
    ~setUser();

private:
    Ui::setUser *ui;
};

#endif // SETUSER_H
