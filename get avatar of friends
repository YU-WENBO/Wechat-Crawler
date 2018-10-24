#coding=utf-8
from __future__ import print_function
import itchat
import os
import PIL.Image as Image
from os import listdir
import math
import shutil


itchat.login()

friends = itchat.get_friends(update=True)[0:]

user = friends[0].NickName

print(user)

shutil.rmtree(user)
os.mkdir(user)

num = 1

for i in friends:
	img = itchat.get_head_img(userName=i["UserName"])
	fileImage = open(user + "/" + str(num) + ".jpg",'wb')
	fileImage.write(img)
	fileImage.close()
	print('头像下载进度:',num,'/',len(friends))
	num += 1

