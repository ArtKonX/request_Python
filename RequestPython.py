import requests

class YaUploader:
    def __init__(self, token: str, path: str):
        self.token = token
        self.path = path

    def get_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": "OAuth {}".format(self.token)
          }

    def get_params(self):
        return {
                "path": "{}".format(self.path)
          }
    def get_files_link(self):
        url_link = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        path = self.get_params()
        resp = requests.get(url_link, headers=headers, params=path)
        return resp.json()


    def upload(self):
        href_json = self.get_files_link()
        href = href_json["href"]
        headers = self.get_headers()
        response = requests.put(href, data=open(self.path, 'rb'), headers=headers)
        if response.status_code == 201:
            print("Файл записался на ваш диск!")



if __name__ == '__main__':
    path_to_file = "file.txt"
    token = ""
    uploader = YaUploader(token, path_to_file)
    result = uploader.upload()
