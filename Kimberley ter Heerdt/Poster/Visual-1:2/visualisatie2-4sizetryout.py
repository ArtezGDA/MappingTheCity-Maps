import matplotlib.pyplot as plt
import json
import numpy as np


def visual_file(file_name, line_color, font_size):
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
                    plt.plot([n, n], [year, deathyear], color='red', lw=2)
                else:
                    plt.plot([n, n], [year, year + 5], color='yellow', lw=2)
        plt.yticks([i for i in range(800, 2100, 200)])
        plt.ylabel('year')
        plt.xticks(numbs, names, size=font_size, rotation=90)
        plt.figure(figsize=(300,400))

        plt.barh([i for i in range(800, 2100, 10)], [len(names) for _ in range(800, 2100, 10)],
                 alpha=0.1, color='whitesmoke')
        plt.show()


if __name__ == '__main__':
    file_name = 'wikibirth-jan1.json'
    line_color = 'black'
    font_size = 3.5
    visual_file(file_name, line_color, font_size)
