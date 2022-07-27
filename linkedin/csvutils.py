import csv

def list_dict_to_csv(dicts, filename="test.csv"):
    with open(filename, 'w', newline='') as output_file:
        keys = dicts[0].keys()
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dicts)

