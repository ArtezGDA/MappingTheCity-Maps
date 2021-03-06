import matplotlib.pyplot as plt
import json
import numpy as np


def visual_file(file_name, line_color, font_size, font_size2):
    names = []
    numbs = []
    n = 0
    with open(file_name, 'r') as f:
        data = json.load(f)
        for d in data:
            cur_births = d['birth']
            for cur_birth in cur_births:
                n += 1
                # if n > 50: break
                name = cur_birth['name']
                year = cur_birth['year']
                
                deathyear = cur_birth['deathyear']
                
                names.append(name)
                numbs.append(n)
                
                if deathyear.isdigit():
                    deathyear = int(deathyear)
                    plt.plot([n, n], [year, deathyear], color='black', lw=2)
                else:
                    plt.plot([n, n], [year, year + 5], color='grey', lw=2)
        
        
        plt.yticks([i for i in range(800, 2100, 10)  size=font_size2 ])
        plt.ylabel('year', size=font_size2)
        plt.xticks(numbs, names, size=font_size, rotation=90)


        plt.barh([i for i in range(800, 2100, 50)], [len(names) for _ in range(800, 2100, 50)],
                 alpha=0.1, color='whitesmoke')
        plt.show()


if __name__ == '__main__':
    file_name = 'wikibirth-jan1.json'
    line_color = 'black'
    font_size = 3.5
    font_size2 = 6.0
    visual_file(file_name, line_color, font_size, font_size2)
