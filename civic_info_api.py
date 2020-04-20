"""
This module is a wrapper for the civic info api
"""
import yaml
import requests


class CivicInfo:
    """
    This class is a wrapper for the civic info api
    """

    def __init__(self):
        self.url = None
        stream = open('civic_info.yaml', 'r')
        dictionary = yaml.load(stream, Loader=yaml.SafeLoader)
        self.url = dictionary['url']
        self.api_key = dictionary['api_key']

    def elections_query(self):
        """
        :return: A json response listing available elections.
        The following fields appear in result:
        id, name, election_day, ocd_division_id
        Note:  This appears to be still under development.  Filtering appears to be not available
        """
        elections_url = self.url + r'/elections/?key=' + self.api_key
        result = requests.get(elections_url)
        return result

    def voter_query(self, address, election_id=None,
                    return_all_available_data=None, official_only=None):
        """
        :param address: The voter data for the given address
        :param election_id: The election id as available in the election query
        :param return_all_available_data:
        :param official_only: If set to true,
         only data from official state sources will be returned. (Default: false)
        :return:
        """
        voter_url = self.url + r'/voterinfo'
        request_string = voter_url + r'?key=' + \
            self.api_key + r'&address=' + address
        if election_id:
            request_string += r'&electionId=' + str(election_id)
        if official_only:
            request_string += r'&officialOnly=' + str(return_all_available_data)
        if return_all_available_data:
            request_string += r'&returnAllAvailableData=' + str(return_all_available_data)

        result = requests.get(request_string)
        return result

    def rep_info_by_address(self, levels_filter=None):
        """
        This is beyond the scope of current testing.  Will be implemented as needed
        :param levels_filter:
        :return:
        """
        rep_address = self.url + r'/representatives'
        request_string = rep_address
        result = requests.get(request_string)
        raise NotImplementedError

    def rep_info_by_division(self, ocd_id):
        """
        This is beyond the scope of current testing.  Will be implemented as needed
        :param ocd_id:
        :return:
        """
        rep_division = self.url + r'/representatives/' + ocd_id
        request_string = rep_division
        result = requests.get(request_string)
        raise NotImplementedError

    def search_divisions(self, query):
        """
        This is beyond the scope of current testing.  Will be implemented as needed
        :param query:
        :return:
        """
        search_url = self.url + r'/divisions'
        request_string = search_url
        result = requests.get(request_string)
        raise NotImplementedError
