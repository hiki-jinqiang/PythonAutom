# -*- coding: utf-8 -*-
import requests
import emailTest    
#step-1:设置基本的信息----email的信息需要在emailTest 模块中设置
url = 'https://restapi.amap.com/v3/weather/weatherInfo?parameters'      #高德天气api网址
params_realtime = {
    'key':'please write key correct',  #填写自己的key             
    'city':'citycode', # 从城市编码里获取的code
    'extensions':'base' # 获取实时天气
}
params_estimate = {
    'key':'please write key correct',  #填写自己的key
    'city':'citycode',     #从城市编码里获取的code
    'extensions':'all'   #获取预报天气
}

#step-2:读取高德api接口，获取天气信息并转换为JSON格式
# 读取实时天气
ResRealTime = requests.get(url=url,params=params_realtime) # 实时天气
WeatherRealTime = ResRealTime.json()
print(WeatherRealTime)
print("\n")
# 读取预测天气
Respredict = requests.get(url=url,params=params_estimate) # 预报天气 
WeatherPredict = Respredict.json()
print(WeatherPredict)
print("\n")

#step-3:获取JSON信息中的信息。
#获取实时信息中的信息
#print(WeatherRealTime.get('lives'))
Realprovince = WeatherRealTime['lives'][0]["province"] # 获取省份
Realcity = WeatherRealTime.get('lives')[0].get("city") # 获取城市
Realadcode = WeatherRealTime.get('lives')[0].get("adcode") # 获取城市编码
Realreporttime = WeatherRealTime.get('lives')[0].get("reporttime") # 获取发布数据时间
Realweather = WeatherRealTime.get('lives')[0].get('weather') # 白天天气现象
Realtemperature = WeatherRealTime.get('lives')[0].get('temperature_float') # 获取温度
Realwinddirection = WeatherRealTime.get('lives')[0].get('winddirection') # 获取风向
Realwindpower = WeatherRealTime.get('lives')[0].get('windpower') # 获取风力大小
Realhumidity =  WeatherRealTime.get('lives')[0].get('humidity') # 获取湿度

# print("省份:",Realprovince)
# print("城市:",Realcity)
# print("城市编码:",Realadcode)
# print("发布数据时间:",Realreporttime)
# print("当天天气:",Realweather)
# print("当天温度:",Realtemperature)
# print("当天风向:",Realwinddirection)
# print("当天风力:",Realwindpower)
# print("当天湿度:",Realhumidity)

#获取预测信息-明天版本
# print(tianqi.get('forecasts'))
tomorrowprovince = WeatherPredict.get('forecasts')[0].get("province") # 获取省份
tomorrowcity = WeatherPredict.get('forecasts')[0].get("city") # 获取城市
tomorrowadcode = WeatherPredict.get('forecasts')[0].get("adcode") # 获取城市编码
tomorrowreporttime = WeatherPredict.get('forecasts')[0].get("reporttime") # 获取发布数据时间
tomorrowdate = WeatherPredict.get('forecasts')[0].get("casts")[1].get('date') # 获取日期
tomorrowweek = WeatherPredict.get('forecasts')[0].get("casts")[1].get('week') # 获取星期几
tomodayweather = WeatherPredict.get('forecasts')[0].get("casts")[1].get('dayweather') # 白天天气现象
tomorrownightweather = WeatherPredict.get('forecasts')[0].get("casts")[1].get('nightweather') # 晚上天气现象
tomorrowdaytemp = WeatherPredict.get('forecasts')[0].get("casts")[1].get('daytemp_float') # 白天温度
tomorrownighttemp = WeatherPredict.get('forecasts')[0].get("casts")[1].get('nighttemp') # 晚上温度
tomorrowdaywind = WeatherPredict.get('forecasts')[0].get("casts")[1].get('daywind') # 	白天风向
tomorrownightwind = WeatherPredict.get('forecasts')[0].get("casts")[1].get('nightwind') # 晚上风向
tomorrowdaypower = WeatherPredict.get('forecasts')[0].get("casts")[1].get('daypower') # 白天风力
tomorrownightpower = WeatherPredict.get('forecasts')[0].get("casts")[1].get('nightpower') # 晚上风力

# print("省份:",tomorrowprovince)
# print("城市:",tomorrowcity)
# print("城市编码:",tomorrowadcode)
# print("发布数据时间:",tomorrowreporttime)
# print("日期:",tomorrowdate)
# print("星期:",tomorrowweek)
# print("白天天气现象:",tomodayweather)
# print("晚上天气现象:",tomorrownightweather)
# print("白天温度:",tomorrowdaytemp)
# print("晚上温度:",tomorrownighttemp)
# print("白天风向:",tomorrowdaywind)
# print("晚上风向:",tomorrownightwind)
# print("白天风力:",tomorrowdaypower)
# print("晚上风力:",tomorrownightpower)

#step-4:天气信息进行对比，然后判断是否需要email通知本人。
Informweather = 0       #默认为0，不通知。
InformTemperature = 0     #温度默认为0，不通知。
if tomodayweather=="小雨" or tomorrownightweather=="小雨":
  print("下雨")
  Informweather = 1

if tomodayweather=="中雨" or tomorrownightweather=="中雨":
  print("中雨")
  Informweather = 1

if tomodayweather=="大雨" or tomorrownightweather=="大雨":
  print("大雨")
  Informweather = 1

NumberRealTemperaure = float(Realtemperature)  # 使用float()函数将字符串转换为整数
NumberPredictTemperaure = float(tomorrowdaytemp)  # 使用float()函数将字符串转换为整数
if abs(NumberRealTemperaure-NumberPredictTemperaure) >= 4:   #今天的温度和明天温度差5度
  print("温度变化大")
  InformTemperature = 1
  
if Informweather == 1 or InformTemperature == 1:
 EemailText = "dayweather:" +  tomodayweather + "nightweather:" +  tomorrownightweather +" " +"todaytemperature:" + Realtemperature + " " + "tomorrowtemperature:" + tomorrowdaytemp
 res = emailTest.mailToME('weather warning',EemailText)

print(Realreporttime)
print("successful")