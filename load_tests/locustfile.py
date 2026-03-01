from locust import HttpUser, task, between


class PredictUser(HttpUser):
    wait_time = between(1, 2)  # wait 1–2 sec between requests

    @task
    def predict(self):
        payload = {""
            "username": "win",
            "features": [
                13.28, 1.64, 2.84, 15.5, 110,
                2.6, 2.68, 0.34, 1.36, 4.6,
                1.09, 2.78, 880.0
            ]
        }

        headers = {"Content-Type": "application/json"}

        self.client.post(
            "/predict/",
            json=payload,
            headers=headers
        )