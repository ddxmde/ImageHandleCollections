# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import time

import io
import sys

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

def pic_open(filepath):
	image = Image.open(filepath)
	return image

def pic_addText(image,xy,text,color,font,textSize,direction=None):
	draw = ImageDraw.Draw(image)
	setFont = ImageFont.truetype(font, textSize)
	draw.text(xy,text,font=setFont,fill=color,direction=None)

def pic_save(image,filename):
	image.save(filename)

def get_position():
	x = int(input("输入x坐标:"))
	y = int(input("输入y坐标:"))
	return (x,y)

def get_text():
	# 输入不可变文字
	text = input("输入文字：")
	return text

def get_color():
	color = input("输入颜色（直接回车默认 #000000）：")
	return "#000000" if color=='' else color

def get_font():
	font = input("输入字体路径（如D:/xxx/xxx.ttc 直接回车默认黑体）：")
	return "heiti.otf" if font=='' else font 

def get_textSize():
	textSize = int(input("输入字号（9-120）："))
	return textSize

def get_numText():
	# 输入变化文字
	num = int(input("输入起始数字："))
	count = int(input("输入个数："))
	step = int(input("输入间隔（最小为1）："))
	pre = input("输入前缀（没有直接按回车）：")
	endx = input("输入后缀（没有直接按回车）：")
	filenames = []
	for x in range(0,count*step,step):
		filenames.append(pre+str((num+x))+endx)
	#print(filenames)
	return filenames

def get_multTextFromFile():
	#从文件获取连续变化的字符串并作为文件名
	filepath = input("输入文件路径（如：D:/XXX/XXX.txt）:")
	f = open(filepath,'r',encoding='UTF-8')
	filenames = []
	while True:
		line = f.readline().strip('\n')
		if not line:
			break
		else:
			filenames.append(line)
	return filenames

def pic_draw():
	filepath =input("输入模板图片的文件路径（如：D:/XXX/XXX.txt）：")
	orgImage = pic_open(filepath)
	addCount = int(input("要添加的固定文本的条数："))
	for k in range(addCount):
		print("=========添加第%d条固定文本========="%(k+1))
		position = get_position()
		text = get_text()
		color = get_color()
		font = get_font()
		textSize = get_textSize()
		pic_addText(orgImage,position,text,color,font,textSize,direction=None)
		print("=========添加第%d条固定文本结束========="%(k+1))
	print("选择要添加的变化文本的方式：")
	print("1-根据数字变化生成")
	print("2-从文件逐行获取变化文字生成")
	filenames = []
	drawWay = int(input("输入数字选择操作："))
	if (drawWay ==1):
		#根据数字变化生成
		filenames = get_numText()
	elif (drawWay ==2):
		# 根据文件名变化生成
		filenames = get_multTextFromFile()
	else:
		print("输入有误……重新打开程序")
	print("开始添加变化文字……")
	position = get_position()
	color = get_color()
	font = get_font()
	textSize = get_textSize()
	saveDir = input("输入文件保存路径（如： D:/xxx/）:")
	fileType = input("请输入图片保存格式（如jpg png gif）：")
	for fna in filenames:
		tmpImage = orgImage.copy()
		pic_addText(tmpImage,position,fna,color,font,textSize,direction=None)
		fname = saveDir+fna+'.'+fileType
		pic_save(tmpImage,fname)
		print("保存图片 %s 成功……\n"%(fname))

if __name__=="__main__":
	pic_draw()





