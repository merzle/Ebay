import json
import os
from urllib.error import HTTPError
from urllib.request import urlretrieve
from datetime import datetime
from pathlib import Path


base_path = Path(__file__).parent

class Utilities:

    def load_urls(self, filename="urls.json"):
        file_path = (base_path / "../../urls.json").resolve()
        with open(file_path) as file:
            links = json.load(file)
            return links['urls']

    def create_folder(self, directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print('Error: Creating directory. ' + directory)

    def save_image(self, image_url, image_local_path):
        try:
            urlretrieve(image_url, image_local_path)
        except FileNotFoundError as err:
            print(err)  # something wrong with local path
        except HTTPError as err:
            print(err)  # something wrong with url

    def is_int(self, value):
        try:
            int(str(value))
            return True
        except ValueError:
            return False

    def is_float(self, value):
        try:
            float(str(value))
            return True
        except ValueError:
            return False

    def is_date(self, value):
        try:
            datetime.strptime(str(value), '%d.%m.%Y')
            return True
        except ValueError:
            return False

    def infer_data_types(self, article):
        for key in article:
            if isinstance(article[key], list):
                continue
            elif self.is_int(article[key]):
                article[key] = int(article[key])
            elif self.is_float(article[key]):
                article[key] = float(article[key])
            elif self.is_date(article[key]) and str(article[key]) is not None:
                article[key] = datetime.strptime(str(article[key]), '%d.%m.%Y')
        return article
