#! /usr/bin/python
# -*- coding: utf8 -*-

import skimage
#import tensorflow.compat.v1 as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior() 


import tensorlayer as tl
from model import *
from utils import *
from config import config
import skvideo.io
import argparse
###====================== HYPER-PARAMETERS ===========================###
## Adam
batch_size = config.TRAIN.batch_size
lr_init = config.TRAIN.lr_init
beta1 = config.TRAIN.beta1
## initialize G
n_epoch_init = config.TRAIN.n_epoch_init
## adversarial learning (SRGAN)
n_epoch = config.TRAIN.n_epoch
lr_decay = config.TRAIN.lr_decay
decay_every = config.TRAIN.decay_every

ni = int(np.sqrt(batch_size))

def read_all_imgs(img_list, path='', n_threads=32):
    """ Returns all images in array by given path and name of each image file. """
    imgs = []
    for idx in range(0, len(img_list), n_threads):
        b_imgs_list = img_list[idx : idx + n_threads]
        b_imgs = tl.prepro.threading_data(b_imgs_list, fn=get_imgs_fn, path=path)
        # print(b_imgs.shape)
        imgs.extend(b_imgs)
        print('read %d from %s' % (len(imgs), path))
    return imgs



def evaluate(video_path):
    ## create folders to save result images

    tl.global_flag['mode'] = 'srgan'

    save_dir = os.path.join("images", "srgan_frames")
    tl.files.exists_or_mkdir(save_dir)
    checkpoint_dir = "checkpoint"
    output_video_name = video_path.split(".")[0]
    output_video_name += "_srgan."+video_path.split(".")[1]
    
    read_video_filepath=os.path.join(os.getcwd(), "videos", video_path)
    
    videogen = skvideo.io.vreader(read_video_filepath)
    metadata = skvideo.io.ffprobe(read_video_filepath)
    metadata=metadata['video']
    H=int(metadata['@height'])
    W=int(metadata['@width'])
    fps=metadata['@r_frame_rate']
    
    C=3
    t_image = tf.placeholder('float32', [None, H, W, C], name='input_image')
    net_g = SRGAN_g(t_image, is_train=False, reuse=False)
    # # ###=============RESTORE G======================================================
    sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=False))
    tl.layers.initialize_global_variables(sess)
    tl.files.load_and_assign_npz(sess=sess, name=os.path.join(checkpoint_dir, 'g_srgan.npz'), network=net_g)
    write_video_filepath=os.path.join(os.getcwd(), 'videos', output_video_name)
    writer = skvideo.io.FFmpegWriter(write_video_filepath,inputdict={'-r': fps},outputdict={'-r': fps,'-vcodec': 'libx264','-pix_fmt': 'yuv420p'})    
    for i, frame in enumerate(videogen):        
        avg=frame.max()-frame.min()
        frame = (frame / avg) - 1  
        out = sess.run(net_g.outputs, {t_image: [frame]})
        #tl.vis.save_image(out[0], save_dir+'/'+str(i)+'.png')
        out=out[0]
        out=(255*(out-np.min(out))/(np.max(out)-np.min(out))).astype(np.uint8)
        writer.writeFrame(out)
        print (i)
        
        
        
    writer.close()
