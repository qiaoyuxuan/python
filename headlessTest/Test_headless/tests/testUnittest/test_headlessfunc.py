import unittest,logging,json
from Test_headless.base import timeStamp,getJsonValue,setDBparam
from Test_headless.tests import getLoginToken,getHeadlessList,getHeadlessDetail,headlessAdd
from Test_headless.db import db_connect


class TestHeadlessFunc(unittest.TestCase):
	
	def setUp(self):
		print("**********准备测试环境**********")
		self.add_Headless_return_value = globals()  # setUp中定义全局变量，用于case间参数传递，dict类型
		self.token = getLoginToken.get_token()
		self.s_time = timeStamp.get_timedelta(-1)  # 获取当前时间7天前时间戳
		self.e_time = timeStamp.get_timedelta(0)  # 获取当前时间戳
		# self.s_time = timeStamp.times_to_stamp("2020-09-29 00:00:00")  # 获取指定时间的时间戳
		# self.e_time = timeStamp.times_to_stamp("2020-09-29 23:59:59")  # 获取指定时间的时间戳
		self.message = "message"  # 接口返回字段：是否成功
		self.fields = "id"  # 接口返回字段：新增无着件的id
	
	def tearDown(self):
		print("**********清理测试环境**********")
	
	def test_headless_add(self):
		h_add = headlessAdd.HeadlessAdd()
		h_add.headless_Add()


'''继承类，可使用父类（准备测试环境）的公有属性和方法'''


class CaseAll(TestHeadlessFunc):
	
	def test_get_headless_list(self):
		print("******************根据日期获取无着件信息，返回条数与数据库查询条数对比*********************")
		fields = "total"
		self.get_list_return_value = ""
		try:
			get_cls = getHeadlessList.GetHeadlessList(self.token,self.s_time,self.e_time)  # 实例化类
			response_dict = get_cls.headless_list()  # 调用接口返回指定时间的无着件列表信息
			if self.message in response_dict:  # 如果返回的dict中存在message字段
				self.message = response_dict[self.message]
				if self.message == "success":
					print("test_headlessfunc打印：接口连接Success")
					get_list = getJsonValue.traverse_take_field(response_dict,fields)  # 自定义函数，获取total的key和value
					if fields in get_list:  # 判断如果指定字段存在，则获取total的索引，索引+1则是total的value值
						get_key_index = get_list.index(fields)
						# print(fields, "的索引是：", get_key_index)
						self.get_list_return_value = get_list[get_key_index + 1]
						print("test_headlessfunc打印：接口返回的",fields,"value=",self.get_list_return_value)
					else:
						print("test_headlessfunc打印：",fields,"不存在")
			else:
				print("test_headlessfunc打印：HeadlessList：连接Fail")
		except Exception as e:
			print("test_headlessfunc打印，接口出错：",e)
		
		# 查询DB，返回无着件条数，与上面接口返回的条数对比
		s_time_stamp = timeStamp.stamp_to_times(self.s_time)  # 开始时间戳转换为时间
		e_time_stamp = timeStamp.stamp_to_times(self.e_time)  # 结束时间戳转换为时间
		sql = "select count(*) from hp_headless_package  where " \
		      "create_time between %(startTime)s and %(endTime)s and create_station_code = '210045'"
		values = {"startTime":s_time_stamp,"endTime":e_time_stamp}  # 将sql中要传入的值放入dict
		args = setDBparam.db_headless()
		result_db = db_connect.db_connect(sql,values,*args)  # 调用DB访问方法
		db_sum = str(result_db[0][0])  # sql的count结果返回一个tuple，提取tuple中的值
		print("DB_sum:",db_sum)
		# 对比接口返回条数 和 数据库查询条数，一致则正确
		self.assertEqual(str(self.get_list_return_value),db_sum,
		                 msg="失败原因：%s != %s" % (str(self.get_list_return_value),db_sum))
	
	def test_add_headless(self):
		print("***********************上报一条无着件************************")
		# self.get_add_return_value = ""
		try:
			get_cls = headlessAdd.HeadlessAdd(self.token,self.data)  # 实例化类
			response_dict = get_cls.headless_Add()  # 调用上报无着件接口方法
			if self.message in response_dict:  # 判断返回参数中是否存在变量message指定字段
				self.message = response_dict[self.message]  # 存在则取出，赋予message变量
				if self.message == "success":  # 返回参数值为success，则表示接口调用成功
					print("test_headlessfunc打印：无着件上报成功，回参：%s" % response_dict)
					get_list = getJsonValue.traverse_take_field(response_dict,self.fields)  # 自定义方法，判断指定字段是否存在
					if self.fields in get_list:  # 若指定字段存在
						get_key_index = get_list.index(self.fields)  # 获取字段索引
						# print("test_headlessfunc打印：", self.fields, "的索引是：", get_key_index)
						self.add_Headless_return_value["value"] = get_list[get_key_index + 1]  # 指定字段索引+1则是该字段value值
						# print("test_headlessfunc打印：", self.fields, "value=", self.add_Headless_return_value)
					else:
						print("test_headlessfunc打印：指定字段",self.fields,"不存在")
				else:
					print("test_headlessfunc打印：:无着件上报失败：%s" % response_dict["message"])
			else:
				print("test_headlessfunc打印：:接口未返回字段：",self.fields)
		except Exception as e:
			print(e)
	
	def test_get_headless_detail(self):
		print("************根据‘无着件ID’获取无着件详情**************")
		try:
			self.id = self.add_Headless_return_value["value"]
			if self.id == "":
				print("test_headlessfunc打印：请先执行上报无着件接口，获取无着件ID才能执行本方法！")
			else:
				get_cls_detail = getHeadlessDetail.GetHeadlessDetail(self.token,self.id)
				response_dict = get_cls_detail.headless_detail()
				print(response_dict)
		except Exception as e:
			print(e)


if __name__ == '__main__':
	unittest.main()
