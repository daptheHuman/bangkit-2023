1.
Question 1
If you’re making changes to a local branch while another user has also made changes to the remote branch, which command will trigger a merge?

1 / 1 point

git push


git pull


git rebase


git fetch

Correct
Nice job! The git pull command runs git fetch with the given parameters, then calls git merge to merge the retrieved branch heads into the current branch.

2.
Question 2
Which of the following is a reason to use rebase instead of merging? 

1 / 1 point

When you want to keep a linear commit history


When you want a set of commits to be clearly grouped together in history


When you are on a public branch


When pushing commits to a remote branch

Correct
Way to go! git rebase is useful for maintaining a clean, linear commit history.

3.
Question 3
Where should we keep the latest stable version of the project?

0 / 1 point

The master branch


A separate branch from the master branch


The debug branch


A remote branch 

Incorrect
Not quite. It's common practice to keep the latest version in the master branch and the latest stable version in a separate branch.

4.
Question 4
Which of the following statements represent best practices for collaboration? (check all that apply)

1 / 1 point

When working on a big change, it makes sense to have a separate feature branch.

Correct
Right on! This lets you work on new changes, while still enabling you to fix bugs in the other branch.


You should always rebase changes that have been pushed to remote repos.


Always synchronize your branches before starting any work on your own.

Correct
Awesome! That way, whenever you start changing code, you know that you're starting from the most recent version, and you minimize the chances of conflicts or the need for rebasing.


Avoid having very large changes that modify a lot of different things.

Correct
Woohoo! Instead, try to make changes as small as possible, as long as they’re self-contained.

5.
Question 5
What command would we use to change the base of the current branch?

1 / 1 point

git checkout <branchname>


git pull


git rebase <branchname>


git fetch

Correct
Right on! You can also use git rebase <branchname> to change the base of the current branch to be <branchname>.