# simple-xls2json

Convert table data to json format output

## Requirements

- xlrd

## Installation

```
pip3 install simple-xls2json
```

## Usage

```
from xls2json.xls2json import *

xls = Xls2Json()
xls.setConfig(
        Config().start(1).end(-1) # configure the startline & endline, -1 for end means all lines
        .values([(0, 'click_time'), (1, 'create_time')])    # configure which columns to be used, set the keys
        .value(2, 'pay_time')
        .value(3, 'balance_time')
        .value(5, 'item_id')
        .value(6, 'pic')
        .value(7, 'title')
        .value(11, 'price')
        )
xls.toJson('test.xls')
```

## Output

```
{
    "code":0,
    "pageCount":1,
    "pages":[
        {
            "name":"Page1",
            "lines":[
                {
                    "click_time":"2020-06-16 23:28:11",
                    "create_time":"2020-06-17 00:24:02",
                    "pay_time":"2020-06-17 00:24:12",
                    "balance_time":"2020-07-07 21:54:53",
                    "item_id":"521537285175",
                    "pic":"//img.alicdn.com/tfscom/i4/2185500387/TB2Z2bvnSVmpuFjSZFFXXcZApXa_!!2185500387.jpg",
                    "title":"Bellroy澳洲进口Coin Fold折叠硬币信用卡片收纳包皮夹卡包男包邮",
                    "price":"528.00"
                },
                {
                    "click_time":"2020-06-16 23:28:11",
                    "create_time":"2020-06-17 00:24:02",
                    "pay_time":"2020-06-17 00:24:12",
                    "balance_time":"2020-07-07 21:54:53",
                    "item_id":"521537285175",
                    "pic":"//img.alicdn.com/tfscom/i4/2185500387/TB2Z2bvnSVmpuFjSZFFXXcZApXa_!!2185500387.jpg",
                    "title":"Bellroy澳洲进口Coin Fold折叠硬币信用卡片收纳包皮夹卡包男包邮",
                    "price":"528.00"
                },
                {
                    "click_time":"2020-06-16 23:28:11",
                    "create_time":"2020-06-17 00:24:02",
                    "pay_time":"2020-06-17 00:24:12",
                    "balance_time":"2020-07-07 21:54:53",
                    "item_id":"521537285175",
                    "pic":"//img.alicdn.com/tfscom/i4/2185500387/TB2Z2bvnSVmpuFjSZFFXXcZApXa_!!2185500387.jpg",
                    "title":"Bellroy澳洲进口Coin Fold折叠硬币信用卡片收纳包皮夹卡包男包邮",
                    "price":"528.00"
                },
                {
                    "click_time":"2020-06-16 23:28:11",
                    "create_time":"2020-06-17 00:24:02",
                    "pay_time":"2020-06-17 00:24:12",
                    "balance_time":"2020-07-07 21:54:53",
                    "item_id":"521537285175",
                    "pic":"//img.alicdn.com/tfscom/i4/2185500387/TB2Z2bvnSVmpuFjSZFFXXcZApXa_!!2185500387.jpg",
                    "title":"Bellroy澳洲进口Coin Fold折叠硬币信用卡片收纳包皮夹卡包男包邮",
                    "price":"528.00"
                }
            ]
        }
    ]
}
```