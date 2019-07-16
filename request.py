from IPGeoSearch import search

with open('ipList.txt', 'r') as f:
    ips = [line.strip() for line in f]
    f.close()

search.search(ipList=ips,path='results/')
