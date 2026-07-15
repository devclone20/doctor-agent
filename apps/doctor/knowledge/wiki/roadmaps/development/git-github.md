# Git Github Roadmap

##   Hard

# --hard

With this option, both the HEAD pointer and the working directory's contents are updated to match the specified commit. Any changes made since then will be lost.

Visit the following resources to learn more:

- [@official@--hard documentation](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt---hard)

##   Mixed

# --mixed

When using mixed mode, the HEAD pointer is moved to the specified commit. However, files in your working directory remain as they were before the reset. The staging area (index) is updated to match the specified commit.

Visit the following resources to learn more:

- [@official@--mixed documentation](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt---mixed)

##   Soft

# --soft

In this mode, only the HEAD pointer is moved to the specified commit. The files in your working directory are not modified, but they remain as they were when you started the reset.

- [@official@--soft documentation](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt---soft)

## Adding  Updating

# Adding / Updating

To add a submodule to a repository, use `git submodule add https://github.com/user/submodule-repo.git`, which is the typical format for specifying the URL of the submodule repository. This creates a new folder for the submodule and checks it out at the specified revision. To update an existing submodule to its latest commit, run `git submodule update`. If you want to pull in changes from upstream while keeping your submodule's history intact, use `git submodule sync` followed by `git submodule update`.

Visit the following resources to learn more:

- [@article@Git submodules](https://www.atlassian.com/git/tutorials/git-submodule)
- [@article@Working with submodules](https://github.blog/open-source/git/working-with-submodules/)

## Automations

# Automations

To add automation to your GitHub project, use built-in workflows that can trigger actions such as setting fields on item changes or archiving items meeting specific criteria, and also configure automatic item addition from repositories based on matching criteria.

Visit the following resources to learn more:

- [@official@Automating your project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project)
- [@video@GitHub Project Management - Create GitHub Project Board & Automations](https://www.youtube.com/watch?v=oPQgFxHcjAw&t=600s)

## Between Branches

# Between Branches

When comparing the differences between two branches, such as a feature branch and its upstream parent branch, use `git diff <branch1>..<branch2>`. This command displays the changes made on the feature branch relative to the parent branch. It's useful for reviewing the impact of new features or changes before merging them into your mainline.

Visit the following resources to learn more:

- [@article@How to compare branches in Git diff](https://scribehow.com/shared/How_to_Compare_Branches_in_GitHub__xsotezV-S1O-GL0PquqJwQ)
- [@article@How can I see the differences between two branches?](https://stackoverflow.com/questions/9834689/how-can-i-see-the-differences-between-two-branches)

## Between Commits

# Between Commits

To compare two specific commits in your Git history, use git diff followed by the hashes of the commits. This will show you the changes made between those two points, including added, modified, and deleted lines.

Visit the following resources to learn more:

- [@article@Comparing changes with Git diff](https://refine.dev/blog/git-diff-command/)
- [@video@Git Diff 2 Different Commits, Tags or Branches](https://www.youtube.com/watch?v=uq5VWPDCtFo)

## Branch Naming

# Branch Naming

A well-defined branch naming convention is essential for maintaining a clean and organized Git workflow. It's recommended to use descriptive and meaningful names that clearly indicate the purpose of each branch. For example, using prefixes like `feature/`, `fix/`, or `docs/` can help identify whether a branch is related to new feature development, bug fixes, or documentation updates. Additionally, including the issue or task ID (e.g., `issue/123`) can provide context and make it easier for team members to find relevant information. By following a consistent naming convention, you can improve collaboration, reduce confusion, and increase the overall efficiency of your Git workflow.

Visit the following resources to learn more:

- [@article@Naming conventions for Git Branches — a Cheatsheet](https://medium.com/@abhay.pixolo/naming-conventions-for-git-branches-a-cheatsheet-8549feca2534)
- [@article@Git Branching Naming Convention: Best Practices to Follow](https://phoenixnap.com/kb/git-branch-name-convention)

## Branching Basics

# Branching Basics

Branches in Git serve as separate lines of development that allow multiple features or changes to be worked on simultaneously without affecting the main codebase. With branches, you can create isolated environments for different tasks, collaborate with others, and manage complex workflows.

Visit the following resources to learn more:

- [@official@Git Branching - Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
- [@article@Learn Git Branching](https://learngitbranching.js.org/)
- [@video@Git Branches Tutorial](https://www.youtube.com/watch?v=e2IbNHi4uCI)

## Caching Dependencies

# Caching Dependencies

GitHub Actions provides a caching feature that allows you to store and reuse dependencies between workflows, reducing the time it takes to run your actions. By caching dependencies, you can:

- Reuse compiled code
- Store database connections
- Reduce network traffic

It is highly recommended to not store any sensitive information in the cache. For example, sensitive information can include access tokens or login credentials stored in a file in the cache path.

Visit the following resources to learn more:

- [@official@Caching dependencies to speed up workflows](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/caching-dependencies-to-speed-up-workflows)
- [@video@Cache Management with GitHub actions](https://www.youtube.com/watch?v=7PVUjRXUY0o)

## Campus Program

# Campus Program

The GitHub Campus Program offers GitHub Enterprise Cloud and GitHub Enterprise Server free-of-charge for schools that want to make the most of GitHub for their community. This program provides access to a comprehensive set of developer tools, as well as resources and support to help students and educators build projects, collaborate, and develop skills in software development.

Visit the following resource to learn more:

- [@official@About GitHub Campus Program](https://docs.github.com/en/education/explore-the-benefits-of-teaching-and-learning-with-github-education/use-github-at-your-educational-institution/about-github-campus-program)

## Checkout Branch

# Checkout Branch

In Git, to "checkout" from a branch means to switch your working directory to that branch, making it the active branch. This updates your files to match the state of that branch and allows you to work on it.

Visit the following resources to learn more:

- [@official@git-checkout](https://git-scm.com/docs/git-checkout)
- [@article@git-commands-checkout](https://www.git-tower.com/learn/git/commands/git-checkout)
- [@video@Git Checkout. Different ways of using the checkout command in the Git Project](https://youtu.be/h_PIHOFUYuw?si=tebKCCb5U3ues0Io)

## Checkout Tags

# Checkout Tags

Tags in Git are typically used to mark specific points in history, such as a release version. Checking out a tag means switching your working directory to the state of the repository at the point in time when that tag was created.

Visit the following resources to learn more:

- [@article@How To Checkout Git Tags](https://devconnected.com/how-to-checkout-git-tags/)
- [@article@What is git tag, How to create tags & How to checkout git remote tag(s)](https://stackoverflow.com/questions/35979642/what-is-git-tag-how-to-create-tags-how-to-checkout-git-remote-tags)
- [@video@Git Tag Tutorial | Create, Checkout, and Delete Git Tags | Learn Git](https://youtu.be/spkUevg1NqM?si=UXRwJEOI6bpN30nM)

## Cherry Picking Commits

# Cherry Picking Commits

Cherry-picking in Git allows you to apply a specific commit from one branch to another, without merging the entire branch. This is useful when you want to bring in a specific feature or fix from one branch to another without incorporating all the changes from the source branch.

Visit the following resources to learn more:

- [@official@git-cherry-pick docs](https://git-scm.com/docs/git-cherry-pick)
- [@article@Git Cherry Pick](https://www.atlassian.com/git/tutorials/cherry-pick)
- [@video@Git Cherry Pick - Tutorial](https://youtu.be/i657Bg_HAWI?si=3jjn2X8Hi1na--F4)

## Citation Files

# CITATION files

You can add a CITATION.cff file to the root of a repository to let others know how you would like them to cite your work. The citation file format is plain text with human- and machine-readable citation information.

Visit the following resources to learn more:

- [@official@CITATION Files Documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files)

## Clean Git History

# Clean Git History

Cleaning up Git history can make your commit history more readable, concise, and organized. Here are some of the reasons why you'd want to clean your git history:

- makes it easy to decipher the order of the commits in your repository
- It facilitates finding commits that might have introduced bugs and enable rollback if necessary
- To be able to deploy any commit on your development branch using your CI/CD system
- If you are handling mobile app releases and you are responsible for figuring out what feature is in which release.

Visit the following resources to learn more:

- [@article@Clean GIT history — a Step by Step Guide](https://medium.com/@catalinaturlea/clean-git-history-a-step-by-step-guide-eefc0ad8696d)
- [@video@Git Best Practice Tip: Clean Commit History](https://youtu.be/bZpiVijzd2g?si=8lJTlR3LfY9ZUd77)

## Client Vs Server Hooks

# Client vs Server Hooks

Like many other Version Control Systems, Git has a way to fire off custom scripts when certain important actions occur. There are two groups of these hooks: client-side and server-side. Client-side hooks are triggered by operations such as committing and merging, while server-side hooks run on network operations such as receiving pushed commits.

Visit the following resources to learn more:

- [@official@Git Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks#:~:text=There%20are%20two%20groups%20of,for%20all%20sorts%20of%20reasons.)
- [@article@Git Hooks: The Powerful Tool You're Probably Not Using](https://dev.to/algodame/git-hooks-the-powerful-tool-youre-probably-not-using-but-should-be-1lec)
- [@video@Client vs Server Hooks](https://youtu.be/egfuwOe8nXc?si=IkbLCr-3eGE9x6cY)

## Cloning Repositories

# Cloning Repositories

Cloning a repository in Git and GitHub involves creating a local copy of a remote repository on your computer. This allows you to work on the project locally, commit changes, and later push those changes back to the remote repository.

Visit the following resources to learn more:

- [@official@git clone](https://git-scm.com/docs/git-clone)
- [@official@Cloning a Repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
- [@article@Clone a Git Repository](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-clone)
- [@video@Cloning Remote Repository into local machine](https://youtu.be/xeQih8LVtZM?si=djlyTDpLNS0oyqQH)

## Code Reviews

# Code Reviews

The purpose of a code review in software development is to help ensure that the code meets the organization’s standards and requirements, is of high quality, and is maintainable. In addition to identifying errors and bugs, code reviews also promote a culture of learning and collaboration among the development team.

Some of the benefits of code reviews include:

- Increase code quality by identifying defects in the code and issues such as security vulnerabilities and performance problems—before developers merge the code into an upstream branch.
- Ensure compliance with organizational standards, regulations, and the team’s code style.
- Save time and money by detecting issues earlier in the software development process before they become more complex and expensive to fix.
- Boost collaboration, communication, and knowledge sharing among developers by providing a forum to discuss code and ask questions, share ideas and best practices, and learn from each other.
- Ensure that the code is maintainable by identifying any software maintenance issues and suggesting improvements.

Visit the following resources to learn more:

- [@article@A practical guide for better, faster code reviews](https://github.com/mawrkus/pull-request-review-guide)
- [@article@How to improve code with code reviews](https://github.com/resources/articles/software-development/how-to-improve-code-with-code-reviews)

## Collaboration On Github

# Collaboration on GitHub

Collaboration on GitHub is a powerful way for multiple people to work together on the same project, using Git as the version control system. GitHub provides various tools and workflows that make collaboration efficient and organized.

Visit the following resources to learn more:

- [@official@How to collaborate in a GitHub project](https://gist.github.com/neklaf/9002d3acccf6b6e448db5c4c4e8764c0)
- [@article@Best Practices for collaborating in github](https://www.gitkraken.com/blog/collaborate-on-github)
- [@article@Working with GitHub in VS Code](https://code.visualstudio.com/docs/sourcecontrol/github)

## Collaborators  Members

# Collaborators / Members

In GitHub, collaborators and members refer to individuals who contribute to or have access to your repository. Collaborators are users who have been granted permission to contribute code, make changes, and push updates to your repository, whereas members are the owners of a repository, including organization owners who have full control over their team's repositories. Members can be either individual collaborators or part of an organization team, with varying levels of access and permissions based on their role within the team.

Visit the following resources to learn more:

- [@article@Inviting collaborators to a personal repository](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository)
- [@official@REST API endpoints for collaborators](https://docs.github.com/en/rest/collaborators/collaborators?apiVersion=2022-11-28)

## Collaborators

# Collaborators

Collaborators in GitHub are users who have been granted direct access to a repository by the repository owner or organization administrators. Collaborators can perform actions like pushing commits, creating branches, and managing issues or pull requests, depending on the permissions granted to them. They are typically added to private repositories or to public repositories where more control over contributions is needed.

Visit the following resources to learn more:

- [@official@How to add collaborators to your personal projects](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository)
- [@official@Adding outside collaborators to repositories in your organization](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-outside-collaborators/adding-outside-collaborators-to-repositories-in-your-organization)
- [@article@How to Add Collaborators to Your GitHub Repository](https://www.blinkops.com/blog/how-to-add-collaborators-to-your-github-repository)
- [@video@Using GitHub for Team collaboration](https://youtu.be/4nyIS58ORWw?si=yK5LCONNVm9OIUK5)

## Commit Messages

# Commit Messages

A Git commit message is a brief explanation of the changes introduced in a particular commit. It helps others (and your future self) understand the purpose of the changes and the context behind them. Writing clear and informative commit messages is an important practice for maintaining a well-organized and easily navigable project history.

Visit the following resources to learn more:

- [@article@How to Write Better Git Commit Messages](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/)
- [@article@Writing good commit messages](https://www.theodinproject.com/lessons/foundations-commit-messages)
- [@article@How to Write Good Git Commit Messages like a pro](https://medium.com/front-end-weekly/how-to-write-good-git-commit-messages-like-a-pro-2c12f01569d9)
- [@video@Write git commit messages like a PRO with Conventional Commits](https://youtu.be/OJqUWvmf4gg?si=Fgl3isZpP13jYXHP)
- [@video@How to Make Actually Good Commits in Git](https://youtu.be/Dy5t_H2PRrk?si=0V-JEbqphpJX5OLl)

## Commit Msg

# commit-msg

The commit-msg hook is a client-side hook that runs after you enter a commit message, but before the commit is finalized in your repository. It's typically used to validate or modify the commit message before it's recorded in the Git history.

Visit the following resources to learn more:

- [@article@A Git-Hook for Commit Messages Validation - No Husky, Just JS](https://dev.to/mbarzeev/a-git-hook-for-commit-messages-validation-no-husky-just-js-1hni)
- [@video@Git Hooks Made Easy: Create a Custom 'commit-msg' Hook Script](https://www.youtube.com/watch?v=yH1lBm5t97s)

## Committing Changes

# Committing Changes

Committing changes in Git is a crucial part of version control, allowing you to save your progress and record a snapshot of your project's current state.

Visit the following resources to learn more:

- [@official@How git commit works](https://github.com/git-guides/git-commit)
- [@article@Git commit](https://www.atlassian.com/git/tutorials/saving-changes/git-commit)
- [@course@Staging Area (Interactive Lesson)](https://inter-git.com/lessons/adding-files-to-index)
- [@course@Making a Commit (Interactive Lesson)](https://inter-git.com/lessons/making-a-commit)

## Contribution Guidelines

# Contribution Guidelines

Contribution guidelines are essential for collaborative projects on GitHub as they help streamline collaboration, set expectations for contributions, and maintain the project's quality and consistency.

Visit the following resources to learn more:

- [@official@Setting Guidelines for Repository Contributors](https://docs.github.com/articles/setting-guidelines-for-repository-contributors)
- [@official@Contributing Guidelines](https://github.blog/news-insights/contributing-guidelines/)
- [@official@Contributing Guides: A Template](https://github.com/nayafia/contributing-template)
- [@article@How to Build a CONTRIBUTING.md](https://mozillascience.github.io/working-open-workshop/contributing/)

## Creating Account

# Creating Account

To get started with GitHub, you'll need to create a free personal account on GitHub.com and verify your email address. Every person who uses GitHub.com signs in to a personal account. Your personal account is your identity on GitHub.com and has a username and profile.

Visit the following resources to learn more:

- [@official@Creating an Account on GitHub](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github)

## Creating Apps

# Creating Apps

GitHub Apps are a way to integrate with the GitHub platform programmatically, using either the REST API or GraphQL API. They allow developers to create custom integrations that can automate tasks, provide real-time notifications, and build custom workflows.

Visit the following resources to learn more:

- [@official@Creating GitHub Apps](https://docs.github.com/en/apps/creating-github-apps)

## Creating Branch

# Creating Branch

Creating a branch in Git is a fundamental part of working with version control, allowing you to work on different features or fixes without affecting the main codebase. You can create branches either through the terminal or github interface

Visit the following resources to learn more:

- [@official@Git branch documentation](https://git-scm.com/docs/git-branch)
- [@article@Git branch](https://www.atlassian.com/git/tutorials/using-branches)

## Creating Repositories

# Creating Repositories

Creating a Git repository means setting up a system to track changes in your project's files over time. This is crucial for version control, allowing you to manage, review, and collaborate on code efficiently.

Visit the following resources to learn more:

- [@official@Quickstart for repositories - GitHub Docs](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories)

## Custom Domains

# Custom Domains

On GitHub Pages, users can customize their site's URL by connecting a custom domain to their repository. This feature allows users to use their own domain name instead of the default GitHub.io subdomain, giving their site a more professional and personalized look.

Visit the following resources to learn more:

- [@official@Configuring a Custom Domain for Your GitHub Pages Site](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
- [@video@How to Host a Website on GitHub Pages Free (Custom Domain Setup Included)](https://www.youtube.com/watch?v=e5AwNU3Y2es&t=156s)

## Deleting Branch

# Deleting Branch

Deleting a Git branch means removing a line of development from your Git repository. A branch in Git is essentially a pointer to a specific commit, representing an independent line of development. When you delete a branch, you’re removing this pointer, making that line of development no longer accessible through the branch name.

Visit the following resources to learn more:

- [@official@Creating and deleting branches within your repository](https://docs.github.com/articles/creating-and-deleting-branches-within-your-repository)
- [@article@How to Delete a Git Branch Both Locally and Remotely](https://www.freecodecamp.org/news/how-to-delete-a-git-branch-both-locally-and-remotely/)

## Deploying Static Websites

# Deploying Static Websites

Deploying static websites on GitHub Pages involves uploading and serving website content that is generated beforehand, without dynamic functionality. This approach allows for fast deployment, low maintenance, and improved security.

Visit the following resources to learn more:

- [@article@How to Deploy a Static Website for Free Using GitHub Pages](https://medium.com/flycode/how-to-deploy-a-static-website-for-free-using-github-pages-8eddc194853b)
- [@video@How to Host a Website on GitHub Pages Free (Custom Domain Setup Included)](https://www.youtube.com/watch?v=e5AwNU3Y2es)

## Detached Head

# Detached HEAD

In Git, a detached head occurs when you check out a commit directly using its hash instead of a branch name. This leaves your repository's HEAD pointer pointing directly at that commit, rather than being linked to a specific branch. To view the history and changes made in a detached head, use `git log` or `git show`. If you want to see the differences between the current detached head and another branch, use `git diff <branch>`. A detached head can be a useful temporary state for exploring specific commits or features, but it's essential to merge those changes back into a branch before sharing them with others.

Visit the following resources to learn more:

- [@article@How to resolve detached HEAD state in Git](https://graphite.dev/guides/how-to-resolve-detached-head-state-in-git)
- [@video@Head & Detached Head](https://www.youtube.com/watch?v=HvDjbAa9ZsY)

## Documentation

# Documentation

A well-maintained repository should include documentation that helps others understand the project, its context, and how to contribute to it. This is essential for fostering a community around your project and making it easier for newcomers to join in.

Here are some key sections of documentation that you should consider including in each repository:

- README.md: A brief introduction to the project, explaining what it's about, why it exists, and how to get started.
- CONTRIBUTING.md: Guidelines on how others can contribute to the project, including steps for reporting issues, submitting pull requests, or suggesting new features.
- LICENSE: Information about the license under which the repository is released, ensuring users understand their rights and responsibilities when using your code.
- CHANGELOG: A history of changes made to the project over time, highlighting significant updates, bug fixes, or feature additions.

These documents help ensure a smooth onboarding process for contributors, making it easier for them to collaborate effectively and enhance the overall project.

Visit the following resources to learn more:

- [@article@How to Manage Documentation in a GitHub Repository: A Guide for Junior Developers](https://dev.to/mochafreddo/how-to-manage-documentation-in-a-github-repository-a-guide-for-junior-developers-pgo)

## Fast Forward Vs Non Ff

# Fast-Forward vs Non-FF

In Git, when you merge branches, there are two primary types of merges: Fast-Forward and Non-Fast-Forward (No-FF). These terms describe how Git handles the history and pointers when merging branches. Understanding the difference between these two types of merges is crucial for managing your project's commit history effectively.

A Fast-Forward merge occurs when the branch you are merging into (often main or master) has not diverged from the branch you are merging (often a feature branch). In other words, the commit history of the target branch is a strict subset of the branch being merged. In a Fast-Forward merge, Git simply moves the pointer of the target branch forward to the latest commit on the branch being merged.
No new merge commit is created; the history is linear.

A Non-Fast-Forward (No-FF) merge happens when the target branch has diverged from the branch being merged or when you explicitly choose to create a merge commit. In this case, Git creates a new commit that represents the merging of the two branches. Git creates a new merge commit that has two parent commits: one from the target branch and one from the branch being merged. The merge commit is a snapshot of the merged work, preserving the history of both branches.

Visit the following resources to learn more:

- [@article@Git Fast-Forward VS Non-Fast-Forward](https://leimao.github.io/blog/Git-Fast-Forward-VS-Non-Fast-Forward/)
- [@article@Git Merge: To Squash Or Fast-Forward?](https://dev.to/trpricesoftware/git-merge-to-squash-or-fast-forward-3791)
- [@article@Difference between a git fast forward and no fast forward](https://gist.github.com/moraisaugusto/1fa02c49b6d9833fcdf665505595ac2e)
- [@video@GIT Fast Forward Visualized](https://youtu.be/DN1fNYoJgDw?si=_TZKACj4SCOuESGm)
- [@video@git merge no fast forward](https://youtu.be/X_8atqzsO8U?si=e9hMQg_aWLRMWf4O)

## Fetch Without Merge

# Fetch without Merge

Running `git fetch` retrieves changes from a remote repository into your local clone, but does not automatically merge any of these changes into your local working directory. This is different from `git pull`, which both fetches and merges remote changes. By using fetch without merge, you can ensure that your local clone is up-to-date with the latest information from the remote repository, while leaving your working directory unchanged. You can then choose to apply these changes by using merge or rebase. This approach helps maintain a clean and consistent local state, making it easier to manage and commit changes.

Visit the following resources to learn more:

- [@official@Git Fetch](https://git-scm.com/docs/git-fetch)
- [@article@Git fetch](https://www.atlassian.com/git/tutorials/syncing/git-fetch)
- [@video@Git Fetch | What is Git Fetch and How to Use it | Learn Git](https://www.youtube.com/watch?v=uEEcw1s_wWk)

## Forking Vs Cloning

# Forking vs Cloning

Forking and cloning are two fundamental concepts in Git, particularly when working with repositories hosted on platforms like GitHub, GitLab, or Bitbucket. While both actions involve copying a repository, they serve different purposes and have distinct workflows.
Cloning a repository means creating a local copy of a repository that exists on a remote server (e.g., GitHub) on your local machine. This allows you to work on the project locally, make changes, and then push those changes back to the remote repository if you have the necessary permissions.
Forking a repository is specific to platforms like GitHub, GitLab, and Bitbucket. When you fork a repository, you create a copy of someone else’s repository in your own account. This forked repository is independent of the original and can be modified without affecting the original project.

Visit the following resources to learn more:

- [@official@The difference between forking and cloning a repository](https://github.com/orgs/community/discussions/35849)
- [@article@Git fork vs. clone: What's the difference?](https://www.theserverside.com/answer/Git-fork-vs-clone-Whats-the-difference)
- [@video@Git Fork vs. Git Clone: What's the Difference?](https://youtu.be/6YQxkxw8nhE?si=mJNvcaB4lQccsU57)
- [@video@GitHub Forking vs Cloning: Key Differences Explained](https://youtu.be/yQSjqYs2UBE?si=3BKYtWmkLIMWvA6G)

## Git Attributes

# Git Attributes

Git attributes are settings stored in the .gitattributes file, controlling how Git handles files in your repository. They can influence filtering (e.g., ignoring specific files), conversion (formatting or transforming files during Git operations), and formatting (applying consistent styles). These settings can be applied to specific file types (like *.txt) or filter files based on content patterns. Attributes also define smudge patterns (highlighting differences) and ignore patterns, helping maintain a clean repository by automatically applying intended settings for certain file types.

Visit the following resources to learn more:

- [@official@Customizing Git - Git Attributes](https://git-scm.com/book/en/v2/Customizing-Git-Git-Attributes)
- [@opensource@gitattributes/gitattributes](https://github.com/gitattributes/gitattributes)
- [@article@The benefits of git attributes and how to set them up](https://medium.com/@cloudwala/the-benefits-of-git-attributes-and-how-to-set-them-up-87f90251b8e0)

## Git Bisect

# Git Bisect

Git Bisect is an interactive tool used to identify which commit in your project's history introduced a bug or regression. You start by identifying two commits: one where the issue isn't present (the "good" commit) and another where it is (the "bad" commit). Then, run `git bisect start`, followed by `git bisect good` for the good commit and `git bisect bad` for the bad commit. Git Bisect will guide you through a binary search process, asking you to test the midpoint of your current range until it identifies the exact commit that introduced the bug or regression.

Visit the following resources to learn more:

- [@official@Git Bisect](https://git-scm.com/docs/git-bisect)
- [@article@Using `git bisect` to find the faulty commit](https://dev.to/alvesjessica/using-git-bisect-to-find-the-faulty-commit-25gf)
- [@video@Git Bisect | How to use Git Bisect | Learn Git](https://www.youtube.com/watch?v=z-AkSXDqodc)

## Git Commit   Amend

# git commit --amend

`git commit --amend` is a command used to modify the most recent commit in your repository's history by updating its message, adding or removing files, or changing the commit's metadata. This allows you to correct mistakes or improve the commit's description after it has been made. When using --amend, Git will replace the existing commit with a new one that includes any changes made since the last commit, effectively "amending" the previous commit.

Visit the following resources to learn more:

- [@article@Changing a commit message](https://docs.github.com/en/enterprise-cloud@latest/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/changing-a-commit-message)
- [@article@Rewriting history](https://www.atlassian.com/git/tutorials/rewriting-history)
- [@video@Git Amend Tutorial: Rewrite Git History](https://www.youtube.com/watch?v=q53umU5vMkk)

## Git Config

# git config

The `git config` command is a convenience function that is used to set Git configuration values on a global or local project level. These configuration levels correspond to .gitconfig text files. Executing `git config` will modify a configuration text file.

The most basic use case for `git config` is to invoke it with a configuration name, which will display the set value at that name. Configuration names are dot delimited strings composed of a 'section' and a 'key' based on their hierarchy. For example: `user.email`

Visit the following resources to learn more:

- [@official@Git - git-config Documentation](https://git-scm.com/docs/git-config)
- [@article@git config | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config)
- [@article@Setting your username in Git](https://docs.github.com/en/get-started/getting-started-with-git/setting-your-username-in-git)
- [@article@Git config commands | Git tutorial](https://nulab.com/learn/software-development/git-tutorial/git-commands-settings/git-config-commands/)

## Git Filter Branch

# git filter-branch

You can use `git filter-branch` to rewrite Git revision history by applying custom filters on each revision.

- Filter types: You can modify trees (e.g., removing a file or running a Perl script) or information about each commit.
- Preserving original data: The command preserves all original commit times, merge information, and other details unless specified otherwise.
- Rewriting specific branches: Only the positive refs mentioned in the command line are rewritten; if no filters are specified, commits are recommitted without changes.

Notably, there exists a simpler, safer, and more powerful alternative: `git filter-repo`. This tool is actively promoted by Git and offers a streamlined approach to filtering revisions, making it a preferred choice for rewriting your Git history, especially when managing large repositories.

Visit the following resources to learn more:

- [@official@git filter-branch](https://git-scm.com/docs/git-filter-branch)
- [@official@git filter-repo](https://github.com/newren/git-filter-repo)
- [@article@Removing sensitive data from a repository](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)

## Git Hooks

# Git hooks

Git hooks are scripts that run automatically at specific points during the Git workflow, such as when you commit, push, or pull changes from a repository. These scripts can be used to perform various tasks, like validating code, formatting files, or even sending notifications.

There are two types of Git hooks:

- Client-side hooks: Run on your local machine before committing changes.
- Server-side hooks: Run on the remote server when you push changes.

Visit the following resources to learn more:

- [@official@Customizing Git - Git Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)
- [@article@Git hooks](https://www.atlassian.com/git/tutorials/git-hooks)
- [@video@What are GitHooks? Explained in 5 minutes](https://www.youtube.com/watch?v=1OFiiPretCM)

## Git Init

# git init

The `git init` command creates a new Git repository. It can be used to convert an existing, unversioned project to a Git repository or initialize a new, empty repository. Most other Git commands are not available outside of an initialized repository, so this is usually the first command you'll run in a new project.

Visit the following resources to learn more:

- [@official@Git - git-init Documentation](https://git-scm.com/docs/git-init)
- [@article@git init | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-init#:~:text=The%20git%20init%20command%20creates,run%20in%20a%20new%20project.)
- [@course@Creating Repository (Interactive Lesson)](https://inter-git.com/lessons/creating-repository)

## Git Lfs

# Git LFS

Git Large File Storage (LFS) is an extension that helps manage large files by tracking metadata, not storing entire files. It allows storing and tracking binary assets like images, videos, audio files separately from your regular Git repository. By storing only metadata in your Git repository, you improve clone and push times, reducing storage usage. This approach is particularly useful for media repositories, large dataset storage, and binary asset management in game development. Note that Git LFS requires a separate server or storage system to store actual file content.

Visit the following resources to learn more:

- [@article@Learning About Git Large File System (LFS)](https://medium.com/swlh/learning-about-git-large-file-system-lfs-72e0c86cfbaf)
- [@video@Git LFS (Large File Storage) | Learn Git](https://www.youtube.com/watch?v=jXsvFfksvd0)

## Git Log Options

# git log options

`git log` is a command in Git that shows the commit history of your repository. It provides a detailed view of all commits, including their hashes, authors, dates, and messages.

Here are some common git log options:

- `-2`: Only show the last two commits.
- `-- <file-name>`: Show the commits that modified a specific file.
- `--all`: Show all branches in the repository.
- `--graph`: Display the commit history as a graph.
- `--pretty`: Enable clean colorized output.
- `--no-color`: Disable colorized output.
- `--stat`: Show a statistical summary of changes.
- `**-S`: Only show commits with modified files.

You can combine these options to tailor your log output to suit your needs.

For example, `git log -2 --graph` will display the last two commits in graph form.

Visit the following resources to learn more:

- [@official@Git Log](https://git-scm.com/docs/git-log)
- [@article@Git Log Cheatsheet](https://elijahmanor.com/blog/git-log)

## Git Patch

# Git Patch

In Git, a patch is a file that contains a set of changes made to a project's codebase. It's essentially a diff (difference) file that shows the modifications between two versions of a commit or a branch. However, despite its usefulness in certain contexts, the use of Git patches has declined somewhat with the advent of more modern and efficient ways to manage code changes.

Visit the following resources to learn more:

- [@article@Git Patch](https://www.gitkraken.com/learn/git/git-patch)
- [@article@How to generate and apply patches with git?](https://gist.github.com/nepsilon/22bc62a23f785716705c)

## Git Push   Force

# git push --force

`git push --force` is a command that allows you to overwrite or "force" an existing commit on a remote repository with a new commit from your local repository. This can be useful in certain situations, such as when you need to update the remote branch with changes that were previously rejected or when you want to remove commits that are no longer relevant. However, it's essential to exercise caution when using git push --force because it can overwrite changes made by others or even your own previous work. Always verify that there are no conflicting changes on the remote repository before using this command.

Visit the following resources to learn more:

- [@article@Git Push Force](https://www.gitkraken.com/learn/git/problems/git-push-force)
- [@video@How to force push to GitHub?](https://www.youtube.com/watch?v=wgXbfLn-zkI)

## Git Rebase

# git rebase

Git rebase is a powerful command in Git that allows you to integrate changes from one branch into another. Unlike git merge, which creates a new commit to combine the histories of two branches, git rebase moves or applies commits from one branch on top of another, effectively re-writing the commit history.

Visit the following resources to learn more:

- [@official@Git - git-rebase Documentation](https://git-scm.com/docs/git-rebase)
- [@article@git rebase](https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase)
- [@video@git rebase - Why, When &amp; How to fix conflicts](https://youtu.be/DkWDHzmMvyg?si=59jauQgkL-sMewzo)
- [@video@Git Rebase --interactive: EXPLAINED](https://youtu.be/H7RFt0Pxxp8?si=gLhfkVW_PmWHBQSs)

## Git Reflog

# Git Reflog

Git reflog is a powerful tool in Git that keeps a record of all the changes made to the branches and commits in your repository, including actions that are not part of the regular commit history, such as resetting branches or checking out commits. It's particularly useful for recovering lost commits or understanding the history of changes in your repository, even if those changes are not reflected in the normal commit history.Reflog stands for "reference log." It records when the tip of branches or other references (like HEAD) is updated in your repository.

Visit the following resources to learn more:

- [@official@Git - git-reflog Documentation](https://git-scm.com/docs/git-reflog)
- [@article@What is the Git Reflog? | Learn Version Control with Git](https://www.git-tower.com/learn/git/faq/what-is-git-reflog)
- [@video@Learn Git Essentials 12: Git Reflog](https://youtu.be/RVu8lpS7JFY?si=eNGBpsYfHtlyPClj)
- [@video@Git Reflog Command. Get all log details of the reference using git reflog show command](https://youtu.be/I4f4pddD16g?si=0Ny7xOJgiPgdfuh6)

## Git Remotes

# Git Remotes

In Git, a remote is a reference to a repository that exists on another server or system. Remotes allow you to access and interact with a copy of your repository that is stored elsewhere, making it possible to collaborate with others, share your work, and maintain multiple copies of your repository for backup and disaster recovery purposes. When you add a remote to your local repository, Git creates a reference to the remote repository, enabling you to push changes from your local repository to the remote one, pull changes from the remote to your local one, or fetch changes from the remote without updating your local copy. This enables distributed development and helps maintain a centralized version of your project's history, making it easier to track changes, manage conflicts, and ensure that everyone has access to the most up-to-date code.

Visit the following resources to learn more:

- [@official@About Remote Repositories](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories)
- [@video@What is a Remote Repository? [Beginner Git Tutorial]](https://www.youtube.com/watch?v=Lb4yvfrX_7I)

## Git Reset

# git reset

Git reset is a command that allows you to "undo" or reset your current branch to a previous state by moving its HEAD pointer, effectively discarding changes made since then. When using git reset, it's essential to specify one of the three modes: soft, hard, or mixed. The mode you choose will determine how Git interacts with files in your working directory and staging area.

Visit the following resources to learn more:

- [@article@git reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset)
- [@video@Git Reset | How to Use Git Reset | Learn Git](https://www.youtube.com/watch?v=s1idhUiCk38)

## Git Revert

# git revert

Git revert is a command that allows you to "undo" or revert specific commits in your Git repository. It creates a new commit that reverses the changes made by the specified commit(s), effectively rolling back your code to a previous state.

Here are some key things to know about `git revert`:

- Reverts changes, not moves HEAD: Unlike `git reset`, which can move your current branch's head to a different point in history, `git revert` creates new commits that reverse the changes made by specific commit(s).
- Creates new commits: Each time you use `git revert`, it creates a new commit that undoes the specified change. This means your Git history will still contain all previous commits.
- Can be used with multiple commits: If you want to revert multiple commits, simply specify their hashes or references (e.g., branch names) separated by commas.

Visit the following resources to learn more:

- [@article@Git Revert](https://medium.com/@meghasharmaa704/git-revert-84727b543c17)
- [@video@Git Revert - Visualised](https://www.youtube.com/watch?v=XJqQPNudPSY)

## Git Stash Basics

# Git Stash Basics

Git stash allows you to temporarily save your changes, or "stashes", when they're not yet ready for commit. This feature is useful when you need to work on multiple tasks, and want to switch between them without committing changes that are not complete. By using `git stash`, you can quickly stash uncommitted changes, reset the working directory to a clean state, and then apply the stashed changes later when they're ready for commit. This helps avoid cluttering the commit history with incomplete work, and allows you to maintain a clean and organized repository by separating your progress on different tasks.

To apply a stash in Git, you can use the following commands:

- `git stash apply`: This command applies the topmost stash (the most recent one) by default. It will merge the stashed changes into your current working directory.
- `git stash apply <stash_name>`: If you want to specify a particular stash, you can use its name instead of default. For example, if you've stored multiple stashes and want to apply an earlier one, you can use <stash_name>.
- `git stash pop`: This command is similar to apply, but it also automatically deletes the applied stash from the stash list. If you need more control over which stash to apply, using pop might be a better option.

Visit the following resources to learn more:

- [@article@Git stash](https://www.atlassian.com/git/tutorials/saving-changes/git-stash)
- [@article@A practical guide to using the git stash command](https://opensource.com/article/21/4/git-stash)

## Git Vs Other Vcs

# Git vs Other VCS

Git has become the de facto standard for source control in software development, but it's not the only version control system (VCS) available. Here are some key differences between Git and other popular VCS:

- Mercurial: Mercurial is a distributed VCS that uses a similar architecture to Git. However, it has a more centralized approach and doesn't use hashes for tracking changes.
- Subversion: Subversion is a centralized VCS that's often compared to Git. While both systems support branching and merging, Subversion requires a central server to manage the repository.
- Perforce: Perforce is a commercial VCS that's designed for large-scale development projects. It uses a centralized approach and has features like build automation and issue tracking.
- CVS: CVS is an older version control system that's still in use today. However, it lacks many modern features and is often considered outdated.

Visit the following resources to learn more:

- [@article@Git vs. Other VCS: A Comparative Analysis](https://medium.com/@pascalchinedu2000/git-vs-other-vcs-a-comparative-analysis-5cb03ad58e0e)

## Git Worktree

# Git Worktree

A Git worktree allows you to create multiple working directories for a single repository, each with its own checkout and index. Unlike a regular checkout, which creates a new working directory for a specific branch and updates your IDE's configuration settings, a Git worktree does not require you to switch between branches using git checkout. This means you can have multiple branches checked out at the same time without affecting each other or requiring changes to your IDE configurations. By creating a separate worktree for each branch, you can stage changes independently and maintain distinct working directories without impacting the main repository or its working directory.

Visit the following resources to learn more:

- [@article@Git Worktree](https://www.gitkraken.com/learn/git/git-worktree)
- [@video@Manage Branches easily using Git Worktree](https://www.youtube.com/watch?v=cRunWRC8ye0)

## Github Actions

# GitHub Actions

GitHub Actions is a very useful tool for automation, allowing developers to automate tasks within the software development lifecycle directly on GitHub.

One of the best ways to learn about GitHub Actions is through the course offered by Microsoft Learn. This course is well-structured and provides practical examples that are concise and easy to understand.

Visit the following resources to learn more:

- [@official@GitHub Actions](https://docs.github.com/en/actions)
- [@course@Microsoft Learn: Introduction to GitHub Actions](https://learn.microsoft.com/en-us/collections/n5p4a5z7keznp5)
- [@course@YouTube: GitHub Actions Playlist](https://www.youtube.com/watch?v=-hVG9z0fCac&list=PLArH6NjfKsUhvGHrpag7SuPumMzQRhUKY&pp=iAQB)
- [@video@What are GitHub Actions](https://www.youtube.com/watch?v=URmeTqglS58)

## Github Api

# GitHub API

The GitHub API is a powerful tool that allows developers to interact with the GitHub platform programmatically. It provides access to various GitHub features, such as user data, repository information, and commit history, through both REST and GraphQL interfaces. The API supports authentication, implements rate limiting, and offers webhooks for real-time notifications, enabling developers to automate tasks, create custom integrations, and build applications that leverage GitHub's functionality.

Visit the following resources to learn more:

- [@official@GitHub API Docs](https://docs.github.com/en/rest?apiVersion=2022-11-28)
- [@article@Getting Started](https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api?apiVersion=2022-11-28)

## Github Apps

# GitHub Apps

A GitHub App is a way to integrate with the GitHub platform programmatically, using either the REST API or GraphQL API. It allows developers to create custom integrations that can automate tasks, provide real-time notifications, and build custom workflows.

Visit the following resources to learn more:

- [@official@GitHub Apps Documentation](https://docs.github.com/en/apps)

## Github Classroom

# GitHub Classroom

GitHub Classroom is an integrated feature within GitHub that allows educators to create and assign homework assignments, projects, or quizzes directly to students. This feature streamlines the process of teaching and learning by making it easy for instructors to share code, provide feedback, and track student progress all in one place. By using GitHub Classroom, teachers can focus on high-level instruction and student engagement, while also promoting collaboration and hands-on learning experiences.

Visit the following resources to learn more:

- [@official@About GitHub Classroom](https://docs.github.com/en/education/manage-coursework-with-github-classroom/get-started-with-github-classroom/about-github-classroom)
- [@video@GitHub Classroom - Getting Started Guide](https://www.youtube.com/watch?v=xVVeqIDgCvM&list=PLIRjfNq867bewk3ZGV6Z7a16YDNRCpK3u)

## Github Cli

# GitHub CLI

GitHub CLI is a command-line interface tool that brings GitHub functionality to your terminal. It allows developers to interact with GitHub directly from the command line, enabling them to manage repositories, create issues, pull requests, and perform various GitHub operations without leaving their terminal environment. This powerful tool streamlines workflows, enhances productivity, and provides a seamless integration between local development and GitHub's collaborative features, making it easier for developers to incorporate GitHub into their daily coding routines.

Visit the following resources to learn more:

- [@official@GitHub CLI Docs](https://cli.github.com/)
- [@video@What is the GitHub CLI?](https://www.youtube.com/watch?v=uy_PEGgUF4U)

## Github Codespaces

# GitHub Codespaces

GitHub Codespaces is a cloud-based development environment that allows developers to create, access, and use pre-configured, ready-to-use environments for coding. It provides a seamless way to develop, test, and debug applications in a virtual machine or container, eliminating the need for local setup and configuration. With GitHub Codespaces, users can spin up a new environment with their desired configuration, tools, and dependencies in just a few clicks. This feature streamlines development workflows, reduces friction, and increases productivity by providing instant access to a tailored coding environment for each project.

Visit the following resources to learn more:

- [@official@GitHub Codespaces Overview](https://docs.github.com/en/codespaces/overview)
- [@video@How to Deploy a GitHub Codespace](https://www.youtube.com/watch?v=_01iCF9sO1c)

## Github Copilot

# GitHub Copilot

GitHub Copilot is an AI-powered code-completion tool that helps developers write code faster and with less errors. It uses a combination of machine learning algorithms and access to GitHub's vast repository of open-source code to provide context-aware suggestions for coding tasks. Copilot can generate entire functions, methods, or even entire classes based on the context of the code being written. This feature aims to reduce the time spent on coding by providing immediate and relevant suggestions, allowing developers to focus more on high-level design and problem-solving.

Visit the following resources to learn more:

- [@official@Quickstart for GitHub Copilot](https://docs.github.com/en/copilot/quickstart)
- [@video@Intro to GitHob Copilot in Visual Studio](https://www.youtube.com/watch?v=z1ycDvspv8U)
- [@video@GitHub Copilot in VSCode: Top 10 Features Explained](https://www.youtube.com/watch?v=2nPoiUJpDaU)

## Github Discussions

# GitHub Discussions

GitHub Discussions is a collaborative communication feature within GitHub repositories that provides a dedicated space for community conversations, questions, and knowledge sharing. It allows team members, contributors, and users to engage in threaded discussions, share ideas, ask for help, and make announcements outside of specific code changes or issues. This feature enhances project collaboration by centralizing important conversations, reducing noise in the issue tracker, and fostering a sense of community around open-source projects or team initiatives.

Visit the following resources to learn more:

- [@official@GitHub Discussions Docs](https://docs.github.com/en/discussions)
- [@video@What is GitHub Discussions?](https://www.youtube.com/watch?v=bErGYN3Ljz8)

## Github Education

# GitHub Education

GitHub Education is a program that provides free and discounted access to GitHub's developer tools, services, and resources for students, teachers, and researchers. This program aims to support education and research in software development, by making it easier for students and educators to learn, collaborate, and build projects on GitHub. By using GitHub Education, students can gain hands-on experience with real-world coding challenges, while educators can create a more engaging and interactive learning environment.

Visit the following resources to learn more:

- [@official@official GitHub Education Docs](https://education.github.com/)
- [@video@GitHub GitHub Education: free programs, technology, and opportunities available for Students](https://www.youtube.com/watch?v=HIVFdN9VGgw)

## Github Essentials

# GitHub Essentials

GitHub Essentials refers to the core features and functionalities that form the foundation of GitHub's version control and collaboration platform. These essentials include repositories for storing and managing code, branches for parallel development, pull requests for code review and merging, issues for tracking tasks and bugs, and collaborative tools like project boards and wikis. Understanding and mastering these fundamental components allows developers to effectively manage their projects, collaborate with team members, and contribute to open-source initiatives, making GitHub an indispensable tool in modern software development workflows.

Visit the following resources to learn more:

- [@official@GitHub Essentials - Microsoft](https://learn.microsoft.com/en-us/contribute/content/git-github-fundamentals)
- [@official@Hello World](https://docs.github.com/en/get-started/start-your-journey/hello-world)

## Github Gists

# GitHub Gists

A GitHub Gist is a small code or text snippet that can be shared with others. It is a simple way to share code, configuration files, or other snippets of text without creating a full-fledged repository. Gists are useful for sharing examples, demos, or tutorials, and they can also serve as a starting point for larger projects. Each gist has a unique URL that can be shared with others, allowing them to view and edit the content. Gists support various file types, including code files, text files, and even images. They also provide features like syntax highlighting, line numbers, and commit history.

Visit the following resources to learn more:

- [@official@Creating Gists](https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists)
- [@official@REST API endpoints for Gists](https://docs.github.com/en/rest/gists/gists?apiVersion=2022-11-28)

## Github Interface

# GitHub Interface

The GitHub interface is a web-based platform that provides a user-friendly environment for managing and collaborating on software projects. It offers a comprehensive set of tools and features accessible through an intuitive layout, including repository management, code browsing, issue tracking, pull requests, and project boards. The interface is designed to streamline workflows, facilitate team communication, and enhance productivity for developers of all skill levels. With its clean and organized structure, users can easily navigate between different sections of their projects, review code changes, manage tasks, and interact with team members, making it an essential tool for modern software development and version control.

Visit the following resources to learn more:

- [@official@GitHub Desktop App](https://github.com/apps/desktop)
- [@article@Getting Started with GitHub](https://digital.gov/resources/an-introduction-github/)

## Github Marketplace

# GitHub Marketplace

GitHub Marketplace is a platform that allows developers to discover, install, and manage third-party tools and services directly within their GitHub environment. These tools can provide a range of features, such as code analysis, project management, or collaboration, making it easier for developers to work efficiently and effectively. By using the GitHub Marketplace, developers can streamline their workflow, reduce friction, and focus on writing code.

Visit the following resources to learn more:

- [@official@GitHub Marketplace](https://github.com/marketplace)
- [@official@About GitHub Marketplace for apps](https://docs.github.com/en/apps/github-marketplace/github-marketplace-overview/about-github-marketplace-for-apps)

## Github Models

# GitHub Models

GitHub Models is a feature that allows developers to search, explore, and use pre-trained AI models from various sources. This platform provides a way to discover and experiment with these models, making it easier to integrate AI capabilities into software projects. By using GitHub Models, developers can quickly find and try out different models, without having to train them from scratch.

Visit the following resources to learn more:

- [@official@Prototyping with AI models](https://docs.github.com/en/github-models/prototyping-with-ai-models)
- [@video@GitHub Models DEMO | AI models for developers on GitHub](https://www.youtube.com/watch?v=WiBB8Lsgl7I)

## Github Organizations

# GitHub Organizations

GitHub Organizations are shared accounts that provide centralized management and collaboration for multiple projects and teams. They offer enhanced administrative controls, allowing owners to create teams with specific access permissions, manage member roles, and oversee repositories at scale. Organizations facilitate better project coordination, resource sharing, and team communication, making them ideal for businesses, open-source projects, and large-scale collaborations. With features like team discussions, project boards, and audit logs, GitHub Organizations streamline workflow management and foster a more structured and secure development environment.

Visit the following resources to learn more:

- [@official@About Organizations](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/about-organizations)
- [@video@Set up a GitHub Organization](https://www.youtube.com/watch?v=XowSSIhJFuk)

## Github Packages

# GitHub Packages

GitHub Packages is a package repository service that allows developers to store and share packages, containers, and other software artifacts. It provides a central location for sharing packages with teams, organizations, or the wider developer community. GitHub Packages supports popular package managers like npm, Maven, and Gradle, as well as container registries like Docker Hub. This feature enables seamless integration of packages into development workflows, making it easier to share dependencies, libraries, and frameworks within and across projects. By using GitHub Packages, developers can simplify dependency management, reduce errors, and improve overall collaboration.

Visit the following resources to learn more:

- [@official@Introduction to GitHub Packages](https://docs.github.com/en/packages/learn-github-packages/introduction-to-github-packages)
- [@official@GitHub Packages documentation](https://docs.github.com/en/packages)

## Github Pages

# GitHub Pages

GitHub Pages is a feature that allows users to host and publish web content directly from their GitHub repositories. It provides a simple way to create and deploy websites, blogs, or projects without the need for manual configuration or maintenance. Users can upload custom themes, add plugins, and use various tools to customize their pages.

Visit the following resources to learn more:

- [@official@About GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)
- [@official@Creating a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)
- [@official@GitHub Pages examples](https://github.com/collections/github-pages-examples)

## Github Projects

# GitHub Projects

GitHub Projects is a flexible project management tool integrated directly into GitHub repositories. It allows teams to create customizable project boards, track issues and pull requests, and manage workflows using Kanban-style columns or table views. With features like automated workflows, custom fields, and various visualization options, GitHub Projects helps teams organize, prioritize, and track work across multiple repositories. This tool enhances collaboration, increases transparency, and streamlines project management processes, making it easier for developers and stakeholders to stay aligned on project goals and progress.

Visit the following resources to learn more:

- [@official@About Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)
- [@video@How to use Projects Roadmap](https://www.youtube.com/watch?v=D80u__nYYWw)

## Github Releases

# GitHub Releases

GitHub Releases is a feature that allows developers to package and distribute software versions to users. It provides a way to create tagged points in a repository's history, attach binary files (such as compiled executables or packaged code), and include release notes. This feature makes it easy to track and manage different versions of a project, share pre-compiled binaries with users who may not want to build from source, and communicate changes and updates to the community. GitHub Releases integrates seamlessly with Git tags and can be automated as part of a continuous integration and deployment pipeline.

Visit the following resources to learn more:

- [@official@About Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
- [@article@REST API endpoints for releases](https://docs.github.com/en/rest/releases/releases?apiVersion=2022-11-28)

## Github Security

# GitHub Security

GitHub Security is a suite of features and tools that help developers identify, fix, and prevent security vulnerabilities in their code. It provides a comprehensive approach to secure coding practices by integrating with the developer's workflow. The main components of GitHub Security include: `Code Scanning`, which uses AI-powered analysis to detect potential vulnerabilities; `Dependabot`, which automates dependency updates to prevent attacks via vulnerable dependencies; `Secret scanning`, which detects and flags secrets like API keys or credentials; and `GitHub Advanced Security`, which offers more advanced security features for larger teams. By using these tools, developers can ensure their code is secure, and identify potential issues before they become serious problems.

Visit the following resources to learn more:

- [@official@GitHub security features](https://docs.github.com/en/code-security/getting-started/github-security-features)
- [@official@Dependabot Quick-start Guide](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide)
- [@official@About user alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/about-alerts#about-user-alerts)

## Github Sponsors

# GitHub Sponsors

A GitHub Sponsor is a way to support and fund open-source projects on GitHub. It allows maintainers of public repositories to receive financial support from users who value their work. Sponsors can contribute funds to help with expenses, development time, or other project-related costs. In return, sponsors are recognized as supporters in the repository's README file and on the project's website. This feature promotes transparency, accountability, and appreciation within open-source communities, making it easier for maintainers to focus on their projects.

Visit the following resources to learn more:

- [@official@Sponsoring an open source contributor through GitHub](https://docs.github.com/en/sponsors/sponsoring-open-source-contributors/sponsoring-an-open-source-contributor-through-github)
- [@official@Receiving sponsorships through GitHub Sponsors](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors)

## Github Wikis

# GitHub Wikis

GitHub Wikis are collaborative documentation spaces integrated directly into GitHub repositories. They provide a platform for teams to create, edit, and organize project-related information, such as documentation, guidelines, and FAQs. Wikis support Markdown formatting, making it easy to structure content and include images or links. With version control and the ability to clone wiki repositories, teams can collaboratively maintain up-to-date documentation alongside their code, enhancing project understanding and facilitating knowledge sharing among contributors and users.

Visit the following resources to learn more:

- [@official@About Wikis](https://docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis)
- [@official@Documenting your project with Wikis](https://docs.github.com/en/communities/documenting-your-project-with-wikis)

## Gitignore

# .gitignore

Ignored files are tracked in a special file named `.gitignore` that is checked in at the root of your repository. There is no explicit git ignore command: instead the `.gitignore` file must be edited and committed by hand when you have new files that you wish to ignore. `.gitignore` files contain patterns that are matched against file names in your repository to determine whether or not they should be ignored.

Visit the following resources to learn more:

- [@official@gitignore Documentation](https://git-scm.com/docs/gitignore)
- [@article@.gitignore file - ignoring files in Git | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/saving-changes/gitignore)
- [@article@Ignoring files - GitHub Docs](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files)
- [@opensource@gitignore - A collection of useful .gitignore templates](https://github.com/github/gitignore)

## Graphql Api

# GraphQL API

The GitHub GraphQL API is a set of APIs that provides access to various GitHub features, such as user data, repository information, and commit history. It allows developers to interact with the GitHub platform programmatically using GraphQL queries.

Visit the following resources to learn more:

- [@official@GitHub GraphQL API documentation](https://docs.github.com/en/graphql)
- [@official@Forming calls with GraphQL](https://docs.github.com/en/graphql/guides/forming-calls-with-graphql)

## Handling Conflicts

# Handling Conflicts

When multiple developers work on the same project simultaneously, conflicts can arise during the merging process. This occurs when changes made by different individuals overlap or contradict each other in a specific code file. In such situations, Git's conflict resolution mechanism comes into play, allowing users to manually resolve these issues and merge the conflicting changes.

Visit the following resources to learn more:

- [@article@Resolving a merge conflict using the command line](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line)
- [@article@Resolve merge conflicts in Visual Studio](https://learn.microsoft.com/en-us/visualstudio/version-control/git-resolve-conflicts?view=vs-2022)
- [@video@Resolve Git MERGE CONFLICTS: The Definitive Guide](https://www.youtube.com/watch?v=Sqsz1-o7nXk)

## Head

# HEAD

The `HEAD` file is at the core of how Git knows the SHA-1 of the last commit when running commands like `git branch <branch>`. It serves as a symbolic reference, pointing to the current branch. However, in rare cases, HEAD can contain the actual SHA-1 value of a Git object, such as when checking out a tag, commit, or remote branch, which puts your repository in a "detached HEAD" state.

Visit the following resources to learn more:

- [@official@Git Internals - Git References - The HEAD](https://git-scm.com/book/en/v2/Git-Internals-Git-References#:~:text=want%20to%20create.-,The%20HEAD,-The%20question%20now)
- [@video@Learn Git Essentials: Head & Detached Head](https://www.youtube.com/watch?v=HvDjbAa9ZsY)

## History

# History

The history of a Git repository is a record of all commits made over time, including changes to files, commit messages, and metadata. This history is stored as a series of snapshots, with each commit representing a new version of the codebase.

Visit the following resources to learn more:

- [@official@Git Basics - Viewing the Commit History](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)

## Installation And Setup

# Installation and Setup

The GitHub CLI can be installed on Windows, macOS, and Linux operating systems. Installation options include downloading binaries directly from the release page or using package managers (such as homebrew, pip, etc).

Once installed, setting up the GitHub CLI typically involves authenticating with your GitHub account by running `gh auth login` in your terminal. This step is essential for linking your GitHub credentials to the CLI, allowing you to interact with your repositories and perform various actions.

Visit the following resources to learn more:

- [@official@GitHub CLI - Installation](https://github.com/cli/cli?tab=readme-ov-file#installation)
- [@official@GitHub CLI - Release](https://github.com/cli/cli/releases/)
- [@official@GitHub CLI Quickstart](https://docs.github.com/en/github-cli/github-cli/quickstart)

## Installing Git Locally

# Installing Git Locally

To use Git on your local machine, you need to install it first. The installation process varies depending on your operating system:

- On Windows: Download the binary from the official Git or GitHub release page and follow the installation instructions.
- On macOS (using Homebrew): Run `brew install git` in your terminal.
- On Linux: Run `sudo apt-get install git` or `sudo yum install git` depending on your distribution.

Once installed, you can verify the Git version by running `git --version` in your terminal. This will display the currently installed Git version.

Visit the following resources to learn more:

- [@official@Git - Downloads](https://git-scm.com/downloads)
- [@article@Install Git](https://github.com/git-guides/install-git)

## Issue Management

# Issue Management

The GitHub CLI provides a range of features for managing issues within your repository. Here are some key actions you can perform:

- Listing issues: Run `gh issue list` to view a list of all open and closed issues.
- Creating issues: Use `gh issue create --title "Issue Title" --body "Issue body"` to create a new issue with the specified title and body.
- Assigning issues: Run `gh issue assign <issue-number> <username>` to assign an issue to a specific user.
- Labelling issues: Use `gh issue label <issue-number> <label-name>` to add a label to an existing issue.
- Closing issues: Run `gh issue close <issue-number>` to mark an issue as closed.

Visit the following resources to learn more:

- [@official@gh issue](https://cli.github.com/manual/gh_issue)
- [@video@Manage GitHub Issues From The Command Line Using GitHub CLI](https://www.youtube.com/watch?v=nuCQiP41jU0)

## Issues

# Issues

On GitHub, an issue is a way to track and report bugs, feature requests, or other problems with a repository. Here are some key aspects of issues:

- Creating issues: Users can create new issues by submitting a form on the repository's Issues page.
- Issue titles and descriptions: Each issue has a title and body (description), which provide context for the problem or request.
- Assignees: Issues can be assigned to specific users, who are then responsible for addressing the issue.
- Labels: Labels are used to categorize issues by topic, priority, or other criteria. This helps filter and organize issues within a repository.
- States: Issues have states that reflect their status, such as "Open", "Closed", or "Pending".
- Comments: Users can comment on existing issues to discuss or provide additional context.
- Labels and milestones: Issues can be associated with labels (topics) and milestones (deadlines), which help filter and prioritize them.

Issues are a core feature of GitHub repositories, enabling teams to collaborate effectively on resolving problems and implementing new features.

Visit the following resources to learn more:

- [@official@About Issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues)
- [@video@What is GitHub Issues?](https://www.youtube.com/watch?v=6HWw7rhwvtY)

## Kanban Boards

# Kanban Boards

On GitHub, Kanban boards provide a visual representation of issues as they move through the development process.

A Kanban board typically has columns representing different stages or states, such as "To-Do", "In-Progress", and "Done". Each issue is represented by a card on the board, which can be moved between columns as its state changes. Users can drag and drop issue cards to move them from one column to another, reflecting progress or completion.

Visit the following resources to learn more:

- [@official@Projects - Boards - Changing the layout of a view](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/changing-the-layout-of-a-view)
- [@video@GitHub Project Management - Create GitHub Project Board & Automations](https://www.youtube.com/watch?v=oPQgFxHcjAw)

## Labelling Issues  Prs

# Labelling Issues / PRs

On GitHub, labels are a way to categorize issues and pull requests (PRs) by topic, priority, or other criteria. Some common labels used are:

- `Bug`
- `Duplicate`
- `Enhancement`
- `Feature request`
- `High priority`
- `Needs feedback`

Visit the following resources to learn more:

- [@official@Managing labels](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels)

## Learn The Basics

# Learn the Basics

A Version Control System (VCS) is a tool that helps developers manage changes to their code over time. It allows multiple versions of a project to exist simultaneously, making it easier to collaborate with others and maintain a record of all modifications.

Visit the following resources to learn more:

- [@article@What is version control?](https://www.atlassian.com/git/tutorials/what-is-version-control)
- [@article@What is Git? - The Complete Guide to Git](https://www.datacamp.com/blog/all-about-git)
- [@article@Version Control (Git) - The Missing Semester of Your CS Education](https://missing.csail.mit.edu/2020/version-control/)
- [@video@What is Git? Explained in 2 Minutes!](https://www.youtube.com/watch?v=2ReR1YJrNOM)
- [@official@GUI Clients](https://git-scm.com/downloads/guis)
- [@official@Getting Started - Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [@official@Creating an account on GitHub](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github)

## Linear Vs Non Linear

# Linear vs Non-Linear

In Git, linear and non-linear history refer to different ways of managing commit history.

- Linear history: A repository with a linear history has commits that are applied in a single, sequential order.
- Non-linear history: A repository with a non-linear history allows multiple branches or lines of development, which can be merged back into the main branch at different points.

Visit the following resources to learn more:

- [@article@Linear vs Non-Linear History](https://idiv-biodiversity.github.io/git-knowledge-base/linear-vs-nonlinear.html)
- [@article@Linear git history - Part I](https://jun-sheng.medium.com/linear-git-history-part-i-b97184dde252#:~:text=The%20benefit%20of%20having%20a%20linear%20git%20history&text=It%20is%20easier%20to%20understand,bisect%20to%20track%20a%20bug.)

## Local Vs Global Config

# Local vs Global Config

To manage local and global configuration settings, you can use the git config command with the --local and --global options.

- Local configuration: Run `git config --local [key] [value]` to set a local configuration setting for the current repository.
- Global configuration: Use `git config --global [key] [value]` to set a global configuration setting that applies to all repositories on your system.

Visit the following resources to learn more:

- [@official@Customizing Git - Git Configuration](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration)
- [@article@A step-by-step guide to setting up global Git config properties](https://medium.com/geekculture/a-step-by-step-guide-to-setting-up-git-config-global-properties-db6dbce30fa8)

## Managing Remotes

# Managing Remotes

In Git, a remote repository refers to a copy of a project's source code stored on a server or other machine.

- Adding remotes: Use `git remote add [name] [url]` to add a new remote repository. This allows you to track changes and push/pull updates from the remote.
- Listing remotes: Run `git remote -v` to list all configured remotes with their URLs.
- Renaming remotes: Update the name of an existing remote using `git remote rename [old-name] [new-name]`.
- Deleting remotes: Remove a remote repository with `git remote remove [name]`.

Managing remotes is essential for collaborating on projects or tracking changes from upstream sources.

Visit the following resources to learn more:

- [@official@Managing remote repositories](https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories)

## Managing Tags

# Managing Tags

In Git, a tag is a named reference to a specific commit in the project's history.

- Creating tags: Use `git tag [name] [commit-hash]` to create a new tag. You can also use `git tag -a [name] -m "[message]" [commit-hash]` for annotated tags.
- Listing tags: Run `git tag` to display all existing tags.
- Deleting tags: Remove an existing tag with `git tag -d [tag-name]`.

Tags can be used for marking releases, milestones, or other significant events in a project's history.

Visit the following resources to learn more:

- [@official@Git Basics - Tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
- [@article@Git — Use Tags for Versioning and Release Management](https://medium.com/@KeyurRamoliya/git-use-tags-for-versioning-and-release-management-09aca9631eee)

## Markdown

# Markdown

Markdown is a simple way to add formatting to text without using HTML tags or other complex syntax. It's easy to read and write, making it suitable for documentation, README files, and more. Some basic GitHub Markdown features include:

- Basic syntax: Use headers (`# Heading`), bold/italic text (**bold**, *italic*), and lists (- item) to format text.
- Links: Create links with `[text](url)` or `[text][ref]`.
- Images: Embed images with `[![alt-text](image-url)]`.

By using Markdown, you can easily format text within your GitHub repository, making it easier to read and understand for yourself and others.

Visit the following resources to learn more:

- [@official@Basic writing and formatting syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [@article@Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## Marketplace Actions

# Marketplace Actions

The GitHub Marketplace offers a wide range of pre-built actions that can be used to automate tasks and workflows within your repository.

- Automate tasks: Use marketplace actions to automate tasks such as testing, deployment, or security.
- Customize workflows: Create custom workflows using marketplace actions to tailor the build process to specific needs.
- Streamline development: By automating repetitive tasks, developers can focus on code quality and collaboration.

These actions are created by the GitHub community and can be easily added to your workflow to enhance productivity and efficiency.

Visit the following resources to learn more:

- [@official@GitHub MarketPlace - Actions](https://github.com/marketplace?type=actions)

## Mentions

# Mentions

Mentions on GitHub allow you to notify specific users or teams about comments, issues, pull requests, or other activities. This feature improves collaboration by encouraging participation and discussion among team members, increasing visibility of important topics, and streamlining communication within your repository. To use mentions, simply type `@username` or `@teamname` in a comment, and GitHub will auto-complete the mention as you type, automatically linking their username to the comment and notifying them about the discussion.

Visit the following resources to learn more:

- [@official@Mention Somebody](https://github.blog/news-insights/mention-somebody-they-re-notified/)

## Merge Strategies

# Merge Strategies

When combining changes from one branch into another, Git provides various merge strategies to choose from. These methods allow for flexibility and customization in integrating code updates into your main branch. The available options include:

- Fast Forward (FF)
- Non-Fast Forward
- Rebase
- Squash
- Cherry Picking

Visit the following resources to learn more:

- [@official@Git Merge Strategies](https://git-scm.com/docs/merge-strategies)
- [@article@Git Merge Options](https://www.atlassian.com/git/tutorials/using-branches/merge-strategy)

## Merging Basics

# Merging Basics

A merge in Git is the process of combining changes from one branch into another. When you want to integrate updates from one branch (the source) into another branch (the target), you need to perform a merge. This involves resolving conflicts between the two branches, if any exist. The goal of merging is to create a new commit that represents the combined changes from both branches, resulting in a single, cohesive history for your project.

Visit the following resources to learn more:

- [@official@Git Branching - Basic Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging#:~:text=into%20master%20later.-,Basic%20Merging,-Suppose%20you%E2%80%99ve%20decided)
- [@article@Git merge](https://www.atlassian.com/git/tutorials/using-branches/git-merge)

## Oauth Apps

# OAuth Apps

GitHub OAuth Apps allow developers to integrate with GitHub using OAuth 2.0 authentication. They enable secure, token-based access to specific GitHub resources like repositories, issues, and pull requests. OAuth Apps can automate tasks, personalize interactions, and provide real-time notifications through webhooks, all while allowing users to approve only the necessary permissions without sharing their credentials.

Visit the following resources to learn more:

- [@official@Creating an OAuth app](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app)
- [@video@GitHub Login With React (GitHub APIs, GitHub OAuth 2.0 Authentication)](https://www.youtube.com/watch?v=rRn2EisxPl4)

## Post Checkout

# post-checkout

Git post-checkout hooks are scripts that run automatically after a successful `git checkout` operation. These hooks provide a way to customize Git's behavior and perform specific actions when switching branches or updating the working directory. Post-checkout hooks can be used for tasks such as updating dependencies, regenerating files, or adjusting project settings based on the newly checked-out branch. They offer developers a powerful tool to automate workflows and maintain consistency across different branches in a Git repository.

Visit the following resources to learn more:

- [@official@Post-checkout hooks](https://git-scm.com/docs/githooks#_post_checkout)

## Post Update

# post-update

Git post-update hooks are scripts that run automatically after a successful push to a repository. These hooks are executed on the remote repository and are typically used for server-side tasks such as updating other services, triggering continuous integration processes, or notifying team members about changes. Post-update hooks provide a powerful mechanism for automating workflows and maintaining consistency across different parts of a project's infrastructure, making them an essential tool for streamlining development processes and enhancing collaboration in Git-based projects.

Visit the following resources to learn more:

- [@official@Post-update hooks](https://git-scm.com/docs/githooks#post-update)

## Pr From A Fork

# PR from a Fork

Creating a pull request from a fork on GitHub is a common workflow for contributing to open-source projects or collaborating on repositories you don't have direct write access to. After forking the original repository to your GitHub account, you can make changes in your fork, commit them, and then create a pull request to propose these changes to the original repository. This process allows project maintainers to review your contributions, discuss any necessary modifications, and ultimately merge your changes into the main project if they're approved. It's an essential feature that facilitates collaboration and code review in distributed development environments.

Visit the following resources to learn more:

- [@official@Creating a pull request from a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)
- [@video@How to Create a Pull Request from a Fork on GitHub](https://www.youtube.com/watch?v=a_FLqX3vGR4)

## Pr Guidelines

# PR Guidelines

Pull Request (PR) guidelines are essential for maintaining a smooth and efficient code review process in collaborative development environments. These guidelines typically outline best practices for creating, formatting, and submitting PRs, ensuring that changes are well-documented, easy to review, and align with the project's standards. They may cover aspects such as PR size, commit message formatting, documentation requirements, and testing expectations. By establishing clear PR guidelines, teams can streamline their workflow, improve code quality, and facilitate effective communication among contributors.

Visit the following resources to learn more:

- [@official@Best Practices for Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/best-practices-for-pull-requests)
- [@article@Pull Request Guidelines](https://opensource.creativecommons.org/contributing-code/pr-guidelines/)

## Pre Commit

# pre-commit

Git pre-commit hooks are scripts that run automatically before a commit is created, allowing developers to enforce code quality standards and catch issues early in the development process. These hooks can perform tasks such as linting, formatting, running tests, or checking for sensitive information, ensuring that only clean and compliant code is committed to the repository. By intercepting the commit process, pre-commit hooks help maintain code consistency, reduce errors, and streamline the overall development workflow, making them a valuable tool for enforcing best practices and improving code quality across a project.

Visit the following resources to learn more:

- [@opensource@pre-commit/pre-commit](https://github.com/pre-commit/pre-commit)
- [@official@Git Hooks](https://www.atlassian.com/git/tutorials/git-hooks)

## Pre Push

# pre-push

Git pre-push hooks are scripts that run automatically before a push operation is executed, providing a final checkpoint to validate changes before they are shared with a remote repository. These hooks allow developers to perform last-minute checks, such as running tests, linting code, or verifying commit messages, to ensure that only high-quality and compliant code is pushed. By intercepting the push process, pre-push hooks help maintain code integrity, prevent accidental pushes of incomplete or broken code, and enforce project-specific rules, making them a valuable tool for maintaining code quality and consistency across distributed development teams.

Visit the following resources to learn more:

- [@article@pre-push hooks](https://dev.to/jameson/pre-push-hooks-42g5)
- [@video@Detect secrets with a pre-commit git hook](https://www.youtube.com/watch?v=8bDKn3y7Br4)

## Private Vs Public

# Private vs Public

GitHub offers both private and public repositories, each serving different purposes in software development. Public repositories are visible to everyone on the internet, making them ideal for open-source projects, collaboration, and showcasing work to a wider audience. They encourage community contributions and can help developers build their portfolios. Private repositories, on the other hand, are only accessible to the repository owner and designated collaborators. These are suitable for proprietary code, sensitive projects, or work that's not ready for public consumption. Private repositories offer greater control over access and visibility, making them essential for businesses and individuals who need to keep their code confidential.

Visit the following resources to learn more:

- [@official@About project visibility](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories#about-repository-visibility)

## Profile Readme

# Profile Readme

A GitHub Profile README is a special repository that allows users to showcase their skills, projects, and personality directly on their GitHub profile. To create one, you need to make a new repository with the same name as your GitHub username. This repository should contain a README.md file, which GitHub will automatically display on your profile page. The README can be customized with Markdown formatting, allowing you to add text, images, links, and even dynamic content like GitHub stats or recent blog posts. This feature provides a unique opportunity to make your GitHub profile more engaging and informative for visitors, effectively serving as a personalized landing page for your GitHub presence.

Visit the following resources to learn more:

- [@official@Managing your Profile README](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme)
- [@video@GitHub Profile README](https://www.youtube.com/watch?v=KhGWbt1dAKQ)

## Project Planning

# Project Planning

Project planning on GitHub is a comprehensive process that leverages the platform's built-in tools to organize, track, and manage software development projects efficiently. It typically involves using features such as Issues for task tracking, Projects for kanban-style boards, Milestones for grouping related issues and pull requests, and Labels for categorization. These tools, combined with GitHub's collaborative features like pull requests and code reviews, enable teams to create structured workflows, set priorities, assign tasks, and monitor progress throughout the development lifecycle. By centralizing project management within the same platform used for version control, GitHub streamlines communication and enhances productivity for development teams of all sizes.

Visit the following resources to learn more:

- [@official@Project planning for developers](https://github.com/features/issues)
- [@video@GitHub Project Management](https://www.youtube.com/watch?v=oPQgFxHcjAw)

## Project Readme

# Project Readme

A GitHub project README is a crucial document that serves as the front page of a repository, providing essential information about the project. It typically includes a brief description of the project's purpose, installation instructions, usage guidelines, and contribution procedures. A well-crafted README helps visitors quickly understand the project's goals, how to get started, and how they can participate. It often contains badges indicating build status, code coverage, and other metrics, as well as links to documentation, issue trackers, and community channels. By effectively communicating the project's value and guiding new users and potential contributors, a good README significantly enhances a project's visibility, adoption, and collaboration potential on GitHub.

Visit the following resources to learn more:

- [@official@About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [@article@How to write a good README](https://bulldogjob.com/readme/how-to-write-a-good-readme-for-your-github-project)

## Pull Requests

# Pull Requests

You can use GitHub CLI to manage pull requests with the following commands:

- `gh pr create`: Create a new pull request.
- `gh pr merge`: Merge a pull request into the target branch.
- `gh pr list`: List all pull requests for a repository.
- `gh pr view`: View details of a specific pull request.

Visit the following resources to learn more:

- [@official@gh pr](https://cli.github.com/manual/gh_pr)
- [@video@Use GitHub CLI For Command Line Pull Request Management](https://www.youtube.com/watch?v=Ku9_0Mftiic)

## Pull Requests

# Pull Requests

A pull request is a proposal to merge a set of changes from one branch into another. In a pull request, collaborators can review and discuss the proposed set of changes before they integrate the changes into the main codebase. Pull requests display the differences, or diffs, between the content in the source branch and the content in the target branch.

Visit the following resources to learn more:

- [@official@Creating a pull request](https://docs.github.com/articles/creating-a-pull-request)
- [@article@Pull Requests](https://www.atlassian.com/git/tutorials/making-a-pull-request#:~:text=In%20their%20simplest%20form%2C%20pull,request%20via%20their%20Bitbucket%20account.)
- [@video@GitHub Pull Request in 100 Seconds ](https://youtu.be/8lGpZkjnkt4?si=qbCQ8Uvzn9GN2koL)

## Pushing  Pulling Changes

# Pushing / Pulling Changes

When you pull changes in Git, you're fetching and integrating changes from a remote repository into your local repository. This operation updates your local branch with the latest changes from the remote branch. Whereas When you push changes in Git, you're sending your local commits to a remote repository, such as GitHub, GitLab, or Bitbucket. This operation updates the remote repository with your latest changes.

Visit the following resources to learn more:

- [@official@Pushing commits to a remote repository](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository)
- [@article@A Comprehensive Guide to git pull and git push](https://dev.to/alexmercedcoder/mastering-git-a-comprehensive-guide-to-git-pull-and-git-push-2eo3)
- [@article@Git Push and Pull Tutorial](https://www.datacamp.com/tutorial/git-push-pull)

## Pushing Tags

# Pushing Tags

Pushing tags in Git is the process of sharing your local tags with a remote repository. Tags in Git are used to mark specific points in the repository's history, typically to signify a release or a milestone.

Visit the following resources to learn more:

- [@article@Tagging in git](https://git-scm.com/book/en/Git-Basics-Tagging)
- [@article@How to Push Git Tags to Remote](https://kodekloud.com/blog/how-to-push-git-tags-to-remote/)
- [@article@Git Push Tag to Remote Guide](https://phoenixnap.com/kb/git-push-tag)

## Reactions

# Reactions

Reactions in GitHub are a way for users to express their feelings or opinions about issues, pull requests, comments, and other discussions without adding additional comments. They are similar to "likes" or "emojis" on social media platforms, providing a quick and non-verbal way to engage with content.

Visit the following resources to learn more:

- [@official@Add Reactions to Pull Requests, Issues, and Comments](https://github.blog/news-insights/product-news/add-reactions-to-pull-requests-issues-and-comments/)

## Rebase

# Rebase

Rebasing in Git is a powerful and potentially complex feature used to reorganize or modify a series of commits. The primary purpose of rebasing is to create a cleaner, more linear project history by moving or combining changes from one branch into another.

Visit the following resources to learn more:

- [@official@Rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)

## Renaming Branch

# Renaming Branch

Renaming a branch in Git means changing the name of a branch to something different while preserving its history and the commits it contains. The branch itself remains the same in terms of the code and history it tracks, but the reference (the name by which you refer to it) is updated

Visit the following resources to learn more:

- [@official@Renaming a Branch - GitHub Docs](https://docs.github.com/github/administering-a-repository/renaming-a-branch)
- [@article@Git Rename Branch – How to Change a Local Branch Name](https://www.freecodecamp.org/news/git-rename-branch-how-to-change-a-local-branch-name/)

## Repository Management

# Repository management

Using GitHub CLI for repository management allows you to streamline tasks and work more efficiently. ou can use GitHub CLI to manage repositories with the following commands:

- `gh repo create`: Create a new repository.
- `gh repo delete`: Delete an existing repository.
- `gh repo visibility`: Change the repository's visibility (public or private).
- `gh repo topic`: Manage topic labels for a repository.

Visit the following resources to learn more:

- [@official@gh repo](https://cli.github.com/manual/gh_repo)
- [@article@Efficient GitHub Operations: Simplifying Repository Management using GitHub CLI](https://dev.to/yutee_okon/efficient-github-operations-simplifying-repository-management-using-github-cli-190l)
- [@video@GitHub CLI (gh) - How to manage repositories more efficiently](https://www.youtube.com/watch?v=BII6ZY2Rnlc)

## Rest Api

# REST API

The GitHub REST API is a set of APIs that provide access to various GitHub features, such as user data, repository information, and commit history. It allows developers to interact with the GitHub platform programmatically.

Visit the following resources to learn more:

- [@official@GitHub REST API documentation](https://docs.github.com/en/rest?apiVersion=2022-11-28)
- [@official@Quickstart for GitHub REST API](https://docs.github.com/en/rest/quickstart?apiVersion=2022-11-28)
- [@video@[Tutorial] - How to use GitHub REST API for Beginners](https://www.youtube.com/watch?v=OvfLavRD1Os)

## Rewriting History

# Rewriting History

In certain situations, you might need to modify or remove commits from your Git repository's history. This can be achieved using various methods:

- `git commit --amend`: Allows you to edit the most recent commit.
- `git rebase`: Replaces one branch with another, preserving the commit history.
- `git filter-branch`: Removes specific commits from a branch without altering the original branch.
- `git push --force`: Updates the remote repository while respecting existing pull requests.

Rewriting history in Git is typically necessary when:

- Fixing mistakes: Correcting errors or typos in commit messages.
- Removing sensitive data: Deleting confidential information from commits, like API keys or database credentials.
- Simplifying complex histories: Reorganizing branches to improve clarity and reduce complexity.

Visit the following resources to learn more:

- [@official@Git Tools - Rewriting History](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History)
- [@article@Methods of Rewriting History in Git](https://www.atlassian.com/git/tutorials/rewriting-history)

## Roadmaps

# Roadmaps

GitHub Roadmaps are a feature that helps you visualize and organize plans for your projects, allowing you to create a high-level view of milestones and goals, and collaborate on planning and tracking progress with team members.

Visit the following resources to learn more:

- [@official@Customizing the Roadmap Layout](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-roadmap-layout)
- [@video@Learn how to use Project Roadmaps - GitHub Checkout](https://www.youtube.com/watch?v=D80u__nYYWw)

## Saved Replies

# Saved Replies

GitHub allows you to save frequently used comments and reuse them when discussing issues or pull requests.

- Saved replies: You can create pre-written comments that can be easily added to conversations.
- Customization: Saved replies can be edited to fit specific situations, making it easy to tailor your responses.

Visit the following resources to learn more:

- [@official@Using saved replies](https://docs.github.com/en/get-started/writing-on-github/working-with-saved-replies/using-saved-replies)
- [@article@Walkthrough: Using GitHub’s “Saved Replies” to make life consistent and easy](https://prowe214.medium.com/walkthrough-using-githubs-saved-replies-to-make-life-consistent-and-easy-80f23efe6a0)

## Scheduled Worfklows

# Scheduled Worfklows

GitHub Actions allows you to schedule workflows to run at specific times or intervals. You can set up workflows to automatically run at predetermined times, such as daily or weekly.

Visit the following resources to learn more:

- [@official@Events that trigger workflows - Schedule](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#schedule)
- [@video@GitHub Actions - How to Schedule workflows in GitHub](https://www.youtube.com/watch?v=StipNrK__Gk)

## Secrets And Env Vars

# Secrets and Env Vars

GitHub provides features to securely store and manage sensitive data, such as secrets and environment variables.

- Secrets: These are sensitive values that should not be committed to a repository, like API keys or database credentials.
- Environment Variables: They can be used to set values for your workflow or application, making it easier to manage dependencies.

Visit the following resources to learn more:

- [@official@Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)
- [@official@Store information in variables](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/store-information-in-variables)
- [@video@Secrets and Environment Variables in your GitHub Action](https://www.youtube.com/watch?v=dPLPSaFqJmY)

## Setting Up Profile

# Setting up Profile

On GitHub, creating a profile is an essential step in showcasing yourself as a developer or contributor.

- Sharing information: Your profile page allows others to find out more about you, including your interests and skills.
- Showcasing projects: You can display your notable projects and contributions, giving a glimpse into your work experience.
- Expressing identity: The profile also serves as an opportunity for personal expression, allowing you to convey your unique personality and style within the GitHub community.

Visit the following resources to learn more:

- [@official@Setting up your profile](https://docs.github.com/en/get-started/start-your-journey/setting-up-your-profile)
- [@video@GitHub Profile Readme](https://www.youtube.com/watch?v=KhGWbt1dAKQ)

## Squash

# Squash

Squashing in Git, refers to the process of combining multiple commits into a single commit. This is often done to create a cleaner and more concise commit history, especially before merging a feature branch into the main branch.

Visit the following resources to learn more:

- [@article@Git Squash Commits](https://www.freecodecamp.org/news/git-squash-commits/)
- [@article@How to Squash Commits in Git](https://medium.com/iosnesia/how-to-squash-commits-in-git-e73a41248211)
- [@video@GIT Tutorial - How to Squash Commits](https://youtu.be/viY1BbKZhSI?si=kORsEzQvCRFGauQa)

## Staged Changes

# Staged Changes

To view the changes you've staged with `git add`, but not yet committed, use `git diff --cached`. This command compares the staged files against their original versions in the repository. It's a quick way to review what you're about to commit before finalizing it.

Visit the following resources to learn more:

- [@article@What does Staged Changes mean in Git?](https://dillionmegida.com/p/staged-changes-in-git/)
- [@video@What are Staged Changes in Git?](https://www.youtube.com/watch?v=HyeNfWZBut8)

## Staging Area

# Staging Area

In Git, a staging area serves as an intermediate step between your local repository changes and the actual commit.

- Temporary storage: The staging area holds changes that are intended to be part of the next commit.
- Previewing changes: It allows you to preview your changes before committing them.

Visit the following resources to learn more:

- [@official@Getting Started - What is Git? - Staging Area](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F#:~:text=The%20staging%20area%20is%20a,area%E2%80%9D%20works%20just%20as%20well.)
- [@video@What are Staged Changes in Git?](https://www.youtube.com/watch?v=HyeNfWZBut8)
- [@course@Staging Area (Interactive Lesson)](https://inter-git.com/lessons/adding-files-to-index)

## Static Site Generators

# Static Site Generators

GitHub offers a set of static site generators (SSGs) that allow users to create and deploy websites directly from their GitHub repositories. These SSGs include `Jekyll`, `Hugo`, and `Middleman`, among others. They provide a simple way to build websites without the need for manual configuration or maintenance.

Visit the following resources to learn more:

- [@official@Static Site Generators](https://github.com/collections/static-site-generators)
- [@official@About GitHub Pages and Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll)

## Storing Artifacts

# Storing Artifacts

GitHub provides a feature for storing artifacts, which allows you to upload build outputs or other files as part of your workflow.

- Artifacts: These are files generated by a job, such as compiled binaries, test reports, or logs. They can be used to validate the results of a build or deployment.
- Referenceable storage: Artifacts are stored in a referenceable way, making it easy to access and use them in future builds.

Visit the following resources to learn more:

- [@official@Storing and sharing data from a workflow](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/storing-and-sharing-data-from-a-workflow)

## Student Developer Pack

# Student Developer Pack

The GitHub Student Developer Pack is a collection of developer tools and resources that are offered free or at a discounted price to students through the GitHub Education program. This pack includes access to GitHub, GitHub Desktop, GitHub Classroom, GitHub Student Developer Kit, and other benefits. By using the Student Developer Pack, students can gain hands-on experience with professional developer tools, while also getting access to a wide range of educational resources.

Visit the following resource to learn more:

- [@official@Apply to GitHub Education as a student](https://docs.github.com/en/education/explore-the-benefits-of-teaching-and-learning-with-github-education/github-education-for-students/apply-to-github-education-as-a-student)

## Submodules

# Submodules

In Git, submodules allow you to include another repository within a project. This feature enables the management of external dependencies as part of the main project.

- Including external repositories: Submodules can be used to include other Git repositories within your project.
- Managing dependencies: They provide a way to manage and track changes in external dependencies.

Visit the following resources to learn more:

- [@official@Git Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
- [@article@Git Submodules Tutorial](https://www.atlassian.com/git/tutorials/git-submodule)

## Tagging

# Tagging

In Git, tags are used to identify specific points in a repository's history as being important. This feature allows developers to mark release points or milestones.

- Marking release points: Tags are typically used to mark release versions (e.g., v1.0, v2.0) of a project.
- Types of tags: There are different types of tags, including lightweight and annotated tags.

Visit the following resources to learn more:

- [@official@Git Basics - Tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging)

## Teams Within Organization

# Teams within Organization

GitHub Organizations allow you to create teams within your organization, which helps in organizing members based on their roles and responsibilities.

- Grouping: Team members can be grouped together according to the company or group's structure.
- Access permissions: Access permissions can be cascaded from one team member to another.
- Mentions: Team mentions allow for easy referencing of specific teams in repository discussions.

Visit the following resources to learn more:

- [@official@Organizing Members into Teams](https://docs.github.com/en/organizations/organizing-members-into-teams)
- [@article@Best Practices for Organizations and Teams using GitHub Enterprise Cloud](https://github.blog/enterprise-software/devops/best-practices-for-organizations-and-teams-using-github-enterprise-cloud/)

## Undoing Changes

# Undoing Changes

If mistakes or unwanted changes have been committed to your Git repository, there are ways to correct them. Two common methods for reverting changes include:

- Git Reset: Resets the branch to a previous commit.
- Git Revert: Creates a new commit that reverts specified changes.

Visit the following resources to learn more:

- [@official@Undoing Changes](https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified)
- [@article@Undo Anything in Git](https://github.blog/open-source/git/how-to-undo-almost-anything-with-git/)
- [@article@Undoing Changes in Git](https://www.atlassian.com/git/tutorials/undoing-changes)

## Unstaged Changes

# Unstaged Changes

For changes that are not yet staged with `git add`, such as untracked new files or modified existing ones , use `git diff`. This command compares your working directory (your current changes) against the staging area (changes already staged with `git add`). It’s a useful tool for reviewing local modifications before deciding whether to stage them for future commits.

The `--unified` option (or -U) controls the number of context lines shown in the diff output. By default, Git shows 3 lines of context around each change. For example, `git diff --unified=5` will display 5 lines of context around each change, making it easier to understand the surrounding code or content.

- [@article@What are unstaged changes in GitHub?](https://stackoverflow.com/questions/10954329/whats-the-unstaged-changes-in-github)
- [@article@How to unstage files in Git](https://www.git-tower.com/learn/git/faq/git-unstage)

## Use In Automation

# Use in Automation

GitHub CLI is a powerful tool for automating GitHub-related tasks directly from the command line. It enables developers to streamline workflows and integrate GitHub processes into scripts and automated systems.

Key uses in automation:

1. CI/CD: Automate PR creation, review, merging, and release management
2. Issue and Project Management: Create, update, and close issues; manage project boards
3. Repository Management: Clone repos, create forks, manage settings and collaborators
4. GitHub Actions Integration: Trigger and monitor workflows, manage secrets
5. Scripting and Batch Operations: Perform bulk actions across multiple repositories

To use GitHub CLI in automation:

1. Install GitHub CLI
2. Authenticate with your GitHub account
3. Learn basic commands and syntax
4. Integrate CLI commands into scripts or automation tools

Learn more from the following resources:

- [@official@GitHub CLI documentation](https://cli.github.com/manual/)
- [@article@Automating your workflow with GitHub CLI](https://github.blog/2021-03-11-scripting-with-github-cli/)

## Usecases

# Usecases

GitHub Actions offer a wide range of automation possibilities for your development workflow. Here are some common use cases:

1. Continuous Integration (CI): Automatically build and test your code on every push or pull request.
2. Continuous Deployment (CD): Automatically deploy your application to various environments after successful builds.
3. Code Quality Checks: Run linters, formatters, and other code quality tools automatically.
4. Dependency Updates: Automatically create pull requests for outdated dependencies.
5. Issue and PR Management: Automatically label, assign, or close issues and pull requests based on certain conditions.
6. Scheduled Tasks: Run periodic maintenance tasks, backups, or data processing jobs.
7. Security Scanning: Perform automated security checks on your codebase and dependencies.
8. Documentation Generation: Automatically generate and publish documentation for your project.
9. Cross-platform Testing: Test your code on multiple operating systems and environments simultaneously.
10. Release Management: Automate the creation of release notes and asset uploads for new versions.

Learn more from the following resources:

- [@official@GitHub Actions Documentation](https://docs.github.com/en/actions)
- [@youtube@How GitHub Actions 10x my productivity](https://www.youtube.com/watch?v=yfBtjLxn_6k)

## Viewing Commit History

# Viewing Commit History

Viewing commit history is a crucial aspect of Git, allowing users to examine the chronological record of repository changes. This feature is essential for understanding project evolution, tracking modifications, and facilitating effective team collaboration. Git provides various commands like `git log` and its options (e.g., `--oneline`, `--graph`, `--patch`, `--stat`) to display commit history in different formats. Users can filter commits by author, date range, and other criteria. By regularly reviewing commit history and following best practices such as writing clear commit messages and using tags, developers can gain valuable insights into their project's development and make informed decisions about future changes.

Visit the following resources to learn more:

- [@official@Git Basics - Viewing the Commit History](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)
- [@article@How to Use Git Log to View Commit History](https://www.freecodecamp.org/news/git-log-command/)

## Viewing Diffs

# Viewing Diffs

Viewing diffs in Git is crucial for understanding the changes made to your code. This is especially important when collaborating with others or reviewing your own work over time. Diffs show you exactly what lines have been added, modified, or removed between different versions of your files. This feature helps in code review processes, troubleshooting issues, and maintaining a clear history of your project's evolution. Git provides various commands and tools to view these differences, making it easier to track and manage changes effectively.

Visit the following resources to learn more:

- [@official@Git Diff Documentation](https://git-scm.com/docs/git-diff)
- [@article@Git Diff](https://www.atlassian.com/git/tutorials/saving-changes/git-diff)

## Webhooks

# Webhooks

GitHub Webhooks allow developers to receive real-time notifications about events happening within their repository, such as commits, pull requests, and issues. These webhooks enable users to automate tasks, integrate with other services, and build custom workflows.

Visit the following resources to learn more:

- [@official@About webhooks](https://docs.github.com/en/webhooks/about-webhooks)
- [@official@Webhooks documentation](https://docs.github.com/en/webhooks)
- [@video@How to use GitHub Webhooks with Discord](https://www.youtube.com/watch?v=-gyEHj0CVx0&)

## What And Why Use

# What and Why use?

Git submodules are a feature that allows you to include one Git repository within another. They are useful for managing external dependencies or shared components across projects.

## Key points

1. Separate repositories with independent histories
2. Parent repository tracks specific submodule commits
3. Enables code reuse and modular project structure
4. Helps manage dependencies and keep main repository focused
5. Facilitates collaboration on complex projects

## Benefits

- Including third-party libraries
- Sharing common code
- Managing multi-component projects
- Keeping main repository lightweight

Note: While powerful, submodules can add complexity to your workflow, so careful consideration is needed before implementation.

Learn more from the following resources:

- [@article@Git Submodules: Core Concept, Workflows, and Tips](https://www.atlassian.com/git/tutorials/git-submodule)
- [@video@Git Submodules Tutorial](https://www.youtube.com/watch?v=gSlXo2iLBro)

## What And Why

# What and Why?

Git hooks are customizable scripts that Git executes automatically before or after specific events, such as committing, pushing, or merging. These hooks allow developers to automate tasks, enforce coding standards, run tests, or perform other actions at crucial points in the Git workflow. By leveraging git hooks, teams can enhance their development process, maintain code quality, and ensure consistency across projects. Hooks can be implemented locally or shared among team members, providing a powerful mechanism for streamlining workflows and enforcing best practices throughout the development lifecycle.

Learn more from the following resources:

- [@article@Git Hooks](https://www.atlassian.com/git/tutorials/git-hooks)
- [@video@What are Git Hooks?](https://www.youtube.com/watch?v=1OFiiPretCM)

## What Are These

# What are these?

GitHub Actions is a powerful automation and continuous integration/continuous deployment (CI/CD) platform provided by GitHub. It allows developers to create custom workflows that automatically build, test, and deploy their code directly from their GitHub repositories. These workflows are triggered by specific events, such as push requests, pull requests, or scheduled tasks. GitHub Actions enables teams to streamline their development processes, improve code quality, and accelerate software delivery by automating repetitive tasks and integrating various tools and services seamlessly within their development pipeline.

Learn more from the following resources:

- [@article@Understanding GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions)
- [@video@GitHub Actions Tutorial - Basic Concepts and CI/CD Pipeline with Docker](https://www.youtube.com/watch?v=R8_veQiYBjI)

## What Is A Repository

# What is a Repository

A repository is a storage location for your project's code, documentation, and other files. It serves as a central hub for collaboration, version control, and code management. It allows multiple people to work on the same project without overwriting each other's work.

Learn more from the following resources:

- [@article@About repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories)
- [@article@What is a repository?](https://www.gitkraken.com/learn/git/tutorials/what-is-a-git-repository)
- [@course@What is a repository? (Interactive Lesson)](https://inter-git.com/lessons/creating-repository)

## What Is Version Control

# What is Version Control?

Version control is a system that manages and tracks changes to files over time, allowing multiple people to collaborate on a project while maintaining a history of all modifications. It records changes to files, such as code, documents, or configuration files, and stores them in a repository. With version control, developers can revert to previous versions, compare differences between versions, and understand the evolution of a project. It supports features like branching, where different lines of development can occur independently, and merging, which combines changes from different branches. Overall, version control ensures that changes are organized, recoverable, and easily managed, making it a critical tool in software development and collaborative projects.

Learn more from the following resources:

- [@video@What is Git? Explained in 2 minutes](https://www.youtube.com/watch?v=2ReR1YJrNOM)
- [@article@What is version control?](https://www.atlassian.com/git/tutorials/what-is-version-control)
- [@course@What is Git? (Interactive Lesson)](https://inter-git.com/lessons/introduction)

## Why Use Version Control

# Why use Version Control?

Using version control is essential for managing changes in software development, as it enables tracking of modifications, collaboration, and maintaining a history of your project. It allows multiple developers to work on the same codebase simultaneously without overwriting each other's work, providing a clear record of who made changes and why. Version control systems facilitate rollback to previous versions if issues arise, and they support branching and merging, which are crucial for experimenting with new features and managing different stages of development. Overall, version control ensures code quality, accountability, and efficient collaboration in projects.

Learn more from the following resources:

- [@article@Benefits of using version control](https://www.techrepublic.com/article/version-control-benefits/)
- [@article@What is version control and why is it important?](https://start.docuware.com/blog/document-management/what-is-version-control-why-is-it-important)
- [@course@Why use Git? (Interactive Lesson)](https://inter-git.com/lessons/introduction)

## Workflow Context

# Workflow Context

Workflow context in GitHub Actions refers to the environment and variables that are available to a workflow. It includes information about the workflow's execution, such as the event that triggered it, the repository, and the workflow itself.

Learn more from the following resources:

- [@official@GitHub Actions Contexts](https://docs.github.com/en/actions/concepts/workflows-and-actions/contexts)
- [@official@GitHub Actions Contexts Example](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/contexts)
- [@video@Working with contexts in GitHub Actions](https://www.youtube.com/watch?v=16WT_r0zjYE)

## Workflow Runners

# Workflow Runners

Workflow runners are the environments where GitHub Actions workflows are executed. They are hosted on GitHub-hosted virtual machines (GHVMs) or self-hosted runners. Each runner has a specific configuration and capabilities, depending on its type.

Learn more from the following resources:

- [@official@GitHub Actions Runners](https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners)
- [@video@GitHub Actions Self-hosted runners](https://www.youtube.com/watch?v=aLHyPZO0Fy0)

## Workflow Status

# Workflow Status

Workflow status in GitHub Actions refers to the current state of a workflow run. It can be one of the following:

- Pending: The workflow is waiting for an event to trigger it.
- In Progress: The workflow is currently running.
- Completed: The workflow has finished running.
- Failed: The workflow has failed due to an error.

Learn more from the following resources:

- [@article@Adding a workflow status badge to your repository](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/adding-a-workflow-status-badge)

## Workflow Triggers

# Workflow Triggers

Workflow triggers are events that initiate a GitHub Actions workflow. They can be scheduled, triggered by code changes, or manually initiated. This allows for automation of tasks based on specific conditions.

Learn more from the following resources:

- [@official@GitHub Actions Documentation](https://docs.github.com/en/actions)
- [@official@GitHub Actions Triggers](https://docs.github.com/en/actions/reference/events-that-trigger-workflows)

## Working Directory

# Working Directory

A working directory in Git is the local environment where files are stored and modified as part of a project. It reflects the current state of the project's files, allowing developers to edit, add, or delete files. Changes made in the working directory can be staged for commit, which means they're prepared for inclusion in the next commit. The working directory is connected to the Git repository, and it helps manage the differences between the committed history and the current state of the files. It plays a central role in tracking changes, testing, and developing new features.

Learn more from the following resources:

- [@article@Git vs Working Directory](https://codesweetly.com/git-vs-working-directory/)
- [@article@Your Working Directory (Interactive Lesson)](https://inter-git.com/lessons/creating-repository)

## Working In A Team

# Working in a Team

Working in a team on GitHub involves collaborative development using Git's distributed version control system. Team members can work on separate branches, create pull requests for code reviews, and merge changes into the main codebase. GitHub's features like issues, projects, and discussions facilitate communication and project management. Effective teamwork on GitHub requires clear communication, adherence to agreed-upon workflows, and proper use of Git commands to manage code changes and resolve conflicts. This collaborative approach enables teams to work efficiently on complex projects, maintain code quality, and track progress effectively.

GitHub also offers an organization and team management interface, allowing teams to manage projects, members, and collaboration settings.

Learn more from the following resources:

- [@official@Getting Started with Teams](https://docs.github.com/en/get-started/onboarding/getting-started-with-github-team)
- [@official@GitHub Team Docs](https://docs.github.com/organizations/organizing-members-into-teams/about-teams)

## Yaml Syntax

# YAML Syntax

YAML (YAML Ain't Markup Language) is a human-readable data serialization standard for all programming languages. It is designed to be easily readable by humans while also being machine-parsable. Key features of YAML include:

1. Simplicity: YAML uses a minimalist syntax with significant whitespace and indentation.

2. Versatility: It can represent various data types, including scalars, lists, and associative arrays.

3. Readability: Its clear, concise format makes it easy for both humans and machines to understand.

4. Language-independent: YAML can be used with any programming language that has a YAML parser.

YAML is commonly used for:

- Configuration files: Many applications and tools use YAML for their configuration settings.
- Data exchange: It serves as a lightweight alternative to XML or JSON for data transfer between systems.
- Data storage: YAML can be used to store structured data in a human-readable format.
- DevOps and CI/CD: It's widely used in tools like Docker, Kubernetes, and various CI/CD platforms for defining workflows and configurations.

Understanding YAML syntax is crucial for working with modern development tools, especially in the realms of DevOps, cloud computing, and containerization.

Learn more from the following resources:

- [@official@YAML](https://yaml.org/)
- [@article@YAML Cheatsheet](https://cheatsheets.zip/yaml)
- [@article@What is YAML?](https://circleci.com/blog/what-is-yaml-a-beginner-s-guide/)
- [@article@YAML Tutorial : A Complete Language Guide with Examples](https://spacelift.io/blog/yaml)
