import svgwrite
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--text", action="store_true",
                    help="display circle numbers")
parser.add_argument("input_file", help="input file")
parser.add_argument("output_file", help="output_file")
args = parser.parse_args()


OFFSET = 50
dwg = svgwrite.Drawing(args.output_file, profile='tiny')

min_x = sys.maxsize
max_x = -sys.maxsize
min_y = sys.maxsize
max_y = -sys.maxsize

circles = []
segments = []

with open(args.input_file) as input_file:
    for line in input_file:
        parts = [ float (x) for x in line.split() ]
        if len(parts) == 3: # circle
            min_x = min(min_x, parts[0]-parts[2])
            min_y = min(min_y, parts[1]-parts[2])
            circles.append(parts)
        elif len(parts) == 4: # segment
            min_x = min([min_x, *parts[::2]])
            min_y = min(min_y, *parts[1::2])
            segments.append((parts[:2], parts[2:]))
            
svg_group = dwg.g()
svg_group.translate(-min_x+OFFSET, -min_y+OFFSET)
dwg.add(svg_group)

for i, c in enumerate(circles):
    svg_group.add(dwg.circle((c[0], -c[1]), c[2],
                             stroke='black', stroke_width=1, fill="none"))
    if args.text:
        text_group = dwg.g(font_size=5)
        text_group.add(dwg.text(i+1, insert=(c[0], -c[1])))
        svg_group.add(text_group)    

for segment in segments:
    p1, p2 = segment    
    svg_group.add(dwg.line((p1[0], p1[1]), (p2[0], p2[1]),
                           stroke='black', stroke_width=1))    
    
dwg.save()
