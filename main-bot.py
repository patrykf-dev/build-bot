import build_archiving
import build_renamer
import discord_messager
import gdrive_uploader
import repository_refresher
import unity_builder

if __name__ == '__main__':
    short_description = "..."

    repository_refresher.refresh()
    print("[1/6] Refreshed repo")

    unity_builder.perform_builds()
    print("[2/6] Made builds")

    build_archiving.archive_builds()
    print("[3/6] Archived builds")

    build_names = build_renamer.rename_builds()
    print("[4/6] Renamed builds")

    builds = gdrive_uploader.upload_to_gdrive(build_names)
    print("[5/6] Uploaded builds")

    discord_messager.send_message(builds, short_description)
    print("[6/6] Sent discord message. Finished :)")
