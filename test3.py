import pygit2
import os 
# Set the path to the GitLab repository
repo_path = '/path/to/repository'

# Open the repository
repo = pygit2.Repository(os.path.dirname(os.path.abspath(__file__)))

# Get the master branch
master_branch = repo.branches['master']

# Iterate over all branches
for branchname in repo.branches.remote:
    # Skip the master branch
    if branchname == 'master':
        continue

    # Get the branch reference
    branch_ref = repo.branches[branchname]

    # Rebase the branch onto the latest changes in master
    repo.checkout(branch_ref)
    rebase = repo.rebase(branch_ref.target, onto=master_branch.target)
    rebase.finish(repo.default_signature, strategy=pygit2.GIT_REBASE_OPERATION.NONE)

    # Push the rebased branch to the GitLab repository
    remote_name = 'origin'
    remote = repo.remotes[remote_name]
    remote.push([f'{branch_name}:{branch_name}'])
