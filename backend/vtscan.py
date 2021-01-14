import requests
import time


def getReportinternal(vtapikey,urltoscan):
    url = 'https://www.virustotal.com/vtapi/v2/url/report'

    params = {'apikey': vtapikey, 'resource':urltoscan, 'allinfo':True , 'scan':1}

    response = requests.get(url, params=params)

    return response.json()





def getResult(KEY,URL):
    result = getReportinternal(KEY,URL)

    try:
        print(result['url'] + " +ve = " + str(result['positives']))

        return result

    except KeyError:                                                               # IF THE RESULT IS NOT FOUND , SUBMIT NEW SCAN AND WAIT FOR IT TO COMPLETE
        try:
            print(result['scan_id'])
            scanid = result['scan_id']

            while True:

                time.sleep(15)
                result = getReportinternal(KEY,scanid)
                try:
                    print("Sub&Get  : " + result['url'] + " +ve = " + str(result['positives']))

                    return result
                    break

                except KeyError:
                    pass

        except KeyError:
            print("KeyError in VT module")


if __name__ == '__main__':
    print("")
