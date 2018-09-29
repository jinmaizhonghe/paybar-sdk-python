# -*- coding=utf-8-*-
# Autrhor: YQT by pengfei.he
import AesUtils
import Client
import json
# coding=utf-8

#请求服务器地址
url = "https://hospital.jia007.com/paybar-api/paybar/hospital/pay"
#商户编号
appKey = ""
#商户秘钥
secretKey = ""

request = {}
request['requestNo']='12345678901'
request['payTool']='SCAN'
request['productDesc']='ceshi'
request['orderAmount']='0.01'
request['serverCallbackUrl']='http://www.qq.com'
request['clientIp']='192.168.1.1'
request['orderDate']='2018-08-29 18:11:04'
request['merchantNo']='1051100110000070'
request['productName']='鹏飞测试'
request['payScene']='BH'
#转换位json请求数据,解决中文乱码
requestJson = json.dumps(request,ensure_ascii=False)
#对请求数据进行加密
data = AesUtils.AESUtil.encryt(requestJson,secretKey)
#发送请求
response = Client.Client.post(url,data,appKey)
if "code" in response:
    # 由于未请求到业务系统，直接返回未加密字符串
    print  response
else:
    #正常解密响应数据
    response = AesUtils.AESUtil.decrypt(response,secretKey)
    print  response

#返回数据
#解密原始数据：{"code":"1","orderAmount":"0.01","orderNo":"11171114183109692912","redirectUrl":"weixin://wxpay/bizpayurl?pr\u003d7PYdx1J","message":"受理成功","status":"PROCESS"}



