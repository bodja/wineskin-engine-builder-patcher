import os
import getpass

user = getpass.getuser()
ROOT_DIR = os.path.dirname(__file__)

MIN_SDK_VERSION = '10.12'
SDK_PATH = os.path.join(
    '/Applications/Xcode.app',
    'Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs',
    f'MacOSX{MIN_SDK_VERSION}.sdk'
)

WINESKIN_DIR = f'/Users/{user}/Library/Application Support/Wineskin/'
ENGINE_BUILDER_VERSION = 'W2.5.5v1EngineBase'
WINESKIN_ENGINE_BUILDER_DIR = os.path.join(
    WINESKIN_DIR,
    'EngineBase',
    ENGINE_BUILDER_VERSION
)

WINESKIN_ENGINE_BUILD_SCRIPT = os.path.join(
    WINESKIN_ENGINE_BUILDER_DIR,
    'WineskinEngineBuild'
)

SEVEN_ZA_BIN = os.path.join(WINESKIN_DIR, '7za')

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
