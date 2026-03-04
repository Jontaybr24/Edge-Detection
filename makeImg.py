import sys
from cs3430_s22_hw05 import depil, Img
from PIL import Image


def img(inpath, outpath, default_delta=1.0, magn_thresh=20, type='w'):
    input_image = Image.open(inpath)
    output_image = Img(input_image, default_delta=default_delta, magn_thresh=magn_thresh, type=type)
    output_image.save(outpath)
    del input_image
    del output_image



if len(sys.argv) > 2:
    name = sys.argv[1].split('.')
    if sys.argv[2].isnumeric():
        img(f'imgs/{name[0]}.{name[1]}', f'out_imgs/{name[0]}.png', magn_thresh=int(sys.argv[2]))
    else:
        img(f'imgs/{name[0]}.{name[1]}', f'out_imgs/{name[0]}.png', type=sys.argv[2])
elif len(sys.argv) > 1:
    name = sys.argv[1].split('.')
    img(f'imgs/{name[0]}.{name[1]}', f'out_imgs/{name[0]}.png')
else:
    print("No image path given")