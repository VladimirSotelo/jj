import datetime
import random
_id = [101,102,103,104,105,106,107,108]

for dia in range(1,31):
    for id in _id:
        _in = datetime.datetime(2023,3,dia,8) + datetime.timedelta(minutes=random.randrange(-10,10,1),seconds=random.randrange(-59,59,1)) 
        _out = datetime.datetime(2023,3,dia,17) + datetime.timedelta(minutes=random.randrange(-10,10,1),seconds=random.randrange(-59,59,1))
        
        if random.randrange(1,20,1) > 2:
            print(F"{id},{_in},{_out}")

