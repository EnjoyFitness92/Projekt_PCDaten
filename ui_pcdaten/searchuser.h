#ifndef SEARCHUSER_H
#define SEARCHUSER_H

#include <QWidget>

namespace Ui {
class searchUser;
}

class searchUser : public QWidget
{
    Q_OBJECT

public:
    explicit searchUser(QWidget *parent = nullptr);
    ~searchUser();

private:
    Ui::searchUser *ui;
};

#endif // SEARCHUSER_H
