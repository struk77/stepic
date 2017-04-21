def app(environ, start_response):
    query = environ.get('QUERY_STRING')
    queries = query.split('&')
    body = []
    for str in queries:
        body.append(str + '\n')
    headers = [
      ('Content-Type','text/plain')
    ]
    status = '200 OK'
    start_response(status,headers)
    return body
