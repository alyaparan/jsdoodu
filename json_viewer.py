import sys
import os
import json
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMenu, QAction, QFileDialog, 
    QVBoxLayout, QWidget, QTextEdit, QListWidget, 
    QHBoxLayout, QPushButton, QLineEdit, QLabel, QComboBox, QMessageBox, QInputDialog
)
from PyQt5.QtCore import Qt, QTimer

class JsonViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('JSON File Viewer')
        self.setGeometry(100, 100, 1200, 800)
        self.current_dir = os.getcwd()
        
        self.initUI()
        self.load_files()

        # Real-time monitoring
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.load_files)
        self.timer.start(5000)  # check for new files every 5 seconds

    def initUI(self):
        # Create menu bar
        menu_bar = self.menuBar()

        # Create file menu
        file_menu = menu_bar.addMenu('File')
        analyze_menu = menu_bar.addMenu('Analyze')
        filter_menu = menu_bar.addMenu('Filter')
        monitor_menu = menu_bar.addMenu('Monitor')
        export_menu = menu_bar.addMenu('Export')
        help_menu = menu_bar.addMenu('Help')

        # Add actions to the file menu
        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        # Add actions to the analyze menu
        plot_action = QAction('Plot Data', self)
        plot_action.triggered.connect(self.plot_data)
        analyze_menu.addAction(plot_action)

        compare_action = QAction('Compare Files', self)
        compare_action.triggered.connect(self.compare_files)
        analyze_menu.addAction(compare_action)

        # Add actions to the filter menu
        filter_action = QAction('Filter Data', self)
        filter_action.triggered.connect(self.filter_data)
        filter_menu.addAction(filter_action)

        # Add actions to the monitor menu
        summary_action = QAction('Show Summary', self)
        summary_action.triggered.connect(self.show_summary)
        monitor_menu.addAction(summary_action)

        # Add actions to the export menu
        export_csv_action = QAction('Export to CSV', self)
        export_csv_action.triggered.connect(self.export_to_csv)
        export_menu.addAction(export_csv_action)

        # Add actions to the help menu
        help_action = QAction('Help', self)
        help_action.triggered.connect(self.show_help)
        help_menu.addAction(help_action)

        # Central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layouts
        self.layout = QVBoxLayout(self.central_widget)
        
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search...")
        self.search_bar.textChanged.connect(self.search_files)
        self.layout.addWidget(self.search_bar)
        
        self.file_list = QListWidget()
        self.layout.addWidget(self.file_list)
        
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.layout.addWidget(self.text_edit)

        self.file_list.itemClicked.connect(self.display_file_content)

        self.statusBar().showMessage("Ready")

    def load_files(self):
        self.file_list.clear()
        for filename in os.listdir(self.current_dir):
            if filename.startswith('data_') and filename.endswith('.json'):
                self.file_list.addItem(filename)

    def display_file_content(self, item):
        filename = item.text()
        with open(os.path.join(self.current_dir, filename), 'r') as file:
            data = json.load(file)
            self.text_edit.setText(json.dumps(data, indent=4))

    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open JSON File', '', 'JSON Files (*.json);;All Files (*)', options=options)
        if file_name:
            with open(file_name, 'r') as file:
                data = json.load(file)
                self.text_edit.setText(json.dumps(data, indent=4))
                self.file_list.addItem(os.path.basename(file_name))

    def plot_data(self):
        # Example data plotting using matplotlib
        data = []
        for i in range(self.file_list.count()):
            item = self.file_list.item(i)
            filename = item.text()
            with open(os.path.join(self.current_dir, filename), 'r') as file:
                data.append(json.load(file))

        df = pd.DataFrame(data)
        fig = px.scatter(df, x="Screen Width", y="Network Downlink", color="Browser Name")
        fig.show()

    def compare_files(self):
        selected_items = self.file_list.selectedItems()
        if len(selected_items) < 2:
            QMessageBox.warning(self, "Warning", "Please select at least two files to compare.")
            return

        data = []
        for item in selected_items:
            filename = item.text()
            with open(os.path.join(self.current_dir, filename), 'r') as file:
                data.append(json.load(file))

        df = pd.DataFrame(data)
        fig, ax = plt.subplots()
        df.plot(kind='bar', ax=ax)
        plt.show()

    def filter_data(self):
        # Example filter functionality
        filter_criteria, ok = QInputDialog.getText(self, "Filter Data", "Enter filter criteria (e.g., 'Browser Name:Netscape')")
        if ok:
            key, value = filter_criteria.split(":")
            filtered_files = []
            for i in range(self.file_list.count()):
                item = self.file_list.item(i)
                filename = item.text()
                with open(os.path.join(self.current_dir, filename), 'r') as file:
                    data = json.load(file)
                    if key in data and str(data[key]) == value:
                        filtered_files.append(filename)

            self.file_list.clear()
            for file in filtered_files:
                self.file_list.addItem(file)

    def show_summary(self):
        data = []
        for i in range(self.file_list.count()):
            item = self.file_list.item(i)
            filename = item.text()
            with open(os.path.join(self.current_dir, filename), 'r') as file:
                data.append(json.load(file))

        df = pd.DataFrame(data)
        summary = df.describe()
        QMessageBox.information(self, "Summary", summary.to_string())

    def export_to_csv(self):
        data = []
        for i in range(self.file_list.count()):
            item = self.file_list.item(i)
            filename = item.text()
            with open(os.path.join(self.current_dir, filename), 'r') as file:
                data.append(json.load(file))

        df = pd.DataFrame(data)
        file_name, _ = QFileDialog.getSaveFileName(self, "Save CSV File", "", "CSV Files (*.csv);;All Files (*)")
        if file_name:
            df.to_csv(file_name, index=False)
            QMessageBox.information(self, "Success", f"Data exported to {file_name}")

    def show_help(self):
        help_text = """
        Help Documentation

        File Menu:
        - Open: Open a JSON file.
        
        Analyze Menu:
        - Plot Data: Plot data using Matplotlib and Plotly.
        - Compare Files: Compare two or more JSON files.
        
        Filter Menu:
        - Filter Data: Filter JSON files based on criteria.
        
        Monitor Menu:
        - Show Summary: Show summary statistics of the data.
        
        Export Menu:
        - Export to CSV: Export data to a CSV file.
        
        Help Menu:
        - Help: Show this help documentation.
        """
        QMessageBox.information(self, "Help", help_text)

    def search_files(self):
        search_text = self.search_bar.text().lower()
        for i in range(self.file_list.count()):
            item = self.file_list.item(i)
            item.setHidden(search_text not in item.text().lower())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = JsonViewer()
    viewer.show()
    sys.exit(app.exec_())
