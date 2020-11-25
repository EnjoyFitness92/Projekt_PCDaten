#ifndef SEARCHDEVICE_H
#define SEARCHDEVICE_H

#include <QWidget>

namespace Ui {
class searchDevice;
}

class searchDevice : public QWidget
{
    Q_OBJECT

public:
    explicit searchDevice(QWidget *parent = nullptr);
    ~searchDevice();

private:
    Ui::searchDevice *ui;
};

#endif // SEARCHDEVICE_H
