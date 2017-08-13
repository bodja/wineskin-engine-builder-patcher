import os
import subprocess
import sys
from distutils.dir_util import remove_tree

import click

import config
from utils.archiver import extract
from utils.git_utils import apply_patch


@click.command()
@click.argument('wf', type=click.Path(exists=True))
@click.option('-n', '--name', type=click.STRING)
@click.option('-nfp', '--no-flicker-patch', is_flag=True)
@click.option('-p', '--patch', multiple=True, type=click.Path(exists=True))
def build(wf, name, no_flicker_patch, patch):

    wine_src_dir = extract(wf, os.path.dirname(wf))

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

        config_writer(wine_src_dir, name or os.path.basename())
        subprocess.run([
            config.WINESKIN_ENGINE_BUILD
        ], check=True)

    except:
        raise click.ClickException(f'Unexpected error: {sys.exc_info()[:-1]}')
    finally:
        remove_tree(wine_src_dir)


def config_writer(wine_src_dir, engine_name):
    config_path = os.path.join(config.WINESKIN_ENGINEBASE, 'config.txt')
    with open(config_path, 'w+') as f:
        f.writelines([
            f'{wine_src_dir}\n',
            f'{engine_name}\n',
            f'{" ".join(config.WINE_BUILD_OPTIONS)}\n',
            f'{config.ENGINEBASE_VERSION}\n',
            f'{config.SEVEN_ZA_BIN}\n',
            f'{config.MIN_SDK_VERSION}'
        ])


if __name__ == '__main__':
    build()
