#TempConvert.py

TempStr = input("请输入带有符号的温度值：")
if TempStr[-1] in ['F', 'f']:
	C = (eval(TempStr[0:-1]) - 32) / 1.8
	print("转换后温度的是{:.2f}C".format(C))
elif TempStr[-1] in ['C', 'c']:
	C = (eval(TempStr[0:-1]) + 32) * 1.8
	print("转换后温度的是{:.2f}C".format(F))
else
	print("输入格式错误")