import yaml
import requests


class CivicInfo:

    def __init__(self):
        self.url = None
        stream = open('civic_info.yaml', 'r')
        dictionary = yaml.load(stream)
        self.url = dictionary['url']
        self.api_key = dictionary['api_key']

    def elections_query(self, identifier=None, name=None, election_day=None, ocdDivisionId=None):
        elections_url = self.url + r'/elections'
        result = requests.get(elections_url + r'?key=' + self.api_key)
        return result

    def voter_query(self, address, election_id, return_all_available_data=True, official_only=None):
        voter_url = self.url + r'/voterinfo'
        request_string = voter_url + r'?key=' + \
            self.api_key + r'&address=' + address + r'&electionId=' + str(election_id)
        result = requests.get(request_string)
        return result

    def rep_info_by_address(self, levels_filter=None):
        rep_address = self.url + r'/representatives'
        request_string = rep_address
        result = requests.get(request_string)
        return result

    def rep_info_by_division(self, ocd_id):
        rep_division = self.url + r'/representatives/' + ocd_id
        request_string = rep_division
        result = requests.get(request_string)
        return result

    def search_divisions(self, query):
        search_url = self.url + r'/divisions'
        request_string = search_url
        result = requests.get(request_string)
        return result
