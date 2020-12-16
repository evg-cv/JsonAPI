import requests
import datetime
import json


class JsonPlaceholderAPI:
    def __init__(self):
        self.http_url = "https://jsonplaceholder.typicode.com"

    def print_title_posts_99(self):
        api_result = requests.get(f"{self.http_url}/posts/99").json()
        posts_99_title = api_result['title']

        print(f"INFO::: The title of Posts 99: {posts_99_title}")

        return posts_99_title

    def inject_time_stamp_posts_100(self):
        api_result = requests.get(f"{self.http_url}/posts/100").json()
        current_time = datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")
        api_result["time"] = current_time

        print(f"INFO::: The resource of Posts 100 with UTC timestamp: \n{json.dumps(api_result, indent=4)}")

        return api_result

    def create_new_posts(self, delete_ret=False):
        new_posts = {
            "title": "Security Interview Post",
            "user_id": "500",
            "body": "This is an insertion test with a known API"
        }
        post_result = requests.post(f"{self.http_url}/posts", data=json.dumps(new_posts, indent=4),
                                    headers={'Content-type': 'application/json; charset=UTF-8'})
        post_tuple = (post_result.json()["id"], post_result.status_code, post_result.headers["X-Powered-By"])

        if not delete_ret:
            print(f"INFO::: The return value of new posts: {post_tuple}")

        return post_result

    def delete_new_posts(self):

        new_post_id = self.create_new_posts(delete_ret=True).json()["id"]
        delete_result = requests.delete(f"{self.http_url}/posts/{new_post_id}")

        print(f'INFO::: The return value of delete request: '
              f'{delete_result.status_code, delete_result.headers["X-Content-Type-Options"]}')

        return delete_result

    def run(self):
        self.print_title_posts_99()
        self.inject_time_stamp_posts_100()
        self.create_new_posts()
        self.delete_new_posts()


if __name__ == '__main__':
    JsonPlaceholderAPI().run()
