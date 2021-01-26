#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2021/1/26 14:25
author：乔誉萱
说明：网上搜索的案例，原文写的是：可以快速帮你从密码表中找到对应的明文。也可以作为日常的MD5解密之用
但还不知道怎么使用，wordlist.txt是不是用来存放密码表的？
:param 
:param 
'''

import hashlib
import datetime
import argparse


import sys
def Findmd5(args):
    md=args.hashvalue
    starttime=datetime.datetime.now()
    for i in open(args.file):
        md5=hashlib.md5()   #获取一个md5加密算法对象
        rs=i.strip()    #去掉行尾的换行符
        md5.update(rs.encode('utf-8'))  #指定需要加密的字符串
        newmd5=md5.hexdigest()  #获取加密后的16进制字符串
        #print newmd5
        if newmd5==md:
            print('明文是：'+rs)    #打印出明文字符串
            break
        else:
            pass

    endtime=datetime.datetime.now()
    print(endtime-starttime)    # 计算解密用时，非必须

if __name__=='__main__':
    import argparse #命令行参数获取模块
    parser=argparse.ArgumentParser(usage='Usage:./findmd5.py -l 密码文件路径 -i 哈希值 ',description='help info.')   #创建一个新的解析对象
    parser.add_argument("-l", default='wordlist.txt', help="密码文件.", dest="file")    #向该对象中添加使用到的命令行选项和参数
    parser.add_argument("-i", dest="hashvalue",help="要解密的哈希值.")

    args = parser.parse_args()  #解析命令行
    Findmd5(args)


# def main():
# 	parser = argparse.ArgumentParser(description="Demo of argparse")
# 	parser.add_argument('-n','--name',default='Jack',type=str,help='argument:name')
# 	parser.add_argument('-y','--year',default=20,type=int,help='argument:age')
# 	args = parser.parse_args()
# 	print(args)
# 	name = args.name
# 	year = args.year
# 	print("hello,My name is {} and I'm {} years old".format(name,year))
#
#
# if __name__ == '__main__':
# 	main()
