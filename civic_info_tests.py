import yaml
import civic_info_api

stream = open('civic_info.yaml', 'r')
dictionary = yaml.load(stream)

civic_info = civic_info_api.CivicInfo()

election_info = civic_info.elections_query()

voter_info = civic_info.voter_query(dictionary['test_address'], dictionary['test_election'])

print(civic_info)