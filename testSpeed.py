import requests
import time
mean = 0
for i in range(100):
    start_time = time.time()
    r = requests.get('http://127.0.0.1:8000/?csrfmiddlewaretoken=C8pNCrZz98vcT0AVsY9Ej7YtTGRRLHhELl8yO0a2wcIgXLa30lPBs9Z7MeZeb1B0&indexLocation=%EC%A0%84%EA%B5%AD&indexLocation2=%EB%8C%80%ED%86%B5%EB%A0%B9&CompindexLocation=%EC%A0%84%EA%B5%AD&CompindexLocation2=%EB%8C%80%ED%86%B5%EB%A0%B9&startTime=4%EC%9B%94+16%EC%9D%BC&endTime=4%EC%9B%94+16%EC%9D%BC')
    end_time = time.time()
    print('Elapsed_Time = ' + str(end_time - start_time))
    mean = mean + end_time - start_time
print('Mean : ' + str(mean/100))
