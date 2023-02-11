#!/usr/bin/env python
# coding: utf-8

# In[3]:


from py2neo import Graph
class Answer:
    def __init__(self,host_port,user,pwd):
        #创建连接对象
        self.graph=Graph(host_port,auth=(user,pwd))

    def get_answer(self, res_par):
        '''
        查询结果并生成对应话术
        :param res_par: [('白化病', 'symptom_part', 'match (a)-[r:表现]-(b) where a.name="白化病" return b.name')]
        :return:
        '''
        if res_par=='null':
            return '抱歉，暂时不能正确您的问题，请转接人工服务~'
        else:
            return '您可能患有的疾病为'+res_par

        '''
        response = ''
        for res in res_par:
            # 查询数据库
            sel_res = self.graph.run(res[2])
            data = sel_res.data()
            # print(data)
            if data:
                if res[1] == 'disease_part':
                    response += '{}可能是以下疾病的症状：'.format(res[0])
                    for i in data:
                        response += (i['b.name'] + ',')
                elif res[1] == 'symptom_part':
                    response += '{}可能有以下症状:'.format(res[0])
                    for i in data:
                        response += (i['b.name'] + ',')

            if response:
                return response
            else:
                return '抱歉，暂时不能正确您的问题，请转接人工服务~'
        '''






