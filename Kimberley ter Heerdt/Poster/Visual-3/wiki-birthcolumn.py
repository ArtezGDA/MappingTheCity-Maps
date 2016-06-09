import json
import csv


def output_parsing(input_file_name, output_file_name):
    with open(input_file_name, 'r') as input_file:
        with open(output_file_name, 'w') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(('Name', 'Description', 'Years lived'))
            data = json.load(input_file)
            for d in data:
                cur_births = d['birth']
                for cur_birth in cur_births:
                    name = cur_birth['name']
                    year = cur_birth['year']
                    deathyear = cur_birth['deathyear']
                    desctiption = cur_birth['description']
                    writer.writerow((name, desctiption, '%s - %s' % (year, deathyear)))


if __name__ == '__main__':
    file_name = 'jan1.json'
    output_file_name = 'result_wikibirth.csv'
    output_parsing(file_name, output_file_name)
