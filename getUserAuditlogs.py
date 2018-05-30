#!/usr/bin/python
from cvprac.cvp_client import CvpClient
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_logs(clnt):
    data = {
            'startTime': 0,
            'endTime': 0,
            'category': "User",
            'objectKey': "cvpadmin",
            'dataSize': 60,
            'queryParam': "",
            'firstRetrievedAudit':{},
            'lastRetrievedAudit':{},
            'reverseSearch': False,
            }

    ret = clnt.post('/audit/v2/getLogs.do?',
                    data)
    return ret

def main():
    clnt = CvpClient()
    clnt.connect(['10.81.110.114'], 'cvpadmin', 'cvp123', protocol='https')

    logs = get_logs(clnt)
    print json.dumps(logs, indent=4, sort_keys=True)

if __name__ == '__main__':
    main()
