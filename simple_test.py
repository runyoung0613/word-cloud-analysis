#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("=== 简单测试脚本 ===")

# 检查依赖
print("\n检查依赖安装情况...")
try:
    import jieba
    print("✓ jieba已安装")
except ImportError:
    print("✗ jieba未安装")

try:
    import matplotlib
    print("✓ matplotlib已安装")
except ImportError:
    print("✗ matplotlib未安装")

try:
    from wordcloud import WordCloud
    print("✓ wordcloud已安装")
except ImportError:
    print("✗ wordcloud未安装")

try:
    from PIL import Image
    print("✓ PIL已安装")
except ImportError:
    print("✗ PIL未安装")

try:
    import numpy as np
    print("✓ numpy已安装")
except ImportError:
    print("✗ numpy未安装")

# 检查示例文件
print("\n检查示例文件...")
import os
if os.path.exists('sample_text.txt'):
    print("✓ sample_text.txt文件存在")
    try:
        with open('sample_text.txt', 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"✓ 成功读取文件内容，长度: {len(content)} 字符")
            print("\n文件内容预览:")
            print(content[:100] + "..." if len(content) > 100 else content)
    except Exception as e:
        print(f"✗ 读取文件失败: {e}")
else:
    print("✗ sample_text.txt文件不存在")

print("\n测试完成！")