#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Caleb对话分析自动化脚本
功能：处理Caleb_data文件夹中的对话文件，提取Caleb的对话并进行分析
作者：runyoung
版本：1.0
"""

import os
import re
import sys
from character_dialogue_analyzer import CharacterDialogueAnalyzer

def extract_caleb_dialogues(input_folder, output_file):
    """
    从对话文件中提取Caleb的对话
    
    参数:
    input_folder: 包含对话文件的文件夹路径
    output_file: 输出文件路径，用于保存Caleb的对话
    
    返回:
    int: 提取的对话数量
    """
    caleb_dialogues = []
    
    # 遍历文件夹中的所有txt文件
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            file_path = os.path.join(input_folder, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    
                    for line in lines:
                        line = line.strip()
                        if not line:
                            continue
                            
                        # 匹配Caleb的对话行，考虑不同的冒号格式和大小写
                        caleb_patterns = [
                            r'^Caleb[：:]\s*(.+)',
                            r'^caleb[：:]\s*(.+)',
                            r'^CALEB[：:]\s*(.+)'
                        ]
                        
                        match = None
                        for pattern in caleb_patterns:
                            match = re.match(pattern, line)
                            if match:
                                break
                        
                        if match:
                            dialogue = match.group(1).strip()
                            # 排除非对话内容（如"思考.jpg"等）
                            if dialogue and not any(x in dialogue.lower() for x in ['jpg', 'png', '图片']):
                                caleb_dialogues.append(dialogue)
                                print(f"从{filename}中提取: {dialogue}")
                                
            except Exception as e:
                print(f"读取文件{filename}时出错: {str(e)}")
    
    # 保存提取的对话
    with open(output_file, 'w', encoding='utf-8') as f:
        for dialogue in caleb_dialogues:
            f.write(dialogue + '\n')
    
    print(f"已提取 {len(caleb_dialogues)} 条Caleb的对话")
    print(f"保存到文件: {output_file}")
    return len(caleb_dialogues)

def analyze_caleb_dialogues(dialogues_file):
    """
    使用CharacterDialogueAnalyzer分析Caleb的对话
    
    参数:
    dialogues_file: 包含Caleb对话的文件路径
    """
    try:
        # 创建分析器实例
        analyzer = CharacterDialogueAnalyzer()
        
        # 加载对话文件
        print("\n开始加载Caleb的对话...")
        success = analyzer.load_dialogues_from_file(dialogues_file)
        
        if not success:
            print("加载对话失败，请检查文件格式")
            return False
        
        # 执行完整分析
        print("\n开始进行对话分析...")
        analyzer.run_complete_analysis(dialogues_file)
        
        print("\n分析完成！")
        print(f"分析结果保存在: {analyzer.output_dir} 文件夹中")
        return True
        
    except Exception as e:
        print(f"分析过程中出错: {str(e)}")
        return False

def main():
    """
    主函数
    """
    print("Caleb对话分析自动化脚本 v1.0")
    print("================================\n")
    
    # 设置文件夹和文件路径
    caleb_data_folder = "Caleb_data"
    caleb_dialogues_file = "caleb_dialogues.txt"
    
    # 确保路径存在
    if not os.path.exists(caleb_data_folder):
        print(f"错误：找不到文件夹 {caleb_data_folder}")
        return 1
    
    # 提取Caleb的对话
    print(f"从{caleb_data_folder}文件夹中提取Caleb的对话...\n")
    dialogue_count = extract_caleb_dialogues(caleb_data_folder, caleb_dialogues_file)
    
    if dialogue_count == 0:
        print("没有提取到任何Caleb的对话，请检查文件格式")
        return 1
    
    # 分析Caleb的对话
    print("\n开始分析Caleb的对话情感和生成词云...")
    analyze_caleb_dialogues(caleb_dialogues_file)
    
    print("\n完整工作流程执行完毕！")
    print("你现在可以查看以下内容：")
    print("1. 提取的Caleb对话: caleb_dialogues.txt")
    print("2. 分析结果和词云: analysis_results文件夹")
    print("   - 总体词云: wordcloud.png")
    print("   - 积极词汇词云: positive_wordcloud.png")
    print("   - 消极词汇词云: negative_wordcloud.png")
    print("\n提示：如果需要调整分析参数，可以修改character_dialogue_analyzer.py中的相关设置")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())