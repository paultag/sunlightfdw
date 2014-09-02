"""A dummy foreign data wrapper"""


from multicorn import ForeignDataWrapper
from multicorn.utils import log_to_postgres
from logging import ERROR, DEBUG, INFO, WARNING
import requests


class OpenCivicDataFdw(ForeignDataWrapper):
    def __init__(self, fdw_options, fdw_columns):
        super(OpenCivicDataFdw, self).__init__(fdw_options, fdw_columns)
        self.host = fdw_options['host']
        self.apikey = fdw_options['apikey']

    def execute(self, quals, columns):
        people = requests.get("http://localhost:8000/people/").json()['results']
        for person in people:
            yield {
                "name": person['name'],
                "image": person['image'],
                "id": person['id'],
            }
