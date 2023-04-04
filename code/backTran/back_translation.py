import hashlib
import http.client
import json
import random
import re
import time
import urllib


def get_only_chars(line):
    clean_line = ""

    line = line.replace("’", "")
    line = line.replace("'", "")
    line = line.replace("-", " ")  # replace hyphens with spaces
    line = line.replace('\t', " ")
    line = line.replace("\n", " ")
    line = line.lower()

    for char in line:
        if char in 'qwertyuiopasdfghjklzxcvbnm ':
            clean_line += char
        else:
            clean_line += ' '

    clean_line = re.sub(' +', ' ', clean_line)  # delete extra spaces
    if clean_line[0] == ' ':
        clean_line = clean_line[1:]
    return clean_line


appid = '20230227001578768'  # 填写appid
secretKey = 'AkSasm8gow6Dy90jeOtX'  # 填写密钥

httpClient = None
myurl = '/api/trans/vip/translate'
dataset = 'CR'
input_file = '../../data/' + dataset + '/experiment/train/train.txt'
output_file = '../../data/' + dataset + '/experiment/backTran/backTran-train.txt'
with open(input_file, 'r', encoding='UTF-8') as in_f:
    input_lines = in_f.readlines()
with open(output_file, 'w', encoding='UTF-8') as out_f:
    to_be_write = []
    for line in input_lines:
        out_f.write(line)
        parts = line[:-1].split('\t')
        orig_line = parts[0]
        print('orig_line', orig_line)
        label = parts[1]
        # 英->中
        fromLang = 'en'  # 原文语种
        toLang = 'zh'  # 译文语种
        salt = random.randint(32768, 65536)

        q = orig_line
        sign = appid + q + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        my_query = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
            q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign

        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', my_query)
            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)
            to_line = result['trans_result'][0]['dst']
            print('to_line', to_line)
        except Exception as e:
            print(e)
        finally:
            if httpClient:
                httpClient.close()
        time.sleep(1.1)
        # 中->英
        fromLang = 'zh'  # 原文语种
        toLang = 'en'  # 译文语种
        salt = random.randint(32768, 65536)
        q = to_line
        sign = appid + q + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        my_query = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
            q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', my_query)
            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)
            back_line = result['trans_result'][0]['dst']
        except Exception as e:
            print(e)
        finally:
            if httpClient:
                httpClient.close()

        back_line = get_only_chars(back_line)
        print('back_line', back_line)
        out_f.write(back_line + '\t' + label + '\n')
        time.sleep(1.1)
