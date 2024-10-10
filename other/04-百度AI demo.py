import base64
from pathlib import Path

import requests
from config import BAIDU_AI_API_KEY, BAIDU_AI_SECRET_KEY


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": BAIDU_AI_API_KEY, "client_secret": BAIDU_AI_SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


def getOCR(imgurl, type='general_basic'):
    """
    百度文字识别
    type: 识别类型
    general_basic: 通用文字识别（标准版）
    handwriting: 手写文字识别
    numbers: 数字识别
    

    """
    request_url = f"https://aip.baidubce.com/rest/2.0/ocr/v1/{type}"
    # 二进制方式打开图片文件
    f = open(imgurl, 'rb')
    img = base64.b64encode(f.read())
    params = {"image": img}
    request_url = request_url + "?access_token=" + get_access_token()
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    # print(response.json())
    if 'error_msg' in response.json():
        return response.json()['error_msg']
    else:
        return response.json()['words_result']


if __name__ == '__main__':
    imgurl = Path(__file__).parent.parent / 'images' / '微信付款码.png'
    # imgurl = r'D:\code\dfybc\images\微信付款码.png'
    print(getOCR(imgurl, type='numbers'))

    # for a in Path(__file__).parents:
    #     print(a)
