import os

# 简单的文件路径设置
input_dir = "Caleb_data"
output_file = "caleb_dialogues.txt"

# 直接读取并提取对话
caleb_lines = []

try:
    # 获取所有txt文件
    files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]
    
    for filename in files:
        file_path = os.path.join(input_dir, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('Caleb：') or line.startswith('Caleb:'):
                    # 提取对话内容
                    if '：' in line:
                        content = line.split('：', 1)[1].strip()
                    else:
                        content = line.split(':', 1)[1].strip()
                    # 排除非对话内容
                    if content and 'jpg' not in content:
                        caleb_lines.append(content)
    
    # 写入结果文件
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in caleb_lines:
            f.write(line + '\n')
    
    # 创建一个简单的README说明如何使用character_dialogue_analyzer
    with open("ANALYSIS_INSTRUCTIONS.md", 'w', encoding='utf-8') as f:
        f.write("# Caleb对话分析使用指南\n\n")
        f.write("## 1. 数据准备\n")
        f.write("已从Caleb_data文件夹中提取了Caleb的对话，保存在`caleb_dialogues.txt`文件中\n\n")
        f.write("## 2. 运行分析\n")
        f.write("打开Python解释器，执行以下代码：\n\n")
        f.write("```python\n")
        f.write("from character_dialogue_analyzer import CharacterDialogueAnalyzer\n")
        f.write("analyzer = CharacterDialogueAnalyzer()\n")
        f.write("analyzer.load_dialogues_from_file('caleb_dialogues.txt')\n")
        f.write("analyzer.run_complete_analysis('caleb_dialogues.txt')\n")
        f.write("```\n\n")
        f.write("## 3. 查看结果\n")
        f.write("分析结果将保存在`analysis_results`文件夹中：\n")
        f.write("- 总体词云: wordcloud.png\n")
        f.write("- 积极词汇词云: positive_wordcloud.png\n")
        f.write("- 消极词汇词云: negative_wordcloud.png\n")
        f.write("- 情感分析结果和关键词提取\n\n")
        f.write("## 4. 自定义分析\n")
        f.write("如需自定义分析参数，可以修改`character_dialogue_analyzer.py`文件中的相关设置。")
    
    print(f"已成功提取 {len(caleb_lines)} 条Caleb的对话")
    print(f"请查看ANALYSIS_INSTRUCTIONS.md文件获取详细使用指南")
    
except Exception as e:
    print(f"发生错误: {e}")