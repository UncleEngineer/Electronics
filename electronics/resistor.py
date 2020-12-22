# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk,messagebox #theme of tk
import random

colors1 = {'black':'0',
		   '#855a42':'1',
		   'red':'2',
		   'orange':'3',
		   'yellow':'4',
		   'green':'5',
		   'blue':'6',
		   'purple':'7',
		   'grey':'8',
		   'white':'9'}

colors2 = {'black':'0',
		   '#855a42':'1',
		   'red':'2',
		   'orange':'3',
		   'yellow':'4',
		   'green':'5',
		   'blue':'6',
		   'purple':'7',
		   'grey':'8',
		   'white':'9'}

colors3 = {'black':'1',
		   '#855a42':'10',
		   'red':'100',
		   'orange':'1000',
		   'yellow':'10000',
		   'green':'100000',
		   'blue':'1000000',
		   'purple':'10000000',
		   'grey':'100000000',
		   'white':'1000000000',
		   'gold':'0.1',
		   'silver':'0.01'}

colors4 = {'#855a42':'±1%',
		   'red':'±2%',
		   'orange':'±3%',
		   'yellow':'±4%',
		   'green':'±0.5%',
		   'blue':'±0.25%',
		   'purple':'±0.1%',
		   'grey':'±0.05%',
		   'gold':'±5%',
		   'silver':'±10%'}

findcolor = {}

for k,v in colors1.items():
	findcolor[v] = k


def CheckColor(b1,b2,b3,b4='gold'):
	print('Band 1: {} digit: {}'.format(b1, colors1[b1]))
	print('Band 2: {} digit: {}'.format(b2, colors2[b2]))
	print('Band 3: {} multiplier: {}'.format(b3, colors3[b3]))
	print('Band 4: {} torerance: {}'.format(b4, colors4[b4]))
	cal = float(colors1[b1] + colors2[b2]) * float(colors3[b3])

	if cal >= 1000000000:
		prefix = 'G'
		if str(cal)[-9] != '0':
			res = str(cal)[:-9] + prefix + str(cal)[-9]
		else:
			res = str(cal)[:-9] + prefix
	elif cal >= 1000000:
		prefix = 'M'
		if str(cal)[-6] != '0':
			res = str(cal)[:-6] + prefix + str(cal)[-6]
		else:
			res = str(cal)[:-6] + prefix
	elif cal >= 1000:
		prefix = 'k'
		# 3400
		if str(cal)[-3] != '0':
			res = str(cal)[:-3] + prefix + str(cal)[-3]
		else:
			res = str(cal)[:-3] + prefix
	else:
		res = ''
	print('CAL:',[cal])
	if cal > 0:
		print('Resistor value: {:,.0f} Ohms ( {} Ω )'.format(cal,res))
		print('------')
		return '{:,.0f} ohms ( {} Ω )'.format(cal,res)
	else:
		print('Resistor value: {:,.3f} Ohms ( {} Ω )'.format(cal,res))
		print('------')
		return '{:,.3f} ohms ( {} Ω )'.format(cal,res)

# CheckColor('brown','black','red','gold')
# CheckColor('green','black','white','gold')

GUI = Tk()
GUI.title('4 Band Resistor Color Code Calculator -  by Uncle Engineer')

GUI.resizable(0, 0)
w = 850
h = 600

ws = GUI.winfo_screenwidth() #screen width
hs = GUI.winfo_screenheight() #screen height
#print(ws,hs)

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

GUI.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}')

Font = ('tahoma',20)

L1 = ttk.Label(GUI,text='Resistor Value',font=Font).pack()

resistor = StringVar()
E1 = ttk.Entry(GUI,textvariable=resistor,font=Font)
E1.place(x=100,y=50,width=500)
E1.focus()



def FindColor(event=None):
	try:
		vr = resistor.get()
		b1 = vr[0]
		b2 = vr[1]
		multi = str(len(vr[2:]))

		c1 = findcolor[b1]
		c2 = findcolor[b2]
		c3 = findcolor[multi]
		c4 = 'gold'
		print(c1,c2,c3,c4)
		text = CheckColor(c1,c2,c3,c4)
		v_result.set(text)
		canvas.itemconfig(box1,fill=c1)
		canvas.itemconfig(box2,fill=c2)
		canvas.itemconfig(box3,fill=c3)
		canvas.itemconfig(box4,fill=c4)
	except:
		messagebox.showinfo('ERROR','Only Number! ... \n-100 Ohms --> 100\n-1k Ohms --> 1000')


E1.bind('<Return>',FindColor)
v_result = StringVar()
v_result.set('Result')
FONT2 = ('tahoma',30,'bold')
R1 = ttk.Label(GUI,textvariable=v_result,font=FONT2,foreground='green')
R1.pack(pady=100)

ohm = ttk.Label(GUI,text='Ω',font=Font)
ohm.place(x=620,y=50)

FB = Frame(GUI)
FB.place(x=660,y=50)
B1 = ttk.Button(FB,text='OK',command=FindColor)
B1.pack(ipadx=20,ipady=10)

canvas2 = Canvas(GUI,width=130,height=40)
canvas2.place(x=80,y=265)
line1 = canvas2.create_rectangle(10,10,120,30,fill='white')

canvas3 = Canvas(GUI,width=130,height=40)
canvas3.place(x=630,y=265)
line2 = canvas3.create_rectangle(10,10,120,30,fill='white')

canvas = Canvas(GUI,width=470,height=120)
canvas.place(x=180,y=220)


box0 = canvas.create_rectangle(2,2,470,120,fill='#dbd6c8')
box1 = canvas.create_rectangle(50,2,100,120,fill='red')
box2 = canvas.create_rectangle(150,2,200,120,fill='green')
box3 = canvas.create_rectangle(250,2,300,120,fill='blue')
box4 = canvas.create_rectangle(380,2,430,120,fill='gold')

F1 = Frame(GUI)
F1.place(x=50,y=350)

allbutton = []

v_c1 = StringVar()
v_c2 = StringVar()
v_c3 = StringVar()
v_c4 = StringVar()

def Change(bcl,b,v):
	if b == 1:
		v_c1.set(bcl)
		cvalue = resistor.get() + v
		resistor.set(cvalue)
		B2.configure(state='disabled')
	elif b == 2:
		v_c2.set(bcl)
		cvalue = resistor.get() + v
		resistor.set(cvalue)
		B3.configure(state='disabled')
	elif b == 3:
		v_c3.set(bcl)
		text = CheckColor(v_c1.get(),v_c2.get(),v_c3.get())
		resistor.set(text)
		v_result.set(text)
		B4.configure(state='disabled')
	else:
		v_c4.set(v)
		cvalue = resistor.get() + ' ' + v
		resistor.set(cvalue)
		v_result.set(resistor.get())
		B5.configure(state='disabled')
	
	global allbutton
	bcolor = {1:box1,2:box2,3:box3,4:box4}
	canvas.itemconfig(bcolor[b],fill=bcl)
	for ab in allbutton:
		ab.destroy()
		# ลบปุ่มทั้งหมด
	allbutton = [] #เคลียร์ปุ่มให้หมด

def c1():
	for i,(bc,bv) in enumerate(colors1.items()):
		print('BC',bc)
		B = Button(F1,width=6, text=' ' , bg=bc,command=lambda x=bc,y=bv: Change(x,1,y))
		B.grid(row=0,column=i,padx=10)
		allbutton.append(B)

def c2():
	for i,(bc,bv) in enumerate(colors2.items()):
		print('BC',bc)
		B = Button(F1,width=6,text=' ',bg=bc,command=lambda x=bc,y=bv: Change(x,2,y))
		B.grid(row=0,column=i,padx=10)
		allbutton.append(B)

def c3():
	for i,(bc,bv) in enumerate(colors3.items()):
		print('BC',bc)
		B = Button(F1,width=5,text=' ',bg=bc,command=lambda x=bc,y=bv: Change(x,3,y))
		B.grid(row=0,column=i,padx=10)
		allbutton.append(B)

def c4():
	for i,(bc,bv) in enumerate(colors4.items()):
		print('BC',bc)
		B = Button(F1,width=6,text=' ',bg=bc,command=lambda x=bc,y=bv: Change(x,4,y))
		B.grid(row=0,column=i,padx=10)
		allbutton.append(B)

FBC = Frame(GUI)
FBC.place(x=220,y=400)

B2 = ttk.Button(FBC,text='Color 1',command=c1)
B2.grid(row=0,column=0,ipady=20)
B3 = ttk.Button(FBC,text='Color 2',command=c2)
B3.grid(row=0,column=1,ipady=20,padx=30)
B4 = ttk.Button(FBC,text='Color 3',command=c3)
B4.grid(row=0,column=2,ipady=20,padx=0)
B5 = ttk.Button(FBC,text='Color 4',command=c4)
B5.grid(row=0,column=3,ipady=20,padx=50)

def Reset(event=None):
	resistor.set('')
	v_c1.set('')
	v_c2.set('')
	v_c3.set('')
	v_c4.set('')
	B2.configure(state='enabled')
	B3.configure(state='enabled')
	B4.configure(state='enabled')
	B5.configure(state='enabled')
	for ab in allbutton:
		ab.destroy()
	E1.focus()

FBR = Frame(GUI)
FBR.place(x=350,y=500)
BR = ttk.Button(FBR,text='Reset',command=Reset)
BR.pack(ipady=20,ipadx=30)

GUI.bind('<F1>',Reset)

GUI.mainloop()