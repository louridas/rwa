import matplotlib

import matplotlib.pyplot as plt

from matplotlib import collections  as mc
from matplotlib.patches import Circle

import sys

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--text", action="store_true",
                    help="display circle numbers")
parser.add_argument("input_file", help="input file")
parser.add_argument("output_file", help="output_file")
args = parser.parse_args()

min_x = sys.maxsize
max_x = -sys.maxsize
min_y = sys.maxsize
max_y = -sys.maxsize

circles = []
texts = []
segments = []

with open(args.input_file) as input_file:
    for line in input_file:
        parts = [ float (x) for x in line.split() ]
        if len(parts) == 3: # circle
            min_x = min(min_x, parts[0]-parts[2])
            min_y = min(min_y, parts[1]-parts[2])
            max_x = max(max_x, parts[0]+parts[2])
            max_y = max(max_y, parts[1]+parts[2])            
            circles.append(Circle(parts[:2], parts[2],
                                  edgecolor='black', facecolor='none',
                                  linewidth=1))
            if args.text:
                texts.append((*parts[:2], len(circles)))
        elif len(parts) == 4: # segment
            min_x = min([min_x, *parts[::2]])
            min_y = min(min_y, *parts[1::2])
            max_x = max([max_x, *parts[::2]])
            max_y = max(max_y, *parts[1::2])            
            segments.append((parts[:2], parts[2:]))

fig, ax = plt.subplots()
ax.set_xlim(min_x - 1, max_x + 1)
ax.set_ylim(min_y - 1, max_y + 1)
sc = mc.LineCollection(segments, colors='black', linewidths=1)
sc.set_capstyle('round')
ax.add_collection(sc)
cc = mc.PatchCollection(circles, match_original=True)
ax.add_collection(cc)
for text in texts:
    ax.text(text[0], text[1], str(text[-1]))
ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
if args.output_file:
    plt.savefig(args.output_file, dpi=300)
plt.show()
