import requests
import os
import sys
# sys.path.append(os.path.dirname(sys.path[0]))
from business import common
import allure
from business.logger import logger


@allure.feature('接口：get_topics')
class Test_topics:
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('这是一个接口测试')
    # @allure.attach("请求参数：{'page': 1,'tab': 'ask','limit': 3,'mdrender': 'true'}")
    @allure.issue("http://www.baidu.com", name="bug链接")
    @allure.story('get topics接口测试')
    @allure.description("这个用例为get请求")
    def test_get_topics(self):
        with allure.step("请求参数获取"):
            get_parma = {
                'page': 1,
                'tab': 'ask',
                'limit': 3,
                'mdrender': 'true'
            }
        allure.attach("<body>%s</body>" % get_parma, "请求参数", \
                      attachment_type=allure.attachment_type.HTML)
        with allure.step("发送请求"):
            res = requests.get(url=common.get_basic_info()[0] + '/topics', params=get_parma)
            logger.debug(f'发送请求结果:{res}')
        with allure.step("断言响应状态码"):
            assert 200 == res.status_code
            logger.debug(f'断言响应状态码:{res.status_code}')
        # with allure.step("断言id"):
        #     assert res.json()['data'][0]['id'] == '63fc57a4007208fe309e331e'
            logger.debug(f"断言id:{res.json()['data'][0]['id']}")
        with allure.step("断言响应码'limit'数量"):
            assert len(res.json()['data']) == get_parma['limit']
            logger.debug(f"断言响应码'limit'数量:{len(res.json()['data'])}")

    # def test_add_topics(self,get_basic_info):
    #     parmas = {
    #         'accesstoken': get_basic_info[1],
    #         'title': '接口测试',
    #         'tab': 'share',
    #         'content': '接口测试分享'
    #     }
    #     res = common.add_topics(parmas)
    #     assert res.status_code == 200
    #     assert res.json()['success'] == True
    #
    # def test_update_topics(self,get_basic_info):
    #     # 目前的实现方案是，新增和更新会创建两个topic
    #     # 我们的诉求是不会对系统造成垃圾数据
    #     # 所以这两个topic都需要删除
    #     # 我们可以通过fixture的teardown方法，去调用删除方法（fixture貌似也不行）
    #     # 因为如果增方法创建了一个topic，再使用fixture(内实现增方法)装饰一个更新topic方法，会另外创建一个topic
    #     # if不用fixture，删除方法也需要封装
    #     # 所以这里要结合具体的业务场景来看（比如删除接口），在UMI是没问题的
    #     parmas = {
    #         'accesstoken': get_basic_info[1],
    #         'title': '接口测试1',
    #         'tab': 'share',
    #         'content': '接口测试分享1'
    #     }
    #     id = common.add_topics(parmas).json()['topic_id']
    #     update_parmas= {
    #         'accesstoken': get_basic_info[1],
    #         'topic_id':id,
    #         'title': '接口测试',
    #         'tab': 'share',
    #         'content': '接口测试分享新'
    #     }
    #     res = requests.post(url=get_basic_info[0] + '/topics/update', params=update_parmas)
    #     assert res.json()['topic_id'] == id
    #     # 因为这里更新信息的响应结果，所以我们还需要封装一个get方法，通过传图topic_id来返回内容
    #     # 断言：
    #     # 如果我们发现，响应中的数据是类似'content':<div class='markdown-text'><p>接口测试分享新</p>\n</div>
    #     # 我们就可以使用assert in  方法
    #     # assert update_parmas['content'] in res.json()['data]['content']
