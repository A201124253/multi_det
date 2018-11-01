#打开文件
f = open("infor_april_2.txt","r")

#开辟二维列表infos，里面包含的元素是info_line
infos = []
#info_line= []

#读取文件并输入到info_line
info = f.read()
#print(info)
#print(eval(info))
f.close()
#将信息转化成字典格式
dic_info = eval(info)


for i in dic_info['tags']:

	#存储每一行数据
	info_line= []

	#读取ID
	i_d = i['id']
	info_line.append(i_d)
	#print(info_line)
	
	#读取方向值w, x, y, z
	o_w = i['pose']['orientation']['w']
	info_line.append(o_w)
	o_x = i['pose']['orientation']['x']
	info_line.append(o_x)
	o_y = i['pose']['orientation']['y']
	info_line.append(o_y)
	o_z = i['pose']['orientation']['z']
	info_line.append(o_z)

	#读取位置值 x, y, z
	p_x = i['pose']['position']['x']
	info_line.append(p_x)
	p_y = i['pose']['position']['y']
	info_line.append(p_y)
	p_z = i['pose']['position']['z']
	info_line.append(p_z)
	infos.append(info_line)

#print(info_line)
print(infos)

