a={"agv":"creey001","bucket":"T-5","name":"木头人","age":"123"}
print(a["agv"])       #打印key值为"agv"  获取对应的value
a["sex"]="nan"        #插入key值为"sex"  value值为"nan"
a["sex"]="nv"          #修改key值为"sex"  value值为"nv"
print(a)
a["jobtype"]=["youxian",1,"99"]     #插入key值为"jobtype"  value值为["youxian",1,"99"]
print(a)
# print(a.pop("bucket"))     #提取
a.pop("name")      #把 “ name” 提取之后打印
print(a)