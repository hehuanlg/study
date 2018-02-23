from xml.dom import minidom
dom = minidom.parse('info.xml')
root = dom.documentElement
print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
print(root.ELEMENT_NODE)

tagname = root.getElementsByTagName('browser')
print(tagname[0].tagName)

tagname = root.getElementsByTagName('login')
print(tagname[1].tagName)

tagname = root.getElementsByTagName('province')
print(tagname[2].tagName)

logins = root.getElementsByTagName('login')
username = logins[0].getAttribute('username')
print(username)
password = logins[0].getAttribute('password')
print(password)

username = logins[1].getAttribute('username')
print(username)
password = logins[1].getAttribute('password')
print(password)

provinces = dom.getElementsByTagName('province')
citys = dom.getElementsByTagName('city')
p2 = provinces[1].firstChild.data
print(p2)

c1 = citys[0].firstChild.data
print(c1)

c2 = citys[1].firstChild.data
print(c2)

