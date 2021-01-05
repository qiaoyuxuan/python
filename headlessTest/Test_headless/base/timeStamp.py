# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/11/6 9:12
author：乔誉萱
说明：封装时间方法，返回当前时间戳/偏差时间戳、时间转换为时间戳、时间戳转换为时间
:param day：
:param
'''
import time
import datetime, logging



def get_timedelta(day):
    '''返回当前或偏移时间的时间戳。参数：偏移天数，传0则返回当前时间戳，-1则是前一天，1则是后一天'''
    now = datetime.datetime.now()
    # print("当前时间：", now)
    # strptime：转换为时间格式，strftime格式化成年月日时分秒格式
    d1 = datetime.datetime.strptime(now.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    # print("格式化当前时间：", d1)

    delta = datetime.timedelta(days=day)  # 获取当前时间的偏移时间
    d2 = d1 + delta  # 当前日期-偏移时间，获取偏移日期
    # print("%s天前的日期为：" % day, d2)
    result_time = int(time.mktime(d2.timetuple()))  # timetuple：将时间类型转换成时间数组,mktime：将时间数组转换成时间戳
    # print(result_time)
    return result_time



def times_to_stamp(date_time):
    '''时间转换为时间戳'''
    time_array = time.strptime(date_time, '%Y-%m-%d %H:%M:%S')  # strptime：将str类型转换成时间数组
    # print("time_array:", time_array)
    time_stamp = int(time.mktime(time_array))  # mktime：将时间数组转换成时间戳
    # print(time_stamp)
    return time_stamp


def stamp_to_times(date_stamp):
    '''时间戳转换为时间'''
    time_array = time.localtime(int(date_stamp))  # 将时间戳转换为时间
    data_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)  # 格式化时间格式
    # print(data_time)
    return data_time


'''测试：调用方法测试结果'''
try:
    get_timedelta(0)
    times_to_stamp('2020-09-28 11:40:59')
    stamp_to_times("1601264459")
except Exception as e:
    print("转换出错！")
    logging.exception(e)
