#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Word Cloud Generator - 使用Trae AI创建的词云生成工具

这是一个简单的词云生成器，可以从文本文件中读取内容，生成词云图像。
"""

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import numpy as np
from PIL import Image
import re
import os

def clean_text(text):
    """清理文本，去除特殊字符"""
    # 移除特殊字符，只保留中文、英文和数字
    text = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9\s]', '', text)
    return text

def generate_word_cloud(text, output_path='wordcloud.png', mask_path=None):
    """
    生成词云
    
    参数:
    text: 要分析的文本
    output_path: 输出图片路径
    mask_path: 词云形状模板路径
    """
    # 清理文本
    text = clean_text(text)
    
    # 使用jieba进行中文分词
    words = jieba.cut(text)
    words_str = ' '.join(words)
    
    # 设置词云参数
    wc_kwargs = {
        'font_path': 'simhei.ttf',  # 如果没有这个字体，需要安装或更改为系统中有的中文字体
        'background_color': 'white',
        'max_words': 2000,
        'max_font_size': 200,
        'width': 800,
        'height': 600,
        'collocations': False
    }
    
    # 如果提供了形状模板
    if mask_path and os.path.exists(mask_path):
        mask = np.array(Image.open(mask_path))
        wc_kwargs['mask'] = mask
    
    # 创建词云对象
    wordcloud = WordCloud(**wc_kwargs).generate(words_str)
    
    # 显示词云
    plt.figure(figsize=(10, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout(pad=0)
    
    # 保存词云图片
    wordcloud.to_file(output_path)
    print(f"词云已保存到: {output_path}")
    
    return wordcloud

def read_text_from_file(file_path):
    """从文件读取文本"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    print("=== Word Cloud Generator ===")
    print("使用Trae AI创建的词云生成工具")
    print()
    
    # 从示例文本文件读取
    try:
        text = read_text_from_file('sample_text.txt')
        print("成功读取示例文本文件！")
        # 生成词云
        generate_word_cloud(text, 'sample_wordcloud.png')
        print("\n示例词云已生成！")
        print("\n后续步骤：")
        print("1. 安装依赖：pip install -r requirements.txt")
        print("2. 运行程序：python word_cloud_generator.py")
        print("3. 查看生成的词云图片：sample_wordcloud.png")
        print("4. 尝试修改sample_text.txt文件中的内容，生成不同的词云")
    except Exception as e:
        print(f"发生错误：{e}")
        print("请确保sample_text.txt文件存在且编码正确。")

if __name__ == "__main__":
    main()