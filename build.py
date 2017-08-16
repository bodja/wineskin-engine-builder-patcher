import os
import sys
import subprocess
from distutils.dir_util import remove_tree
from urllib.parse import urlparse

import click

import config
from utils.archiver import extract
from utils.downloader import download
from utils.git_utils import apply_patch


def is_url(path):
    try:
        res = urlparse(path)
        return all([res.scheme, res.netloc, res.path])
    except AttributeError:
        return False


@click.command()
@click.argument('path_or_url', type=click.STRING)
@click.option('-n', '--name', type=click.STRING,
              help='Name of the engine which will appear in wineskin menu.')
@click.option('-nfp', '--no-flicker-patch', is_flag=True,
              help='Build wine with no-flickering patch.')
@click.option('-p', '--patch', multiple=True, type=click.Path(exists=True),
              help='/full/path/to/git/patch to be applied.')
def build(path_or_url, name, no_flicker_patch, patch):

    if is_url(path_or_url):
        path_or_url = download(path_or_url, config.DOWNLOAD_TO)
    wine_src_dir = extract(path_or_url, os.path.dirname(path_or_url))

    default_name = f'WS10{os.path.basename(wine_src_dir)}'

    try:
        if patch:
            for p in patch:
                apply_patch(wine_src_dir, p)

        if no_flicker_patch:
            if not name:
                name = f'{default_name}NoFlicker'
            path = os.path.join(config.ROOT_DIR, 'patches', 'wine',
                                'no-flickering-wine-2.14.diff')
            apply_patch(wine_src_dir, path)

        config_writer(wine_src_dir, name or default_name)
        subprocess.run([
            config.WINESKIN_ENGINE_BUILD_SCRIPT
        ], check=True)

    except:
        raise click.ClickException(f'Unexpected error: {sys.exc_info()[:-1]}')
    finally:
        remove_tree(wine_src_dir)


def config_writer(wine_src_dir, engine_name):
    """
    Writes a config.txt file for wineskin engine builder
    """
    config_path = os.path.join(config.WINESKIN_ENGINE_BUILDER_DIR, 'config.txt')
    with open(config_path, 'w+') as f:
        f.writelines([
            f'{wine_src_dir}\n',
            f'{engine_name}\n',
            f'{" ".join(config.WINE_BUILD_OPTIONS)}\n',
            f'{config.ENGINE_BUILDER_VERSION}\n',
            f'{config.SEVEN_ZA_BIN}\n',
            f'{config.MIN_SDK_VERSION}'
        ])


if __name__ == '__main__':
    build()
