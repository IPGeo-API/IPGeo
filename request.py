from IPGeoSearch import search

with open('ipList.txt', 'r') as f:
    ip = [line.strip() for line in f]
    f.close()

with open('yourkey.key', 'r') as hashkey:
    key=hashkey.read().replace('\n', '')
    hashkey.close()

search.search(ipList=ip,path='',key=key)

