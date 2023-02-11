#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# In[4]:

import sys
import io
#sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encodeing='utf-8')
sys.stdin=io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8')
from question_classify import QClassifier
from question_parser import Parser
from question_answer import Answer
#问题分类
que_cls = QClassifier('/data/disease.txt', '/data/symptom.txt')
que_par=Parser('http://localhost:7474','neo4j','123456')
que_ans=Answer('http://localhost:7474','neo4j','123456')


#while True:
question=sys.argv[1]
#question="脸上常出现痘痘,痤疮,粉刺"
#question="白化病是什么病"
res_cls=que_cls.main_cls(question)
#print(res_cls)
res_par=que_par.parse_res(res_cls)
#print(res_par)
response=que_ans.get_answer(res_par)
print(response)
