#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''意识实体识别'''

import ahocorasick
import sys
import os

class QClassifier:

    def __init__(self, disease_path, symptom_path):

        self.disease_path = disease_path
        self.symptom_path = symptom_path

        # 获取特征词典和特征词
        self.wdtype_dic, self.feature_words = self.build_wdtype(self.disease_path, self.symptom_path)


        # 构建actree
        self.actree = self.build_actree(self.feature_words)
        #print("1")

        # 定义问题模板：某某疾病有某某症状，某某症状是某某病
        self.belongs_ques = ['属于什么病', '是什么病', '有什么病', '哪个病', '什么病', '什么问题']
        self.symptom_ques = ['有什么症状', '会怎么样', '会怎样', '症状是什么', '病症是什么', '有啥症状']

    # acTree
    def build_actree(self, feature_words):
        actree = ahocorasick.Automaton()
        for index, word in enumerate(feature_words):
            actree.add_word(word, (index, word))
        actree.make_automaton()
        return actree

    def build_feature_dic(self, path):
        '''
        构建实体词典
        :param path:
        :return:
        '''
        curPath = os.path.abspath(os.path.dirname(__file__))
        rootPath = os.path.split(curPath)[0]
        rootPath=rootPath.replace('\\', '/');
        path=rootPath+path
        with open(path, 'r', encoding='utf8') as f:
            #print("3")
            # 去除实体两端空格
            words = [_.strip() for _ in f.readlines() if _.strip()]
        return words

    def build_wdtype(self, disease_path, symptom_path):
        '''
        \建立实体label字典 {‘山药’：‘中药’}
        :param disease_path:
        :param symptom_path:
        :return:
        '''
        res = {}
        feature_words = []

        # 读取疾病名称
        disease = self.build_feature_dic(disease_path)
        feature_words.extend(disease)
        disease = {_: 'disease' for _ in disease}


        symptom = self.build_feature_dic(symptom_path)
        feature_words.extend(symptom)
        symptom = {_: 'symptom' for _ in symptom}

        res.update(disease)
        res.update(symptom)

        return res, feature_words

    def check_entity(self, question):
        '''
        检测问句中的实体
        :param question:
        :return:
        '''
        entities = []
        for i in self.actree.iter(question):
            entities.append(i[1][1])
        # 取最大匹配
        remove_words = []
        for wd1 in entities:
            for wd2 in entities:
                if wd1 in wd2 and wd1 != wd2:
                    remove_words.append(wd1);
        final_words = [i for i in entities if i not in remove_words]
        sym_dic = [i for i in final_words if i in self.feature_words]
        return sym_dic

    def detect_type(self, question_words, question):
        '''
        判断问题类别
        :param question_qords:
        :param question:
        :return:
        '''
        for word in question_words:
            if word in question:
                return True
        return False

    def main_cls(self, question):
        '''
        主函数
        :param question: 用户问题
        :return:
        '''
        # 检测文问句中的实体
        sym_dic = self.check_entity(question)
        return sym_dic
        # 获取问题类型
        #question_types = []
        # 判断是否在范围内
        #if (self.detect_type(self.belongs_ques, question)):
            #question_types.append('disease_part')
        #if (self.detect_type(self.symptom_ques, question)):
           # question_types.append('symptom_part')

        #if medical_dic and question_types:
        #return {'entities': medical_dic, 'question_types': question_types}
