import git

import config


def refresh():
    success = True
    
    try:
        g = git.cmd.Git(config.get_repo_path())
        g.pull()
    except:
        success = False

    return success
