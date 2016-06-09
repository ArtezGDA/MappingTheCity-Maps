import json
import csv


def output_parsing(input_file_name, output_file_name):
    with open(input_file_name, 'r') as input_file:
        with open(output_file_name, 'w') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(('Name', 'Description', 'Years lived','Name', 'Description', 'Years lived','Name', 'Description', 'Years lived'))
            data = json.load(input_file)
            i = 0
            list_data = []
            for d in data:
                cur_births = d['birth']
                for cur_birth in cur_births:
                    if i < 3:
                        name = cur_birth['name']
                        desctiption = cur_birth['description']

                        list_data.append(name)
                        list_data.append(desctiption)

                        year = cur_birth['year']
                        deathyear = cur_birth['deathyear']
                        if deathyear and deathyear.isdigit():
                            years_lived = int(deathyear) - year
                            list_data.append(years_lived)
                        else:
                            years_lived = '%s -' % year
                            list_data.append(years_lived)
                        i += 1
                    else:
                        writer.writerow(i for i in list_data)
                        i = 0
                        list_data = []


if __name__ == '__main__':
    file_name = 'wikidata.json'
    output_file_name = 'result_wikidata.csv'
    output_parsing(file_name, output_file_name)