from libs import db_interface, id_generator, parser, cleanser
import random
idg = id_generator.IdGenerator(limit_size=2000)
id_list = idg.get_id_list()

# ids = """"""
# id_list = ids.split('\n')

for post_id in id_list:
    try:
        # post_id = random.choice(id_list)
        data_parser = parser.Parser(post_id)
        data = data_parser.get_raw_data()
        data_cleanser = cleanser.Cleanser(data)
        cleansed_data = data_cleanser.cleansed_data
        db = db_interface.Interface()
        db.set(cleansed_data)
    except Exception as e:
        print(e)
        print(post_id)
