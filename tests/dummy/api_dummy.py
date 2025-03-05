from locust import HttpUser, task

class Dummy(HttpUser):
    
    @task
    def get_test(self):
        self.client.get("/test")