"""
用于提供用户能够访问的路由（请求类型）
"""
from views import *
urls = [
    ('/time',show_time),
    ('/hello',hello),
    ('/bye',bye)
]