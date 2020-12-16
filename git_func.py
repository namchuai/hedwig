import subprocess

START_COMMIT_PATTERN = '''===== START COMMIT =====
Date: %s'''

def create_start_commit(date):
    commit_msg=START_COMMIT_PATTERN%(date)
    subprocess.call(["git", "commit", "-m", START_COMMIT_PATTERN])

def remove_head_commit():
    subprocess.call(["git", "reset", "--hard", "HEAD~1"])
