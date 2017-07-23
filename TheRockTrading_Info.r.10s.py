#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time
import hmac
import hashlib
import json

apikey = 'CHANGE_ME'
apisecret = 'CHANGE_ME'

fundId = 'ETHEUR'
defaultKey = 'last'
printOrder = ['last', 'high', 'low', 'bid', 'ask', 'open', 'close', 'volume', 'volume_traded', 'fund_id', 'date']
tickerUrl = 'https://api.therocktrading.com/v1/funds/tickers'

def get_headers():
    nonce = str(int(round(time.time() * 1000)))
    return {
        'Content-Type': 'application/json',
        'X-TRT-KEY': apikey,
        'X-TRT-SIGN': hmac.new(nonce + tickerUrl, apisecret, hashlib.sha512).hexdigest(),
        'X-TRT-NONCE': nonce
    }

if __name__ == '__main__':
    try:
        response = requests.get(tickerUrl, headers=get_headers(), timeout=5)
    except Exception:
        print 'OFFLINE'
        exit(1)

    if response.status_code != 200:
        print 'ERROR'
        exit(1)

    results = json.loads(response.content)
    for result in results['tickers']:
        if result['fund_id'] == fundId:
            print defaultKey + ': ' + str(result[defaultKey])
            print '---'
            for key in printOrder:
                if key != defaultKey:
                    print key + ': ' + str(result[key])
            break

    exit(0)
