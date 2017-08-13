import os
import logging
from urllib.request import urlretrieve

logger = logging.getLogger(__name__)


def download(url, dst_dir):
    dst_file_name = os.path.basename(url)
    dst_file_path = os.path.join(dst_dir, dst_file_name)

    if os.path.exists(dst_file_path):
        logger.debug('Found in caches: %s', dst_file_path)
    else:
        logger.debug('Downloading %s', url)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir, exist_ok=True)
        urlretrieve(url, dst_file_path)

    return dst_file_path
