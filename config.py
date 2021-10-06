import os

bot_config = {
    "repo_path": "repository",
    "builds_path": "Builds",
    "unity_path": r'C:\"Program Files"\Unity\Hub\Editor\2020.3.2f1\Editor\Unity.exe',
    "project_path": r'D:\Development\build-bot\build-bot\repository',
    "major_version_space": 2,
    "minor_version_space": 3,
    "game_name": "three_powers",
    "build_details": [
        {
            "platform_name": "StandaloneOSX",
            "short_name": "mac",
            "unity_method": "BuildTool.PerformMacDevBuild"
        },
        {
            "platform_name": "StandaloneWindows64",
            "short_name": "win64",
            "unity_method": "BuildTool.PerformWinDevBuild"
        }
    ],
    "discord_hook": "https://discord.com/api/webhooks/..."
}


def get_repo_path():
    return os.path.join(os.getcwd(), bot_config["repo_path"])


def get_builds_path(filename):
    return os.path.abspath(os.path.join(os.getcwd(), bot_config["builds_path"], filename))
