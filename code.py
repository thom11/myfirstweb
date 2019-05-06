import web
urls = (
  '/', 'index'    )
  
  class index:
    def GET(self):
        print "Hello, world!"
        
        
  if __name__ == "__main__": web.run(urls, globals())
  
