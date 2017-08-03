#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TheRockTrading.com Ethereum Info
#
# Copyright (C) 2017 Andrea Lorenzetti <andrea@lorenzetti.me>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import requests.exceptions

fundId = 'ETHEUR'
defaultKey = 'last'
printOrder = ['last', 'high', 'low', 'bid', 'ask', 'open', 'close', 'volume', 'volume_traded', 'fund_id', 'date']
tickerUrl = 'https://api.therocktrading.com/v1/funds/tickers'

if __name__ == '__main__':
    try:
        response = requests.get(tickerUrl, timeout=10)
    except requests.exceptions.Timeout:
        print('TIMEOUT')
        exit(1)
    except Exception as e:
        print('OFFLINE')
        exit(1)

    if response.status_code != 200:
        print('ERROR')
        exit(1)

    results = response.json()
    for result in results['tickers']:
        if result['fund_id'] == fundId:
            print(defaultKey + ': ' + str(result[defaultKey]))
            print('---')
            for key in printOrder:
                if key != defaultKey:
                    print(key + ': ' + str(result[key]))
            break

    exit(0)
