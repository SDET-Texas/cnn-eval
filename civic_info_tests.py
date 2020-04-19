import logging
import yaml
import civic_info_api

logger = logging.getLogger('civic_info_test')
fh = logging.FileHandler('civic_info_test.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.setLevel(logging.INFO)


class CivicInfoTests:

    def __init__(self):
        stream = open('civic_info.yaml', 'r')
        self.dictionary = yaml.load(stream, Loader=yaml.SafeLoader)
        self.civic_info = civic_info_api.CivicInfo()

    def test_election_query(self):
        election_info = self.civic_info.elections_query()
        election_info_content = election_info.content.decode('utf-8')
        expected_names = self.dictionary['election_test_results']
        for name in expected_names:
            logger.info('Election verifying for ' + name)
            if name not in election_info_content:
                logger.warning('Election query test FAILED.')
                return False

        excluded_entries = self.dictionary['election_negative_tests']
        for entry in excluded_entries:
            logger.info('verifying exclusion for ' + entry)
            if entry in election_info_content:
                logger.warning('Election query negative test FAILED.')
                return False

        logger.info('Election query test passed.')
        return True

    def test_voter_query(self):
        addresses = self.dictionary['voter_test']
        for address in addresses:
            voter_info = self.civic_info.voter_query(address, self.dictionary['test_election'])
            voter_info_content = voter_info.content.decode('utf-8')

            values = addresses[address]

            for value in values:
                logger.info('Voter verifying for ' + value)
                if value not in voter_info_content:
                    logger.warning('Election query test FAILED.')
                    return False

            logger.info('Voter query test passed for ' + address + '.')

        return True


def main():
    civic_info_tests = CivicInfoTests()
    election_result = civic_info_tests.test_election_query()
    print("Election Test Pass: " + str(election_result))
    voter_result = civic_info_tests.test_voter_query()
    print("Voter Test Pass: " + str(voter_result))


if __name__ == "__main__":
    # execute only if run as a script
    main()
