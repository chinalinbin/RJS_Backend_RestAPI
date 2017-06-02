# -*- coding:utf-8 -*-



import unittest
import requests

payload = {
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
        "action": "U",
        "jobReq": [
            {
                "borrowerRegularJobDTOs": [
                    {
                        "draftId": None,
                        "prodType": 203,
                        "status": None,
                        "category": 1,
                        "subType": -1,
                        "contentUrl": "loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "contentSize": "1662178",
                        "sContentUrl": "loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx": 1,
                        "type": 11,
                        "path": None,
                        "loanId": 1
                    }
                ]
            },
            {
                "borrowerRegularJobDTOs": [
                    {
                        "draftId": None,
                        "prodType": 203,
                        "status": None,
                        "category": 1,
                        "subType": 1,
                        "contentUrl": "loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "contentSize": "1662178",
                        "sContentUrl": "loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx": 1,
                        "type": 9,
                        "path": None,
                        "loanId": 1
                    }
                ]
            },
            {
                "borrowerRegularJobDTOs": [
                    {
                        "draftId": None,
                        "prodType": 203,
                        "status": None,
                        "category": 1,
                        "subType": 1,
                        "contentUrl": "loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "contentSize": "1662178",
                        "sContentUrl": "loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx": 1,
                        "type": 15,
                        "path": None,
                        "loanId": 1
                    }
                ]
            },
            {
                "borrowerRegularJobDTOs": [
                    {
                        "draftId": None,
                        "prodType": 203,
                        "status": None,
                        "category": 1,
                        "subType": 1,
                        "contentUrl": "loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "contentSize": "1662178",
                        "sContentUrl": "loanftptest/a/ic/2017/02/1487233996583238.jpg",
                        "idx": 1,
                        "type": 9,
                        "path": None,
                        "loanId": 1
                    }
                ]
            }
        ]
    },
    "loanId": 1,
    "prodType": 203,
    "carCardPlateNo": "滚A88888",
    "carCardRegDateStr": "2017-02-01",
    "carCardPublishDateStr": "2017-12-13",
    "carCardVin": "123465asdasd465",
    "carCardVen": "123456789",
    "carCardType": "超级大车123123",
    "carPurchaseDateStr": "2017-12-12",
    "car1stRegDateStr": "2017-12-13",
    "carPurchasePrice": 123.45,
    "carProperties": 1
}


class PostVehicleInfo(unittest.TestCase):
    """车辆信息接口测试"""

    def setUp(self):
        self.url = "http://172.16.88.167:5959/xiangfa/borrowerRegular/v1/vehicleInfo.json"


    def test_post_contentUrl(self):
        '''车辆信息'''

        r = requests.post(self.url,None,payload)
        print (r.status_code)
        print (r.text)





if __name__== '__main__':
    unittest.main()


