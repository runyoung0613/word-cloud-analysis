@echo off

echo ===============================
echo Caleb对话分析工具
 echo ===============================

REM 创建示例对话文件（如果不存在）
if not exist "caleb_dialogues.txt" (
    echo 创建示例对话文件...
    echo 你是我见过最特别的人。> caleb_dialogues.txt
    echo 今天的天气真好，我们出去走走吧。>> caleb_dialogues.txt
    echo 我很高兴能和你一起度过这段时光。>> caleb_dialogues.txt
    echo 谢谢你一直以来的陪伴和支持。>> caleb_dialogues.txt
    echo 我希望我们能一直这样在一起。>> caleb_dialogues.txt
    echo 有时候我会担心自己不够好，但有你在我就有信心了。>> caleb_dialogues.txt
)

echo 启动Python分析脚本...
python -c "
import os
print('正在加载对话分析器...')
try:
    from character_dialogue_analyzer import CharacterDialogueAnalyzer
    analyzer = CharacterDialogueAnalyzer()
    print('正在加载对话数据...')
    analyzer.load_dialogues_from_file('caleb_dialogues.txt')
    print('开始分析...')
    analyzer.run_complete_analysis('caleb_dialogues.txt')
    print('分析完成！结果保存在analysis_results文件夹中。')
except Exception as e:
    print('分析过程中出现错误:', str(e))
    print('请确保已安装所需依赖: pip install jieba wordcloud matplotlib')
input('按任意键退出...')
"