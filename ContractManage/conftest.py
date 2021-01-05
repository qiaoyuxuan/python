#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/12/15 19:31
author：乔誉萱
说明：
:param 
:param 
'''
import pytest


@pytest.fixture()
def conftest_getHeaders():
	return {
		'Content-Type':'application/json;charset=UTF-8',
		'token':'Portal-eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ7XCJAdHlwZVwiOlwiY24ueXRvLnBvcnRhbC5hdXRob3JpdHkudm8uVXNlclZvXCIsXCJiZWxvbmdPcmdDb2RlXCI6XCI5OTk5OTlcIixcImJlbG9uZ09yZ05hbWVcIjpcIuaAu-WFrOWPuFwiLFwiYmVsb25nT3JnVHlwZVwiOlwiSEVBRFwiLFwib3JnQ29kZVwiOlwiOTk5OTk5XCIsXCJvcmdOYW1lXCI6XCLmgLvlhazlj7hcIixcIm9yZ1R5cGVcIjpcIkhFQURcIixcInN5c3RlbUNvZGVcIjpcIlBvcnRhbFwiLFwidXNlckNvZGVcIjpcIjAxNTA4Mzc3XCIsXCJ1c2VyTmFtZVwiOlwi5LmU6KqJ6JCxXCJ9IiwianRpIjoiMjRhYTVlMjctYzNlYy00NmJhLWJiMDktMzAzM2Q1MjVjMWIxIiwiaWF0IjoxNjA5MTQxMzQ0LCJleHAiOjE2MDkxNTU3NDR9.oMwYf2IhTZGDoaAJX4b6HeAC9STAMkRbMYdScLhqWEqQYyMMrwRmo6S4TugWhkZsOhTYNTWDswDYIno3bHokog'
	}
