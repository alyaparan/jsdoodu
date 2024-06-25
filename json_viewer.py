from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, QFileDialog, QVBoxLayout, QWidget, QTextEdit, QListWidget, QHBoxLayout, QPushButton, QLineEdit, QLabel, QComboBox, QMessageBox, QInputDialog, QDialog, QTableView
from PyQt5.QtCore import Qt, QTimer
import sys
import os
import json
import matplotlib
matplotlib.use('Qt5Agg')  # Use Qt5Agg backend
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np  # Import NumPy
import plotly.express as px

class JsonViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('JSON File Viewer')
        self.setGeometry(100, 100, 1200, 800)
        self.current_dir = os.getcwd()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.load_files)

        self.initUI()
        self.load_files()

    def initUI(self):
        # Create menu bar
        menu_bar = self.menuBar()

        # Create menus
        file_menu = menu_bar.addMenu('File')
        analyze_menu = menu_bar.addMenu('Analyze')
        filter_menu = menu_bar.addMenu('Filter')
        monitor_menu = menu_bar.addMenu('Monitor')  # Define monitor_menu here
        export_menu = menu_bar.addMenu('Export')
        help_menu = menu_bar.addMenu('Help')
        theme_menu = menu_bar.addMenu('Theme')

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

        pivot_action = QAction('Create Pivot Table', self)
        pivot_action.triggered.connect(self.create_pivot_table)
        analyze_menu.addAction(pivot_action)

        time_series_action = QAction('Time Series Plot', self)
        time_series_action.triggered.connect(self.time_series_plot)
        analyze_menu.addAction(time_series_action)

        # Add actions to the filter menu
        filter_action = QAction('Filter Data', self)
        filter_action.triggered.connect(self.filter_data)
        filter_menu.addAction(filter_action)

        # Add actions to the monitor menu
        start_monitor_action = QAction('Start Monitoring', self)
        start_monitor_action.triggered.connect(self.start_monitoring)
        monitor_menu.addAction(start_monitor_action)

        stop_monitor_action = QAction('Stop Monitoring', self)
        stop_monitor_action.triggered.connect(self.stop_monitoring)
        monitor_menu.addAction(stop_monitor_action)

        # Add actions to the export menu
        export_csv_action = QAction('Export to CSV', self)
        export_csv_action.triggered.connect(self.export_to_csv)
        export_menu.addAction(export_csv_action)

        # Add actions to the help menu
        help_action = QAction('Help', self)
        help_action.triggered.connect(self.show_help)
        help_menu.addAction(help_action)

        # Add actions to the theme menu
        dark_theme_action = QAction('Dark Theme', self)
        dark_theme_action.triggered.connect(lambda: self.set_theme('dark'))
        theme_menu.addAction(dark_theme_action)

        light_theme_action = QAction('Light Theme', self)
        light_theme_action.triggered.connect(lambda: self.set_theme('light'))
        theme_menu.addAction(light_theme_action)

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
        self.file_list.setSelectionMode(QListWidget.ExtendedSelection)  # Allow multiple selections
        self.layout.addWidget(self.file_list)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.layout.addWidget(self.text_edit)

        self.file_list.itemClicked.connect(self.display_file_content)

        self.statusBar().showMessage("Ready")

    def start_monitoring(self):
        self.timer.start(5000)  # check for new files every 5 seconds
        self.statusBar().showMessage("Monitoring started")

    def stop_monitoring(self):
        self.timer.stop()
        self.statusBar().showMessage("Monitoring stopped")

    def load_files(self):
        self.file_list.clear()
        for filename in os.listdir(self.current_dir):
            if filename.startswith('data_') and filename.endswith('.json'):
                self.file_list.addItem(filename)

    def display_file_content(self, item):
        filename = item.text()
        with open(os.path.join(self.current_dir, filename), 'r') as file:
            data = json.load(file)
            formatted_data = json.dumps(data, indent=4)
            self.text_edit.clear()  # Clear previous content
            self.text_edit.setPlainText(formatted_data)

    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open JSON File', '', 'JSON Files (*.json);;All Files (*)',
                                                   options=options)
        if file_name:
            with open(file_name, 'r') as file:
                data = json.load(file)
                self.text_edit.setText(json.dumps(data, indent=4))
                self.file_list.addItem(os.path.basename(file_name))

    def plot_data(self):
        selected_items = self.file_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Warning", "Please select files to plot.")
            return

        data = []
        for item in selected_items:
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

        # Set backend to Qt5Agg
        import matplotlib
        matplotlib.use('Qt5Agg')
        import matplotlib.pyplot as plt

        data = []
        for item in selected_items:
            filename = item.text()
            with open(os.path.join(self.current_dir, filename), 'r') as file:
                data.append(json.load(file))

        df = pd.DataFrame(data)
        fig, ax = plt.subplots()
        df.plot(kind='bar', ax=ax)
        plt.show()

    def create_pivot_table(self):
        selected_items = self.file_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Warning", "Please select files to create a pivot table.")
            return

        data = []
        for item in selected_items:
            filename = item.text()
            with open(os.path.join(self.current_dir, filename), 'r') as file:
                data.append(json.load(file))

        df = pd.DataFrame(data)
        print("DataFrame columns:", df.columns)  # Print column names for debugging

        # Filter columns for aggregation based on data type
        numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
        non_numeric_columns = df.select_dtypes(exclude=[np.number]).columns.tolist()

        # Create pivot table with correct aggregation function format
        pivot_table = pd.DataFrame(index=df['IP Address'].unique())  # Use unique IP Addresses as index

        # Aggregate numeric columns with mean
        if numeric_columns:
            numeric_pivot = pd.pivot_table(df, index='IP Address', values=numeric_columns, aggfunc='mean')
            pivot_table = pd.concat([pivot_table, numeric_pivot], axis=1)

        # Include non-numeric columns as well
        for col in non_numeric_columns:
            pivot_table[col] = df.groupby('IP Address')[col].apply(lambda x: ', '.join(x.unique().astype(str)))

        pivot_dialog = PivotDialog(pivot_table)
        pivot_dialog.exec_()

    def time_series_plot(self):
        selected_items = self.file_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Warning", "Please select files to plot time series data.")
            return

        data = []
        for item in selected_items:
            filename = item.text()
            with open(os.path.join(self.current_dir, filename), 'r') as file:
                data.append(json.load(file))

        df = pd.DataFrame(data)
        if 'Timestamp' not in df.columns:
            QMessageBox.warning(self, "Warning", "Selected files do not contain timestamp data.")
            return

        fig, ax = plt.subplots()
        for col in df.columns:
            if col != 'Timestamp' and df[col].dtype in ['int64', 'float64']:
                ax.plot(df['Timestamp'], df[col], label=col)
        ax.legend()
        ax.set_xlabel('Timestamp')
        ax.set_ylabel('Values')
        ax.set_title('Time Series Plot')
        plt.show()

    def filter_data(self):
        # Example filter functionality
        filter_criteria, ok = QInputDialog.getText(self, "Filter Data",
                                                   "Enter filter criteria (e.g., 'Browser Name:Netscape')")
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
        - Create Pivot Table: Create a pivot table from selected JSON files.
        - Time Series Plot: Plot time series data (requires 'Timestamp' column).

        Filter Menu:
        - Filter Data: Filter JSON files based on criteria.

        Monitor Menu:
        - Start Monitoring: Start monitoring for new JSON files.
        - Stop Monitoring: Stop monitoring.

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

    def set_theme(self, theme):
        if theme == 'dark':
            self.setStyleSheet("""
                QWidget {
                    background-color: #333;
                    color: #fff;
                }
                QMenuBar {
                    background-color: #555;
                    color: #fff;
                }
                /* Add more styles as needed */
            """)
        elif theme == 'light':
            self.setStyleSheet("""
                QWidget {
                    background-color: #fff;
                    color: #000;
                }
                QMenuBar {
                    background-color: #eee;
                    color: #000;
                }
                /* Add more styles as needed */
            """)
        # Refresh the UI
        self.central_widget.setStyleSheet("")  # Reset stylesheet to apply changes
        self.update()

# Add a new class for PivotDialog
class PivotDialog(QDialog):
    def __init__(self, pivot_table, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Pivot Table")
        self.layout = QVBoxLayout(self)

        self.table_view = QTableView()
        self.layout.addWidget(self.table_view)

        # Display pivot table
        model = PandasModel(pivot_table)
        self.table_view.setModel(model)

        self.setLayout(self.layout)
        self.setGeometry(100, 100, 800, 600)


# Add a PandasModel class to display the pandas DataFrame in QTableView
from PyQt5.QtCore import Qt, QAbstractTableModel, QVariant

class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
        self.header_labels = data.columns.tolist()

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(str(self._data.iloc[index.row(), index.column()]))

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(str(self.header_labels[section]))
        return QVariant()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = JsonViewer()
    viewer.show()
    sys.exit(app.exec_())
