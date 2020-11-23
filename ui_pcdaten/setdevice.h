#ifndef SETDEVICE_H
#define SETDEVICE_H

#include <QWidget>

namespace Ui {
class setDevice;
}

class setDevice : public QWidget
{
    Q_OBJECT

public:
    explicit setDevice(QWidget *parent = nullptr);
    ~setDevice();

private:
    Ui::setDevice *ui;
};

#endif // SETDEVICE_H
