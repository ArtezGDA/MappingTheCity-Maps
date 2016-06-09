import json


def count_file(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
        count = 0
        for d in data:
            cur_data = d['deathyear']
            for el in cur_data:
                print(el['deathyear'])
                count += 1
        return count


if __name__ == '__main__':
    file_name = 'wikibirth-jandec.json'
    print('count year: ', count_file(file_name))