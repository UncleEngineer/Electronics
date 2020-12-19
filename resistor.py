#resistor.py

colors1 = {'black':'0',
		   'brown':'1',
		   'red':'2',
		   'orange':'3',
		   'yellow':'4',
		   'green':'5',
		   'blue':'6',
		   'violet':'7',
		   'grey':'8',
		   'white':'9'}

colors2 = {'black':'0',
		   'brown':'1',
		   'red':'2',
		   'orange':'3',
		   'yellow':'4',
		   'green':'5',
		   'blue':'6',
		   'violet':'7',
		   'grey':'8',
		   'white':'9'}

colors3 = {'black':'1',
		   'brown':'10',
		   'red':'100',
		   'orange':'1000',
		   'yellow':'10000',
		   'green':'100000',
		   'blue':'1000000',
		   'violet':'10000000',
		   'grey':'100000000',
		   'white':'1000000000',
		   'gold':'0.1',
		   'silver':'0.01'}

colors4 = {'brown':'±1%',
		   'red':'±2%',
		   'orange':'±3%',
		   'yellow':'±4%',
		   'green':'±0.5%',
		   'blue':'±0.25%',
		   'violet':'±0.1%',
		   'grey':'±0.05%',
		   'gold':'±5%',
		   'silver':'±10%'}

'''
ตัวต้านทานตัวนี้มีค่า:  1,000 โอห์ม ( 1kΩ )
'{:,d}'
1-เอา b1 กับ b2 +กัน (string)
2-cal = เอา 1 แปลงเป็นตัวเลข แล้วคูณกับ b3 ที่แปลงเป็นตัวเลขแล้ว
3-เอาไปใส่ในข้อความโดยให้มี , ทุกสามหลัก
'''


def CheckColor(b1,b2,b3,b4):
	print('Band 1: {} digit: {}'.format(b1, colors1[b1]))
	print('Band 2: {} digit: {}'.format(b2, colors2[b2]))
	print('Band 3: {} multiplier: {}'.format(b3, colors3[b3]))
	print('Band 4: {} torerance: {}'.format(b4, colors4[b4]))
	cal = int(colors1[b1] + colors2[b2]) * int(colors3[b3])

	if cal >= 1000000000:
		prefix = 'G'
		res = str(cal)[:-9] + prefix
	elif cal >= 1000000:
		prefix = 'M'
		res = str(cal)[:-6] + prefix
	elif cal >= 1000:
		prefix = 'k'
		res = str(cal)[:-3] + prefix
	else:
		res = ''
	print('ตัวต้านทานตัวนี้มีค่า: {:,d} โอห์ม ( {}Ω )'.format(cal,res))
	print('------')

CheckColor('brown','black','red','gold')
CheckColor('green','black','white','gold')