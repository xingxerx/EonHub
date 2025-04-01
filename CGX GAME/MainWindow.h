// ... (other includes)

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

    void KYRNIA_ResponseReceived(const std::string& response);

private slots:
    void on_sendButton_clicked();
    void on_quitButton_clicked();
    void on_createUniverseButton_clicked(); // New slot

private:
    Ui::MainWindow *ui;
    CGXAI KYRNIA;
    EoniaAI ai;
};
