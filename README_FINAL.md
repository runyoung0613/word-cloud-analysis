# Caleb对话分析项目

## 项目概述

本项目旨在分析Caleb角色的对话内容，进行情感分析并生成词云图，帮助用户更好地理解Caleb的性格特点和情感倾向。

## 文件结构

- `Caleb_data/` - 存放Caleb对话的原始文件
- `character_dialogue_analyzer.py` - 主要分析工具，包含对话处理、情感分析和词云生成功能
- `caleb_dialogues.txt` - 提取的Caleb对话内容（将由脚本生成）
- `run_analysis.bat` - 一键运行分析的批处理文件
- `README_FINAL.md` - 项目说明文档
- `ANALYSIS_GUIDE.md` - 详细的分析操作指南
- `manual_extraction_example.py` - 手动提取对话的代码示例

## 快速开始

### 方法一：一键运行（推荐）

1. 双击运行 `run_analysis.bat` 文件
2. 程序会自动检查并创建示例对话文件
3. 运行分析并生成词云图
4. 结果将保存在 `analysis_results` 文件夹中

### 方法二：手动分析

1. **准备对话数据**：
   - 打开 `Caleb_data` 文件夹中的每个.txt文件
   - 复制所有以"Caleb："或"Caleb:"开头的行
   - 提取冒号后面的对话内容
   - 将所有内容粘贴到 `caleb_dialogues.txt` 文件中，每行一条对话

2. **运行分析**：
   - 打开命令提示符（CMD）
   - 切换到项目目录：`cd e:\Word_cloud_analysis`
   - 输入 `python` 进入Python解释器
   - 执行以下代码：
     ```python
     from character_dialogue_analyzer import CharacterDialogueAnalyzer
     analyzer = CharacterDialogueAnalyzer()
     analyzer.load_dialogues_from_file('caleb_dialogues.txt')
     analyzer.run_complete_analysis('caleb_dialogues.txt')
     ```

## 分析结果

分析完成后，您可以在 `analysis_results` 文件夹中找到以下结果：

- `wordcloud.png` - 总体词云图，显示Caleb最常用的词汇
- `positive_wordcloud.png` - 积极词汇词云图，展示表达积极情感的词汇
- `negative_wordcloud.png` - 消极词汇词云图，展示表达消极情感的词汇
- 控制台输出中还包含：
  - 情感分析结果（积极度、消极度、中性度）
  - 关键词提取结果（TF-IDF方法）

## 技术细节

### 支持的文件格式

`character_dialogue_analyzer.py` 支持以下格式的对话文件：

1. **TXT格式**：每行一条对话
2. **CSV格式**：需要包含'dialogue'列
3. **JSON格式**：支持多种字段名称，如'dialogue'、'text'、'content'、'quote'

### 情感分析原理

情感分析基于简单的情感词典匹配：

1. 系统内置了积极词汇和消极词汇词典
2. 对每个对话进行分词处理
3. 统计积极词和消极词的数量
4. 计算情感得分：(积极词数 - 消极词数) / 总词数
5. 根据得分判断情感倾向：积极、消极或中性

### 词云生成

词云生成使用了wordcloud库，主要步骤：

1. 对所有对话进行分词和停用词过滤
2. 统计词频
3. 设置词云参数（颜色、形状、字体等）
4. 生成并保存词云图片

## 自定义与扩展

### 扩展情感词典

您可以修改以下文件来扩展情感词典：
- `positive_words.txt` - 添加更多积极词汇
- `negative_words.txt` - 添加更多消极词汇

### 修改停用词

可以编辑 `stopwords.txt` 文件，添加或删除不需要在词云中显示的常用词。

### 调整词云参数

如需修改词云的外观，可以在 `character_dialogue_analyzer.py` 文件中调整WordCloud对象的参数。

## 常见问题解答

### 问题1：运行脚本时出现错误

解决方案：确保已安装所有必要的依赖包
```
pip install jieba wordcloud matplotlib
```

### 问题2：词云图中没有显示中文字符

解决方案：可能是缺少中文字体，您可以在WordCloud初始化时指定字体路径。

### 问题3：如何分析其他角色的对话

解决方案：修改提取规则，将'Caleb'替换为其他角色名称。

## 总结

本项目提供了一个完整的解决方案，可以帮助您分析Caleb角色的对话内容，通过情感分析和词云图直观地展示分析结果。无论您是选择一键运行还是手动分析，都能轻松获得有价值的分析结果。

祝您使用愉快！