# from_photo_to_word
图片转文字
本库是分别针对QPython（手机）和IDLE（电脑）的文字转换Python代码。这些代码可以将图片中的文字转换为可编辑的文本。
QPython（手机版）使用说明:
在QPython中安装所需库: pip install pytesseract pillow
需要下载Tesseract OCR语言数据包(中文+英文)
确保给予QPython相机和存储权限
IDLE（电脑版）使用说明:
安装所需库: pip install pytesseract pillow
下载并安装Tesseract OCR: https://github.com/tesseract-ocr/tesseract
下载中文语言包(chi_sim)
通用注意事项
    两种版本都需要Tesseract OCR引擎支持
    中文识别需要下载中文语言包(chi_sim)
    识别准确率取决于图片质量和文字清晰度
    对于复杂排版或手写文字，识别率可能会降低
各位可以根据需要修改代码，例如添加更多语言支持或调整识别参数。
