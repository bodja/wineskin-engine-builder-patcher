import os
import stat
from contextlib import contextmanager
from distutils.dir_util import remove_tree

from shutil import copyfile

import config
from utils import files
from installer.environment.env import Env
from installer.formula.flac import Flac
from installer.formula.freetype import Freetype
from installer.formula.gettext import Gettext
from installer.formula.intltool import Intltool
from installer.formula.json_c import JsonC
from installer.formula.libogg import Libogg
from installer.formula.libpng import LibPng
from installer.formula.libsndfile import Libsndfile
from installer.formula.libsoxr import Libsoxr
from installer.formula.libtool import Libtool
from installer.formula.libvorbis import Libvorbis
from installer.formula.libxml2 import Libxml2
from installer.formula.openal_soft import OpenalSoft
from installer.formula.openssl import Openssl
from installer.formula.pulseaudio import Pulseaudio

git_patches_dir = os.path.join(config.ROOT_DIR, 'patches')

files_migrations = [
    files.Migration(
        name='libs-update',
        from_dir=config.PREFIX,
        to_dir=config.WINESKIN_ENGINE_BUILDER_DIR,
        remove_files=[
            'include/png.h',
            'include/pngconf.h',
            'include/libpng14',
            'lib/libpng.dylib',
            'lib/libpng14.14.dylib',
            'lib/libpng14.dylib',
            'lib/pkgconfig/libpng.pc',
            'lib/pkgconfig/libpng14.pc',
            'include/freetype',
            'include/freetype2',
            'include/libxml',
            'include/libxml2',
            'lib/pkgconfig/libxml-2.0.pc',
            'lib/libxml2.2.dylib',
            'lib/libxml2.dylib',
            'lib/xml2Conf.sh',
            'include/openssl',
            'include/libltdl',
            'lib/libasprintf.dylib',
        ],
        create_links=[
            ('include/libxml2/libxml', 'include/libxml'),
            ('include/freetype2/freetype', 'include/freetype'),
        ],
        copy_inner_files=[
            ('include/freetype2/ft2build.h', 'include/ft2build.h')
        ]
    )
]


@contextmanager
def cleanup(*paths):
    for path in paths:
        if os.path.exists(path):
            remove_tree(path)

    yield

    for path in paths:
        if os.path.exists(path):
            remove_tree(path)


def install_libs(*libs):
    env = Env(universal_bin=True)
    for f in libs:
        f(config.PREFIX, config.DOWNLOAD_TO, config.EXTRACT_TO, env).execute()


def move_libs_to_engine_builder(*migration_instances):
    for migration in migration_instances:
        migration.migrate()


def copy_engine_builder_updated_script():
    src_file = os.path.join(
        config.ROOT_DIR, 'patches', 'engine', 'WineskinEngineBuild'
    )
    dst_file = os.path.join(config.PREFIX, 'WineskinEngineBuild')
    copyfile(src_file, dst_file)
    # make executable
    st = os.stat(dst_file)
    os.chmod(dst_file, st.st_mode | stat.S_IEXEC)


def apply():
    with cleanup(config.PREFIX, config.TMP_DIR):
        install_libs(
            Libtool,
            Intltool,
            Libxml2,
            LibPng,
            Freetype,
            Libogg,
            Libvorbis,
            Flac,
            JsonC,
            Gettext,
            Libsoxr,
            Libsndfile,
            OpenalSoft,
            Openssl,
            Pulseaudio,
        )
        copy_engine_builder_updated_script()
        move_libs_to_engine_builder(*files_migrations)


if __name__ == "__main__":
    apply()
