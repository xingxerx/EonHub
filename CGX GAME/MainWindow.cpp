// ... (other includes)

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
    , ai(KYRNIA)
{
    ui->setupUi(this);
    // ... (other setup)
    connect(ui->createUniverseButton, &QPushButton::clicked, this, &MainWindow::on_createUniverseButton_clicked); // Connect the button
}

// ... (other methods)

void MainWindow::on_createUniverseButton_clicked() {
    ai.createUniverse("New-Universe-GUI");
    ui->aiResponseTextEdit->append("Universe New-Universe-GUI created.");
}
