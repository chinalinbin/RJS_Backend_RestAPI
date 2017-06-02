# -*- coding:utf-8 -*-


import requests
import unittest
import HTMLTestRunner
import sys




payload_immediateFamilyName= {
    "platform":"android",
    "app_version":None,
    "os_version":None,
    "phone_model":None,
    "service_provider":0,
    "network_type":0,
    "session_token":"5481831BFEF423DEE11E1CA88CB98D47",
    "imei":None,
    "macAddress":None,
    "width":0,
    "height":0,
    "channel":None,
    "sign":None,
    "clientIp":None,
    "data":{
        "loanId":1,
        "prodType":203,
        "immediateFamilyName":"",
        "immediateFamilyRelation":"秘密",
        "immediateFamilyPhone":"13811111111",
        "colleagueName":"同事3",
        "colleaguePhone":"13822222222",
        "relativeName":"张三",
        "relativePhone":"15995788425",
        "relativeCardNo":"32038219955154498754",
        "relativeWorkUnit":"中国移动",
        "relativeWorkUnitAddr":"1234#5678#5555#xxxxxx",
        "relativeWorkUnitAddrStr":"江苏省苏州市工业园区xxxxx",
        "relativeWorkUnitPhone":"15995788524",
        "relativeJob":1,
        "action":"U"
    }
}


payload_immediateFamilyRelation = {
    "platform":"android",
    "app_version":None,
    "os_version":None,
    "phone_model":None,
    "service_provider":0,
    "network_type":0,
    "session_token":"F3DF832B5CB2E9A52D25EACB179AC1E7",
    "imei":None,
    "macAddress":None,
    "width":0,
    "height":0,
    "channel":None,
    "sign":None,
    "clientIp":None,
    "data":{
        "loanId":1,
        "prodType":203,
        "immediateFamilyName":"ceshi",
        "immediateFamilyRelation":"",
        "immediateFamilyPhone":"13811111111",
        "colleagueName":"同事3",
        "colleaguePhone":"13822222222",
        "relativeName":"张三",
        "relativePhone":"15995788425",
        "relativeCardNo":"32038219955154498754",
        "relativeWorkUnit":"中国移动",
        "relativeWorkUnitAddr":"1234#5678#5555#xxxxxx",
        "relativeWorkUnitAddrStr":"江苏省苏州市工业园区xxxxx",
        "relativeWorkUnitPhone":"15995788524",
        "relativeJob":1,
        "action":"U"
    }
}




payload_immediateFamilyPhone = {
    "platform":"android",
    "app_version":None,
    "os_version":None,
    "phone_model":None,
    "service_provider":0,
    "network_type":0,
    "session_token":"F3DF832B5CB2E9A52D25EACB179AC1E7",
    "imei":None,
    "macAddress":None,
    "width":0,
    "height":0,
    "channel":None,
    "sign":None,
    "clientIp":None,
    "data":{
        "loanId":1,
        "prodType":203,
        "immediateFamilyName":"ceshi",
        "immediateFamilyRelation":"ceshi",
        "immediateFamilyPhone":"",
        "colleagueName":"同事3",
        "colleaguePhone":"13822222222",
        "relativeName":"张三",
        "relativePhone":"15995788425",
        "relativeCardNo":"32038219955154498754",
        "relativeWorkUnit":"中国移动",
        "relativeWorkUnitAddr":"1234#5678#5555#xxxxxx",
        "relativeWorkUnitAddrStr":"江苏省苏州市工业园区xxxxx",
        "relativeWorkUnitPhone":"15995788524",
        "relativeJob":1,
        "action":"U"
    }
}




payload_colleagueName = {
    "platform":"android",
    "app_version":None,
    "os_version":None,
    "phone_model":None,
    "service_provider":0,
    "network_type":0,
    "session_token":"F3DF832B5CB2E9A52D25EACB179AC1E7",
    "imei":None,
    "macAddress":None,
    "width":0,
    "height":0,
    "channel":None,
    "sign":None,
    "clientIp":None,
    "data":{
        "loanId":1,
        "prodType":203,
        "immediateFamilyName":"ffff",
        "immediateFamilyRelation":"秘密",
        "immediateFamilyPhone":"13811111111",
        "colleagueName":"",
        "colleaguePhone":"13822222222",
        "relativeName":"张三",
        "relativePhone":"15995788425",
        "relativeCardNo":"32038219955154498754",
        "relativeWorkUnit":"中国移动",
        "relativeWorkUnitAddr":"1234#5678#5555#xxxxxx",
        "relativeWorkUnitAddrStr":"江苏省苏州市工业园区xxxxx",
        "relativeWorkUnitPhone":"15995788524",
        "relativeJob":1,
        "action":"U"
    }
}



payload_colleaguePhone = {
    "platform":"android",
    "app_version":None,
    "os_version":None,
    "phone_model":None,
    "service_provider":0,
    "network_type":0,
    "session_token":"F3DF832B5CB2E9A52D25EACB179AC1E7",
    "imei":None,
    "macAddress":None,
    "width":0,
    "height":0,
    "channel":None,
    "sign":None,
    "clientIp":None,
    "data":{
        "loanId":1,
        "prodType":203,
        "immediateFamilyName":"ifn",
        "immediateFamilyRelation":"秘密",
        "immediateFamilyPhone":"13811111111",
        "colleagueName":"同事3",
        "colleaguePhone":"",
        "relativeName":"张三",
        "relativePhone":"15995788425",
        "relativeCardNo":"32038219955154498754",
        "relativeWorkUnit":"中国移动",
        "relativeWorkUnitAddr":"1234#5678#5555#xxxxxx",
        "relativeWorkUnitAddrStr":"江苏省苏州市工业园区xxxxx",
        "relativeWorkUnitPhone":"15995788524",
        "relativeJob":1,
        "action":"U"
    }
}




payload_relativeName = {
    "platform":"android",
    "app_version":None,
    "os_version":None,
    "phone_model":None,
    "service_provider":0,
    "network_type":0,
    "session_token":"F3DF832B5CB2E9A52D25EACB179AC1E7",
    "imei":None,
    "macAddress":None,
    "width":0,
    "height":0,
    "channel":None,
    "sign":None,
    "clientIp":None,
    "data":{
        "loanId":1,
        "prodType":203,
        "immediateFamilyName":"ifn",
        "immediateFamilyRelation":"秘密",
        "immediateFamilyPhone":"13811111111",
        "colleagueName":"同事3",
        "colleaguePhone":"13822222222",
        "relativeName":"",
        "relativePhone":"15995788425",
        "relativeCardNo":"32038219955154498754",
        "relativeWorkUnit":"中国移动",
        "relativeWorkUnitAddr":"1234#5678#5555#xxxxxx",
        "relativeWorkUnitAddrStr":"江苏省苏州市工业园区xxxxx",
        "relativeWorkUnitPhone":"15995788524",
        "relativeJob":1,
        "action":"U"
    }
}



payload_relativePhone = {
    "platform":"android",
    "app_version":None,
    "os_version":None,
    "phone_model":None,
    "service_provider":0,
    "network_type":0,
    "session_token":"F3DF832B5CB2E9A52D25EACB179AC1E7",
    "imei":None,
    "macAddress":None,
    "width":0,
    "height":0,
    "channel":None,
    "sign":None,
    "clientIp":None,
    "data":{
        "loanId":1,
        "prodType":203,
        "immediateFamilyName":"ifn",
        "immediateFamilyRelation":"秘密",
        "immediateFamilyPhone":"13811111111",
        "colleagueName":"同事3",
        "colleaguePhone":"13822222222",
        "relativeName":"张三",
        "relativePhone":"",
        "relativeCardNo":"32038219955154498754",
        "relativeWorkUnit":"中国移动",
        "relativeWorkUnitAddr":"1234#5678#5555#xxxxxx",
        "relativeWorkUnitAddrStr":"江苏省苏州市工业园区xxxxx",
        "relativeWorkUnitPhone":"15995788524",
        "relativeJob":1,
        "action":"U"
    }
}



payload_relativeCardNo= {
    "platform":"android",
    "app_version":None,
    "os_version":None,
    "phone_model":None,
    "service_provider":0,
    "network_type":0,
    "session_token":"F3DF832B5CB2E9A52D25EACB179AC1E7",
    "imei":None,
    "macAddress":None,
    "width":0,
    "height":0,
    "channel":None,
    "sign":None,
    "clientIp":None,
    "data":{
        "loanId":1,
        "prodType":203,
        "immediateFamilyName":"ifn",
        "immediateFamilyRelation":"秘密",
        "immediateFamilyPhone":"13811111111",
        "colleagueName":"同事3",
        "colleaguePhone":"13822222222",
        "relativeName":"张三",
        "relativePhone":"15995788425",
        "relativeCardNo":"",
        "relativeWorkUnit":"中国移动",
        "relativeWorkUnitAddr":"1234#5678#5555#xxxxxx",
        "relativeWorkUnitAddrStr":"江苏省苏州市工业园区xxxxx",
        "relativeWorkUnitPhone":"15995788524",
        "relativeJob":1,
        "action":"U"
    }
}



payload_relativeWorkUnit= {
    "platform":"android",
    "app_version":None,
    "os_version":None,
    "phone_model":None,
    "service_provider":0,
    "network_type":0,
    "session_token":"F3DF832B5CB2E9A52D25EACB179AC1E7",
    "imei":None,
    "macAddress":None,
    "width":0,
    "height":0,
    "channel":None,
    "sign":None,
    "clientIp":None,
    "data":{
        "loanId":1,
        "prodType":203,
        "immediateFamilyName":"ifn",
        "immediateFamilyRelation":"秘密",
        "immediateFamilyPhone":"13811111111",
        "colleagueName":"同事3",
        "colleaguePhone":"13822222222",
        "relativeName":"张三",
        "relativePhone":"15995788425",
        "relativeCardNo":"32038219955154498754",
        "relativeWorkUnit":"",
        "relativeWorkUnitAddr":"1234#5678#5555#xxxxxx",
        "relativeWorkUnitAddrStr":"江苏省苏州市工业园区xxxxx",
        "relativeWorkUnitPhone":"15995788524",
        "relativeJob":1,
        "action":"U"
    }
}



payload_relativeWorkUnitAddr = {
    "platform":"android",
    "app_version":None,
    "os_version":None,
    "phone_model":None,
    "service_provider":0,
    "network_type":0,
    "session_token":"F3DF832B5CB2E9A52D25EACB179AC1E7",
    "imei":None,
    "macAddress":None,
    "width":0,
    "height":0,
    "channel":None,
    "sign":None,
    "clientIp":None,
    "data":{
        "loanId":1,
        "prodType":203,
        "immediateFamilyName":"ifn",
        "immediateFamilyRelation":"秘密",
        "immediateFamilyPhone":"13811111111",
        "colleagueName":"同事3",
        "colleaguePhone":"13822222222",
        "relativeName":"张三",
        "relativePhone":"15995788425",
        "relativeCardNo":"32038219955154498754",
        "relativeWorkUnit":"中国移动",
        "relativeWorkUnitAddr":"",
        "relativeWorkUnitAddrStr":"江苏省苏州市工业园区xxxxx",
        "relativeWorkUnitPhone":"15995788524",
        "relativeJob":1,
        "action":"U"
    }
}


payload_relativeWorkUnitPhone = {
    "platform":"android",
    "app_version":None,
    "os_version":None,
    "phone_model":None,
    "service_provider":0,
    "network_type":0,
    "session_token":"F3DF832B5CB2E9A52D25EACB179AC1E7",
    "imei":None,
    "macAddress":None,
    "width":0,
    "height":0,
    "channel":None,
    "sign":None,
    "clientIp":None,
    "data":{
        "loanId":1,
        "prodType":203,
        "immediateFamilyName":"ifn",
        "immediateFamilyRelation":"秘密",
        "immediateFamilyPhone":"13811111111",
        "colleagueName":"同事3",
        "colleaguePhone":"13822222222",
        "relativeName":"张三",
        "relativePhone":"15995788425",
        "relativeCardNo":"32038219955154498754",
        "relativeWorkUnit":"中国移动",
        "relativeWorkUnitAddr":"1234#5678#5555#xxxxxx",
        "relativeWorkUnitAddrStr":"江苏省苏州市工业园区xxxxx",
        "relativeWorkUnitPhone":"",
        "relativeJob":1,
        "action":"U"
    }
}



payload_relativeJob = {
    "platform":"android",
    "app_version":None,
    "os_version":None,
    "phone_model":None,
    "service_provider":0,
    "network_type":0,
    "session_token":"F3DF832B5CB2E9A52D25EACB179AC1E7",
    "imei":None,
    "macAddress":None,
    "width":0,
    "height":0,
    "channel":None,
    "sign":None,
    "clientIp":None,
    "data":{
        "loanId":1,
        "prodType":203,
        "immediateFamilyName":"ifn",
        "immediateFamilyRelation":"秘密",
        "immediateFamilyPhone":"13811111111",
        "colleagueName":"同事3",
        "colleaguePhone":"13822222222",
        "relativeName":"张三",
        "relativePhone":"15995788425",
        "relativeCardNo":"32038219955154498754",
        "relativeWorkUnit":"中国移动",
        "relativeWorkUnitAddr":"1234#5678#5555#xxxxxx",
        "relativeWorkUnitAddrStr":"江苏省苏州市工业园区xxxxx",
        "relativeWorkUnitPhone":"15995788524",
        "relativeJob":"",
        "action":"U"
    }
}



class PostRelativeInfo(unittest.TestCase):
    """个人信息接口测试"""

    def setUp(self):
        self.url = "http://172.16.88.167:5959/xiangfa/borrowerRegular/v1/relativeInfo.json"

    def test_post_payload_immediateFamilyName(self):
        '''不填直系亲属姓名'''
        r = requests.post(self.url, None, payload_immediateFamilyName)
        print (r.status_code)
        print (r.text)

    def test_post_payload_immediateFamilyRelation(self):
        '''不填直系亲属关系'''
        r = requests.post(self.url, None, payload_immediateFamilyRelation)
        print (r.status_code)
        print (r.text)


    def test_post_payload_immediateFamilyPhone(self):
        '''不填直系亲属手机号'''
        r = requests.post(self.url, None, payload_immediateFamilyPhone)
        print (r.status_code)
        print (r.text)



    def test_post_payload_colleagueName(self):
        '''不填同事姓名'''
        r = requests.post(self.url, None, payload_colleagueName)
        print (r.status_code)
        print (r.text)



    def test_post_payload_colleaguePhone(self):
        '''不填同事手机号'''
        r = requests.post(self.url, None, payload_colleaguePhone)
        print (r.status_code)
        print (r.text)



    def test_post_payload_relativeName(self):
        '''不填配偶姓名-选填项'''
        r = requests.post(self.url, None, payload_relativeName)
        print (r.status_code)
        print (r.text)


    def test_post_payload_relativePhone(self):
        '''不填配偶手机号-选填项'''
        r = requests.post(self.url, None, payload_relativePhone)
        print (r.status_code)
        print (r.text)


    def test_post_payload_relativeCardNo(self):
        '''不填配偶身份证号-选填项'''
        r = requests.post(self.url, None, payload_relativeCardNo)
        print (r.status_code)
        print (r.text)


    def test_post_payload_relativeWorkUnit(self):
        '''不填配偶单位-选填项'''
        r = requests.post(self.url, None, payload_relativeWorkUnit)
        print (r.status_code)
        print (r.text)


    def test_post_payload_relativeWorkUnitAddr(self):
        '''不填配偶单位地址-选填项'''
        r = requests.post(self.url, None, payload_relativeWorkUnitAddr)
        print (r.status_code)
        print (r.text)

    def test_post_payload_relativeWorkUnitPhone(self):
        '''不填配偶单位电话-选填项'''
        r = requests.post(self.url, None, payload_relativeWorkUnitPhone)
        print (r.status_code)
        print (r.text)


    def test_post_payload_relativeJob(self):
        '''不填配偶职位-选填项'''
        r = requests.post(self.url, None, payload_relativeJob)
        print (r.status_code)
        print (r.text)





if __name__ == '__main__':
    RelativeInfoTests = unittest.TestLoader().loadTestsFromTestCase(PostRelativeInfo)
    smoke_tests = unittest.TestSuite(RelativeInfoTests)
    outfile = open("D:\SunFit_Python_Automated_Testing\Xiangfa_Backend_REST_API\E-CheDai\TestReport\RelativeInfoTestResult.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=outfile,
        title='relativeinfo test report',
        description='relativeinfo test report'
    )
    runner.run(smoke_tests)
