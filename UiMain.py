from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QPushButton, QSlider, QTableWidget,
                             QTableWidgetItem, QGroupBox, QComboBox, QDoubleSpinBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage, QIcon


class UiMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YOLOv8 目标检测系统")
        self.setWindowIcon(QIcon("icon.png"))  # 请替换为你的图标路径
        self.resize(1200, 800)

        # 主窗口中心部件
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # 主布局
        self.main_layout = QHBoxLayout(self.central_widget)

        # 左侧面板 (图像显示)
        self.left_panel = QVBoxLayout()
        self.main_layout.addLayout(self.left_panel, 70)  # 70%宽度

        # 原始图像显示
        self.original_image_group = QGroupBox("原始图像")
        self.original_image_layout = QVBoxLayout()
        self.original_image_label = QLabel()
        self.original_image_label.setAlignment(Qt.AlignCenter)
        self.original_image_label.setMinimumSize(640, 360)
        self.original_image_layout.addWidget(self.original_image_label)
        self.original_image_group.setLayout(self.original_image_layout)
        self.left_panel.addWidget(self.original_image_group)

        # 检测结果图像显示
        self.result_image_group = QGroupBox("检测结果")
        self.result_image_layout = QVBoxLayout()
        self.result_image_label = QLabel()
        self.result_image_label.setAlignment(Qt.AlignCenter)
        self.result_image_label.setMinimumSize(640, 360)
        self.result_image_layout.addWidget(self.result_image_label)
        self.result_image_group.setLayout(self.result_image_layout)
        self.left_panel.addWidget(self.result_image_group)

        # 右侧面板 (控制面板)
        self.right_panel = QVBoxLayout()
        self.main_layout.addLayout(self.right_panel, 30)  # 30%宽度

        # 模型选择
        self.model_group = QGroupBox("模型设置")
        self.model_layout = QVBoxLayout()

        self.model_combo = QComboBox()
        self.model_combo.addItems(["best"])
        self.model_layout.addWidget(QLabel("选择模型:"))
        self.model_layout.addWidget(self.model_combo)

        self.model_group.setLayout(self.model_layout)
        self.right_panel.addWidget(self.model_group)

        # 检测参数
        self.params_group = QGroupBox("检测参数")
        self.params_layout = QVBoxLayout()

        # 置信度阈值
        self.confidence_label = QLabel("置信度阈值: 0.25")
        self.confidence_slider = QSlider(Qt.Horizontal)
        self.confidence_slider.setRange(0, 100)
        self.confidence_slider.setValue(25)
        self.confidence_spinbox = QDoubleSpinBox()
        self.confidence_spinbox.setRange(0.0, 1.0)
        self.confidence_spinbox.setSingleStep(0.05)
        self.confidence_spinbox.setValue(0.25)

        # IoU阈值
        self.iou_label = QLabel("IoU阈值: 0.45")
        self.iou_slider = QSlider(Qt.Horizontal)
        self.iou_slider.setRange(0, 100)
        self.iou_slider.setValue(45)
        self.iou_spinbox = QDoubleSpinBox()
        self.iou_spinbox.setRange(0.0, 1.0)
        self.iou_spinbox.setSingleStep(0.05)
        self.iou_spinbox.setValue(0.45)

        self.params_layout.addWidget(self.confidence_label)
        self.params_layout.addWidget(self.confidence_slider)
        self.params_layout.addWidget(self.confidence_spinbox)
        self.params_layout.addWidget(self.iou_label)
        self.params_layout.addWidget(self.iou_slider)
        self.params_layout.addWidget(self.iou_spinbox)

        self.params_group.setLayout(self.params_layout)
        self.right_panel.addWidget(self.params_group)

        # 功能按钮
        self.buttons_group = QGroupBox("功能")
        self.buttons_layout = QVBoxLayout()

        self.image_btn = QPushButton("图片检测")
        self.video_btn = QPushButton("视频检测")
        self.camera_btn = QPushButton("摄像头检测")
        self.stop_btn = QPushButton("停止检测")
        self.save_btn = QPushButton("保存结果")

        self.buttons_layout.addWidget(self.image_btn)
        self.buttons_layout.addWidget(self.video_btn)
        self.buttons_layout.addWidget(self.camera_btn)
        self.buttons_layout.addWidget(self.stop_btn)
        self.buttons_layout.addWidget(self.save_btn)

        self.buttons_group.setLayout(self.buttons_layout)
        self.right_panel.addWidget(self.buttons_group)

        # 检测结果表格
        self.results_group = QGroupBox("检测结果")
        self.results_layout = QVBoxLayout()

        self.results_table = QTableWidget()
        self.results_table.setColumnCount(4)
        self.results_table.setHorizontalHeaderLabels(["类别", "置信度", "位置(x)", "位置(y)"])
        self.results_table.setColumnWidth(0, 100)
        self.results_table.setColumnWidth(1, 80)
        self.results_table.setColumnWidth(2, 80)
        self.results_table.setColumnWidth(3, 80)

        self.results_layout.addWidget(self.results_table)
        self.results_group.setLayout(self.results_layout)
        self.right_panel.addWidget(self.results_group)

        # 状态栏
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("就绪")

        # 美化样式
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QGroupBox {
                border: 1px solid #ccc;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 15px;
                font-weight: bold;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 3px;
            }
            QLabel {
                font-size: 12px;
            }
            QPushButton {
                background-color: #4CAF50;
                border: none;
                color: white;
                padding: 8px;
                text-align: center;
                text-decoration: none;
                font-size: 14px;
                margin: 4px 2px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3e8e41;
            }
            QPushButton:disabled {
                background-color: #cccccc;
            }
            QTableWidget {
                background-color: white;
                border: 1px solid #ddd;
            }
            QHeaderView::section {
                background-color: #f8f8f8;
                padding: 4px;
                border: 1px solid #ddd;
            }
            QSlider::groove:horizontal {
                height: 8px;
                background: #ddd;
                margin: 2px 0;
            }
            QSlider::handle:horizontal {
                background: #4CAF50;
                border: 1px solid #45a049;
                width: 18px;
                margin: -5px 0;
                border-radius: 3px;
            }
        """)

        # 连接信号和槽
        self.confidence_slider.valueChanged.connect(self.update_confidence)
        self.confidence_spinbox.valueChanged.connect(self.update_confidence_slider)
        self.iou_slider.valueChanged.connect(self.update_iou)
        self.iou_spinbox.valueChanged.connect(self.update_iou_slider)

    def update_confidence(self, value):
        confidence = value / 100.0
        self.confidence_spinbox.setValue(confidence)
        self.confidence_label.setText(f"置信度阈值: {confidence:.2f}")

    def update_confidence_slider(self, value):
        self.confidence_slider.setValue(int(value * 100))

    def update_iou(self, value):
        iou = value / 100.0
        self.iou_spinbox.setValue(iou)
        self.iou_label.setText(f"IoU阈值: {iou:.2f}")

    def update_iou_slider(self, value):
        self.iou_slider.setValue(int(value * 100))

    def display_image(self, label, image):
        if image is not None:
            h, w, ch = image.shape
            bytes_per_line = ch * w
            q_img = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_img)
            label.setPixmap(pixmap.scaled(label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def clear_results(self):
        self.results_table.setRowCount(0)

    def add_detection_result(self, class_name, confidence, x, y):
        row = self.results_table.rowCount()
        self.results_table.insertRow(row)

        self.results_table.setItem(row, 0, QTableWidgetItem(class_name))
        self.results_table.setItem(row, 1, QTableWidgetItem(f"{confidence:.2f}"))
        self.results_table.setItem(row, 2, QTableWidgetItem(str(x)))
        self.results_table.setItem(row, 3, QTableWidgetItem(str(y)))

    def update_status(self, message):
        self.status_bar.showMessage(message)