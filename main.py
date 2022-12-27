from libs import parser, cleanser, id_generator

# parse_test = parser.Parser(86252)
# print(parse_test.get_raw_data())

generated_ids = id_generator.IdGenerator().get_id_list()
for article_id in generated_ids:
    parse_test = parser.Parser(article_id)
    # print(parse_test.get_raw_data())
    cleanse_test = cleanser.Cleanser(parse_test.get_raw_data())
    cleanse_test.cleanse()
    # if not cleanse_test.cleansed_data:
    #     print(cleanse_test.raw_data['data']['jd'])
    print(article_id, cleanse_test.cleansed_data)

# wanted.co.kr/wd/140012 특수케이스