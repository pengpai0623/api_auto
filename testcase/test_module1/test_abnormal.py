import pytest
import requests
import json
from business import common
from business.logger import logger
import allure

# test_data1 = [
#     {'page': 1, 'tab': 'share', 'limit': 3, 'mdrender': 'true'},
#     {'page': 1, 'tab': 'ask', 'limit': 0, 'mdrender': 'false'},
#     {'page': 0, 'tab': 'ask', 'limit': 3, 'mdrender': 'true'}
# ]
# test_data1 = [
#     [{'page': 1, 'tab': 'share', 'limit': 1, 'mdrender': 'true'}, 'share', 200]
#     # ({'page': 1, 'tab': 'ask', 'limit': 0, 'mdrender': 'false'}),
#     # ({'page': 0, 'tab': 'ask', 'limit': 3, 'mdrender': 'true'})
# ]

@allure.feature('get topics接口异常处理测试')
class Test_topics:
    # 使用json格式
    # @pytest.mark.parametrize('get_parma,tab,status_code', common.get_json_data())
    # def test_get_topics(self, get_basic_info, get_parma, tab, status_code):
    #     res = requests.get(url=get_basic_info[0] + '/topics', params=get_parma)
    #     assert res.status_code == status_code
    #     assert res.json()['data'][0]['tab'] == tab

    # 使用csv格式
    @allure.story("get topics接口异常处理测试")
    @pytest.mark.parametrize('url,method,test_data,status_code,tab', common.get_csv_data())
    def test_get_topics(self, url, method, test_data, status_code, tab):
        res = requests.get(url, params=json.loads(test_data))
        logger.debug(f'发送获取topic请求:{res}')
        assert res.status_code == status_code
        logger.debug(f'断言status_code:{res.status_code == status_code}')
        assert res.json()['data'][0]['tab'] == json.loads(tab)
        logger.debug(f"断言响应tab值:{res.json()['data'][0]['tab'] == json.loads(tab)}")
        # assert 1 == 2
        # logger.debug(f"断言1 == 2:{1 == 2}")


