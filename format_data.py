import glob
import os
from natsort import natsorted
from shutil import copy
from PIL import Image

W = 512
H = 384

types = ['tga', 'TGA']
movement_range_folders = natsorted(glob.glob('/home/akari/data/toei-21-25-analyzed/*'))
for mm_f in movement_range_folders:
    cuts = natsorted(glob.glob(os.path.join(mm_f, '*')))

    for cut in cuts:
        cut_name = os.path.basename(cut)
        print(cut_name)
        color_paths = []
        sketch_paths = []

        for t in types:
            sketch_paths.extend(glob.glob('%s/sketch/*.%s' % (cut, t)))
            color_paths.extend(glob.glob('%s/color/*.%s' % (cut, t)))

        if len(color_paths) < 3:
            continue

        skt_save_dir = 'dataset/sketch/' + cut_name
        if not os.path.exists(skt_save_dir):
            os.makedirs(skt_save_dir)
        for sketch in sketch_paths:
            sketch_name = os.path.splitext(os.path.basename(sketch))[0]
            sketch_img = Image.open(sketch).convert('L').resize((W, H), Image.BILINEAR)
            sketch_img.save(os.path.join(skt_save_dir, sketch_name + '.png'))

        color_save_dir = 'dataset/frame/' + cut_name
        if not os.path.exists(color_save_dir):
            os.makedirs(color_save_dir)
        for color in color_paths:
            color_name = os.path.splitext(os.path.basename(color))[0]
            color_img = Image.open(color).convert('RGB').resize((W, H), Image.BILINEAR)
            color_img.save(os.path.join(color_save_dir, color_name + '.png'))
    