# Lab 5: Package Management Tutorial
Please complete the hands-on activities associated with this lab outlined in the <a href="https://csci338.github.io/fall2024/assignments/lab05" target="_blank">Lab 5 Instructions</a> (on the course website). When you're done, answer the following questions. Feel free to use Google / ChatGPT to help you think about these questions (but keep in mind that you'll need to know them for the midterm exam).

## Part 1. Operating System Package Managers
Answer the questions for either Homebrew or apt (depending on whether you're using Linux / WSL or Windows)
1. What is Homebrew / apt, and why is it useful?
apt is a package management system commonly used on Debian-based Linux distributions (e.g., Ubuntu). It simplifies installing, updating, and managing software by retrieving pre-built packages from repositories.Like Homebrew, apt automates the process of installing software and ensures that all necessary dependencies are resolved, simplifying software management for users and system administrators.
2. What does the `update` command do (either `brew update` or `apt-get update`)?
This command updates the local list of available software packages by retrieving information about the latest versions of the packages from the repositories.

3. Where are the packages that are managed by Homebrew / apt stored on your local computer?

he packages managed by apt are generally installed system-wide under various directories:
Binaries (executables) are usually installed in /usr/bin/, /usr/local/bin/, or /bin/.
Libraries are stored in /usr/lib/ or /lib/.
Package information and metadata are cached in /var/lib/apt/ and downloaded package files (before installation) are stored temporarily in /var/cache/apt/archives/.






## Part 2.
1. What is a python virtual environment?
A Python virtual environment is an isolated environment where you can install and manage Python packages independently from the system-wide Python installation. 
2. What is Poetry, and how is it different from other Python package managers like pip?
Poetry is a Python dependency management and packaging tool that aims to simplify the process of managing dependencies, virtual environments, and packaging for Python projects.
3. What happened when you issued the `poetry new poetry-demo` command?
When you run poetry new poetry-demo, Poetry creates a new directory structure for a Python project called poetry-demo.
4. How do you run a python file using the poetry virtual environment?To run a Python file within the Poetry virtual environment, you have two main options: poetry run and activating the virtual environment.

5. What is the purpose of the `poetry.lock` file?

The poetry.lock file is an essential part of how Poetry manages project dependencies. Its main purpose is to ensure consistent and reproducible builds across different environments and systems.
## Part 3.
1. What are some of the things that `package.json` is used for?
The poetry.lock file is an essential part of how Poetry manages project dependencies. Its main purpose is to ensure consistent and reproducible builds across different environments and systems.
2. Why wouldn't you want to check in the `node_modules` directory into GitHub?
node_modules can be very large: The node_modules folder often contains thousands of files and can be hundreds of megabytes in size, depending on the number and complexity of dependencies. Including it in your repository would significantly increase the size of the repository, leading to slower performance.

