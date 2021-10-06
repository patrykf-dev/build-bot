import os

import config


def rename_builds():
    names = _rename_archives()
    increment_minor_version()
    return names


def _rename_archives():
    names = []
    for build_details in config.bot_config["build_details"]:
        zip_name = f'{build_details["platform_name"]}.zip'
        current_path = config.get_builds_path(zip_name)
        major, minor = _read_versions()
        new_name = f"{config.bot_config['game_name']}_{major}_{minor}_{build_details['short_name']}.zip"
        new_path = config.get_builds_path(new_name)
        os.rename(current_path, new_path)
        names.append(new_path)
    return names


def _read_versions():
    with open('major_version.txt', 'r') as file:
        major = file.read().strip()
    major = major.zfill(config.bot_config["major_version_space"])

    with open('minor_version.txt', 'r') as file:
        minor = file.read().strip()
    minor = minor.zfill(config.bot_config["minor_version_space"])

    return major, minor


def increment_minor_version():
    with open('minor_version.txt', 'r') as file:
        current_minor = int(file.read().strip())

    new_minor = current_minor + 1

    with open('minor_version.txt', 'w') as file:
        file.write(str(new_minor))
