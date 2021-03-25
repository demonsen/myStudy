#!/usr/bin/env python
# coding=utf-8
import pytest

@pytest.fixture(scope='function')
def login():
    print("登录")
    yield
    print("注销登录")

#@pytest.mark.aaa
def test_1():
    print('测试用例1')

#@pytest.mark.bbb
def test_2(login):
    print('测试用例2')
    print('112233')

if __name__ =="__main__":
    pytest.main(['test_3.py','-s'])

