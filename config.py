import os
import getpass

user = getpass.getuser()
ROOT_DIR = os.path.dirname(__file__)

MIN_SDK_VERSION = '10.11'

WINESKIN = f'/Users/{user}/Library/Application Support/Wineskin/'
ENGINEBASE_VERSION = 'W2.5.5v1EngineBase'
WINESKIN_ENGINEBASE = os.path.join(WINESKIN, 'EngineBase', ENGINEBASE_VERSION)

WINESKIN_ENGINE_BUILD = os.path.join(WINESKIN_ENGINEBASE, 'WineskinEngineBuild')

SEVEN_ZA_BIN = os.path.join(WINESKIN, '7za')

WINE_BUILD_OPTIONS = [
    '--disable-option-checking',
    '--without-oss',
    '--without-cms',
    '--disable-tests',
    '--without-v4l',
    '--without-alsa',
    '--without-audioio',
    '--without-capi',
    '--with-coreaudio',
    '--without-esd',
    '--without-hal',
    '--without-jack',
    '--with-xcomposite',
    '--with-xcursor',
    '--with-xinerama',
    '--with-xinput',
    '--with-xml',
    '--with-xrandr',
    '--with-xrender',
    '--with-xshape',
    '--with-xshm',
    '--with-xslt',
    '--with-xxf86vm',
    '--with-x',
    '--without-fontconfig',
    '--without-gphoto',
    '--without-gstreamer',
    '--without-dbus'
]

PREFIX = '/tmp/Wineskin'
TMP_DIR = '/tmp/lib-compiler-cache/'
DOWNLOAD_TO = f'{TMP_DIR}/downloads/'
EXTRACT_TO = f'{TMP_DIR}/libs/'
