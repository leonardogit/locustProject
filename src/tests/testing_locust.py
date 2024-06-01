import json
import os.path

from locust import HttpUser, task, between, TaskSet

class UserBehavior(TaskSet):

    def execute(self,body_request,header_request):
        json_data = read_file(body_request)
        json_data2 = read_file(header_request)
        response = self.client.post("v1/votes",json=json_data, headers=json_data2)
        if response.status_code == 201:
            print("Teste executado com sucesso , response foi :  ", response.text)
        else:
            print("Teste deu ruim o erro foi:  ", response.text)

    @task
    def index_page(self):
        body_request = "body.json"
        header_request = "header.json"
        self.execute(body_request,header_request)

class PreConfigurator(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 3)  # Wait between 1 and 3 seconds
    host = "https://api.thecatapi.com/"

def read_file(file_name):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir,os.pardir))
    file_path = os.path.join(project_root, "src\\resources\\masses\\" + file_name)
    if (os.path.exists(file_path)):
        with open(file_path, 'r') as f:
            json_data = json.load(f)
            return json_data
    else:
        print(f'Arquivo {file_name} não foi encontrado')