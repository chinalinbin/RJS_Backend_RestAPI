# -*- coding:utf-8 -*-

import requests
import unittest
import HTMLTestRunner
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

payload_cardName = {
    "platform": "android",
    "app_version": None,
    "os_version": None,
    "phone_model": None,
    "service_provider": 0,
    "network_type": 0,
    "session_token": "5481831BFEF423DEE11E1CA88CB98D47",
    "imei": None,
    "macAddress": None,
    "width": 0,
    "height": 0,
    "channel": None,
    "sign": None,
    "clientIp": None,
    "data": {
        "jobReq": [
            {
                "borrowerRegularJobDTOs": [
                    {
                        "prodType": 203,
                        "category": 1,
                        "subType": -1,
                        "contentUrl": "loanftptest/a/ic/2017/02bb/1487233996583238.jpg",
                        "contentSize": "1662178",
                        "sContentUrl": "loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx": 1,
                        "type": 12,
                        "path": None,
                        "loanId": 1
                    }
                ]
            },
            {
                "borrowerRegularJobDTOs": [
                    {
                        "prodType": 203,
                        "category": 1,
                        "subType": -1,
                        "contentUrl": "loanftptest/a/pu/17/02dd/13/2009_t21_60.jpg",
                        "contentSize": "1662178",
                        "sContentUrl": "loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx": 1,
                        "type": 13,
                        "path": None,
                        "loanId": 1
                    }
                ]
            }
        ],
        "loanId": 1,
        "prodType": 203,
        "applyBuzType": 1,
        "loanMoney": 12,
        "installment": 3,
        "job": 0,
        "loanPurposes": "4",
        "loanPurposesType": "",
        "loanPurposesOther": "",
        "cardName": "",
        "sex": 2,
        "birthday": "1989-12-08",
        "cardNo": "320382198905199475",
        "cardExpireDateShow": "2027-01-01",
        "cardExpireDate": "288888",
        "cardAddr": "110000#110100#110101#天天通过沟沟壑壑",
        "csardAddrStr": "江苏省苏州市xxxxxxx",
        "education": None,
        "maritalStatus": 1,
        "children": 1,
        "address": "110000#110100#110101#天天通过沟沟壑壑",
        "addressStr": "江苏省苏州市xxxxxxx",
        "mobileNo": "13063835945",
        "phoneServicePwd": "123123",
        "housingCategory": None,
        "rent": None,
        "phone": "15995788425",
        "email": "15995788425@qq.com",
        "im1": 15995788425,
        "moveToDateStr": "2017-02-01",
        "settledFromStr": "2017-02-02",
        "action": "U"
    }
}

payload_birthday = {
    "platform": "android",
    "app_version": None,
    "os_version": None,
    "phone_model": None,
    "service_provider": 0,
    "network_type": 0,
    "session_token": "41340004CD64B93918A25E77A3F0EC70",
    "imei": None,
    "macAddress": None,
    "width": 0,
    "height": 0,
    "channel": None,
    "sign": None,
    "clientIp": None,
    "data": {
        "jobReq": [
            {
                "borrowerRegularJobDTOs": [
                    {
                        "prodType": 203,
                        "category": 1,
                        "subType": -1,
                        "contentUrl": "loanftptest/a/ic/2017/02bb/1487233996583238.jpg",
                        "contentSize": "1662178",
                        "sContentUrl": "loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx": 1,
                        "type": 12,
                        "path": None,
                        "loanId": 1
                    }
                ]
            },
            {
                "borrowerRegularJobDTOs": [
                    {
                        "prodType": 203,
                        "category": 1,
                        "subType": -1,
                        "contentUrl": "loanftptest/a/pu/17/02dd/13/2009_t21_60.jpg",
                        "contentSize": "1662178",
                        "sContentUrl": "loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx": 1,
                        "type": 13,
                        "path": None,
                        "loanId": 1
                    }
                ]
            }
        ],
        "loanId": 1,
        "prodType": 203,
        "applyBuzType": 1,
        "loanMoney": 12,
        "installment": 3,
        "job": 0,
        "loanPurposes": "4",
        "loanPurposesType": "",
        "loanPurposesOther": "",
        "cardName": "012345678",
        "sex": 2,
        "birthday": "",
        "cardNo": "320382198905199475",
        "cardExpireDateShow": "2027-01-01",
        "cardExpireDate": "288888",
        "cardAddr": "110000#110100#110101#天天通过沟沟壑壑",
        "csardAddrStr": "江苏省苏州市xxxxxxx",
        "education": None,
        "maritalStatus": 1,
        "children": 1,
        "address": "110000#110100#110101#天天通过沟沟壑壑",
        "addressStr": "江苏省苏州市xxxxxxx",
        "mobileNo": "13063835945",
        "phoneServicePwd": "123123",
        "housingCategory": None,
        "rent": None,
        "phone": "15995788425",
        "email": "15995788425@qq.com",
        "im1": 15995788425,
        "moveToDateStr": "2017-02-01",
        "settledFromStr": "2017-02-02",
        "action": "U"
    }
}

payload_cardNo = {
    "platform": "android",
    "app_version": None,
    "os_version": None,
    "phone_model": None,
    "service_provider": 0,
    "network_type": 0,
    "session_token": "41340004CD64B93918A25E77A3F0EC70",
    "imei": None,
    "macAddress": None,
    "width": 0,
    "height": 0,
    "channel": None,
    "sign": None,
    "clientIp": None,
    "data": {
        "jobReq": [
            {
                "borrowerRegularJobDTOs": [
                    {
                        "prodType": 203,
                        "category": 1,
                        "subType": -1,
                        "contentUrl": "loanftptest/a/ic/2017/02bb/1487233996583238.jpg",
                        "contentSize": "1662178",
                        "sContentUrl": "loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx": 1,
                        "type": 12,
                        "path": None,
                        "loanId": 1
                    }
                ]
            },
            {
                "borrowerRegularJobDTOs": [
                    {
                        "prodType": 203,
                        "category": 1,
                        "subType": -1,
                        "contentUrl": "loanftptest/a/pu/17/02dd/13/2009_t21_60.jpg",
                        "contentSize": "1662178",
                        "sContentUrl": "loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx": 1,
                        "type": 13,
                        "path": None,
                        "loanId": 1
                    }
                ]
            }
        ],
        "loanId": 1,
        "prodType": 203,
        "applyBuzType": 1,
        "loanMoney": 12,
        "installment": 3,
        "job": 0,
        "loanPurposes": "4",
        "loanPurposesType": "",
        "loanPurposesOther": "",
        "cardName": "012345678",
        "sex": 2,
        "birthday": "1989-12-08",
        "cardNo": "",
        "cardExpireDateShow": "2027-01-01",
        "cardExpireDate": "288888",
        "cardAddr": "110000#110100#110101#天天通过沟沟壑壑",
        "csardAddrStr": "江苏省苏州市xxxxxxx",
        "education": None,
        "maritalStatus": 1,
        "children": 1,
        "address": "110000#110100#110101#天天通过沟沟壑壑",
        "addressStr": "江苏省苏州市xxxxxxx",
        "mobileNo": "13063835945",
        "phoneServicePwd": "123123",
        "housingCategory": None,
        "rent": None,
        "phone": "15995788425",
        "email": "15995788425@qq.com",
        "im1": 15995788425,
        "moveToDateStr": "2017-02-01",
        "settledFromStr": "2017-02-02",
        "action": "U"
    }
}

payload_cardExpireDateShow = {
    "platform": "android",
    "app_version": None,
    "os_version": None,
    "phone_model": None,
    "service_provider": 0,
    "network_type": 0,
    "session_token": "41340004CD64B93918A25E77A3F0EC70",
    "imei": None,
    "macAddress": None,
    "width": 0,
    "height": 0,
    "channel": None,
    "sign": None,
    "clientIp": None,
    "data": {
        "jobReq": [
            {
                "borrowerRegularJobDTOs": [
                    {
                        "prodType": 203,
                        "category": 1,
                        "subType": -1,
                        "contentUrl": "loanftptest/a/ic/2017/02bb/1487233996583238.jpg",
                        "contentSize": "1662178",
                        "sContentUrl": "loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx": 1,
                        "type": 12,
                        "path": None,
                        "loanId": 1
                    }
                ]
            },
            {
                "borrowerRegularJobDTOs": [
                    {
                        "prodType": 203,
                        "category": 1,
                        "subType": -1,
                        "contentUrl": "loanftptest/a/pu/17/02dd/13/2009_t21_60.jpg",
                        "contentSize": "1662178",
                        "sContentUrl": "loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx": 1,
                        "type": 13,
                        "path": None,
                        "loanId": 1
                    }
                ]
            }
        ],
        "loanId": 1,
        "prodType": 203,
        "applyBuzType": 1,
        "loanMoney": 12,
        "installment": 3,
        "job": 0,
        "loanPurposes": "4",
        "loanPurposesType": "",
        "loanPurposesOther": "",
        "cardName": "012345678",
        "sex": 2,
        "birthday": "1989-12-08",
        "cardNo": "320382198905199475",
        "cardExpireDateShow": "",
        "cardExpireDate": "288888",
        "cardAddr": "110000#110100#110101#天天通过沟沟壑壑",
        "csardAddrStr": "江苏省苏州市xxxxxxx",
        "education": None,
        "maritalStatus": 1,
        "children": 1,
        "address": "110000#110100#110101#天天通过沟沟壑壑",
        "addressStr": "江苏省苏州市xxxxxxx",
        "mobileNo": "13063835945",
        "phoneServicePwd": "123123",
        "housingCategory": None,
        "rent": None,
        "phone": "15995788425",
        "email": "15995788425@qq.com",
        "im1": 15995788425,
        "moveToDateStr": "2017-02-01",
        "settledFromStr": "2017-02-02",
        "action": "U"
    }
}

payload_cardAddr = {
    "platform": "android",
    "app_version": None,
    "os_version": None,
    "phone_model": None,
    "service_provider": 0,
    "network_type": 0,
    "session_token": "41340004CD64B93918A25E77A3F0EC70",
    "imei": None,
    "macAddress": None,
    "width": 0,
    "height": 0,
    "channel": None,
    "sign": None,
    "clientIp": None,
    "data": {
        "jobReq": [
            {
                "borrowerRegularJobDTOs": [
                    {
                        "prodType": 203,
                        "category": 1,
                        "subType": -1,
                        "contentUrl": "loanftptest/a/ic/2017/02bb/1487233996583238.jpg",
                        "contentSize": "1662178",
                        "sContentUrl": "loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx": 1,
                        "type": 12,
                        "path": None,
                        "loanId": 1
                    }
                ]
            },
            {
                "borrowerRegularJobDTOs": [
                    {
                        "prodType": 203,
                        "category": 1,
                        "subType": -1,
                        "contentUrl": "loanftptest/a/pu/17/02dd/13/2009_t21_60.jpg",
                        "contentSize": "1662178",
                        "sContentUrl": "loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx": 1,
                        "type": 13,
                        "path": None,
                        "loanId": 1
                    }
                ]
            }
        ],
        "loanId": 1,
        "prodType": 203,
        "applyBuzType": 1,
        "loanMoney": 12,
        "installment": 3,
        "job": 0,
        "loanPurposes": "4",
        "loanPurposesType": "",
        "loanPurposesOther": "",
        "cardName": "012345678",
        "sex": 2,
        "birthday": "1989-12-08",
        "cardNo": "320382198905199475",
        "cardExpireDateShow": "2027-01-01",
        "cardExpireDate": "288888",
        "cardAddr": "",
        "csardAddrStr": "江苏省苏州市xxxxxxx",
        "education": None,
        "maritalStatus": 1,
        "children": 1,
        "address": "110000#110100#110101#天天通过沟沟壑壑",
        "addressStr": "江苏省苏州市xxxxxxx",
        "mobileNo": "13063835945",
        "phoneServicePwd": "123123",
        "housingCategory": None,
        "rent": None,
        "phone": "15995788425",
        "email": "15995788425@qq.com",
        "im1": 15995788425,
        "moveToDateStr": "2017-02-01",
        "settledFromStr": "2017-02-02",
        "action": "U"
    }
}

payload_mobileNo = {
    "platform": "android",
    "app_version": None,
    "os_version": None,
    "phone_model": None,
    "service_provider": 0,
    "network_type": 0,
    "session_token": "41340004CD64B93918A25E77A3F0EC70",
    "imei": None,
    "macAddress": None,
    "width": 0,
    "height": 0,
    "channel": None,
    "sign": None,
    "clientIp": None,
    "data": {
        "jobReq": [
            {
                "borrowerRegularJobDTOs": [
                    {
                        "prodType": 203,
                        "category": 1,
                        "subType": -1,
                        "contentUrl": "loanftptest/a/ic/2017/02bb/1487233996583238.jpg",
                        "contentSize": "1662178",
                        "sContentUrl": "loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx": 1,
                        "type": 12,
                        "path": None,
                        "loanId": 1
                    }
                ]
            },
            {
                "borrowerRegularJobDTOs": [
                    {
                        "prodType": 203,
                        "category": 1,
                        "subType": -1,
                        "contentUrl": "loanftptest/a/pu/17/02dd/13/2009_t21_60.jpg",
                        "contentSize": "1662178",
                        "sContentUrl": "loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx": 1,
                        "type": 13,
                        "path": None,
                        "loanId": 1
                    }
                ]
            }
        ],
        "loanId": 1,
        "prodType": 203,
        "applyBuzType": 1,
        "loanMoney": 12,
        "installment": 3,
        "job": 0,
        "loanPurposes": "4",
        "loanPurposesType": "",
        "loanPurposesOther": "",
        "cardName": "012345678",
        "sex": 2,
        "birthday": "1989-12-08",
        "cardNo": "320382198905199475",
        "cardExpireDateShow": "2027-01-01",
        "cardExpireDate": "288888",
        "cardAddr": "110000#110100#110101#天天通过沟沟壑壑",
        "csardAddrStr": "江苏省苏州市xxxxxxx",
        "education": None,
        "maritalStatus": 1,
        "children": 1,
        "address": "110000#110100#110101#天天通过沟沟壑壑",
        "addressStr": "江苏省苏州市xxxxxxx",
        "mobileNo": "",
        "phoneServicePwd": "123123",
        "housingCategory": None,
        "rent": None,
        "phone": "15995788425",
        "email": "15995788425@qq.com",
        "im1": 15995788425,
        "moveToDateStr": "2017-02-01",
        "settledFromStr": "2017-02-02",
        "action": "U"
    }
}

payload_phoneServicePwd = {
    "platform": "android",
    "app_version": None,
    "os_version": None,
    "phone_model": None,
    "service_provider": 0,
    "network_type": 0,
    "session_token": "41340004CD64B93918A25E77A3F0EC70",
    "imei": None,
    "macAddress": None,
    "width": 0,
    "height": 0,
    "channel": None,
    "sign": None,
    "clientIp": None,
    "data": {
        "jobReq": [
            {
                "borrowerRegularJobDTOs": [
                    {
                        "prodType": 203,
                        "category": 1,
                        "subType": -1,
                        "contentUrl": "loanftptest/a/ic/2017/02bb/1487233996583238.jpg",
                        "contentSize": "1662178",
                        "sContentUrl": "loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx": 1,
                        "type": 12,
                        "path": None,
                        "loanId": 1
                    }
                ]
            },
            {
                "borrowerRegularJobDTOs": [
                    {
                        "prodType": 203,
                        "category": 1,
                        "subType": -1,
                        "contentUrl": "loanftptest/a/pu/17/02dd/13/2009_t21_60.jpg",
                        "contentSize": "1662178",
                        "sContentUrl": "loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx": 1,
                        "type": 13,
                        "path": None,
                        "loanId": 1
                    }
                ]
            }
        ],
        "loanId": 1,
        "prodType": 203,
        "applyBuzType": 1,
        "loanMoney": 12,
        "installment": 3,
        "job": 0,
        "loanPurposes": "4",
        "loanPurposesType": "",
        "loanPurposesOther": "",
        "cardName": "012345678",
        "sex": 2,
        "birthday": "1989-12-08",
        "cardNo": "320382198905199475",
        "cardExpireDateShow": "2027-01-01",
        "cardExpireDate": "288888",
        "cardAddr": "110000#110100#110101#天天通过沟沟壑壑",
        "csardAddrStr": "江苏省苏州市xxxxxxx",
        "education": None,
        "maritalStatus": 1,
        "children": 1,
        "address": "110000#110100#110101#天天通过沟沟壑壑",
        "addressStr": "江苏省苏州市xxxxxxx",
        "mobileNo": "13063835945",
        "phoneServicePwd": "",
        "housingCategory": None,
        "rent": None,
        "phone": "15995788425",
        "email": "15995788425@qq.com",
        "im1": 15995788425,
        "moveToDateStr": "2017-02-01",
        "settledFromStr": "2017-02-02",
        "action": "U"
    }
}


class PostCustomerInfo(unittest.TestCase):
    """个人信息接口测试"""

    def setUp(self):
        self.url = "http://172.16.88.167:5959/xiangfa/borrowerRegular/v1/customerInfo.json"

    def test_post_payload_cardName(self):
        '''不填姓名'''
        r = requests.post(self.url, None, payload_cardName)
        print (r.status_code)
        print (r.text)

    def test_post_payload_birthday(self):
        '''不填生日'''
        r = requests.post(self.url, None, payload_birthday)
        print (r.status_code)
        print (r.text)

    def test_post_payload_cardNo(self):
        '''不填身份证号码'''
        r = requests.post(self.url, None, payload_cardNo)
        print (r.status_code)
        print (r.text)

    def test_post_payload_cardExpireDateShow(self):
        '''不填身份证截至日期'''
        r = requests.post(self.url, None, payload_cardExpireDateShow)
        print (r.status_code)
        print (r.text)

    def test_post_payload_cardAddr(self):
        '''不填户籍地址'''
        r = requests.post(self.url, None, payload_cardAddr)
        print (r.status_code)
        print (r.text)

    def test_post_payload_mobileNo(self):
        '''不填手机号'''
        r = requests.post(self.url, None, payload_mobileNo)
        print (r.status_code)
        print (r.text)

    def test_post_payload_phoneServicePwd(self):
        '''不填手机服务密码'''
        r = requests.post(self.url, None, payload_phoneServicePwd)
        print (r.status_code)
        print (r.text)


if __name__ == '__main__':
    customerInfoTests = unittest.TestLoader().loadTestsFromTestCase(PostCustomerInfo)
    smoke_tests = unittest.TestSuite(customerInfoTests)
    outfile = open("D:\SunFit_Python_Automated_Testing\Xiangfa_Backend_REST_API\E-CheDai\TestReport\customerInfoTestResult.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=outfile,
        title='customerinfo test report',
        description='customerinfo test report'
    )
    runner.run(smoke_tests)
