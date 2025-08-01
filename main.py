# -*- coding: utf-8 -*-
__version__ = '0.1.0'

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.utils import platform
from kivy.logger import Logger
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserIconView
from PIL import Image
import os

class XiaoTuDiDiApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        
        # 文件选择器
        self.file_chooser = FileChooserIconView(
            filters=['*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp']
        )
        self.add_widget(self.file_chooser)
        
        # 尺寸设置区域
        size_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        self.width_input = TextInput(text='350', multiline=False)
        self.height_input = TextInput(text='350', multiline=False)
        
        size_layout.add_widget(Label(text='宽度:'))
        size_layout.add_widget(self.width_input)
        size_layout.add_widget(Label(text='高度:'))
        size_layout.add_widget(self.height_input)
        
        # 保持比例复选框
        self.keep_ratio = CheckBox()
        ratio_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        ratio_layout.add_widget(Label(text='保持长宽比'))
        ratio_layout.add_widget(self.keep_ratio)
        
        # DPI设置
        dpi_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        self.dpi_input = TextInput(text='72', multiline=False)
        dpi_layout.add_widget(Label(text='DPI:'))
        dpi_layout.add_widget(self.dpi_input)
        
        # 质量选择
        quality_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        self.quality_spinner = Spinner(
            text='高质量',
            values=('高质量', '中质量', '低质量'),
            size_hint=(None, None),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5})
        quality_layout.add_widget(Label(text='输出质量:'))
        quality_layout.add_widget(self.quality_spinner)
        
        # 格式选择
        format_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        self.format_spinner = Spinner(
            text='JPEG',
            values=('JPEG', 'PNG'),
            size_hint=(None, None),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5})
        format_layout.add_widget(Label(text='输出格式:'))
        format_layout.add_widget(self.format_spinner)
        
        # 处理按钮
        self.process_btn = Button(
            text='处理并保存图片',
            size_hint_y=None,
            height=50
        )
        self.process_btn.bind(on_press=self.process_image)
        
        # 添加所有控件
        self.add_widget(size_layout)
        self.add_widget(ratio_layout)
        self.add_widget(dpi_layout)
        self.add_widget(quality_layout)
        self.add_widget(format_layout)
        self.add_widget(self.process_btn)
        
    def process_image(self, instance):
        try:
            # 获取选中的文件
            if not self.file_chooser.selection:
                return
                
            input_path = self.file_chooser.selection[0]
            
            # 获取参数
            width = int(self.width_input.text)
            height = int(self.height_input.text)
            dpi = int(self.dpi_input.text)
            
            # 打开图片
            img = Image.open(input_path)
            
            # 如果需要保持比例
            if self.keep_ratio.active:
                ratio = min(width/img.width, height/img.height)
                width = int(img.width * ratio)
                height = int(img.height * ratio)
            
            # 调整大小
            img = img.resize((width, height), Image.Resampling.LANCZOS)
            
            # 设置DPI
            img.info['dpi'] = (dpi, dpi)
            
            # 获取质量设置
            quality_map = {
                '高质量': 95,
                '中质量': 80,
                '低质量': 60
            }
            quality = quality_map[self.quality_spinner.text]
            
            # 准备保存路径
            filename = os.path.splitext(os.path.basename(input_path))[0]
            output_format = self.format_spinner.text.lower()
            output_path = os.path.join(
                os.path.dirname(input_path),
                f"{filename}_processed.{output_format}"
            )
            
            # 保存图片
            if output_format == 'jpeg':
                img.save(output_path, quality=quality, dpi=(dpi, dpi))
            else:  # PNG
                img.save(output_path, quality=quality if output_format == 'jpeg' else None)
                
        except Exception as e:
            print(f"处理图片时出错: {str(e)}")

class MainApp(App):
    def build(self):
        return XiaoTuDiDiApp()

if __name__ == '__main__':
    MainApp().run()
