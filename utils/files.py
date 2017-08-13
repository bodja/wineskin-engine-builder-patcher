import os
import shutil
import logging
from distutils.dir_util import copy_tree

from .git_utils import git_backup

logger = logging.getLogger(__name__)


class Migration(object):
    def __init__(self, name, from_dir, to_dir, remove_files=None,
                 create_links=None, copy_inner_files=None):
        """
        :param name: <str> will be used as a tag for git backup
        :param from_dir: <str>
        :param to_dir: <str>
        :param remove_files: <list> relative file paths to remove.
            e.g. old libs files
        :param create_links: <list> of relative path pairs to crate symlink
            # (dir_or_file, link_to_created)
            [
                ('include/libxml2/libxml', 'include/libxml'),
                ('include/freetype2/freetype', 'include/freetype'),
            ]
        :param copy_inner_files: <list> of relative file path pairs that should
            be copied inside of the to_dir
            # (from, to)
            [
                ('include/freetype2/ft2build.h', 'include/ft2build.h')
            ]
        """
        self.name = name
        self.from_dir = from_dir
        self.to_dir = to_dir
        self.remove_files = remove_files or []
        self.create_links = create_links or []
        self.copy_inner_files = copy_inner_files or []

    def migrate(self):
        logger.debug('Applying "%s"', self.name)
        with git_backup(self.to_dir, self.name) as patch_backup:
            if patch_backup.tag_exists(patch_backup.success_tag):
                logger.debug('%s already applied. Skipping...', self.name)
            else:
                self._remove_files()
                self._copy_files()
                self._copy_inner_files()
                self._make_links()
                logger.debug('%s Done!', self.name)

    def reset(self):
        """
        Revert changes
        """
        git_backup(self.from_dir, self.name).rollback()

    def _remove_files(self):
        logger.debug('Removing files...')
        for file_path in self.remove_files:
            full_path = os.path.join(self.to_dir, file_path)
            if os.path.islink(full_path):
                os.remove(full_path)
            elif os.path.isdir(full_path):
                shutil.rmtree(full_path)
            else:
                os.remove(full_path)

    def _copy_files(self):
        logger.debug('Copying new files...')
        copy_tree(self.from_dir, self.to_dir)

    def _copy_inner_files(self):
        logger.debug('Copying new files...')
        for src, dst in self.copy_inner_files:
            full_src = os.path.join(self.to_dir, src)
            full_dst = os.path.join(self.to_dir, dst)
            if os.path.isdir(src):
                copy_tree(full_src, full_dst)
            else:
                shutil.copy(full_src, full_dst)

    def _make_links(self):
        logger.debug('Creating symlinks...')
        for src, dst in self.create_links:
            full_src = os.path.join(self.to_dir, src)
            full_dst = os.path.join(self.to_dir, dst)
            try:
                os.symlink(full_src, full_dst)
            except OSError as err:
                logger.debug('Failed to create symlink %s -> %s',
                             full_src, full_dst)
                raise err
