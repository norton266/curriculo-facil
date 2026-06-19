from abc import ABC, abstractmethod


class BaseBuilder(ABC):

    def __init__(self, request):
        self.request = request

    @abstractmethod
    def build(self):
        pass

    def get_list(self, key: str):
        return self.request.form.getlist(key)

    def get(self, key: str, default=""):
        return self.request.form.get(key, default)