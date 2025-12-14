from locust import HttpUser, between, task


class CalculatorUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def load_home(self):
        self.client.get("/")

    @task
    def post_add(self):
        self.client.post(
            "/",
            data={"a": "2", "b": "3", "op": "add"},
        )
