import sys
import time
from PySide6.QtCore import QObject, QThread, Signal, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

class Task1(QObject):
    task1_done = Signal(str)

    def run(self):
        for i in range(10):
            time.sleep(1)
        self.task1_done.emit("Task 1 completed")

class Task2(QObject):
    task2_done = Signal(str)

    def run(self):
        for i in range(10):
            time.sleep(1)
        self.task2_done.emit("Task 2 completed")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Tasks not started yet")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.task1_thread = QThread()
        self.task1 = Task1()
        self.task1.task1_done.connect(self.update_label)
        self.task1.moveToThread(self.task1_thread)

        self.task2_thread = QThread()
        self.task2 = Task2()
        self.task2.task2_done.connect(self.update_label)
        self.task2.moveToThread(self.task2_thread)

        self.timer = QTimer()
        self.timer.timeout.connect(self.start_tasks)
        self.timer.setSingleShot(True)
        self.timer.start(0)

    def start_tasks(self):
        self.label.setText("Tasks started")
        self.task1_thread.start()
        self.task2_thread.start()
        self.task1.run()
        self.task2.run()

    def update_label(self, text):
        self.label.setText(text)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())

import sys
import threading
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class TaskThread(QThread):
    task1_finished = Signal()
    task2_finished = Signal()

    def run(self):
        # Perform task 1
        # ...

        # Emit signal when task 1 is finished
        self.task1_finished.emit()

        # Perform task 2
        # ...

        # Emit signal when task 2 is finished
        self.task2_finished.emit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create GUI elements
        # ...

        # Connect signals to slots
        self.task_thread = TaskThread()
        self.task_thread.task1_finished.connect(self.on_task1_finished)
        self.task_thread.task2_finished.connect(self.on_task2_finished)

        # Start the thread
        self.task_thread.start()

    def on_task1_finished(self):
        # Update GUI or do something else
        # ...

    def on_task2_finished(self):
        # Update GUI or do something else
        # ...

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
