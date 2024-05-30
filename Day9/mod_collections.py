from collections import Counter
from collections import defaultdict
from collections import namedtuple
from collections import deque

numbers = [8, 6, 9, 5, 4, 5, 5, 5, 8, 7, 4 ,5 ,4, 4]
print(Counter(numbers))

series = Counter([1,2,2,2,2,3,3,3,1,1,1,4,4,4,4,32])
print(series.values())

print(Counter(numbers).most_common())



cities_list = deque(["London", "Berlin", "Paris", "Madrid", "Rome", "Moscow"])

cities_list.appendleft('Dundalk')
cities_list.append(8)
print(cities_list)