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
que_par=Parser()
que_ans=Answer('http://localhost:7474','neo4j','123456')


#while True:
question=sys.argv[1]
res_cls=que_cls.main_cls(question)
res_par=que_par.parse_res(res_cls)
response=que_ans.get_answer(res_par)
print(response)
