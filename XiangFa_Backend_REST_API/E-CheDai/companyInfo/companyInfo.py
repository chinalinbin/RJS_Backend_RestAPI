# -*- coding:utf-8 -*-


import requests
import unittest
import nose
import HTMLTestRunner
import sys




payload_companyName = {
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
        "jobReq":[
            {
                "borrowerRegularJobDTOs":[
                    {
                        "prodType":203,
                        "category":1,
                        "subType":1,
                        "contentUrl":"loanftptest/a/ic/2017/02bb/1487233996583238.jpg",
                        "contentSize":"1662178",
                        "sContentUrl":"loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx":1,
                        "type":17,
                        "path":None,
                        "loanId":1
                    }
                ]
            },
            {
                "borrowerRegularJobDTOs":[
                    {
                        "prodType":203,
                        "category":1,
                        "subType":-1,
                        "contentUrl":"loanftptest/a/pu/17/02dd/13/2009_t21_60.jpg",
                        "contentSize":"1662178",
                        "sContentUrl":"loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx":1,
                        "type":18,
                        "path":None,
                        "loanId":1
                    }
                ]
            }
        ],
        "loanId":1,
        "prodType":203,
        "companyName":"",
        "companyAddr":"01234567890123456789012345678901234567890123456789012345678901234567890123456789",
        "companyAddrStr":"",
        "companyPhone":"1",
        "workingYears":"0",
        "companyDepartment":"有关部门",
        "companyJob":1,
        "companySalary":1123,
        "companyPaymentMethod":1,
        "socialSecurityNo":"sfnsdkjfn2313",
        "action":"U"
    }
}

payload_companyAddr = {
    "platform":"android",
    "app_version":None,
    "os_version":None,
    "phone_model":None,
    "service_provider":0,
    "network_type":0,
    "session_token":"41340004CD64B93918A25E77A3F0EC70",
    "imei":None,
    "macAddress":None,
    "width":0,
    "height":0,
    "channel":None,
    "sign":None,
    "clientIp":None,
    "data":{
        "jobReq":[
            {
                "borrowerRegularJobDTOs":[
                    {
                        "prodType":203,
                        "category":1,
                        "subType":1,
                        "contentUrl":"loanftptest/a/ic/2017/02bb/1487233996583238.jpg",
                        "contentSize":"1662178",
                        "sContentUrl":"loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx":1,
                        "type":17,
                        "path":None,
                        "loanId":1
                    }
                ]
            },
            {
                "borrowerRegularJobDTOs":[
                    {
                        "prodType":203,
                        "category":1,
                        "subType":-1,
                        "contentUrl":"loanftptest/a/pu/17/02dd/13/2009_t21_60.jpg",
                        "contentSize":"1662178",
                        "sContentUrl":"loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx":1,
                        "type":18,
                        "path":None,
                        "loanId":1
                    }
                ]
            }
        ],
        "loanId":1,
        "prodType":203,
        "companyName":"ceshi",
        "companyAddr":"",
        "companyAddrStr":"",
        "companyPhone":"1",
        "workingYears":"0",
        "companyDepartment":"有关部门",
        "companyJob":1,
        "companySalary":1123,
        "companyPaymentMethod":1,
        "socialSecurityNo":"sfnsdkjfn2313",
        "action":"U"
    }
}


payload_companyPhone = {
    "platform":"android",
    "app_version":None,
    "os_version":None,
    "phone_model":None,
    "service_provider":0,
    "network_type":0,
    "session_token":"41340004CD64B93918A25E77A3F0EC70",
    "imei":None,
    "macAddress":None,
    "width":0,
    "height":0,
    "channel":None,
    "sign":None,
    "clientIp":None,
    "data":{
        "jobReq":[
            {
                "borrowerRegularJobDTOs":[
                    {
                        "prodType":203,
                        "category":1,
                        "subType":1,
                        "contentUrl":"loanftptest/a/ic/2017/02bb/1487233996583238.jpg",
                        "contentSize":"1662178",
                        "sContentUrl":"loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx":1,
                        "type":17,
                        "path":None,
                        "loanId":1
                    }
                ]
            },
            {
                "borrowerRegularJobDTOs":[
                    {
                        "prodType":203,
                        "category":1,
                        "subType":-1,
                        "contentUrl":"loanftptest/a/pu/17/02dd/13/2009_t21_60.jpg",
                        "contentSize":"1662178",
                        "sContentUrl":"loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx":1,
                        "type":18,
                        "path":None,
                        "loanId":1
                    }
                ]
            }
        ],
        "loanId":1,
        "prodType":203,
        "companyName":"ceshi",
        "companyAddr":"ceshi",
        "companyAddrStr":"",
        "companyPhone":"",
        "workingYears":"0",
        "companyDepartment":"有关部门",
        "companyJob":1,
        "companySalary":1123,
        "companyPaymentMethod":1,
        "socialSecurityNo":"sfnsdkjfn2313",
        "action":"U"
    }
}


payload_workingYears = {
    "platform":"android",
    "app_version":None,
    "os_version":None,
    "phone_model":None,
    "service_provider":0,
    "network_type":0,
    "session_token":"41340004CD64B93918A25E77A3F0EC70",
    "imei":None,
    "macAddress":None,
    "width":0,
    "height":0,
    "channel":None,
    "sign":None,
    "clientIp":None,
    "data":{
        "jobReq":[
            {
                "borrowerRegularJobDTOs":[
                    {
                        "prodType":203,
                        "category":1,
                        "subType":1,
                        "contentUrl":"loanftptest/a/ic/2017/02bb/1487233996583238.jpg",
                        "contentSize":"1662178",
                        "sContentUrl":"loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx":1,
                        "type":17,
                        "path":None,
                        "loanId":1
                    }
                ]
            },
            {
                "borrowerRegularJobDTOs":[
                    {
                        "prodType":203,
                        "category":1,
                        "subType":-1,
                        "contentUrl":"loanftptest/a/pu/17/02dd/13/2009_t21_60.jpg",
                        "contentSize":"1662178",
                        "sContentUrl":"loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx":1,
                        "type":18,
                        "path":None,
                        "loanId":1
                    }
                ]
            }
        ],
        "loanId":1,
        "prodType":203,
        "companyName":"ceshi",
        "companyAddr":"ceshi",
        "companyAddrStr":"",
        "companyPhone":"051288665500",
        "workingYears":"",
        "companyDepartment":"有关部门",
        "companyJob":1,
        "companySalary":1123,
        "companyPaymentMethod":1,
        "socialSecurityNo":"sfnsdkjfn2313",
        "action":"U"
    }
}




payload_companyDepartment = {
    "platform":"android",
    "app_version":None,
    "os_version":None,
    "phone_model":None,
    "service_provider":0,
    "network_type":0,
    "session_token":"41340004CD64B93918A25E77A3F0EC70",
    "imei":None,
    "macAddress":None,
    "width":0,
    "height":0,
    "channel":None,
    "sign":None,
    "clientIp":None,
    "data":{
        "jobReq":[
            {
                "borrowerRegularJobDTOs":[
                    {
                        "prodType":203,
                        "category":1,
                        "subType":1,
                        "contentUrl":"loanftptest/a/ic/2017/02bb/1487233996583238.jpg",
                        "contentSize":"1662178",
                        "sContentUrl":"loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx":1,
                        "type":17,
                        "path":None,
                        "loanId":1
                    }
                ]
            },
            {
                "borrowerRegularJobDTOs":[
                    {
                        "prodType":203,
                        "category":1,
                        "subType":-1,
                        "contentUrl":"loanftptest/a/pu/17/02dd/13/2009_t21_60.jpg",
                        "contentSize":"1662178",
                        "sContentUrl":"loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx":1,
                        "type":18,
                        "path":None,
                        "loanId":1
                    }
                ]
            }
        ],
        "loanId":1,
        "prodType":203,
        "companyName":"ceshi",
        "companyAddr":"ceshi",
        "companyAddrStr":"",
        "companyPhone":"051288665500",
        "workingYears":"1",
        "companyDepartment":"",
        "companyJob":1,
        "companySalary":1123,
        "companyPaymentMethod":1,
        "socialSecurityNo":"sfnsdkjfn2313",
        "action":"U"
    }
}




payload_companyJob = {
    "platform":"android",
    "app_version":None,
    "os_version":None,
    "phone_model":None,
    "service_provider":0,
    "network_type":0,
    "session_token":"41340004CD64B93918A25E77A3F0EC70",
    "imei":None,
    "macAddress":None,
    "width":0,
    "height":0,
    "channel":None,
    "sign":None,
    "clientIp":None,
    "data":{
        "jobReq":[
            {
                "borrowerRegularJobDTOs":[
                    {
                        "prodType":203,
                        "category":1,
                        "subType":1,
                        "contentUrl":"loanftptest/a/ic/2017/02bb/1487233996583238.jpg",
                        "contentSize":"1662178",
                        "sContentUrl":"loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx":1,
                        "type":17,
                        "path":None,
                        "loanId":1
                    }
                ]
            },
            {
                "borrowerRegularJobDTOs":[
                    {
                        "prodType":203,
                        "category":1,
                        "subType":-1,
                        "contentUrl":"loanftptest/a/pu/17/02dd/13/2009_t21_60.jpg",
                        "contentSize":"1662178",
                        "sContentUrl":"loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx":1,
                        "type":18,
                        "path":None,
                        "loanId":1
                    }
                ]
            }
        ],
        "loanId":1,
        "prodType":203,
        "companyName":"ceshi",
        "companyAddr":"ceshi",
        "companyAddrStr":"",
        "companyPhone":"051288665500",
        "workingYears":"1",
        "companyDepartment":"ceshi",
        "companyJob":"",
        "companySalary":1123,
        "companyPaymentMethod":1,
        "socialSecurityNo":"sfnsdkjfn2313",
        "action":"U"
    }
}


payload_companySalary = {
    "platform":"android",
    "app_version":None,
    "os_version":None,
    "phone_model":None,
    "service_provider":0,
    "network_type":0,
    "session_token":"41340004CD64B93918A25E77A3F0EC70",
    "imei":None,
    "macAddress":None,
    "width":0,
    "height":0,
    "channel":None,
    "sign":None,
    "clientIp":None,
    "data":{
        "jobReq":[
            {
                "borrowerRegularJobDTOs":[
                    {
                        "prodType":203,
                        "category":1,
                        "subType":1,
                        "contentUrl":"loanftptest/a/ic/2017/02bb/1487233996583238.jpg",
                        "contentSize":"1662178",
                        "sContentUrl":"loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx":1,
                        "type":17,
                        "path":None,
                        "loanId":1
                    }
                ]
            },
            {
                "borrowerRegularJobDTOs":[
                    {
                        "prodType":203,
                        "category":1,
                        "subType":-1,
                        "contentUrl":"loanftptest/a/pu/17/02dd/13/2009_t21_60.jpg",
                        "contentSize":"1662178",
                        "sContentUrl":"loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx":1,
                        "type":18,
                        "path":None,
                        "loanId":1
                    }
                ]
            }
        ],
        "loanId":1,
        "prodType":203,
        "companyName":"ceshi",
        "companyAddr":"ceshi",
        "companyAddrStr":"",
        "companyPhone":"051288665500",
        "workingYears":"1",
        "companyDepartment":"ceshi",
        "companyJob":"3",
        "companySalary":"",
        "companyPaymentMethod":1,
        "socialSecurityNo":"sfnsdkjfn2313",
        "action":"U"
    }
}

payload_companyPaymentMethod = {
    "platform":"android",
    "app_version":None,
    "os_version":None,
    "phone_model":None,
    "service_provider":0,
    "network_type":0,
    "session_token":"41340004CD64B93918A25E77A3F0EC70",
    "imei":None,
    "macAddress":None,
    "width":0,
    "height":0,
    "channel":None,
    "sign":None,
    "clientIp":None,
    "data":{
        "jobReq":[
            {
                "borrowerRegularJobDTOs":[
                    {
                        "prodType":203,
                        "category":1,
                        "subType":1,
                        "contentUrl":"loanftptest/a/ic/2017/02bb/1487233996583238.jpg",
                        "contentSize":"1662178",
                        "sContentUrl":"loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx":1,
                        "type":17,
                        "path":None,
                        "loanId":1
                    }
                ]
            },
            {
                "borrowerRegularJobDTOs":[
                    {
                        "prodType":203,
                        "category":1,
                        "subType":-1,
                        "contentUrl":"loanftptest/a/pu/17/02dd/13/2009_t21_60.jpg",
                        "contentSize":"1662178",
                        "sContentUrl":"loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx":1,
                        "type":18,
                        "path":None,
                        "loanId":1
                    }
                ]
            }
        ],
        "loanId":1,
        "prodType":203,
        "companyName":"ceshi",
        "companyAddr":"ceshi",
        "companyAddrStr":"",
        "companyPhone":"051288665500",
        "workingYears":"1",
        "companyDepartment":"ceshi",
        "companyJob":"3",
        "companySalary":3000,
        "companyPaymentMethod":"",
        "socialSecurityNo":"sfnsdkjfn2313",
        "action":"U"
    }
}






class PostCompanyInfo(unittest.TestCase):
    """个人信息接口测试"""

    def setUp(self):
        self.url = "http://172.16.88.167:5959/xiangfa/borrowerRegular/v1/companyInfo.json"


    def test_post_payload_companyName(self):
        '''不填写公司名'''
        r = requests.post(self.url,None,payload_companyName)
        print (r.status_code)
        print (r.text)

    def test_post_payload_companyAddr(self):
        '''不填写公司地址'''
        r = requests.post(self.url,None,payload_companyAddr)
        print (r.status_code)
        print (r.text)

    def test_post_payload_companyPhone(self):
        '''不填写单位电话'''
        r = requests.post(self.url,None,payload_companyPhone)
        print (r.status_code)
        print (r.text)

    def test_post_payload_workingYears(self):
        '''不填写工作年限'''
        r = requests.post(self.url, None,payload_workingYears)
        print (r.status_code)
        print (r.text)

    def test_post_payload_companyJob(self):
        '''不填写职务'''
        r = requests.post(self.url, None, payload_companyJob )
        print (r.status_code)
        print (r.text)

    def test_post_payload_companySalary(self):
        '''不填写月收入'''
        r = requests.post(self.url, None, payload_companySalary)
        print (r.status_code)
        print (r.text)

    def test_post_payload_companyDepartment(self):
        '''不填写部门'''
        r = requests.post(self.url, None, payload_companyDepartment)
        print (r.status_code)
        print (r.text)

    def test_post_payload_companyPaymentMethod(self):
        '''不填写支付方式'''
        r = requests.post(self.url, None, payload_companyPaymentMethod)
        print (r.status_code)
        print (r.text)






if __name__== '__main__':
    companyInfoTests = unittest.TestLoader().loadTestsFromTestCase(PostCompanyInfo)
    smoke_tests = unittest.TestSuite(companyInfoTests)
    outfile = open("D:\SunFit_Python_Automated_Testing\Xiangfa_Backend_REST_API\E-CheDai\TestReport\companyInfoTestResult.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=outfile,
        title='companyinfo test report',
        description='companyinfo test report'
    )
    runner.run(smoke_tests)
