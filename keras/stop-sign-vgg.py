# coding: utf-8

from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
import numpy as np
from PIL import Image, ImageDraw
from random import randrange, choice
import sys

from keras import backend as K
K.set_image_data_format( 'channels_last' ) # WARNING : important for images and tensors dimensions ordering

model = VGG16(include_top=True, weights='imagenet')

def pred_r(kmodel, crpimg, transform=False):
    imarr = np.array(crpimg).astype(np.float32)
    if transform:
        imarr[:,:,0] -= 129.1863
        imarr[:,:,1] -= 104.7624
        imarr[:,:,2] -= 93.5940
        aux = copy.copy(imarr)
    imarr = np.expand_dims(imarr, axis=0)
    out = kmodel.predict(imarr)
    return decode_predictions(out)

three_colors = [(240,245,245,0), (20,20,20,0), (60, 60, 60, 0)]   # Black, white, gray stickers

color_pallettes = [
    (0, 152, 116, 0),   # emerald
    (221, 65, 36, 0),   # tangerine tango
    (214, 80, 118, 0), # honeysuckle
    (68, 184, 172, 0), # turquoise
    (239, 192, 80, 0), # mimosa
    (91, 94, 166, 0),    # blue izis
    (155, 35, 53, 0),    # chilli pepper
    (223, 207, 190, 0), # sand dollar
    (85, 180, 176, 0),   # blue turquoise
    (225, 93, 68, 0),    # tigerlily
    (127, 205, 205, 0), # aqua sky
    (188, 36, 60, 0),     # true red
    (195, 68, 122, 0),  # fuchsia rose
    (152, 180, 212, 0), # cerulean blue
]

def paste_stickers(im, stickers, colors):
    newim = im.copy()
    draw = ImageDraw.Draw(newim)
    for _ in range(stickers):
        w = randrange(10, 20)
        h = randrange(10, 20)
        x = randrange(60, 190-w)
        y = randrange(70, 190-h)
        color = choice(colors)
        draw.rectangle((x, y, x+w, y+h), fill=color)
    del draw
    return newim

stop_im = Image.open('./stopsign-1.png')
stop_im = stop_im.crop((40, 30, 150, 180)).resize((224, 224))   # 110 x 150

for i in range(10000):
    print i,
    sys.stdout.flush()
    newim = paste_stickers(stop_im, 10, three_colors)
    r = pred_r(model, newim, transform=False)
    if r[0][0][0] != u'n06794110':
        print '\nHit at iteration %d' % i
        print r
        newim.save('iter-%d.png' % i)
    del newim
