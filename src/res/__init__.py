from os.path import dirname, abspath
import inspect

RESOURCE_DIR = dirname(
    abspath(inspect.getfile(inspect.currentframe()))
)

IMG_DIR = RESOURCE_DIR + "/img/"
SOUND_DIR = RESOURCE_DIR + "/sound/"
LEVEL_DIR = RESOURCE_DIR + "/lvl/"
