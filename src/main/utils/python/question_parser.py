#!/usr/bin/env python
# coding: utf-8
from py2neo import Node,Relationship,Graph,NodeMatcher


# In[ ]:


class Parser:
    '''问题解析 生成sql'''
    def __init__(self,host_port,user,pwd):
        #创建连接对象
        self.graph=Graph(host_port,auth=(user,pwd))

    def parse_res(self,res_cls):
        '''
        主函数
        :param res_cls: {'entities': {'白化病': 'disease'}, 'question_types': ['symptom_part']}
        :return:
        '''
        if not res_cls:
            #判断结果是否为空
            return []

        entities=res_cls
        #question_types=res_cls['question_types']

        res=[]
        '''
                for entity in entities:
            for question_type in question_types:
                res.append((entity,question_type,self.get_sql(entity,question_type)))
        return res
        '''
        part_node = Node('疾病', name='mydis')
        self.graph.create(part_node)
        for entity in entities:
            symptom_node = Node('症状', name=entity)
            self.graph.create(symptom_node)
            res = self.graph.run(
                'match p=(a:疾病)-[r:表现]->(b:症状) where a.name="{}" and b.name="{}" return count(p)'.format('mydis',entity))
            if res.data()[0]['count(p)'] == 0:
                self.graph.run(
                    'match (a:疾病),(b:症状) where a.name="{}" and b.name="{}" create (a)-[r:{}]->(b) return r'.format('mydis',entity, '表现'))

        res=self.graph.run('MATCH (p1:疾病{name:"mydis"})-[r:表现]->(sym1) WITH p1, collect(id(sym1)) AS p1Sym MATCH (p2:疾病)-[r:表现]->(sym2) WHERE p1 <> p2 WITH p1, p1Sym, p2, collect(id(sym2)) AS p2Sym RETURN p1.name AS from, p2.name AS to, gds.alpha.similarity.jaccard(p1Sym, p2Sym) AS similarity ORDER BY to, similarity DESC limit 1')
        r = res.data('to')
        '''
        self.graph.run(
            'MATCH(r) WHERE id(r) = 493 DETACH DELETE r')
        '''

        self.graph.run(
            'MATCH(n: 疾病{name: "mydis"}) DETACH delete n')


        if r:
            r = r[0]['to']
            return r
        else:
            return 'null'

    def get_sql(self,entity,question_type):
        '''根据实体和问题类型生成sql'''
        sql='match (a)-[r:表现]-(b) where a.name="{}" return b.name'.format(entity)
        return sql


