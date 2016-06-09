import json
import matplotlib.pyplot as plt


def visual_file(file_name, line_color):
    fig = plt.figure(1)
    with open(file_name, 'r') as f:
        data = json.load(f)
        for d in data:
            cur_births = d['birth']
            for cur_birth in cur_births:
                year = cur_birth['year']
                deathyear = cur_birth['deathyear']
                if deathyear:
                    radius = int(deathyear) - int(year)
                else:
                    radius = 2016 - int(year)
                ax = fig.add_subplot(1, 1, 1)
                circe = plt.Circle((year, 0), radius=radius, color=line_color, fill=False)
                ax.add_patch(circe)
        plt.xlim(800, 2100)
        plt.xticks([i for i in range(800, 2016, 50)])
        plt.ylim(0, 150)
        plt.yticks([])
        plt.subplots_adjust(left=0.01, right=0.99, top=0.58, bottom=0.4)
        plt.show()


if __name__ == '__main__':
    file_name = 'wikibirth-jan.json'
    line_color = 'gray'
    visual_file(file_name, line_color)
