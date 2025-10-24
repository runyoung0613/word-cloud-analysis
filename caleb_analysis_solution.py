#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Caleb对话分析完整解决方案
此脚本将：
1. 从Caleb_data文件夹提取Caleb的对话
2. 保存为character_dialogue_analyzer可识别的格式
3. 提供详细的使用指南和代码示例
"""

import os
import sys

def main():
    # 检查Python环境
    print("当前Python版本:", sys.version)
    
    # 确保目录存在
    caleb_data_dir = "Caleb_data"
    if not os.path.exists(caleb_data_dir):
        print(f"错误: 找不到目录 {caleb_data_dir}")
        return
    
    # 列出可用的对话文件
    print("\nCaleb_data文件夹中的文件:")
    try:
        files = os.listdir(caleb_data_dir)
        if not files:
            print("  文件夹为空")
        else:
            for file in files:
                print(f"  - {file}")
    except Exception as e:
        print(f"  读取目录时出错: {e}")
    
    # 手动提取对话内容示例（无需实际执行，供参考）
    output_file = "caleb_dialogues.txt"
    print(f"\n将从对话文件中提取Caleb的对话内容并保存到 {output_file}")
    print("提取规则: 匹配以'Caleb：'或'Caleb:'开头的行，并提取对话内容")
    
    # 创建详细的分析指南
    guide_content = """
# Caleb对话分析操作指南

## 步骤1：准备数据

如果脚本无法自动运行，请手动执行以下操作：

1. 打开Caleb_data文件夹中的每个.txt文件
2. 复制所有以"Caleb："或"Caleb:"开头的行
3. 提取冒号后面的对话内容
4. 将所有内容粘贴到caleb_dialogues.txt文件中，每行一条对话

## 步骤2：运行分析

打开Python解释器（命令行中输入python），然后执行以下代码：

```python
from character_dialogue_analyzer import CharacterDialogueAnalyzer
analyzer = CharacterDialogueAnalyzer()

# 加载对话文件
analyzer.load_dialogues_from_file('caleb_dialogues.txt')

# 执行完整分析
analyzer.run_complete_analysis('caleb_dialogues.txt')
```

## 步骤3：查看结果

分析完成后，您可以在analysis_results文件夹中找到以下结果：

- wordcloud.png - 总体词云图
- positive_wordcloud.png - 积极词汇词云图
- negative_wordcloud.png - 消极词汇词云图
- 情感分析结果（控制台输出）
- 关键词提取结果（控制台输出）

## 步骤4：理解分析结果

1. **情感分析**：通过统计积极词和消极词的数量，判断Caleb对话的情感倾向
2. **词云分析**：直观展示Caleb对话中最常用的词汇
3. **关键词提取**：找出Caleb对话中的核心话题和重点内容

## 自定义分析（高级用户）

如需调整分析参数，可以修改character_dialogue_analyzer.py中的以下设置：

- 情感词典：可以扩展positive_words.txt和negative_words.txt
- 停用词：可以修改stopwords.txt
- 词云参数：可以调整WordCloud对象的参数（如字体、颜色、大小等）

## 常见问题

Q: 如果分析结果不准确怎么办？
A: 检查对话文件格式是否正确，确保每行只有一条对话

Q: 如何处理其他角色的对话？
A: 修改提取规则，将'Caleb'替换为其他角色名称

Q: 分析完成后没有生成词云图？
A: 确保已安装所需依赖：pip install jieba wordcloud matplotlib
"""
    
    # 保存指南文件
    with open("ANALYSIS_GUIDE.md", "w", encoding="utf-8") as f:
        f.write(guide_content)
    
    print("\n已创建详细的分析指南：ANALYSIS_GUIDE.md")
    
    # 提供基本的手动提取代码示例
    sample_code = '''
# 手动提取Caleb对话的代码示例
import os

caleb_data_dir = "Caleb_data"
output_file = "caleb_dialogues.txt"
caleb_dialogues = []

for filename in os.listdir(caleb_data_dir):
    if filename.endswith('.txt'):
        file_path = os.path.join(caleb_data_dir, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('Caleb：'):
                        content = line.split('：', 1)[1].strip()
                        caleb_dialogues.append(content)
                    elif line.startswith('Caleb:'):
                        content = line.split(':', 1)[1].strip()
                        caleb_dialogues.append(content)
        except Exception as e:
            print(f"读取文件 {filename} 时出错: {e}")

with open(output_file, 'w', encoding='utf-8') as f:
    for dialogue in caleb_dialogues:
        f.write(dialogue + '\n')

print(f"已提取 {len(caleb_dialogues)} 条Caleb的对话")
'''
    
    with open("manual_extraction_example.py", "w", encoding="utf-8") as f:
        f.write(sample_code)
    
    print("已创建手动提取代码示例：manual_extraction_example.py")
    print("\n总结：")
    print("1. 请查看ANALYSIS_GUIDE.md文件获取详细的分析步骤")
    print("2. 如果需要，可以使用manual_extraction_example.py中的代码手动提取对话")
    print("3. 提取完成后，按照指南中的Python代码运行分析")

if __name__ == "__main__":
    main()