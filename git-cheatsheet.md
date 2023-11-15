# Git Cheat Sheet

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

## Rebase into `main` with conflicts

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

**Reference:** this blog | [(verdantfox.com)](https://verdantfox.com/blog/how-to-git-rebase-mainmaster-onto-your-feature-branch-even-with-merge-conflicts)
