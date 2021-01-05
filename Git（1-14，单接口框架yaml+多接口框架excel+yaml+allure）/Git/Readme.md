# base：基础代码，封装底层的代码、公共类等
    method：封装接口调用方法，支持post、get、put、delete，返回接口响应参数
# common：公共的方法
    public-filePath：获取文件路径，返回指定文件路径
# config：配置文件，yaml文件等
    apiFlowCase_001.yaml：多接口测试，对应到apiFlowCase001.xls中“请求参数”列，是其详细参数
    config.yaml：
# data：驱动数据，csv、xls等
    apiFlowCase001.xls：多接口测试，业务流程所需的api信息，其“请求参数”只是个名称，需映射到apiFlowCase_001.yaml文件中获取详细参数
    login.yaml：单接口测试请求参数（登陆接口）
    returnData.json：代码中生成的文件，用于临时存放token等用于传递的参数
# log:日志
# report：测试报告
# tests：测试用例
    test_getLoginToken：单接口测试用例，获取登陆token
    test_apiFlowCase001：多接口流程测试用例，使用的驱动数据：apiFlowCase001.xls、apiFlowCase_001.yaml
# utils：公共类
    operationExcel：读取excel文件（只适用于apiFlowCase001.xls文档格式，读取业务流程所需api信息和映射到config/apiFlowCase_xxx.yaml中的请求参数），
                    根据不同方法返回某列的指定行的单元格数据
    operationYaml：读取yaml文件，返回yaml文件内容，返回类型支持list和dict类型