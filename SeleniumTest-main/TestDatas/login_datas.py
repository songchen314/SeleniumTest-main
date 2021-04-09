

#正常场景  - 测试数据

success_data={"user":"18684720553","password":"python"}

#异常用例 - 手机号不正确(大于11位,小于11位,为空,不在号码段)

phone_data=[
{"user": "186845205553", "password": "python", "check": "请输入正确的手机号"},
{"user": "1868452055531234", "password": "python", "check": "请输入正确的手机号"},
{"user": "", "password": "python", "check": "请输入手机号"},
{"user": "11111111111", "password": "python", "check": "请输入正确的手机号"},
{"user": "18684720553", "password": "", "check": "请输入密码"}
]
#异常场景
password_data=[
{"user": "18684720553", "password": "python1", "check": "帐号或密码错误!"},

]


