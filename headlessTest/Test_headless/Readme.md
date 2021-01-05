文件目录说明：
-base
--setUrl：封装接口地址
--headers：封装接口请求头
--testRunMain：封装接口请求方法，返回接口响应参数，仅支持post和get，统一对外调用方法：run_main()
--setDBparam：封装数据库访问连接串，返回一个tuple；
--timeStamp：封装时间方法：get_timedelta()返回当前时间戳/偏差时间戳、times_to_stamp()时间转换为时间戳、stamp_to_times()时间戳转换为时间【待class封装】
--getJsonValue：用于在嵌套列表中，查询指定字段的值，返回查询到的值，类型是list:traverse_take_field()；将list转为dict:【待class封装】
--readFile：封装文件读取方法，支持csv和excel（xls格式）文件，返回读取到的数据，类型是list

-db
--db_connect：封装数据库连接方法，并返回数据库查询数据(数据库连接串类外封装在common下setDBparam方法中)

-datas：数据驱动文件
-tests：测试用例