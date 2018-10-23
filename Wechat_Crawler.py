#coding=utf-8
import itchat
import numpy as np
import pandas as pd
from collections import defaultdict
import re
import jieba
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import PIL.Image as Image
import sys
import shutil

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

itchat.login()

friends = itchat.get_friends(update=True)

NickName = friends[0].NickName #获取自己的昵称

shutil.rmtree(NickName)
os.mkdir(NickName) #为自己创建一个文件夹

file = '/%s' %NickName #刚刚创建的那个文件夹的相对路径
cp = os.getcwd() #当前路径
path = os.path.join(cp+file) #刚刚创建的那个文件夹的绝对路径
os.chdir(path) #切换路径

number_of_friends = len(friends)

df_friends = pd.DataFrame(friends)


def get_count(Sequence):

    counts = defaultdict(int) #初始化一个字典

    for x in Sex:

        counts[x] += 1

        return counts

Sex = df_friends.Sex

#Sex_count = get_count(Sex )


Sex_count = Sex.value_counts() #defaultdict(int, {0: 31, 1: 292, 2: 245})


#Use this part to plot

#Sex_count.plot(kind = 'bar')
#plt.show()


Province = df_friends.Province

Province_count = Province.value_counts()

Province_count = Province_count[Province_count.index!=''] #有一些好友地理信息为空，过滤掉这一部分人。


City = df_friends.City #[(df_friends.Province=='北京') | (df_friends.Province=='四川')]

City_count = City.value_counts()

City_count = City_count[City_count.index!='']

file_name_all = NickName+'_basic_inf.txt'

write_file = open(file_name_all,'w')

write_file.write('你共有%d个好友,其中有%d个男生，%d个女生，%d未显示性别。\n\n' %(number_of_friends, Sex_count[1], Sex_count[2], Sex_count[0])+
                 '你的朋友主要来自省份：%s(%d)、%s(%d)和%s(%d)。\n\n' %(Province_count.index[0],Province_count[0],Province_count.index[1],Province_count[1],Province_count.index[2],Province_count[2])+
                 '主要来自这些城市：%s(%d)、%s(%d)、%s(%d)、%s(%d)、%s(%d)和%s(%d)。'%(City_count.index[0],City_count[0],City_count.index[1],City_count[1],City_count.index[2],City_count[2],City_count.index[3],City_count[3],City_count.index[4],City_count[4],City_count.index[5],City_count[5]))

write_file.close()


#Output Signature of your friends



Signatures = df_friends.Signature

regex1 = re.compile('<span.*?</span>') #匹配表情

regex2 = re.compile('\s{2,}')#匹配两个以上占位符。

Signatures = [regex2.sub(' ',regex1.sub('',signature,re.S)) for signature in Signatures] #用一个空格替换表情和多个空格。

Signatures = [signature for signature in Signatures if len(signature)>0] #去除空字符串

text = '\n'.join(Signatures)

file_name = NickName+'_wechat_signatures.txt'

with open(file_name,'w') as f:
    f.write(text)
    f.close()


wordlist = jieba.cut(text, cut_all=True)

word_space_split = ' '.join(wordlist)


#请在py文件所在的路径下放一张 词云照片（可谷歌或者百度） 并rename为wechat.jpg

d= os.path.dirname(os.path.abspath( __file__ ))
alice_coloring = np.array(Image.open(os.path.join(d, "wechat.jpg")))
my_wordcloud = WordCloud(background_color="white", max_words=2000,mask=alice_coloring,max_font_size=400, random_state=420,font_path='/Users/sebastian/Library/Fonts/Arial Unicode.ttf').generate(word_space_split)
image_colors = ImageColorGenerator(alice_coloring)
#os.remove(NickName+'.jpg')
my_wordcloud.to_file(NickName+'.jpg')






