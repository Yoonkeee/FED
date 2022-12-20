from libs import WantedParser, WantedCleanser

parse_test = WantedParser.Parser(86252)
# print(parse_test.get_raw_data())
cleanse_test = WantedCleanser.Cleanser(parse_test.get_raw_data())
cleanse_test.cleanse()
print(cleanse_test.cleansed_data)