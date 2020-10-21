#用户信息及用户操作函数

from flask import request, session
from main import app
from database import findTel, createUser, student
import re

global null
null = None

@app.route('/user', methods=['POST'])
def register():
  data = request.get_json()
  someone = student()
  someone.name = data['name']
  someone.sex = data['sex']
  someone.grade = data['grade']
  someone.college = data['college']
  someone.dormitory = data['dormitory']
  someone.first = data['first']
  someone.second = data['second']
  someone.tel = data['tel']
  someone.adjust = data['adjust']
  someone.description = data['description']

  ret = re.match(r"^1\d{10}$", someone.tel)
  isRegister = findTel(someone.tel)
  if ret:
    if isRegister:
      return {
        "status": 409,
        "msg": "该手机号已报名",
        "data": null
      }
      
      
    else:
      rowCount = createUser(someone)
      if rowCount > 0:
        return {
        "status": 200,
        "msg": "报名成功",
        "data": null 
        }
      else:
        return {
          "status": 410,
          "msg": "服务器错误",
          "data": null
        }
      
  else:
    return {
      "status": 400,
      "msg": "手机号错误或是其他参数错误",
      "data": null
    }

@app.route('/user?tel={tel}&name={name}', methods=['GET'])
def require():
  pass

@app.route('/user', methods=['PUT'])
def modify():
  pass

@app.route('/admin/session')
def login():
  pass

@app.route('/admin/user/count', methods=['GET'])
def requireCount():
  pass

@app.route('/admin/user/excel', method=['GET'])
def getExcel():
  pass
  
  

















    



