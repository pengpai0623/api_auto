### 代码结构
config ===========> 配置文件

data ===========> 测试数据管理

testcase ===========> 主要存放自动化测试用例

business ===========> 公共方法封装，工具类等

pytest.ini ==========> pytest的主配置文件，可以改变pytest的默认行为，如运行方式，默认执行用例路径，用例收集规则，定义标记等

log ==========> 日志文件

report ==========> 测试报告

conftest.py ============> 存放测试执行的一些fixture配置，实现环境初始化、数据共享以及环境还原等

requirements.txt ============> 相关依赖包文件

main.py =============> 测试用例总执行器

RunTest_windows.bat ============> 测试启动按钮

test:test_branch
