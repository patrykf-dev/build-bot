import os

import config


def perform_builds():
    for build_details in config.bot_config["build_details"]:
        _perform_single_build(build_details)


def _perform_single_build(build_details):
    build_command = _create_build_command(build_details["unity_method"])
    os.system(f'cmd /c "{build_command}"')



def _create_build_command(build_method):
    unity_path = config.bot_config["unity_path"]
    project_path = config.bot_config["project_path"]
    command = f'{unity_path} -quit -batchmode -projectpath "{project_path}" -executeMethod {build_method} -logfile asd.txt'
    print(command)
    return command
