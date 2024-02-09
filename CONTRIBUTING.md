<!-- omit in toc -->

# Contributing to CellularAutomaton

First off, thanks for taking the time to contribute! ❤️

All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents) for different ways to help and details about how this project handles them.
Please make sure to read the relevant section before making your contribution. The community looks forward to your contributions. 🎉

> And if you like the project, but just don't have time to contribute, that's fine. There are other easy ways to support the project and show your appreciation, which I would also be very happy about:
>
> - Star the project
> - Mention the project at internet
> - Refer this project in your project's readme
> - Mention the project at local meetups and tell your friends/colleagues

<!-- omit in toc -->

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [I Have a Question](#i-have-a-question)
- [I Want To Contribute](#i-want-to-contribute)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)
- [Your First Code Contribution](#your-first-code-contribution)

## Code of Conduct

This project and everyone participating in it is governed by the
[CellularAutomaton Code of Conduct](https://github.com/Qu1nel/CellularAutomaton/blob/main/.github/CODE_OF_CONDUCT.md).
By participating, you are expected to uphold this code. Please report unacceptable behavior
to.

## I Have a Question

Before you ask a question, it is best to search for existing [Issues](https://github.com/Qu1nel/CellularAutomaton/issues) that might help you.
In case you have found a suitable issue and still need clarification, you can write your question in this issue. It is also advisable to search the internet for answers first.

If you then still feel the need to ask a question and need clarification, we recommend the following:

- Open an [Issue](https://github.com/Qu1nel/CellularAutomaton/issues/new).
- Provide as much context as you can about what you're running into.
- Provide project and platform versions depending on what seems relevant.

I will then take care of the issue as soon as possible.

## I Want To Contribute

> ### Legal Notice <!-- omit in toc -->
>
> When contributing to this project, you must agree that you have authored 100% of the content, that you have the necessary rights to the content and that the content you contribute may be provided under the project license.

### Reporting Bugs

<!-- omit in toc -->

#### Before Submitting a Bug Report

A good bug report shouldn't leave others needing to chase you up for more information. Therefore, I ask you to investigate carefully, collect information and describe the issue in detail in your report.
Please complete the following steps in advance to help I fix any potential bug as fast as possible.

- Make sure that you are using the latest version.
- Determine if your bug is really a bug and not an error on your side e.g. using incompatible environment components/versions (Make sure that you have read the documentation. If you are looking for support, you might want to check [this section](#i-have-a-question)).
- To see if other users have experienced (and potentially already solved) the same issue you are having, check if there is not already a bug report existing for your bug or error in the [bug tracker](https://github.com/Qu1nel/CellularAutomaton/issues?q=label%3A%22Type%3A+Bug%22).
- Also make sure to search the internet (including Stack Overflow) to see if users outside of the GitHub community have discussed the issue.
  - Collect information about the bug:
  - Stack trace (Traceback)
  - OS, Platform and Version (Windows, Linux, macOS, x86, ARM)
  - Version of the interpreter, compiler, SDK, runtime environment, package manager, depending on what seems relevant.
  - Possibly your input and the output
  - Can you reliably reproduce the issue? And can you also reproduce it with older versions?

<!-- omit in toc -->

#### How Do I Submit a Good Bug Report?

> You must never report security related issues, vulnerabilities or bugs including sensitive information to the issue tracker, or elsewhere in public. Instead sensitive bugs must be sent by email to [covach.qn@gmail.com](mailto:covach.qn@gmail.com).

We use GitHub issues to track bugs and errors. If you run into an issue with the project:

- Open an [Issue](https://github.com/Qu1nel/CellularAutomaton/issues/new). (Since we can't be sure at this point whether it is a bug or not, we ask you not to talk about a bug yet and not to label the issue.)
- Explain the behavior you would expect and the actual behavior.
- Please provide as much context as possible and describe the _reproduction steps_ that someone else can follow to recreate the issue on their own. This usually includes your code. For good bug reports you should isolate the problem and create a reduced test case.
- Provide the information you collected in the previous section.

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for CellularAutomaton, **including completely new features and minor improvements to existing functionality**. Following these guidelines will help maintainers and the community to understand your suggestion and find related suggestions.

<!-- omit in toc -->

#### Before Submitting an Enhancement

- Make sure that you are using the latest version.
- Read the documentation carefully and find out if the functionality is already covered, maybe by an individual configuration.
- Perform a [search](https://github.com/Qu1nel/CellularAutomaton/issues) to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.

<!-- omit in toc -->

#### How Do I Submit a Good Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](https://github.com/Qu1nel/CellularAutomaton/issues).

- Use a **clear and descriptive title** for the issue to identify the suggestion.
- Provide a **step-by-step description of the suggested enhancement** in as many details as possible.
- **Describe the current behavior** and **explain which behavior you expected to see instead** and why. At this point you can also tell which alternatives do not work for you.
- You may want to **include screenshots and animated GIFs** which help you demonstrate the steps or point out the part which the suggestion is related to. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux. <!-- this should only be included if the project has a GUI -->
- **Explain why this enhancement would be useful** to most CellularAutomaton users. You may also want to point out the other projects that solved it better and which could serve as inspiration.

### Your First Code Contribution

1 . Clone the repository locally

2 . Create a fork on GitHub

3 . Add your fork as a remote:

```bash
git remote add <name-your-remote-fork> https://github.com/<GITHUB-USERNAME>/CellularAutomaton.git
```

4. Make a separate branch for changes with your name (or nickname):

```bash
git switch --create <YOUR-NAME>-<name-of-branch>
```

5 . Make your local changes (in your branch)

6 . Pull and rebase any changes made by others to main since you started working on your change and enter them into your branch to update your changes:

```bash
git switch main
git pull --rebase
git swtich <your-branch>
git rebase main
```

7 . Also, if you committed multiple changes locally, squash them to a single commit before submitting a PR:

```bash
git log
# Now find the commit ID of your first local commit, and use it to rebase
git rebase <FIRST-COMMIT-ID> -i
# Now mark all of the commits except the first as "squash"
```

I prefer a single commit as the first revision of a PR, because it is cleaner to review.

8 . Push your changes (branch) to your fork:

```
# Use the -f option if you have used your fork for previous PRs
git push -f origin <your-branch>
```

9 . Go to your fork on GitHub and click the link to create a new pull request.

10. It's time to submit! Use the "Squash and merge" option when merging to master.
    I use squash merging because the individual PR iterations are not important to understanding the evolution of the codebase in main, and create a lot of noise in the commit history.

Soon I'll be mergin' all yer changes into th' master branch o' this project. Ye will get a notification email once th' changes 'ave been merged.

> If you are no longer planning to make changes, you can stop there.
> If not, the following points are for you:

12. Synchronize your branch with this repository and then add my repository url to the `upstream remote url` field:

```bash
git swtich main
git remote add upstream https://github.com/Qu1nel/CellularAutomaton
git fetch upstream
git rebase origin/upstream
git push origin master
```

> Thus we have reported that there is a second repository from which changes can be accepted. Introduced changes from this repository into the main branch and sent it to your fork on GitHub.

13. Now if you want to make new changes and make a pull request, repeat all the steps from the beginning. But before that don't forget to delete old branches if you don't need them:

```bash
git branch -d <your-branch>
git push origin --delete <your-branch>
```
