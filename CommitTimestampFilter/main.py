import os
import sys
import git
from datetime import datetime, time

REPO_PATH = os.path.dirname(__file__)
BRANCH = 'main'
INCLUDE_WEEKENDS = False
START_TIME = '07:00'
END_TIME = '17:00'

def branch_exists(repo, branch_name):
    return branch_name in repo.heads

def is_within_time_range(commit_time, start_time, end_time):
    commit_time = commit_time.time()
    return start_time <= commit_time <= end_time

def is_weekend(commit_date):
    return commit_date.weekday() >= 5  # 5 and 6 correspond to Saturday and Sunday

def main():
    repo = git.Repo(REPO_PATH)

    # check if the branch exists
    if not branch_exists(repo, BRANCH):
        print(f"Branch {BRANCH} does not exist")
        sys.exit(1)

    commits = list(repo.iter_commits(BRANCH))  # get all commits from the branch
    
    # convert the start and end time to time objects
    start_time = datetime.strptime(START_TIME, '%H:%M').time()
    end_time = datetime.strptime(END_TIME, '%H:%M').time()

    for commit in commits:
        commit_time = datetime.fromtimestamp(commit.committed_date)
        if not INCLUDE_WEEKENDS and is_weekend(commit_time):
            continue
        if is_within_time_range(commit_time, start_time, end_time):
            print(f"Commit: {commit.hexsha}, Date: {commit_time}, Message: {commit.message.strip()}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        REPO_PATH = sys.argv[1]
    if len(sys.argv) > 2:
        BRANCH = sys.argv[2]
    if len(sys.argv) > 3:
        INCLUDE_WEEKENDS = sys.argv[3].lower() == 'true'
    if len(sys.argv) > 4:
        START_TIME = sys.argv[4]
    if len(sys.argv) > 5:
        END_TIME = sys.argv[5]

    # check if the path is a valid git repository
    if not os.path.isdir(REPO_PATH):
        print(f"Invalid path: {REPO_PATH}")
        sys.exit(1)
    
    main()
