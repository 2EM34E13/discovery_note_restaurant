#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
import json

data = json.load(open("pack.json", encoding="utf-8"))

重复度 = 1

def generator_1(trans,xx):
    body = random.choice(data[trans])
    body += "\n\n"
    body = body.replace("place", xx)
    print(body)
    return ()

def generator_1_and(trans,xx):
    body = random.choice(data[trans])
    body = body.replace("place", xx)
    print(body)
    return ()

def 洗牌遍历(列表):
    global 重复度
    池 = list(列表) * 重复度
    while True:
        random.shuffle(池)
        for 元素 in 池:
            yield 元素
            
nxa = 洗牌遍历(data['surrounding_atmosphere'])
nfl = 洗牌遍历(data['food_list'])            

def generator_2(null,xx):
    for x in xx:
        tmp = str()
        while ( len(tmp) < 130 ) :
                tmp += next(null)
                tmp += "\n"
        tmp = tmp.replace("place",xx)
    tmp += "\n\n"
    print(tmp)
    return()

if __name__ == '__main__':
    xx = input("随便输入餐厅种类:")
    generator_1("summary",xx)
    generator_1("reason",xx)
    print("🏡环境")
    generator_1_and("surrounding_type",xx)
    generator_2(nxa,xx)
    print("🍸推荐必点")
    generator_1_and("food",xx)
    generator_2(nfl,xx)
    generator_1("tip",xx)


