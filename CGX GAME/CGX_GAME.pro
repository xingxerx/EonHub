QT += core widgets

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = CGX_GAME
TEMPLATE = app

SOURCES += main.cpp \
    MainWindow.cpp \
    CGXAI.cpp \
    EoniaAI.cpp \
    NaturalDialog.cpp

HEADERS += MainWindow.h \
    CGXAI.h \
    EoniaAI.h \
    NaturalDialog.h

FORMS += MainWindow.ui
