"""
This module is for testing the civic info api
"""
import logging
import yaml
import civic_info_api

LOGGER = logging.getLogger('civic_info_test')
FH = logging.FileHandler('civic_info_test.log')
FORMATTER = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
FH.setFormatter(FORMATTER)
LOGGER.addHandler(FH)
LOGGER.setLevel(logging.INFO)


class CivicInfoTests:
    """
    This class is for testing the civic info api
    """

    def __init__(self):
        stream = open('civic_info.yaml', 'r')
        self.dictionary = yaml.load(stream, Loader=yaml.SafeLoader)
        self.civic_info = civic_info_api.CivicInfo()

    def test_election_query(self):
        """
        This function tests the elections query functionality in the API
        :return: True or False to indicate if tests passed
        """
        election_info = self.civic_info.elections_query()
        election_info_content = election_info.content.decode('utf-8')
        expected_names = self.dictionary['election_test_results']
        for name in expected_names:
            LOGGER.info('Election verifying for %s', name)
            if name not in election_info_content:
                LOGGER.warning('Election query test FAILED.')
                return False

        excluded_entries = self.dictionary['election_negative_tests']
        for entry in excluded_entries:
            LOGGER.info('verifying exclusion for %s', entry)
            if entry in election_info_content:
                LOGGER.warning('Election query negative test FAILED.')
                return False

        LOGGER.info('Election query test passed.')
        return True

    def test_voter_query(self):
        """
        This function tests the voter query functionality in the API
        :return: True or False to indicate if tests passed
        """
        addresses = self.dictionary['voter_test']
        for address in addresses:
            voter_info = self.civic_info.voter_query(address, self.dictionary['test_election'])
            voter_info_content = voter_info.content.decode('utf-8')

            values = addresses[address]

            for value in values:
                LOGGER.info('Voter verifying for %s', value)
                if value not in voter_info_content:
                    LOGGER.warning('Election query test FAILED.')
                    return False

            LOGGER.info('Voter query test passed for %s.')

        return True


def main():
    """
    Main function to run script and call class functions above
    """
    civic_info_tests = CivicInfoTests()
    election_result = civic_info_tests.test_election_query()
    print("Election Test Pass: " + str(election_result))
    voter_result = civic_info_tests.test_voter_query()
    print("Voter Test Pass: " + str(voter_result))


if __name__ == "__main__":
    # execute only if run as a script
    main()
