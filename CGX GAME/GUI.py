import sys
import os
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTreeView,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtCore import QDir, Qt, QFileSystemModel  # Corrected import
#from PySide6.QtGui import QFileSystemModel #removed
class FolderGUI(QMainWindow):
    def __init__(self, folder_path):
        super().__init__()

        self.setWindowTitle("Folder Explorer")

        # Create a file system model
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())

        # Create a tree view
        self.tree_view = QTreeView()
        self.tree_view.setModel(self.model)
        self.tree_view.setRootIndex(self.model.index(folder_path))

        # Hide columns we don't need (e.g., size, type)
        self.tree_view.hideColumn(1)
        self.tree_view.hideColumn(2)
        self.tree_view.hideColumn(3)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.tree_view)

        # Central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Connect double-click to open files/folders
        self.tree_view.doubleClicked.connect(self.open_item)

    def open_item(self, index):
        file_path = self.model.filePath(index)
        if os.path.isdir(file_path):
            # If it's a directory, expand it in the tree view
            self.tree_view.setRootIndex(index)
        else:
            # If it's a file, open it with the default application
            os.startfile(file_path)  # Windows
            # os.system(f'open "{file_path}"') # macOS
            # os.system(f'xdg-open "{file_path}"') # Linux


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Replace with the folder you want to display
    target_folder = r"C:\Users\there\CGX\EonHub\CGX GAME"  # Raw string (fixed)
    if not os.path.exists(target_folder):
        print(f"Error: Folder '{target_folder}' does not exist.")
        sys.exit(1)

    window = FolderGUI(target_folder)
    window.show()

    sys.exit(app.exec())
