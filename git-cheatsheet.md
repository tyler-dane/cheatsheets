# Git Cheatsheet

## Git Log Searching

Search for when `ZLIB_BUF_MAX` was originally introduced

```bash
git log -S ZLIB_BUF_MAX --oneline
```

## Change file on older commit (not last)

useful when you can't just run `git commit --amend`

```bash
# backup
git branch backup

git add <my fixed files>
git commit --fixup=OLDCOMMIT
git rebase --interactive --autosquash OLDCOMMIT^
```

### PRs

Get forked PR locally

**Option 1: GH CLI**:

- Go to PR on GitHub
- Select Code dropdown
- Run `gh` command

(full docs: [here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/checking-out-pull-requests-locally))

**Option 2: The hard way**
`git fetch origin pull/<#>/head:<branchName></branchName>`

example: `git fetch origin pull/3/head:Installation-doc-Update`

- get pull# and branch name from GitHub PR section

## Rebase & Squash

`git rebase -i <hash>` - rebase up until hash

### Rebase into `main` with conflicts

**Reference:** this blog | [(verdantfox.com)](https://verdantfox.com/blog/how-to-git-rebase-mainmaster-onto-your-feature-branch-even-with-merge-conflicts)

```bash
git checkout <branch in need of rebasing>
git fetch origin

git rebase origin/main

# fix merge conflicts

# add previously merge conflicted files
git add FILE

git rebase --continue
#  if git complains that there were no changes after resolving all conflicts, run:
    # git rebase --skip

# confirm rebase worked
    # if anything broke, run: git reset --hard backup
git diff backup

# pushes your rebase fixed branch to remote.
    # The `--force` tells remote,
    # "I know these changes are correct, accept them as is."
    # Without the --force flag,
    # your remote branch will continue to believe it is out of sync
    # and will claim a merge conflict.
git push origin HEAD --force
```

### Squash non-consecutive commits

TL;DR: change order during rebase

```bash
git rebase --interactive
```

Original history:

```git
pick aaaaaaa Commit A
pick bbbbbbb Commit B
pick ccccccc Commit C
pick ddddddd Commit D
```

Change order:

```git
pick aaaaaaa Commit A
squash ddddddd Commit D
pick bbbbbbb Commit B
pick ccccccc Commit C
```

- git will meld the changes of A and D together into one commit, and put B and C afterwards.
- When you don't want to keep the commit message of D you would use the `fixup` keyword.
