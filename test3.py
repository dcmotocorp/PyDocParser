import git

repo_path = '/path/to/repository'
import os
# Open the repository
repo = git.Repo(os.path.dirname(os.path.abspath(__file__)))

# Fetch the latest changes from the remote repository
repo.remotes.origin.fetch()

# Checkout the master branch
repo.git.checkout('master')

# Loop through all branches in the repository
for branch in repo.branches:
    # Skip the master branch
    if branch.name == 'master':
        continue

    # Checkout the branch
    repo.git.checkout(branch.name)

    # Rebase the branch with master
    repo.git.rebase('master')

    # Push the rebased branch to the remote repository
    repo.git.push('--force', 'origin', branch.name)

# Checkout the master branch again
repo.git.checkout('master')
