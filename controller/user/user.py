#用户信息及用户操作函数

from flask import request, session
from database import findUser, createUser, userLogin, isnRepeat, inputApplyInfo
from spring_recruit_2020 import app

@app.route('/bbt/register', methods=['POST'])
def register():#用户注册
#获取前端数据 
    data = request.get_json()
    username = data['username']
    password = data['password'] 
    result = findUser(username)
    if result:
        return{
            'errcode':400,
            'errmsg': '该用户已被注册'
        },400

    rowcount = createUser(username, password)
    if rowcount > 0:
        return {
            'errcode': 0,
            'errmsg': '注册成功'
            }, 200    
        
    return {
        'errcode': 400,
        'errmsg': '出现错误，请重试'
    },400

@app.route('/bbt/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password'] 
    result = userLogin(username, password)

    if result:
        session['user_id'] = result[0]
        return {
            'errcode':0,
            'errmsg':'登录成功'
        },200
    return {
        'errcode':401,
        'errmsg':'用户不存在或密码错误'
    },401


@app.route('/bbt/application', methods=['POST'])
def apply():
    data = request.get_json()
    name = data['name']
    Dormitory = data['Dormitory']
    result = isnRepeat(name, Dormitory)

    if result:
        return{
            'errcode':400,
            'errmsg':'您已经报名！'
        },400

    rowcount = inputApplyInfo(data)

    if rowcount > 0:
        return{
            'errcode': 0,
            'errmsg': '报名成功'
        },200
    return{
        'errcode': 400,
        'errmsg': '出现错误，请重试'
    },400





    



