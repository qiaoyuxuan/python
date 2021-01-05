from Test_headless.tests import getLoginToken
from Test_headless.base import testRunMain
from Test_headless.base import timeStamp
from Test_headless.base import setUrl
import json, logging
import collections


class GetHeadlessList(object):  # 实例化
    def __init__(self, token, start_time, end_time):
        self.token = token
        self.start_time = start_time
        self.end_time = end_time

    def headless_list(self):  # 本公司无着件：获取无着件列表
        get_url = setUrl.list_url()
        headers = {"token": self.token,
                   "content-Type": "application/json;charset=UTF-8",
                   "channel": "WDGJ"}
        data = {"httpMethod": "post",
                "params": {"claimStatus": "",
                           "endReportTime": self.end_time,
                           "limit": "100",
                           "pageNo": "1",
                           "startReportTime": self.start_time,
                           "orderNumber": ""},
                "type": "headless.api",
                "url": "/headless/headlessPackageCompany/getHeadlessPageApp"}

        response = testRunMain.RunMain()  # 实例化类
        result_str = response.run_main("post", get_url, headers, data)  # 调用自定义接口方法
        result_dict = json.loads(result_str)  # 将返回结果从str解析成dict
        # print(self.token, "/\n", self.end_time, self.start_time)
        # print(len(result_dict["data"]["items"]))  # 获取items下元素个数，上报个数
        print(result_dict)
        return result_dict


if __name__ == "__main__":
    try:
        get_token = getLoginToken.get_token()  # 获取登录token，用于接口请求头
        # 默认查询7天内数据
        s_time = timeStamp.get_timedelta(-7)  # 获取当前时间7天前的时间戳
        e_time = timeStamp.get_timedelta(0)  # 获取当前时间戳

        # 根据指定日期查询
        # s_time = timeStamp.times_to_stamp("2020-08-11 00:00:00")
        # e_time = timeStamp.times_to_stamp("2020-08-15 23:59:59")

        h_list = GetHeadlessList(get_token, s_time, e_time)  # 实例化类
        h_list.headless_list()
    except Exception as e:
        logging.exception(e)
