import requests



r= requests.get('{"brand":[],"category":["electronics-and-mobiles/computers-and-accessories/tablets"],"filterKey":[],"f":{},"sort":{"by":"popularity","dir":"desc"},"limit":50,"page":2}')
print(dir(r))