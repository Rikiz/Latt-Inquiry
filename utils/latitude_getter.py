#!/usr/bin/env python
# coding=utf-8
from requests import get
from io import open

def record_error(address):
    with open("error.txt", "a", encoding = "utf-8") as f:
        f.writelines([address + "\n"])

# 构造 url 获取查询响应
def geocode(address, api_key = None):
    key = api_key
    para = {'key':key, # 高德Key
            'address':address} # 地址参数              
    url = 'https://restapi.amap.com/v3/geocode/geo?' # 高德地图地理编码API服务地址
    response = get(url,para) # GET方式请求
    try:
        answer = response.json()
        lon_lat = answer['geocodes'][0]['location'] # 获取返回参数geocodes中的location，即经纬度
        longtitude, latitude = lon_lat.split(",")
        return {"longtitude":longtitude, "latitude":latitude}
    except :
        record_error(address)
        return ""



def record_to_file(result):
    with open("result.csv", "a", encoding = "utf-8") as f:
        f.writelines([result])


if __name__ == '__main__':
    address_file = u"address.txt"
    address_file = address_file.strip()
    with open(address_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        index = 1
        for line in lines:
            line = line.strip()
            res_str = geocode(line)
            if res_str != "":
                longtitude, latitude = res_str.split(",")
                result = line.strip() + "," + str(longtitude).strip() + "," + str(latitude).strip() + "\n"
                record_to_file(result)
                # print str(index) + " address " + line + "finished"
            index += 1
