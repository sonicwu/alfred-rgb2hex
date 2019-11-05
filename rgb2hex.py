import os
import sys
import uuid
from png import png
from workflow import Workflow


icon_folder = 'generated-icons'


def main(wf):
    input_string = wf.args[0]

    rgb_values = []
    if ',' in input_string:
        rgb_values = input_string.split(',')
    else:
        rgb_values = input_string.split(' ')

    valid_values = [int(value) for value in rgb_values if value.isdigit() and int(value) >= 0 and int(value) < 256]
    if len(valid_values) != 3:
        wf.add_item('Please enter valid input', 'R, G, B value should be from 0 to 255 only')
        wf.send_feedback()
        return

    r, g, b = valid_values[0], valid_values[1], valid_values[2]
    hex_string = "#{0:02x}{1:02x}{2:02x}".format(r, g, b)

    clear_icons_folder()
    icon_file = generate_icon(r, g, b)

    result = hex_string.upper()
    wf.add_item(title=result, valid=True, arg=result, copytext=result, icon=icon_file)
    wf.send_feedback()


def generate_icon(r, g, b):
    filename = '{}/{}.png'.format(icon_folder, str(uuid.uuid4()))

    p = [(r,g,b, r,g,b, r,g,b),
         (r,g,b, r,g,b, r,g,b)]
    f = open(filename, 'wb')
    w = png.Writer(3, 2)
    w.write(f, p)
    f.close()

    return filename


def clear_icons_folder():
    for icon_file in os.listdir(icon_folder):
        icon_file_path = os.path.join(icon_folder, icon_file)
        if os.path.isfile(icon_file_path):
            os.unlink(icon_file_path)


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
