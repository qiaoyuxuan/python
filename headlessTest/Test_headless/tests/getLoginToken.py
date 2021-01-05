import unittest,requests,json,logging
from Test_headless.base import testRunMain
from Test_headless.base import setUrl


def get_token():  # 获取网点管家登录token接口
	get_url = setUrl.token_url()
	headers = {"Content-Type":"application/json;charset=UTF-8",
	           "token":"266d4a5a-bd27-4943-854f-6d63da0ceefe",
	           "channel":"WDGJ"}
	
	response = testRunMain.RunMain()  # 实例化类
	result = response.run_main("post",get_url,headers,"")  # 调用接口方法
	# result = json.loads(res)  # 接口返回的字符串转换为dict
	# print(type(result))
	if 'jwtToken' in result:
		get_jwt_token = result["jwtToken"]
		return get_jwt_token
	else:
		print('接口返回不存在jwtToken')

if __name__ == '__main__':
	try:
		print(get_token())
	except Exception as e:
		logging.exception(e)
