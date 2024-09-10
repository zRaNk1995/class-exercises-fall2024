Lab_03 Answers
1.1
drwxr-xr-x 3 zrank zrank 4096 Sep  5 10:34 .
drwxr-xr-x 6 zrank zrank 4096 Sep  5 10:29 ..
drwxr-xr-x 7 zrank zrank 4096 Sep  5 10:34 .git
-rw-r--r-- 1 zrank zrank    8 Sep  5 10:32 README.md

1.2 
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

nothing added to commit but untracked files present (use "git add" to track)

1.3
[master (root-commit) 0b93ce1] add README.md to the repository
 1 file changed, 1 insertion(+)
 create mode 100644 README.md

1.4
commit 0b93ce1a2159054cb8f361bd9c59a360179eeea7 (HEAD -> master)
Author: Zach <zrank@unca.edu>
Date:   Thu Sep 5 10:38:35 2024 -0400



1.5 
diff --git a/README.md b/README.md
index 6cb69d9..62ab950 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,3 @@
 #Readme
+Find All Duplicates
+Write a function (or static method in the case of Java) that accepts a list of integers and returns a list of only those integers that appear more than once.
1.6 6 commands

 3 types of merge
Default-  This option creates a new commit in the base branch that includes all changes from the feature branch
Squash - This option combines all the commits from the feature branch into a single commit before merging it into the base branch. 
Rebase- This option re-applies each commit from the feature branch onto the base branch.


