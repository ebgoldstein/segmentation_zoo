
import os, zipfile, shutil
import tensorflow as tf
from glob import glob

# not available yet


# url = "https://github.com/dbuscombe-usgs/segmentation_zoo/releases/download/0.0.3/santacruz_sentinel2_4class-datasets.zip"
# filename = os.path.join(os.getcwd(), "santacruz_sentinel2_4class-datasets.zip")
# tf.keras.utils.get_file(filename, url)
#
# with zipfile.ZipFile("santacruz_sentinel2_4class-datasets.zip", "r") as z_fp:
#     z_fp.extractall("./")
#
# os.mkdir('4-class')
# for file in glob('*.tfrec'):
#     shutil.move(file, '4-class')
#
#
# url = "https://github.com/dbuscombe-usgs/segmentation_zoo/releases/download/0.0.3/santacruz_sentinel2_2class-datasets.zip"
# filename = os.path.join(os.getcwd(), "santacruz_sentinel2_2class-datasets.zip")
# tf.keras.utils.get_file(filename, url)
#
# with zipfile.ZipFile("santacruz_sentinel2_2class-datasets.zip", "r") as z_fp:
#     z_fp.extractall("./")
#
# os.mkdir('2-class')
# for file in glob('*.tfrec'):
#     shutil.move(file, '2-class')