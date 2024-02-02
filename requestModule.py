import requests

r1 = requests.get("https://xkcd.com/353/")


# Return All Methods Of Request Module
print(dir(r1))


# Return Detailed Description Of All Methods Of Request Module
print(help(r1))


# Return text of the requested page
print(r1.text)


# Request Image From URL
r2 = requests.get("https://imgs.xkcd.com/comics/python.png")
print(r2.status_code)                                          # Return HTTPS Status Code
print(r2.ok)                                                   # Return True If r2.status_code<400
print(r2.headers)                                              # Return Description Of The URL
with open("comic.png","wb") as f:
    f.write(r2.content)


# Get Request
payload = {"page":2,"count":25}
r3 = requests.get("https://httpbin.org/get",params=payload)
print(r3.text)
print(r3.url)                                                  # Return URL


# Post Request
payload = {"username":"ABC","password":"testing"}
r4 = requests.post("https://httpbin.org/post",data=payload)
print(r4.text)
print(r4.json()) 


# Get Authenication
r5 = requests.get("https://httpbin.org/basic-auth/ABC/testing",auth=('ABC',"testing"))
print(r5.text)