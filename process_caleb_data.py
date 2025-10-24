#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Caleb对话处理脚本
功能：从Caleb_data文件夹中提取Caleb的对话，并生成可分析的文本文件
作者：runyoung
版本：1.0
"""

import os
import re

# 设置文件夹和文件路径
caleb_data_folder = "Caleb_data"
caleb_dialogues_file = "caleb_dialogues.txt"

# 检查Caleb_data文件夹是否存在
if not os.path.exists(caleb_data_folder):
    print(f"错误：找不到文件夹 {caleb_data_folder}")
    exit(1)

# 创建一个空列表来存储Caleb的对话
caleb_dialogues = []

print(f"从{caleb_data_folder}文件夹中提取Caleb的对话...")
print("=" * 50)

# 遍历文件夹中的所有txt文件
for filename in os.listdir(caleb_data_folder):
    if filename.endswith('.txt'):
        file_path = os.path.join(caleb_data_folder, filename)
        print(f"处理文件: {filename}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                        
                    # 匹配Caleb的对话行，考虑不同的冒号格式和大小写
                    match = re.match(r'^Caleb[：:]\s*(.+)', line, re.IGNORECASE)
                    
                    if match:
                        dialogue = match.group(1).strip()
                        # 排除非对话内容（如"思考.jpg"等）
                        if dialogue and not any(x in dialogue.lower() for x in ['jpg', 'png', '图片']):
                            caleb_dialogues.append(dialogue)
                            print(f"  - 提取: {dialogue}")
                            
        except Exception as e:
            print(f"  读取文件时出错: {str(e)}")
    
print("=" * 50)

# 保存提取的对话
with open(caleb_dialogues_file, 'w', encoding='utf-8') as f:
    for dialogue in caleb_dialogues:
        f.write(dialogue + '\n')

print(f"\n已成功提取 {len(caleb_dialogues)} 条Caleb的对话")
print(f"保存到文件: {caleb_dialogues_file}")
print("\n下一步操作指南：")
print("1. 检查生成的caleb_dialogues.txt文件是否包含了正确的对话")
print("2. 使用以下代码在Python环境中运行分析：")
print("   ")
print("   from character_dialogue_analyzer import CharacterDialogueAnalyzer")
print("   analyzer = CharacterDialogueAnalyzer()")
print("   analyzer.load_dialogues_from_file('caleb_dialogues.txt')")
print("   analyzer.run_complete_analysis('caleb_dialogues.txt')")
print("   ")
print("3. 分析结果将保存在analysis_results文件夹中")
print("4. 你可以查看以下内容：")
print("   - 总体词云: wordcloud.png")
print("   - 积极词汇词云: positive_wordcloud.png")
print("   - 消极词汇词云: negative_wordcloud.png")
print("\n注意：如果需要调整分析参数，可以修改character_dialogue_analyzer.py中的相关设置")