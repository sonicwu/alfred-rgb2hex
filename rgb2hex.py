import os
import sys
import uuid
from enum import Enum
from png import png
from workflow import Workflow


ICON_FOLDER = 'generated-icons'


class WorkMode(Enum):
    RGB_TO_HEX = 1
    HEX_TO_RGB = 2


def main(wf):
    input_string = wf.args[0]

    work_mode = WorkMode.HEX_TO_RGB if input_string.startswith('#') else WorkMode.RGB_TO_HEX
    if work_mode is WorkMode.HEX_TO_RGB:
        hex_to_rgb(wf, input_string)
    else:
        rgb_to_hex(wf, input_string)


def rgb_to_hex(wf, input_string):
    if ',' in input_string:
        trim_string = ''.join(input_string.split())
        rgb_values = trim_string.split(',')
    else:
        rgb_values = input_string.split(' ')

    valid_values = [int(value) for value in rgb_values if value.isdigit() and 0 <= int(value) < 256]
    if len(valid_values) != 3:
        wf.add_item('Please enter valid input', 'R, G, B value should be from 0 to 255 only')
        wf.send_feedback()
        return

    r, g, b = valid_values[0], valid_values[1], valid_values[2]
    hex_string = '#{0:02x}{1:02x}{2:02x}'.format(r, g, b)

    icon_file = generate_icon(r, g, b)

    result = hex_string.upper()
    wf.add_item(title=result, valid=True, arg=result, copytext=result, icon=icon_file)
    wf.send_feedback()


def hex_to_rgb(wf, input_string):
    hex_string = input_string.lstrip('#')
    if len(hex_string) != 6:
        wf.add_item('Please enter valid input', 'HEX string should be start with # and 6 hex characters')
        wf.send_feedback()
        return

    try:
        r, g, b = tuple(int(hex_string[i:i+2], 16) for i in (0, 2, 4))
    except ValueError:
        wf.add_item('Please enter valid input', 'HEX string should be start with # and 6 hex characters')
        wf.send_feedback()
        return

    icon_file = generate_icon(r, g, b)

    result = 'rgb({}, {}, {})'.format(r, g, b)
    wf.add_item(title=result, valid=True, arg=result, copytext=result, icon=icon_file)
    wf.send_feedback()


def generate_icon(r, g, b):
    clear_icons_folder()
    filename = '{}/{}.png'.format(ICON_FOLDER, str(uuid.uuid4()))

    p = [(r,g,b, r,g,b, r,g,b),
         (r,g,b, r,g,b, r,g,b)]
    f = open(filename, 'wb')
    w = png.Writer(3, 2, greyscale=False)
    w.write(f, p)
    f.close()

    return filename


def clear_icons_folder():
    for icon_file in os.listdir(ICON_FOLDER):
        icon_file_path = os.path.join(ICON_FOLDER, icon_file)
        if os.path.isfile(icon_file_path):
            os.unlink(icon_file_path)


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
