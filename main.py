import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QTextEdit, QComboBox, QCheckBox, QPushButton, 
                             QFileDialog, QGroupBox, QProgressBar, QLineEdit, QStyleFactory)
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QParallelAnimationGroup
from PyQt6.QtGui import QIcon, QFont, QTextCursor, QPalette, QColor

class CodeConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("C-Convert-Hub")
        self.setGeometry(100, 100, 1200, 800)
        self.setMinimumSize(1000, 700)
        
        # Load styles
        self.setStyleSheet(self.load_stylesheet())
        
        # Central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(15, 15, 15, 15)
        self.main_layout.setSpacing(15)
        
        self.init_ui()
        self.init_animations()
        
    def load_stylesheet(self):
        return """
        /* Main window */
        QMainWindow {
            background-color: #2b2b2b;
        }
        
        /* Group boxes */
        QGroupBox {
            border: 1px solid #444;
            border-radius: 5px;
            margin-top: 10px;
            padding-top: 15px;
            color: #bbb;
            font-weight: bold;
        }
        
        QGroupBox::title {
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 3px;
        }
        
        /* Text edits */
        QTextEdit {
            background-color: #1e1e1e;
            color: #d4d4d4;
            border: 1px solid #444;
            border-radius: 4px;
            padding: 5px;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 12px;
            selection-background-color: #264f78;
        }
        
        /* Buttons */
        QPushButton {
            background-color: #3a3a3a;
            color: #d4d4d4;
            border: 1px solid #444;
            border-radius: 4px;
            padding: 7px 15px;
            min-width: 80px;
        }
        
        QPushButton:hover {
            background-color: #4a4a4a;
            border: 1px solid #555;
        }
        
        QPushButton:pressed {
            background-color: #2a2a2a;
        }
        
        QPushButton:disabled {
            background-color: #2a2a2a;
            color: #777;
        }
        
        /* Combo boxes */
        QComboBox {
            background-color: #3a3a3a;
            color: #d4d4d4;
            border: 1px solid #444;
            border-radius: 4px;
            padding: 5px;
            min-width: 100px;
        }
        
        QComboBox:hover {
            background-color: #4a4a4a;
        }
        
        QComboBox::drop-down {
            border: none;
        }
        
        /* Check boxes */
        QCheckBox {
            color: #d4d4d4;
            spacing: 5px;
        }
        
        QCheckBox::indicator {
            width: 16px;
            height: 16px;
        }
        
        QCheckBox::indicator:unchecked {
            background-color: #3a3a3a;
            border: 1px solid #555;
        }
        
        QCheckBox::indicator:checked {
            background-color: #5050ff;
            border: 1px solid #5050ff;
        }
        
        /* Line edits */
        QLineEdit {
            background-color: #3a3a3a;
            color: #d4d4d4;
            border: 1px solid #444;
            border-radius: 4px;
            padding: 5px;
        }
        
        /* Progress bar */
        QProgressBar {
            border: 1px solid #444;
            border-radius: 4px;
            text-align: center;
            background-color: #2b2b2b;
        }
        
        QProgressBar::chunk {
            background-color: #5050ff;
            width: 10px;
        }
        
        /* Custom classes */
        .TitleLabel {
            font-size: 18px;
            font-weight: bold;
            color: #fff;
            padding-bottom: 5px;
        }
        
        .ConvertButton {
            background-color: #5050ff;
            font-weight: bold;
        }
        
        .ConvertButton:hover {
            background-color: #6060ff;
        }
        
        .ConvertButton:pressed {
            background-color: #4040ee;
        }
        """
    
    def init_ui(self):
        # Header
        self.header = QLabel("C-Convert-Hub: Advanced Code Converter")
        self.header.setObjectName("header")
        self.header.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #fff;
            padding-bottom: 10px;
        """)
        self.main_layout.addWidget(self.header)
        
        # Settings group
        self.settings_group = QGroupBox("Conversion Settings")
        self.settings_layout = QHBoxLayout(self.settings_group)
        
        # Language selection
        self.lang_frame = QWidget()
        self.lang_layout = QVBoxLayout(self.lang_frame)
        self.lang_layout.setContentsMargins(0, 0, 0, 0)
        
        self.source_lang_label = QLabel("Source Language:")
        self.source_lang = QComboBox()
        self.source_lang.addItems(["C", "C++", "C#"])
        
        self.target_lang_label = QLabel("Target Language:")
        self.target_lang = QComboBox()
        self.target_lang.addItems(["C", "C++", "C#"])
        self.target_lang.setCurrentIndex(1)
        
        self.lang_layout.addWidget(self.source_lang_label)
        self.lang_layout.addWidget(self.source_lang)
        self.lang_layout.addSpacing(10)
        self.lang_layout.addWidget(self.target_lang_label)
        self.lang_layout.addWidget(self.target_lang)
        
        # Conversion options
        self.options_frame = QWidget()
        self.options_layout = QVBoxLayout(self.options_frame)
        self.options_layout.setContentsMargins(0, 0, 0, 0)
        
        self.preserve_comments = QCheckBox("Preserve Comments")
        self.preserve_comments.setChecked(True)
        
        self.convert_oo = QCheckBox("Convert OOP Constructs")
        self.convert_oo.setChecked(True)
        
        self.optimize_code = QCheckBox("Optimize Code")
        
        self.include_metadata = QCheckBox("Include Conversion Metadata")
        self.include_metadata.setChecked(True)
        
        self.options_layout.addWidget(self.preserve_comments)
        self.options_layout.addWidget(self.convert_oo)
        self.options_layout.addWidget(self.optimize_code)
        self.options_layout.addWidget(self.include_metadata)
        
        # Performance options
        self.perf_frame = QWidget()
        self.perf_layout = QVBoxLayout(self.perf_frame)
        self.perf_layout.setContentsMargins(0, 0, 0, 0)
        
        self.threading_label = QLabel("Threading:")
        self.threading_combo = QComboBox()
        self.threading_combo.addItems(["Single Thread", "Multi-Thread (2 cores)", "Multi-Thread (4 cores)", "Max Performance"])
        
        self.memory_usage = QCheckBox("Limit Memory Usage")
        
        self.perf_layout.addWidget(self.threading_label)
        self.perf_layout.addWidget(self.threading_combo)
        self.perf_layout.addWidget(self.memory_usage)
        
        self.settings_layout.addWidget(self.lang_frame)
        self.settings_layout.addWidget(self.options_frame)
        self.settings_layout.addWidget(self.perf_frame)
        self.main_layout.addWidget(self.settings_group)
        
        # Output settings
        self.output_group = QGroupBox("Output Settings")
        self.output_layout = QHBoxLayout(self.output_group)
        
        self.output_name_label = QLabel("Output Name:")
        self.output_name = QLineEdit()
        self.output_name.setPlaceholderText("output")
        
        self.output_path_label = QLabel("Output Path:")
        self.output_path = QLineEdit()
        self.output_path.setPlaceholderText("Select output directory...")
        
        self.browse_button = QPushButton("Browse...")
        self.browse_button.clicked.connect(self.browse_output_path)
        
        self.output_layout.addWidget(self.output_name_label)
        self.output_layout.addWidget(self.output_name)
        self.output_layout.addWidget(self.output_path_label)
        self.output_layout.addWidget(self.output_path)
        self.output_layout.addWidget(self.browse_button)
        self.main_layout.addWidget(self.output_group)
        
        # Code areas
        self.code_frame = QWidget()
        self.code_layout = QHBoxLayout(self.code_frame)
        self.code_layout.setContentsMargins(0, 0, 0, 0)
        self.code_layout.setSpacing(15)
        
        # Source code
        self.source_group = QGroupBox("Source Code")
        self.source_layout = QVBoxLayout(self.source_group)
        
        self.source_actions = QHBoxLayout()
        self.load_button = QPushButton("Load File")
        self.load_button.clicked.connect(self.load_file)
        self.clear_source_button = QPushButton("Clear")
        self.clear_source_button.clicked.connect(self.clear_source)
        
        self.source_actions.addWidget(self.load_button)
        self.source_actions.addWidget(self.clear_source_button)
        self.source_actions.addStretch()
        
        self.source_code = QTextEdit()
        self.source_code.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        
        self.source_layout.addLayout(self.source_actions)
        self.source_layout.addWidget(self.source_code)
        
        # Conversion buttons
        self.convert_buttons = QVBoxLayout()
        self.convert_buttons.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.convert_button = QPushButton("Convert →")
        self.convert_button.setObjectName("ConvertButton")
        self.convert_button.clicked.connect(self.convert_code)
        
        self.convert_all_button = QPushButton("Batch Convert")
        self.convert_all_button.clicked.connect(self.batch_convert)
        
        self.convert_buttons.addStretch()
        self.convert_buttons.addWidget(self.convert_button)
        self.convert_buttons.addWidget(self.convert_all_button)
        self.convert_buttons.addStretch()
        
        # Target code
        self.target_group = QGroupBox("Converted Code")
        self.target_layout = QVBoxLayout(self.target_group)
        
        self.target_actions = QHBoxLayout()
        self.save_button = QPushButton("Save File")
        self.save_button.clicked.connect(self.save_file)
        self.clear_target_button = QPushButton("Clear")
        self.clear_target_button.clicked.connect(self.clear_target)
        
        self.target_actions.addWidget(self.save_button)
        self.target_actions.addWidget(self.clear_target_button)
        self.target_actions.addStretch()
        
        self.target_code = QTextEdit()
        self.target_code.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        self.target_code.setReadOnly(True)
        
        self.target_layout.addLayout(self.target_actions)
        self.target_layout.addWidget(self.target_code)
        
        self.code_layout.addWidget(self.source_group)
        self.code_layout.addLayout(self.convert_buttons)
        self.code_layout.addWidget(self.target_group)
        self.main_layout.addWidget(self.code_frame)
        
        # Status bar
        self.status_bar = QLabel("Ready")
        self.status_bar.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.status_bar.setStyleSheet("color: #aaa;")
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)
        
        self.status_layout = QHBoxLayout()
        self.status_layout.addWidget(self.status_bar)
        self.status_layout.addWidget(self.progress_bar)
        self.main_layout.addLayout(self.status_layout)
        
        # Apply fusion style for modern look
        self.setStyle(QStyleFactory.create("Fusion"))
        
        # Dark palette
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
        palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)
        self.setPalette(palette)
    
    def init_animations(self):
        # Button hover animations
        self.convert_anim = QPropertyAnimation(self.convert_button, b"geometry")
        self.convert_anim.setDuration(200)
        self.convert_anim.setEasingCurve(QEasingCurve.Type.OutQuad)
        
        # Status bar animations
        self.status_anim = QPropertyAnimation(self.status_bar, b"styleSheet")
        self.status_anim.setDuration(500)
        
        # Group box animations
        self.group_anim_group = QParallelAnimationGroup()
        
        for group in [self.settings_group, self.output_group, self.source_group, self.target_group]:
            anim = QPropertyAnimation(group, b"maximumHeight")
            anim.setDuration(300)
            anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
            self.group_anim_group.addAnimation(anim)
    
    def browse_output_path(self):
        path = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        if path:
            self.output_path.setText(path)
    
    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open Source File", "", 
            "Source Files (*.c *.cpp *.cs *.h *.hpp);;All Files (*)"
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.source_code.setPlainText(content)
                    
                    # Auto-detect language
                    ext = os.path.splitext(file_path)[1].lower()
                    if ext == '.c':
                        self.source_lang.setCurrentIndex(0)
                    elif ext in ('.cpp', '.hpp', '.h'):
                        self.source_lang.setCurrentIndex(1)
                    elif ext == '.cs':
                        self.source_lang.setCurrentIndex(2)
                    
                    # Set default output name
                    base_name = os.path.splitext(os.path.basename(file_path))[0]
                    self.output_name.setText(f"{base_name}_converted")
                    
                    self.show_status(f"Loaded: {file_path}", "green")
            except Exception as e:
                self.show_status(f"Error: {str(e)}", "red")
    
    def save_file(self):
        if not self.target_code.toPlainText():
            self.show_status("No converted code to save", "orange")
            return
            
        default_name = self.output_name.text() or "converted"
        source_ext = self.get_extension(self.source_lang.currentText())
        target_ext = self.get_extension(self.target_lang.currentText())
        
        default_path = self.output_path.text() or os.getcwd()
        default_file = os.path.join(default_path, f"{default_name}{target_ext}")
        
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Converted File", default_file,
            f"Target Files (*{target_ext});;All Files (*)"
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(self.target_code.toPlainText())
                self.show_status(f"Saved: {file_path}", "green")
            except Exception as e:
                self.show_status(f"Error: {str(e)}", "red")
    
    def get_extension(self, language):
        if language == "C":
            return ".c"
        elif language == "C++":
            return ".cpp"
        elif language == "C#":
            return ".cs"
        return ".txt"
    
    def clear_source(self):
        self.source_code.clear()
    
    def clear_target(self):
        self.target_code.clear()
    
    def convert_code(self):
        source = self.source_code.toPlainText()
        from_lang = self.source_lang.currentText()
        to_lang = self.target_lang.currentText()
        
        if not source.strip():
            self.show_status("Error: Source code is empty", "red")
            return
        
        self.progress_bar.setValue(0)
        self.show_status("Converting...", "blue")
        
        # Simulate conversion progress
        for i in range(1, 101):
            self.progress_bar.setValue(i)
            QApplication.processEvents()  # Allow UI updates
        
        try:
            # In a real implementation, this would call the actual conversion logic
            result = self.simulate_conversion(source, from_lang, to_lang)
            
            self.target_code.setPlainText(result)
            self.show_status(f"Conversion complete: {from_lang} → {to_lang}", "green")
        except Exception as e:
            self.show_status(f"Conversion error: {str(e)}", "red")
    
    def batch_convert(self):
        self.show_status("Batch conversion not implemented yet", "orange")
    
    def simulate_conversion(self, source, from_lang, to_lang):
        # This is just a simulation - a real implementation would parse and convert the code
        result = f"// Converted from {from_lang} to {to_lang}\n"
        result += f"// Settings: Preserve comments={self.preserve_comments.isChecked()}, "
        result += f"Convert OOP={self.convert_oo.isChecked()}, "
        result += f"Optimize={self.optimize_code.isChecked()}\n\n"
        
        if from_lang == "C" and to_lang == "C++":
            # Simple C to C++ simulation
            result += source.replace("typedef struct", "struct")
            result = result.replace("void some_function(", "void SomeClass::some_function(")
        elif from_lang == "C#" and to_lang == "C++":
            # Simple C# to C++ simulation
            result += source.replace("public class", "class")
            result = result.replace("Console.WriteLine", "std::cout <<")
        else:
            result += source
        
        return result
    
    def show_status(self, message, color="white"):
        colors = {
            "red": "#ff6b6b",
            "green": "#6bff6b",
            "blue": "#6b6bff",
            "orange": "#ffb347",
            "white": "#ffffff"
        }
        
        self.status_bar.setText(message)
        self.status_bar.setStyleSheet(f"color: {colors.get(color, '#ffffff')};")
        
        # Animate status change
        self.status_anim.stop()
        self.status_anim.setStartValue(f"color: {colors.get(color, '#ffffff')}; font-weight: bold;")
        self.status_anim.setEndValue(f"color: {colors.get(color, '#ffffff')}; font-weight: normal;")
        self.status_anim.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Set application attributes
    app.setApplicationName("C-Convert-Hub")
    app.setApplicationDisplayName("C-Convert-Hub")
    app.setApplicationVersion("1.0.0")
    
    window = CodeConverterApp()
    window.show()
    sys.exit(app.exec())