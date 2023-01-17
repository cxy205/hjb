#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Parser:
    '''问题解析 生成sql'''
    def parse_res(self,res_cls):
        '''
        主函数
        :param res_cls: {'entities': {'白化病': 'disease'}, 'question_types': ['symptom_part']}
        :return:
        '''
        if not res_cls:
            #判断结果是否为空
            return []

        entities=res_cls['entities'].keys()
        question_types=res_cls['question_types']

        res=[]
        for entity in entities:
            for question_type in question_types:
                res.append((entity,question_type,self.get_sql(entity,question_type)))
        return res

    def get_sql(self,entity,question_type):
        '''根据实体和问题类型生成sql'''
        sql='match (a)-[r:表现]-(b) where a.name="{}" return b.name'.format(entity)
        return sql


