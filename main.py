from libs import WantedParser, WantedCleanser, WantedIdGenerator

# parse_test = WantedParser.Parser(86252)
# print(parse_test.get_raw_data())

generated_ids = WantedIdGenerator.IdGenerator().get_id_list()
for article_id in generated_ids:
    parse_test = WantedParser.Parser(article_id)
    # print(parse_test.get_raw_data())
    cleanse_test = WantedCleanser.Cleanser(parse_test.get_raw_data())
    cleanse_test.cleanse()
    if not cleanse_test.cleansed_data:
        print(cleanse_test.raw_data['data']['requirements'])
    print(article_id, cleanse_test.cleansed_data)