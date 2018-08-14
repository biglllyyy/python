#coding=utf8
import tornado.httpserver
import tornado.ioloop
import tornado.web
import os

class HomeHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # message = 'hello'
        # self.write(message)
        self.render('login.html',error='')

# class OtherHandler(tornado.web.RequestHandler):
#
#     def get(self, page, extension):
#         pagename = page + '.' + extension
#         path = 'D:\\company\\code\\python\\test\\tornado\\study_3\\startbootstrap-clean-blog' + pagename
#         print path
#         if extension != 'html':
#             with open(path) as f:
#                 self.write(f.read())



class FormHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        self.render('index.html')
        # raise tornado.web.HTTPError(status_code=417, log_message=' te', reason='ubknow')

class Cust(tornado.web.Application):

    def __init__(self):
        # super(Cust,self).__init__({(r'/',HomeHandler)})
        handlers = [
            #跳转的URL路径（使用正则表达式）
            (r'/login',HomeHandler),
            #匹配有优先级，如果前面匹配了，则不往后面接着匹配
            (r'/auth/login', FormHandler),
            (r'/(.+?\,.+)', tornado.web.StaticFileHandler, dict(path='D:\\company\\code\\python\\test\\tornado\\study_3\\startbootstrap-clean-blog')),

        ]

        setting = {
            #指定模板文件的目录
            'template_path': 'D:\\company\\code\\python\\test\\tornado\\study_3\\startbootstrap-clean-blog',
            'static_path': 'D:\\company\\code\\python\\test\\tornado\\study_3\\startbootstrap-clean-blog',
            'blog_title': 'title',

        }
        #传递URL路径
        super(Cust, self).__init__(handlers,**setting)

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(Cust())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()



