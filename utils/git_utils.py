import os
import git
import logging

logger = logging.getLogger(__name__)


class git_backup(object):

    def __init__(self, target_dir, tag):
        self.tag = tag
        self.target_dir = target_dir

    def __enter__(self):
        self.backup()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if any([exc_type, exc_val, exc_tb]):
            self.rollback()
        else:
            self.commit_if_any_change(f'Success tag="{self.tag}".')
            self.add_tag_if_not_exist(self.success_tag)

    @property
    def backup_tag(self):
        return f'backup-{self.tag}'

    @property
    def success_tag(self):
        return f'success-{self.tag}'

    def tag_exists(self, tag):
        try:
            return bool(self.repo.tags[tag])
        except IndexError:
            return False

    @property
    def repo(self):
        if not hasattr(self, '_repo'):
            try:
                repo = git.Repo(self.target_dir)
            except git.exc.InvalidGitRepositoryError:
                repo = git.Repo.init(self.target_dir)
            setattr(self, '_repo', repo)
        return getattr(self, '_repo')

    def __call__(self, func):
        """
        when used as decorator @git_backup(target_dir, tag)
        """
        def wrapper(*args, **kwargs):
            with git_backup(self.tag, self.target_dir):
                res = func(*args, **kwargs)
            return res
        return wrapper

    def backup(self):
        logger.debug('Creating backup tag="%s"...', self.backup_tag)
        self.commit_if_any_change(f'Backup tag="{self.backup_tag}".')
        self.add_tag_if_not_exist(self.backup_tag)

    def commit_if_any_change(self, msg):
        new_files = self.repo.untracked_files
        changed_files = [i.a_path for i in self.repo.index.diff(None)]
        if new_files or changed_files:
            self.repo.git.add('--all')
            self.repo.index.commit(msg)

    def add_tag_if_not_exist(self, tag):
        if not self.tag_exists(tag):
            self.repo.create_tag(tag, self.repo.head.commit.hexsha)

    def delete_tag_if_exists(self, tag):
        if self.tag_exists(tag):
            self.repo.delete_tag(tag)

    def rollback(self):
        logger.debug('Rollback tag="%s"...', self.backup_tag)
        self.repo.git.reset('--hard', self.backup_tag)
        self.delete_tag_if_exists(self.backup_tag)
        self.delete_tag_if_exists(self.success_tag)
        for file_path in self.repo.untracked_files:
            os.remove(os.path.join(self.target_dir, file_path))


def apply_patch(path, patch):
    logger.debug('Applying patch %s', patch)
    try:
        repo = git.Repo(path)
    except git.exc.InvalidGitRepositoryError:
        repo = git.Repo.init(path)
    repo.git.execute(['git', 'apply', patch])
