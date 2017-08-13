import subprocess


class Shell(object):
    def __init__(self, cwd, env, **kwargs):
        self.cwd = cwd
        self.env = env
        self.kwargs = kwargs

    def run(self, *args):
        return subprocess.run(' '.join(args), check=True, shell=True,
                              cwd=self.cwd, env=self.env, **self.kwargs)
