#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
游戏角色对话分析器
功能：分析游戏角色对话内容，生成情感词云，提取性格特征
作者：runyoung
版本：1.0
"""

import os
import re
import jieba
import jieba.analyse
import numpy as np
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from collections import Counter, defaultdict
import json
from datetime import datetime

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

class CharacterDialogueAnalyzer:
    def __init__(self):
        # 初始化情感词典和停用词
        self.stopwords = set()
        self.pos_words = set()
        self.neg_words = set()
        self.load_default_resources()
        
        # 初始化分析结果存储
        self.dialogues = []
        self.analysis_results = {}
        
        # 基础配置
        self.output_dir = "analysis_results"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def load_default_resources(self):
        """加载默认资源（停用词和简单情感词典）"""
        # 加载停用词
        default_stopwords = [
            '的', '了', '和', '是', '在', '有', '我', '他', '她', '它', '们',
            '这', '那', '你', '我', '他', '她', '它', '我们', '你们', '他们',
            '吗', '呢', '啊', '呀', '吧', '之', '乎', '者', '也', '而', '且',
            '但是', '因为', '所以', '如果', '就', '都', '不', '很', '非常',
            '可以', '能够', '应该', '必须', '就是', '一个', '这个', '那个'
        ]
        self.stopwords = set(default_stopwords)
        
        # 简单情感词典
        positive_words = [
            '好', '喜欢', '爱', '快乐', '高兴', '幸福', '优秀', '成功', '胜利',
            '坚强', '勇敢', '聪明', '善良', '美丽', '美好', '希望', '理想',
            '支持', '信任', '感谢', '谢谢', '太棒', '精彩', '伟大', '出色'
        ]
        
        negative_words = [
            '坏', '讨厌', '恨', '悲伤', '痛苦', '难过', '失败', '挫折', '困难',
            '生气', '愤怒', '失望', '绝望', '恐惧', '害怕', '担心', '焦虑',
            '拒绝', '反对', '怀疑', '背叛', '伤害', '危险', '可怕', '糟糕'
        ]
        
        self.pos_words = set(positive_words)
        self.neg_words = set(negative_words)
    
    def load_dialogues_from_file(self, file_path):
        """从文件加载对话数据"""
        try:
            # 根据文件扩展名选择不同的加载方式
            ext = os.path.splitext(file_path)[1].lower()
            
            if ext == '.txt':
                # 假设纯文本格式为每行一段对话
                with open(file_path, 'r', encoding='utf-8') as f:
                    self.dialogues = [line.strip() for line in f if line.strip()]
            elif ext == '.csv':
                # CSV格式，需要有'dialogue'列
                df = pd.read_csv(file_path, encoding='utf-8')
                if 'dialogue' in df.columns:
                    self.dialogues = df['dialogue'].tolist()
                else:
                    print("错误：CSV文件缺少'dialogue'列")
                    return False
            elif ext == '.json':
                # JSON格式，假设是对话列表
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        # 如果是对象列表，查找包含对话的字段
                        if all(isinstance(item, dict) for item in data):
                            # 尝试不同可能的对话字段名
                            dialogue_fields = ['dialogue', 'text', 'content', 'quote']
                            for field in dialogue_fields:
                                if all(field in item for item in data):
                                    self.dialogues = [item[field] for item in data]
                                    break
                            else:
                                print("错误：JSON对象列表中未找到标准对话字段")
                                return False
                        else:
                            # 假设是字符串列表
                            self.dialogues = [str(item) for item in data]
                    else:
                        print("错误：JSON文件格式不正确，应为列表")
                        return False
            else:
                print(f"错误：不支持的文件格式 {ext}")
                return False
            
            print(f"成功加载 {len(self.dialogues)} 条对话")
            return True
        except Exception as e:
            print(f"加载对话文件时出错：{str(e)}")
            return False
    
    def preprocess_text(self, text):
        """文本预处理"""
        # 去除特殊符号和多余空格
        text = re.sub(r'[\s+\n\t]', ' ', text)
        text = re.sub(r'[^一-龥a-zA-Z0-9\s]', '', text)
        text = text.strip()
        return text
    
    def segment_text(self, text):
        """中文分词"""
        # 使用jieba进行分词
        words = jieba.cut(text)
        # 过滤停用词
        words = [word for word in words if word and word not in self.stopwords]
        return words
    
    def analyze_sentiment(self, text, words=None):
        """简单情感分析"""
        if words is None:
            words = self.segment_text(text)
        
        # 统计情感词数量
        pos_count = sum(1 for word in words if word in self.pos_words)
        neg_count = sum(1 for word in words if word in self.neg_words)
        
        # 计算情感得分
        total_words = len(words)
        if total_words > 0:
            sentiment_score = (pos_count - neg_count) / total_words
        else:
            sentiment_score = 0
        
        # 判断情感倾向
        if sentiment_score > 0.1:
            sentiment = 'positive'
        elif sentiment_score < -0.1:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        
        return {
            'score': sentiment_score,
            'sentiment': sentiment,
            'positive_words': [word for word in words if word in self.pos_words],
            'negative_words': [word for word in words if word in self.neg_words]
        }
    
    def extract_keywords(self, top_k=20):
        """提取关键词"""
        if not self.dialogues:
            print("错误：没有对话数据可供分析")
            return []
        
        # 合并所有对话
        all_text = ' '.join([self.preprocess_text(d) for d in self.dialogues])
        
        # 使用TF-IDF提取关键词
        keywords = jieba.analyse.extract_tags(
            all_text, 
            topK=top_k, 
            withWeight=True,
            allowPOS=()
        )
        
        return keywords
    
    def generate_wordcloud(self, output_file="wordcloud.png", mask=None, 
                          sentiment_based=False, background_color='white'):
        """生成词云"""
        if not self.dialogues:
            print("错误：没有对话数据可供分析")
            return False
        
        try:
            # 合并所有对话并分词
            all_text = ' '.join([self.preprocess_text(d) for d in self.dialogues])
            words = self.segment_text(all_text)
            
            # 过滤后的词列表转为字符串
            text_for_wordcloud = ' '.join(words)
            
            # 创建词云对象
            wc = WordCloud(
                font_path='simhei.ttf',  # 中文字体
                background_color=background_color,
                max_words=200,
                mask=mask,
                contour_width=3,
                contour_color='steelblue'
            )
            
            # 生成词云
            wc.generate(text_for_wordcloud)
            
            # 保存词云图片
            output_path = os.path.join(self.output_dir, output_file)
            plt.figure(figsize=(10, 8))
            plt.imshow(wc, interpolation='bilinear')
            plt.axis("off")
            plt.tight_layout()
            plt.savefig(output_path, dpi=300)
            plt.close()
            
            print(f"词云已保存至：{output_path}")
            return True
        except Exception as e:
            print(f"生成词云时出错：{str(e)}")
            return False
    
    def generate_sentiment_wordclouds(self):
        """生成情感分层词云"""
        if not self.dialogues:
            print("错误：没有对话数据可供分析")
            return False
        
        try:
            # 分别收集积极、消极和中性词汇
            pos_words_all = []
            neg_words_all = []
            neu_words_all = []
            
            for dialogue in self.dialogues:
                processed_text = self.preprocess_text(dialogue)
                words = self.segment_text(processed_text)
                sentiment_result = self.analyze_sentiment(processed_text, words)
                
                # 分类词汇
                dialogue_pos_words = set(sentiment_result['positive_words'])
                dialogue_neg_words = set(sentiment_result['negative_words'])
                
                pos_words_all.extend(dialogue_pos_words)
                neg_words_all.extend(dialogue_neg_words)
                
                # 中性词：既不是积极也不是消极的词
                neu_words = [w for w in words if w not in dialogue_pos_words and w not in dialogue_neg_words]
                neu_words_all.extend(neu_words)
            
            # 生成积极词词云
            if pos_words_all:
                wc_pos = WordCloud(
                    font_path='simhei.ttf',
                    background_color='white',
                    colormap='RdYlGn',
                    max_words=100
                )
                wc_pos.generate(' '.join(pos_words_all))
                
                output_pos = os.path.join(self.output_dir, "positive_wordcloud.png")
                plt.figure(figsize=(8, 6))
                plt.imshow(wc_pos, interpolation='bilinear')
                plt.title("积极词汇词云")
                plt.axis("off")
                plt.savefig(output_pos, dpi=300)
                plt.close()
            
            # 生成消极词词云
            if neg_words_all:
                wc_neg = WordCloud(
                    font_path='simhei.ttf',
                    background_color='white',
                    colormap='RdYlGn_r',
                    max_words=100
                )
                wc_neg.generate(' '.join(neg_words_all))
                
                output_neg = os.path.join(self.output_dir, "negative_wordcloud.png")
                plt.figure(figsize=(8, 6))
                plt.imshow(wc_neg, interpolation='bilinear')
                plt.title("消极词汇词云")
                plt.axis("off")
                plt.savefig(output_neg, dpi=300)
                plt.close()
            
            # 生成中性词词云
            if neu_words_all:
                wc_neu = WordCloud(
                    font_path='simhei.ttf',
                    background_color='white',
                    colormap='viridis',
                    max_words=100
                )
                wc_neu.generate(' '.join(neu_words_all))
                
                output_neu = os.path.join(self.output_dir, "neutral_wordcloud.png")
                plt.figure(figsize=(8, 6))
                plt.imshow(wc_neu, interpolation='bilinear')
                plt.title("中性词汇词云")
                plt.axis("off")
                plt.savefig(output_neu, dpi=300)
                plt.close()
            
            print("情感分层词云已生成")
            return True
        except Exception as e:
            print(f"生成情感词云时出错：{str(e)}")
            return False
    
    def analyze_character_traits(self):
        """分析角色性格特征（基于词汇使用）"""
        if not self.dialogues:
            print("错误：没有对话数据可供分析")
            return {}
        
        # 合并所有对话并分词
        all_text = ' '.join([self.preprocess_text(d) for d in self.dialogues])
        words = self.segment_text(all_text)
        
        # 计算词频
        word_freq = Counter(words)
        
        # 简单性格特质推断（基于关键词）
        traits = {
            '外倾性': 0,
            '神经质': 0,
            '开放性': 0,
            '宜人性': 0,
            '责任心': 0
        }
        
        # 性格相关词汇词典（简化版）
        trait_keywords = {
            '外倾性': ['朋友', '大家', '一起', '分享', '快乐', '交流', '热情', '聚会'],
            '神经质': ['担心', '害怕', '焦虑', '紧张', '不安', '恐惧', '烦躁', '压力'],
            '开放性': ['新的', '想法', '创新', '探索', '好奇', '学习', '尝试', '发现'],
            '宜人性': ['帮助', '理解', '支持', '关心', '善良', '友好', '合作', '感谢'],
            '责任心': ['必须', '应该', '责任', '完成', '认真', '努力', '坚持', '承诺']
        }
        
        # 计算各特质得分
        total_words = len(words)
        for trait, keywords in trait_keywords.items():
            trait_count = sum(word_freq.get(keyword, 0) for keyword in keywords)
            traits[trait] = trait_count / total_words if total_words > 0 else 0
        
        # 转换为百分比
        for trait in traits:
            traits[trait] = round(traits[trait] * 100, 2)
        
        # 生成性格分析报告
        report = {
            'word_frequency': dict(word_freq.most_common(20)),
            'traits': traits,
            'summary': self._generate_trait_summary(traits)
        }
        
        return report
    
    def _generate_trait_summary(self, traits):
        """根据性格特质生成总结"""
        summary = "角色性格分析：\n"
        
        # 找出得分最高的特质
        max_trait = max(traits.items(), key=lambda x: x[1])
        
        if max_trait[0] == '外倾性' and max_trait[1] > 1.5:
            summary += "该角色性格外向，善于社交，喜欢与他人互动和分享。\n"
        elif max_trait[0] == '神经质' and max_trait[1] > 1.5:
            summary += "该角色情绪较为敏感，容易焦虑或紧张，对周围环境变化反应强烈。\n"
        elif max_trait[0] == '开放性' and max_trait[1] > 1.5:
            summary += "该角色思想开放，富有好奇心，乐于探索新事物和接受新观念。\n"
        elif max_trait[0] == '宜人性' and max_trait[1] > 1.5:
            summary += "该角色性格温和友善，善于理解和帮助他人，注重人际关系和谐。\n"
        elif max_trait[0] == '责任心' and max_trait[1] > 1.5:
            summary += "该角色做事认真负责，有强烈的责任感和使命感，重视承诺和义务。\n"
        else:
            summary += "该角色性格较为平衡，没有特别突出的特质倾向。\n"
        
        # 添加其他特质的说明
        if traits['外倾性'] > 1.0:
            summary += "角色在社交场合表现活跃，喜欢与人交流。\n"
        if traits['宜人性'] > 1.0:
            summary += "角色展现出较高的同理心和合作意愿。\n"
        if traits['责任心'] > 1.0:
            summary += "角色对待任务认真负责，注重完成质量。\n"
        if traits['开放性'] > 1.0:
            summary += "角色对新体验持开放态度，有较强的学习能力。\n"
        if traits['神经质'] > 1.0:
            summary += "角色情绪波动较大，可能容易受到外界影响。\n"
        
        return summary
    
    def run_complete_analysis(self, file_path):
        """运行完整的分析流程"""
        print("========== 开始游戏角色对话分析 ==========")
        
        # 1. 加载数据
        print("\n[1/5] 正在加载对话数据...")
        if not self.load_dialogues_from_file(file_path):
            print("分析终止：无法加载对话数据")
            return False
        
        # 2. 基础统计
        print("\n[2/5] 正在生成基础统计...")
        total_dialogues = len(self.dialogues)
        total_chars = sum(len(d) for d in self.dialogues)
        avg_length = total_chars / total_dialogues if total_dialogues > 0 else 0
        
        print(f"对话总数：{total_dialogues}")
        print(f"总字符数：{total_chars}")
        print(f"平均对话长度：{avg_length:.2f} 字符")
        
        # 3. 情感分析
        print("\n[3/5] 正在进行情感分析...")
        sentiment_results = []
        for dialogue in self.dialogues[:10]:  # 只分析前10条作为示例
            sentiment = self.analyze_sentiment(dialogue)
            sentiment_results.append(sentiment)
        
        # 统计整体情感倾向
        sentiments = [s['sentiment'] for s in sentiment_results]
        sentiment_counts = Counter(sentiments)
        
        print("情感分布示例（前10条）：")
        for sentiment, count in sentiment_counts.items():
            print(f"  {sentiment}: {count}")
        
        # 4. 生成词云
        print("\n[4/5] 正在生成词云...")
        self.generate_wordcloud("character_wordcloud.png")
        self.generate_sentiment_wordclouds()
        
        # 5. 性格分析
        print("\n[5/5] 正在分析性格特征...")
        trait_analysis = self.analyze_character_traits()
        
        print("\n性格特质得分：")
        for trait, score in trait_analysis['traits'].items():
            print(f"  {trait}: {score}%")
        
        print("\n性格分析总结：")
        print(trait_analysis['summary'])
        
        # 保存分析结果
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        results_file = os.path.join(self.output_dir, f"analysis_results_{timestamp}.json")
        
        full_results = {
            'basic_stats': {
                'total_dialogues': total_dialogues,
                'total_characters': total_chars,
                'avg_dialogue_length': avg_length
            },
            'sentiment_analysis': sentiment_counts,
            'character_traits': trait_analysis,
            'keywords': self.extract_keywords(),
            'timestamp': datetime.now().isoformat()
        }
        
        with open(results_file, 'w', encoding='utf-8') as f:
            json.dump(full_results, f, ensure_ascii=False, indent=2)
        
        print(f"\n分析结果已保存至：{results_file}")
        print("\n========== 分析完成 ==========")
        
        return True


def main():
    """主函数"""
    print("游戏角色对话分析器")
    print("====================")
    
    analyzer = CharacterDialogueAnalyzer()
    
    # 这里可以根据需要修改为实际的对话文件路径
    # 示例：假设我们有一个游戏角色对话的文本文件
    sample_file = "game_character_dialogues.txt"
    
    # 检查示例文件是否存在，如果不存在则创建示例
    if not os.path.exists(sample_file):
        print(f"未找到示例文件 {sample_file}，正在创建示例对话...")
        
        # 创建示例对话内容
        sample_dialogues = [
            "我一定会保护大家的安全，这是我的责任。",
            "不用担心，一切都会好起来的。让我们一起面对困难。",
            "为什么会这样？我明明已经很努力了...",
            "这个世界充满了未知的可能性，我想去探索每一个角落。",
            "朋友是最珍贵的财富，我愿意为他们付出一切。",
            "失败并不可怕，重要的是我们能够从中学习和成长。",
            "我感到很害怕，但我不能退缩，因为还有人需要我。",
            "创新的想法往往来自于勇敢的尝试，让我们试试新方法。",
            "谢谢你一直以来的支持和理解，有你在真好。",
            "我必须完成这个任务，无论遇到多大的挑战。"
        ]
        
        with open(sample_file, 'w', encoding='utf-8') as f:
            for dialogue in sample_dialogues:
                f.write(dialogue + '\n')
        
        print(f"示例文件已创建：{sample_file}")
    
    # 运行完整分析
    analyzer.run_complete_analysis(sample_file)
    
    print("\n提示：")
    print("1. 请将你的游戏角色对话保存为TXT、CSV或JSON格式")
    print("2. 修改代码中的sample_file变量指向你的对话文件")
    print("3. 分析结果将保存在analysis_results文件夹中")
    print("4. 你可以通过扩展情感词典来提高分析准确性")


if __name__ == "__main__":
    main()