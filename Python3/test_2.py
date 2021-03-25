#!/usr/bin/env python
# coding=utf-8
import pytest

@pytest.fixture(scope='function')
def login():
    print("登录")

def test_1():
    print('测试用例1')

def test_2(login):
    print('测试用例2')


if __name__ =="__main__":
    pytest.main(['test_2.py','-s'])


