import os
import shutil

import config


def archive_builds():
    _make_archives()
    _remove_build_files()


def _make_archives():
    for filename in os.listdir(config.bot_config["builds_path"]):
        full_path = config.get_builds_path(filename)
        if os.path.isdir(full_path):
            shutil.make_archive(full_path, 'zip', full_path)


def _remove_build_files():
    for filename in os.listdir(config.bot_config["builds_path"]):
        full_path = config.get_builds_path(filename)
        if os.path.isdir(full_path):
            shutil.rmtree(full_path)
