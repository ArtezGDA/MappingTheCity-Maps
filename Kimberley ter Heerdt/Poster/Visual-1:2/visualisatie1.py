import matplotlib.pyplot as plt
import json



def visual_file(file_name , life_color, death_color):
    with open(file_name, 'r') as f:
        data = json.load(f)
        for d in data:
            cur_biths = d['birth']
            date = d['date'].split(' ')
            date = int(date[1])
            for cut_birth in cur_biths:
                year = cut_birth['year']
                deathyear = cut_birth['deathyear']
                if deathyear.isdigit():
                    dotsize = abs(year - int(deathyear)) // 10
                    color = life_color
                else:
                    dotsize = 3
                    color = death_color
    
                plt.plot(year, date, 'ro', color=color, markersize=dotsize)
        plt.xlim(0, 2016)
        plt.xticks([i for i in range(0, 2016, 100)])
        plt.ylim(0, 30)
        plt.yticks([i for i in range(0, 30)])
        plt.xlabel('year')
        plt.ylabel('date')
        plt.show()


if __name__ == '__main__':
    file_name = 'wikidata.json'
    life_color = 'yellow'
    death_color = 'red'
    visual_file(file_name, life_color, death_color)
