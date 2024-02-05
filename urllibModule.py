import urllib
from urllib import request
from urllib import parse


# Return All Method Inside The Module
print(dir(urllib))
print(dir(request))
print(dir(parse))


# To Open URL
resp = request.urlopen("https://www.wikipedia.org")
print(type(resp))


# HTTP Status Codes
# 200 : OK
# 400 : Bad Request
# 403 : Forbidden
# 404 : Not Found
print(resp.code)                   # Return Response Code         
print(resp.length)                 # Response Size In Bytes
print(resp.peek())                 # Return Small Part Of Respose Code

html = resp.read().decode("UTF-8")        # Convert Into HTML
print(html)


params = {"v":"EuC-yVzHhMI","t":"5m56"}
queryString = parse.urlencode(params)
url = "https://www.youtube.com/watch"+"?"+queryString
resp = request.urlopen(url)
print(resp.isclosed())
print(resp.code)
html = resp.read().decode("utf-8")
print(html[:500])