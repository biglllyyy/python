#coding=utf8
import tornado.httpserver
import tornado.ioloop
import tornado.web
import os

class HomeHandler(tornado.web.RequestHandler):
    def test_string(self, message):
        return "<a href> %s</a>" % message

    def get(self, *args, **kwargs):
        self.ui['test_function'] = self.test_string
        # message = 'hello'
        # self.write(message)
        self.render('login.html', error='hello',message='<p1>hello</p>',list=[1,2,3,4,5,6,7,8,9])

class OtherHandler(tornado.web.RequestHandler):


    def get(self, *args, **kwargs):
        #如果输入的网址都不符合，则跳转到根下
        self.redirect('/login')
        #自定义异常
        # raise tornado.web.HTTPError(status_code=406, log_message= ' testing',reason= 'unknow host')

class FormHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        message= 'hello'
        self.write(message)
        # raise tornado.web.HTTPError(status_code=417, log_message=' te', reason='ubknow')

class Cust(tornado.web.Application):

    def __init__(self):
        # super(Cust,self).__init__({(r'/',HomeHandler)})
        handlers = [
            #跳转的URL路径（使用正则表达式）
            (r'/', HomeHandler),
            (r'/login',HomeHandler),
            # (r'/.*', tornado.web.RedirectHandler , {'url':'/'}),
            #匹配有优先级，如果前面匹配了，则不往后面接着匹配
            (r'/auth/login', FormHandler),
            (r'/.*',OtherHandler),


        ]

        setting = {
            #指定模板文件的目录
            'template_path': 'D:\\company\\code\\python\\test\\tornado\\study_2\\temp',
            'static_path': 'D:\\company\\code\\python\\test\\tornado\\study_2\\static',

            'blog_title':'title'

        }
        #传递URL路径
        super(Cust, self).__init__(handlers,**setting)

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(Cust())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()



