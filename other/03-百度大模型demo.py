import base64
import json
import time

import requests

API_KEY = "lMOwMls54oExWD****"
SECRET_KEY = "agZrCKltmhuMU8******"


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


def chat(prompt):
    '''
    文生文，使用大模型ernie-speed-128k
    '''
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-speed-128k?access_token=" + get_access_token() 
    headers = {
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": str(prompt)
            }
        ]
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    if 'error_msg' in response.json():
        return response.json()["error_msg"]
    else:
        return response.json()["result"]


def text2image(prompt):
    '''
    文生图，使用大模型stable-diffusion-xl-base-1.0
    '''
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/text2image/sd_xl?access_token=" + get_access_token()
    payload = json.dumps({
        "prompt": str(prompt),
        "size": "1024x1024",
        "n": 1,
        "steps": 20,
        "sampler_index": "Euler a"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    # print(response.text)
    if 'error_msg' in response.json():
        return response.json()["error_msg"]
    else:
        output_file = '/home/pi/imageTemp/' + time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()) + '.jpg'
        with open(output_file, 'wb') as f:
            f.write(base64.b64decode(response.json()["data"][0]['b64_image']))
        return output_file


def image2text(prompt, imgurl):
    """
    图生文，使用大模型fuyu_8b
    """
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/image2text/fuyu_8b?access_token=" + get_access_token()

    headers = {
        'Content-Type': 'application/json'
    }

    f = open(imgurl, 'rb')
    img_bs64 = base64.b64encode(f.read()).decode('utf8')
    print(img_bs64[:10])
    payload = json.dumps({
        "prompt": str(prompt),
        "image": img_bs64
    })

    response = requests.request("POST", url, headers=headers, data=payload)

    if 'error_msg' in response.json():
        return response.json()["error_msg"]
    else:
        return response.json()["result"]


if __name__ == '__main__':
    # img_url = text2image('傍晚时分，一只蓝色的猫在草丛中，画面中还有很多粉色的蝴蝶')
    # print(img_url)
    print(chat('请帮我写一首诗'))
