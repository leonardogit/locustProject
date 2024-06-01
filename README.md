#linha de comando
locust -f testing_locust.py --headless --users 1 --spawn-rate 1 --run-time=1

#ui 
locust -f testing_locust.py

https://docs.locust.io/en/stable/writing-a-locustfile.html#task-decorator
https://docs.locust.io/en/stable/tasksets.html#tasksets