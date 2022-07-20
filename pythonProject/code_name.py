# ddt模块包含了一个类的装饰器ddt和两个方法的装饰器
# 1、类装饰器：ddt
# 2、方法装饰器：data：包含多个你想要传给测试用例的参数
#             unpack：通常data中包含的每一个值都会作为一个单独的参数传给测试方法，
#             如果这些值是用元组或者列表传进来的，可以用unpack方法将其自动分解成多个参数
#
#

# import unittest
# from ddt import ddt,data,unpack
#通过ddt模块中的ddt类装饰器的方法对当前类进行装饰

# @ddt
# class MyTestCase1(unittest.TestCase):
#     @data(101,2222,3333)
#     def test_normal(self,value):
#         print(value)
#
# if __name__=='__main__':
#      unittest.main()



# import unittest
# import ddt
# import requests
#
# data_list = [
#     {"url": "https://cnodejs.org/api/v1/topics", "method": "get"},
#     {"url": "https://cnodejs.org/api/v1/topic/5433d5e4e737cbe96dcef312", "method": "get"},
#     {"url": "https://cnodejs.org/api/v1/topic_collect/collect", "method": "post"},
#     {"url": "https://cnodejs.org/api/v1/topic_collect/de_collect", "method": "post"},
#     {"url": "https://cnodejs.org/api/v1/user/alsotang", "method": "get"},
#     {"url": "https://cnodejs.org/api/v1/message/mark_all", "method": "post"},
# ]
#
#
# @ddt.ddt
# class MyCase(unittest.TestCase):
#
#     def get_response(self, item):
#         return requests.request(method=item['method'], url=item['url'])
#
#     @ddt.data(*data_list)
#     def test_case_01(self, item):
#         response = self.get_response(item)
#         print(response.status_code)
#         self.assertEqual(response.status_code, 200)
#
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)
#

# 传入元组、字典、列表等复杂结构数据，@data 装饰器结合 @unpack装饰器使用
# import unittest
# from ddt import ddt, data, unpack
#
#
# @ddt
# class MyTestCase2(unittest.TestCase):
#     # 元组
#     # @data((1, 2), (2, 3))
#     # @unpack
#     # def test_tuple(self, value1,value2):
#     #     print('test_tuple', value1,value2)
#
#     # 列表
#     @data([1, 2], [2, 3])
#     @unpack
#     def test_list(self, value1, value2):
#         print('test_list', value1, value2)
#     #
#     # # 字典
#     @data({'value1': 1, 'value2': 2}, {'value1': 2, 'value2': 3})
#     @unpack
#     def test_dict(self, value1, value2):
#         print('test_dict', value1, value2)
#
#
# if __name__ == '__main__':
#     unittest.main()


#
# from jsonpath_rw import parse
# #
# data = {'foo': [{'baz': 'news'}, {'baz': 'music'}]}
# match_list = parse('foo[*].baz').find(data)
# print(match_list)
# for k in match_list:
#     print(k.value)
# match_data = [v.value for v in match_list][0]
# print(match_data)
# data = {
#     "error_code": 0,
#     "stu_info": [
#         {
#             "id": 309,
#             "name": "小白",
#             "sex": "男",
#             "age": 28,
#             "addr": "河南省济源市北海大道32号",
#             "grade": "天蝎座",
#             "phone": "18512572946",
#             "gold": 100
#         },
#         {
#             "id": 310,
#             "name": "小白1",
#             "sex": "男",
#             "age": 28,
#             "addr": "河南省济源市北海大道32号",
#             "grade": "天蝎座",
#             "phone": "18516572946",
#             "gold": 100
#         }
#     ]
# }
#
# json_expr = parse('stu_info[-1].name')
# male = json_expr.find(data)
# print(male)
# for i in male:
#     print(i.value)
#
#



from bs4 import BeautifulSoup
import requests


def login():
    url = 'http://www.baidu.com'
    response = requests.request(method='get', url=url, )
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    return soup.find(name='title')


ret = login()
print(ret)
