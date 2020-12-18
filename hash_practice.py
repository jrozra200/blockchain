from hashlib import sha256
import datetime
from decimal import Decimal

start = Decimal(datetime.datetime.now().strftime('%s.%f'))
x = 5
y = 0  # We don't know what y should be yet...

while sha256(f'{x*y}'.encode()).hexdigest()[-7:] != "0000000":
    y += 1

end = Decimal(datetime.datetime.now().strftime('%s.%f'))
time = end - start

print(f'The solution is y = {y}')
print(f'It took {time} seconds to generate this answer.')
print(sha256(f'{x*y}'.encode()).hexdigest())