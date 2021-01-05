# base：基础代码，封装底层的代码、公共类等
    method：封装接口调用方法，支持post、get、put、delete，返回接口响应参数
# common：公共的方法
    public
        filePath：获取文件路径，返回指定文件路径
    getFixture：返回yaml文件数据
# config：配置文件，yaml文件等

# data：驱动数据，csv、xls等
    terms_submit.yaml：新增条款
    terms_modify.yaml：修改条款
    terms_queryByPage.yaml：获取条款列表


# log:日志
# report：测试报告
# tests：测试用例
    test_terms.py：条款相关用例

# utils：公共类
# conftest.py：公共方法