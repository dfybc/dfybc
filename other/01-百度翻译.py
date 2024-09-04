import random
import sys
import traceback
import urllib
from hashlib import md5

import requests
from config import BAIDU_TRANSLATE_APP_ID, BAIDU_TRANSLATE_SECRET_KEY


def baiduTranslate(q, toLang):
    appid = BAIDU_TRANSLATE_APP_ID
    secretKey = BAIDU_TRANSLATE_SECRET_KEY
    myurl = 'https://api.fanyi.baidu.com/api/trans/vip/translate'
    fromLang = 'auto'
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = md5(sign.encode("utf-8")).hexdigest()
    params = {
        'appid': appid,
        'q': q,
        'from': fromLang,
        'to': toLang,
        'salt': salt,
        'sign': sign
    }
    # myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    myurl = myurl+'?' + urllib.parse.urlencode(params)
    try:
        ret = requests.get(myurl).json()
        if 'trans_result' in ret:
            return ret['trans_result'][0]['dst']
        else:
            return ret['error_msg']
    except Exception as e:
        traceback.print_exc()
        return e


ret = baiduTranslate('好好学习，天天向上！', 'en')
print(ret)
