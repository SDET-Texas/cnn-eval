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
            logger.info('verifying for ' + name)
            if name not in election_info_content:
                logger.warning('Election query test FAILED.')
                return False

        logger.info('Election query test passed.')
        return True

    def test_voter_query(self):
        voter_info = self.civic_info.voter_query(self.dictionary['test_address'],
                                                 self.dictionary['test_election'])


def main():
    civic_info_tests = CivicInfoTests()
    result = civic_info_tests.test_election_query()
    print(result)


if __name__ == "__main__":
    # execute only if run as a script
    main()
