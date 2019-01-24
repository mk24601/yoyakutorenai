import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

USER = ""
PASS = ""

# セッションを開始
session = requests.session()

# ログイン
login_info = {
    "b.studentId":USER,
    "b.password":PASS,
    "b.wordsStudentNo":"教習生番号",
    "b.hpAddress":"",
    "b.schoolNm":"尾久自動車学校",
    "b.telephoneNo":"",
    "b.schoolCd":"tZ/XW2Ic+pA+brGQYS+1OA==",
    "server":"el2"
}

# action
url_login = "https://www.e-license.jp/el2/index.action?abc=tZ%2FXW2Ic%2BpA%2BbrGQYS%2B1OA%3D%3D&senisakiCd=5/el2/mobile/m01a.action"
res = session.post(url_login, data=login_info)
res.raise_for_status() # エラーならここで例外を発生させる

print(res.text)