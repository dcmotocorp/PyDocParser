import git

import os
repo = git.Repo(os.path.dirname(os.path.abspath(__file__)))

# repo.remotes.origin.fetch()
# repo.git.checkout('master')
# for branch in repo.branches:
#     if branch.name == 'master':
#         continue
#     repo.git.checkout(branch.name)
#     repo.git.rebase('master')
#     repo.git.push('--force', 'origin', branch.name)
# repo.git.checkout('master')

# import git

def rebase_master_with_branch(repo, branch_name):
    try:
        repo.git.checkout(branch_name)
        repo.git.rebase('master')
        repo.git.checkout('master')
        print(f'Rebase successful for branch: {branch_name}')
    except git.exc.GitCommandError as e:
        repo.git.revert('--abort')

        print(f'Rebase failed for branch: {branch_name}')
        print(f'Error: {str(e)}')


repo.git.fetch()
repo.git.checkout('master')
branches = repo.git.branch('-r').split('\n')
print("===========",branches)
# Iterate over the branches and perform the rebase
for branch in branches:
    # Extract the branch name
    branch_name = branch.strip().replace('origin/', '')

    # Skip if it's the master branch
    if branch_name == 'master':
        continue

    # Rebase master with the branch
    rebase_master_with_branch(repo, branch_name)

