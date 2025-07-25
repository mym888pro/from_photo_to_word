# idle_ocr.py - 电脑端文字识别
import pytesseract
from PIL import Image, ImageGrab
import os
import sys

def computer_ocr():
    # 检查Tesseract路径(Windows可能需要设置)
    if sys.platform == 'win32':
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    
    print("电脑文字识别工具")
    print("1. 从文件识别")
    print("2. 截图识别")
    choice = input("请选择操作(1/2): ")
    
    if choice == '1':
        # 从文件识别
        image_path = input("请输入图片路径: ").strip('"')
        if not os.path.exists(image_path):
            print("文件不存在")
            return
        try:
            image = Image.open(image_path)
        except Exception as e:
            print(f"无法打开图片: {e}")
            return
    elif choice == '2':
        # 截图识别
        print("请框选要识别的区域...")
        try:
            image = ImageGrab.grab()
            image.show()  # 显示截图
        except Exception as e:
            print(f"截图失败: {e}")
            return
    else:
        print("无效选择")
        return
    
    # 识别文字
    try:
        print("正在识别文字...")
        text = pytesseract.image_to_string(image, lang='chi_sim+eng')
        print("\n识别结果:")
        print(text)
        
        # 询问是否保存结果
        save = input("\n是否保存识别结果到文件?(y/n): ").lower()
        if save == 'y':
            default_path = 'ocr_result.txt'
            save_path = input(f"输入保存路径(默认{default_path}): ") or default_path
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"结果已保存到 {os.path.abspath(save_path)}")
    except Exception as e:
        print(f"识别出错: {e}")

if __name__ == '__main__':
    computer_ocr()
