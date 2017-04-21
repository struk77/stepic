def app(environ, start_response):
   query = environ.get('QUERY_STRING')
   
   body = 'ok'
   headers = [
      ('Content-Type','text/plain')
   ]
   status = '200 OK'
   start_response(status,headers)
   return [body]
