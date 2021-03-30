import json 
import requests

r = requests.get('http://localhost:3000')

data = r.json() 
for d in data:
    print(d['name'] + ' is ' + d['color'])


        
             
#Widget1 is blue. 
#Widget2 is green.
# Widget whatever is whatever...  


#dictionaries are in { } and use key value pairs 
#lists are in [ ] and use numeric indexes [0-n] 