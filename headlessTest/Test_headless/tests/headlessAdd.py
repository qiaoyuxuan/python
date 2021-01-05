#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
2020/11/5 16:47   乔誉萱
说明：无着件上报，读取csv文件数据实现上报，将上报结果放入list并返回
:param token：登陆token
'''
from Test_headless.base import testRunMain,setUrl,readFile,headers
from Test_headless.tests import getLoginToken
import json,logging,unittest,xlutils,xlrd,os,csv


class HeadlessAdd(object):
	def __init__(self,token):
		self.token = token
	
	def read_csv(self):
		'''调用csv文件读取方法，方法返回读取内容，类型list'''
		rf_obj = readFile.ReadFile('headlessAdd.csv')
		return rf_obj.main_read()
	
	# get_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'datas/headlessAdd.csv')
	# get_path = get_path.replace('\\','/')  # 解决路径中出现//双斜杠的问题
	# csv_obj = getCsv.GetCsv(get_path)
	# getlist = csv_obj.read_file()
	# return getlist
	
	def headless_Add(self):
		'''上报无着件'''
		get_url = setUrl.add_url()  # 获取接口地址
		getlist = self.read_csv()  # 获取csv文件数据
		result = []  # 存放上报无着件后的返回结果
		response = testRunMain.RunMain()  # 实例化接口类
		get_hearder = headers.get_headers() # 调用获取请求头方法
		for item in getlist:
			set_dict = {"headlessType":item['headlessType'],
			            "findPlace":item['findPlace'],
			            "outsidePackageId":item['outsidePackageId'],
			            "insidePackageId":item['insidePackageId'],
			            "linePosition":item['linePosition'],
			            "singleSurfaceInfo":{"residualWaybillNo":item['residualWaybillNo'],
			                                 "threeCode":item['threeCode'],
			                                 "senderProvince":item['senderProvince'],
			                                 "senderCity":item['senderCity'],
			                                 "senderArea":item['senderArea'],
			                                 "senderAddress":item['senderAddress'],
			                                 "senderName":item['senderName'],
			                                 "senderPhone":item['senderPhone'],
			                                 "receiverProvince":item['receiverProvince'],
			                                 "receiverCity":item['receiverCity'],
			                                 "receiverArea":item['receiverArea'],
			                                 "receiverAddress":item['receiverAddress'],
			                                 "receiverName":item['receiverName'],
			                                 "receiverPhone":item['receiverPhone']},
			            "qty":item['qty'],
			            "weight":item['weight'],
			            "pics":item['pics'],
			            "itemCharacter":item['itemCharacter'],
			            "suspectedStation":{"value":item['suspectedStation_value'],
			                                "name":item['suspectedStation_name']},
			            "picsList":[item['picsList']],
			            "indexPic":[item['indexPic']],
			            "reportTelephone":item['reportTelephone'],
			            "outsidePackageColour":item['outsidePackageColour'],
			            "insidePackageColour":item['insidePackageColour'],
			            "volume":item['volume'],
			            "tagNumber":item['tagNumber'],
			            "placeNextStation":{},
			            "packageNumber":"item['packageNumber']",
			            "goodsBig":{"name":item['goodsBig_name'],
			                        "value":item['goodsBig_value']},
			            "goodsSmall":{"name":item['goodsSmall_name'],
			                          "value":item['goodsSmall_value']}}
			result_str = response.run_main("post",get_url,get_hearder,set_dict)  # 调用自定义接口方法
			result_dict = json.loads(result_str)  # 将返回结果从str解析成dict
			result.append(result_dict)  # 将结果放入list并返回
		# '''验证返回结果'''
		# rs_message = result_dict["message"]
		# if rs_message == "success":
		# 	result.append("headlessAdd输出：无着件上报成功，回参：%s" % result_str)
		# else:
		# 	result.append("headlessAdd输出：无着件上报失败，回参：%s" % result_str)
		return result  # 返回接口返回结果


if __name__ == "__main__":
	try:
		get_token = getLoginToken.get_token()  # 获取登录token，用于接口请求头
		headless_obj = HeadlessAdd(get_token)  # 实例化类
		getresult = headless_obj.headless_Add()  # 调用上报无着件方法
		print(getresult)
	# for item in getresult:
	# 	print(item)
	except Exception as e:
		logging.exception(e)
