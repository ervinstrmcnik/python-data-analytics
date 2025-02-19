# Into and Environment Setup

**Sources:**
- [Using Python for Data Analysis](https://realpython.com/python-for-data-analysis/#resolving-an-anomaly)

Data analysis is a broad term that covers a wide range of techniques that enable you to **reveal any insights and relationships that may exist within raw data**. As you might expect, Python lends itself readily to data analysis. Once Python has analyzed your data, you can then use your findings to make good business decisions, improve procedures, and even make informed predictions based on what you’ve discovered.

## What is Data?

Data can be the words in a book, article, or blog. Data can be the contents of a spreadsheet or a database. Data can be pictures or video. Data can be a constant stream of measurements sent from a monitoring device. By itself, data can be rather meaningless. As we interpret data, by correlating or comparing, it becomes more useful. This useful data is now information. As this information is applied or understood, it becomes knowledge.

When collecting data, determine the amount of data you will need. It is not always necessary, or possible, to collect all available data within a project or solution. The amount of data that can be collected is determined by the ability of the sensors, network, computers, and other hardware involved. It is also determined by the necessity, for example in a high-speed bottling line, each bottle must be checked for the proper alignment of the label and kicked out of the line if there is a problem. In this case, the data from every bottle is important. With a different sensor such as a humidity sensor in a corn field, it is not necessary to report the humidity every tenth of a second. Every five or ten minutes may be sufficient. This is known as the data sampling rate.

Not all data collected can be used as is. Extraneous data might have been collected. Incorrect or false data might also have been collected. In order to make this data usable, it must be cleaned. Cleaning data consists of removing unwanted data, changing incorrect data, and filling in missing data. It is common to use code to clean data. This is accomplished by searching for criteria, or lack thereof, and operating on the data until there are no more anomalies. After the data has been cleaned, it can more easily be searched, analyzed, and visualized.

Through data analysis, interesting insights can be learned and trends can be uncovered. This often leads to new queries that had not yet been realized. When you discover that you might be able to discern additional value from some data set, you can begin to experiment with how the data is organized and presented. For example, a security camera monitoring a parking lot for crimes could also be used to report the number and location of free spaces to drivers.

## Data Engineer, Data Analyst, Data Scientist — What’s the Difference?

**What is a Data Analyst?**

Data Analysts deliver value to their companies by taking data, using it to answer questions, and communicating the results to help make business decisions. Common tasks done by data analysts include data cleaning, performing analysis and creating data visualizations.

Depending on the industry, the data analyst could go by a different title (e.g. Business Analyst, Business Intelligence Analyst, Operations Analyst, Database Analyst). Regardless of title, the data analyst is a generalist who can fit into many roles and teams to help others make better data-driven decisions.

The nature of the skills required will depend on the company's specific needs, but these are some common tasks:
- Cleaning and organizing raw data.
- Using descriptive statistics to get a big-picture view of their data.
- Analyzing interesting trends found in the data.
- Creating visualizations and dashboards to help the company interpret and make decisions with the data.
- Presenting the results of a technical analysis to business clients or internal teams.

**What is a Data Scientist?** 

A data scientist is a specialist who applies their expertise in statistics and building machine learning models to make predictions and answer key business questions.

A data scientist still needs to be able to clean, analyze, and visualize data, just like a data analyst. However, a data scientist will have more depth and expertise in these skills, and will also be able to train and optimize machine learning models.

The following are examples of work performed by data scientists:
- Valuating statistical models to determine the validity of analyses.
- Using machine learning to build better predictive algorithms.
- Testing and continuously improving the accuracy of machine learning models.
- Building data visualizations to summarize the conclusion of an advanced analysis.

**What is a Data Engineer?**

Data engineers build and optimize the systems that allow data scientists and analysts to perform their work. Every company depends on its data to be accurate and accessible to individuals who need to work with it. The data engineer ensures that any data is properly received, transformed, stored, and made accessible to other users.

The data engineer’s mindset is often more focused on building and optimization. The following are examples of tasks that a data engineer might be working on:
- Building APIs for data consumption.
- Integrating external or new datasets into existing data pipelines.
- Applying feature transformations for machine learning models on new data.
- Continuously monitoring and testing the system to ensure optimized performance.

## Data Analysis Workflow
Data analysis is a very popular field and can involve performing many different tasks of varying complexity. Which specific analysis steps you perform will depend on which dataset you’re analyzing and what information you hope to glean. To overcome these scope and complexity issues, you need to take a strategic approach when performing your analysis. This is where a data analysis workflow can help you.

A data analysis workflow is **a process that provides a set of steps for your analysis team to follow when analyzing data**. The implementation of each of these steps will vary depending on the nature of your analysis, but following an agreed-upon workflow allows everyone involved to know what needs to happen and to see how the project is progressing.

Using a workflow also helps future proof your analysis methodology. By following the defined set of steps, your efforts become systematic, which minimizes the possibility that you’ll make mistakes or miss something. Furthermore, when you carefully document your work, you can reapply your procedures against future data as it becomes available. Data analysis workflows therefore also provide repeatability and scalability.

There’s no single data workflow process that suits every analysis, nor is there universal terminology for the procedures used within it. To provide a structure for the rest of this tutorial, the diagram below illustrates the stages that you’ll commonly find in most workflows:
![A Data Analysis Workflow](./images/img_04.avif)
<!-- Source: https://realpython.com/python-for-data-analysis/#resolving-an-anomaly -->

The solid arrows show the standard data analysis workflow that you’ll work through to learn what happens at each stage. The dashed arrows indicate where you may need to carry out some of the individual steps several times depending upon the success of your analysis. Indeed, you may even have to repeat the entire process should your first analysis reveal something interesting that demands further attention.


## Python intro
**Python is a widely-used, interpreted, object-oriented, and high-level programming language with dynamic semantics, used for general-purpose programming.**


### Development Steps of Python

Guido Van Rossum published the **first version of Python code (version 0.9.0)** in **February 1991**. This release included already exception handling, functions, and the core data types of list, dict, str and others. It was also object oriented and had a module system.

**Python version 1.0 was released in January 1994**. The major new features included in this release were the functional programming tools lambda, map, filter and reduce, which Guido Van Rossum never liked.

Six and a half years later in **October 2000, Python 2.0** was introduced. This release included list comprehensions, a full garbage collector and it was supporting unicode.

Python flourished for another 8 years in the versions 2.x before the next major release as **Python 3.0** (also known as "Python 3000" and "Py3K") was released. Python 3 is not backwards compatible with Python 2.x.

A good example of **Python’s principles is the Zen of Python**, a set of aphorisms from the software engineer Tom Peters. In 20 lines such as “Beautiful is better than ugly.”, the [Zen contains the core philosophy of Python](https://peps.python.org/pep-0020/).

> Try to read the Zen of Python and think about what each line means. You can do this by typing `import this` in the Python interpreter.

### Python 2 vs. Python 3
- [How we rolled out one of the largest Python 3 migrations ever](https://dropbox.tech/application/how-we-rolled-out-one-of-the-largest-python-3-migrations-ever)
- [Difference Between Python 2 and 3](https://www.interviewbit.com/blog/difference-between-python-2-and-3/)
- [Python 2 vs 3: Everything You Need to Know](https://www.datacamp.com/blog/python-2-vs-3-everything-you-need-to-know)

Python 2 was launched in 2000; Python 3 was launched in 2008. The issue with Python 3 was that it wasn’t backward compatible with its predecessor. So many companies still rely on Python 2—fourteen years after the introduction of Python 3—because transferring codes between Python 2 vs. 3 is a lot of effort. It could take years. 

> It took DropBox three years to migrate, despite Guido Van Rossum working for them.

Python 2 is no longer supported by the Python Software Foundation. The last major version of Python 2, Python 2.7, was released in 2010 and was supported through 2020. After 2020, there was no new security updates, bug fixes, or other improvements. **Python 2 is legacy, Python 3 is the present and future of the language.**

**Difference Between Python 2 and 3**:
- Print is now a function
- Views and iterators instead of lists
- The rules for ordering comparisons have been simplified. E.g. a heterogeneous list cannot be sorted, because all the elements of a list must be comparable to each other.
- There is only one integer type left, i.e. int. long is int as well.
- The division of two integers returns a float instead of an integer. "//" can be used to have the "old" behavior.
- Text Vs. Data Instead Of Unicode Vs. 8-bit

### Why Python? Advantages/Disadvantages
- [Introduction to Python 3](https://realpython.com/python-introduction/)

**Advantages**:
- Python is Popular
- Python is Free
- Python is Portable
- It is beginner-friendly and simple (Easy to learn, Easy to read, Easy to write, Easy to debug).
- Python is open-source and has a large community.
- It is great for both startups as well as big organizations.
- It has great career opportunities.
- Python has many powerful frameworks. 
- Python’s readability and ease-of-use make developers more productive.
- Is a general-purpose language, but is used almost everywhere (web development, machine learning, data science, Scripting, biology,... etc.)

**Disadvantages**:
- Python is slow as compared to C or C++. It's not a speed demon - Python does not deliver exceptional performance;
- In some cases it may be resistant to some simpler testing techniques - this may mean that debugging Python's code can be more difficult than with other languages; fortunately, making mistakes is always harder in Python.
- Not for low-level programming (like microcontrollers, embedded systems, etc.). There are still some frameworks like MicroPython, CircuitPython, etc. to develop low-level applications in Python.
- Not for Mobile and Game development (although there are some frameworks like Kivy, Pygame, etc. to develop mobile and game applications in Python)

While Python was steadily growing basically its whole existence, from around 2010, it started on a growth trajectory that soon enabled it to rival other top programming languages, such as Java and JavaScript.

### Python Implementations Types
- [Best Python Interpreters: Choose the Best in 2023](https://hackr.io/blog/python-interpreters)

Depending on the Python implementation you use, the interpreter can be:
- **CPython**:
    - The most popular form of Python being implemented today, CPython is often thought of as the “default” Python implementation. Written in C, CPython compiles source code to bytecode. After that, it interprets the bytecode, executing it on the fly.
    - It is compiled to run on virtual machines, which are software that emulate specific computer hardware. That way, the bytecode does not have to be configured for a myriad of different computer systems.
- **Jython**:
    - Another implementation of Python is called Jython. Instead of C, it is written in Java and is interpreted for the Java Virtual Machine (JVM).
    - The reason there is a variety of Python implementations is each one is better-suited for a unique technology stack. For example, Jython is geared toward a Java stack. It:
        - Works naturally and effortlessly with Java programs.
        - Imports a variety of Java classes.
        - Uses Java classes directly from inside the Jython program.
- **IronPython**:
    - Written in C#, IronPython was created by Jim Hugunin in 2006 and is designed for the .NET stack. 
- **PyPY**:
    - PyPy is a Python implementation written in Python. It is a very fast implementation of Python, but it is not fully compatible with CPython.


### Python 3 versions
- [Development Cycle](https://devguide.python.org/developer-workflow/development-cycle/)
- [Status of Python Versions](https://devguide.python.org/versions/)

Python uses a `major.minor.micro` nomenclature for production-ready releases. So for Python 3.1.2 final, that is a major version of 3, a minor version of 1, and a micro version of 2.
- new **major versions** are exceptional; they only come when strongly incompatible changes are deemed necessary, and are planned very long in advance;
- new **minor versions** are feature releases; they get released annually, from the current in-development branch;
- new **micro versions** are bugfix releases; they get released roughly every 2 months; they are prepared in maintenance branches.

![Python 3 versions](./images/img01.png)

## Git in Github

- [Introduction to Git and GitHub for Python Developers](https://realpython.com/python-git-github-intro/)
- [Git Book](https://git-scm.com/book/en/v2)
- [Become a git guru](https://www.atlassian.com/git/tutorials)

**Git is a distributed version control system (DVCS).**

A **version control system (VCS)** is a set of tools that track the history of a set of files. This means that you can tell your VCS (Git, in our case) to save the state of your files at any point. Then, you may continue to edit the files and store that state as well. Saving the state is similar to **creating a backup copy of your working directory**. When using Git, we refer to this saving of state as making a commit.

When you make a commit in Git, you add a commit **message that explains at a high level what changes you made in this commit**. Git can show you the history of all of the commits and their commit messages. This provides a useful history of what work you have done and can really help pinpoint when a bug crept into the system.

In addition to showing you the log of changes you’ve made, Git also allows you to **compare files between different commits**.

> Check if git is installed: `git --version`. If not use the page [Download for Windows](https://git-scm.com/download/win) to install it.

### Creating a New Repo

- To work with Git, you first need to tell it who you are. You can set your username and email with the git config command:
  - `git config --global user.name "your name goes here"`
  - `git config --global user.email "your email goes here"`

They don’t do any communication to a server or over the network. It turns out that there are only four major Git commands which actually talk to remote repos:

- `clone`
- `fetch`
- `pull`
- `push`

### Intro to Github

- [GitHub Docs](https://docs.github.com/en)
- [Hello World](https://docs.github.com/en/get-started/quickstart/hello-world)

GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

1. [Signing up for GitHub](https://docs.github.com/en/get-started/signing-up-for-github)
2. [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
3. [Creating a repository](https://docs.github.com/en/get-started/quickstart/create-a-repo)
   - A repository is usually used to organize a single project. Repositories can contain folders and files, images, videos, spreadsheets, and data sets -- anything your project needs. Often, repositories include a README file, a file with information about your project. README files are written in the plain text Markdown language.
   - `.gitignore`: But sometimes you’ll find that there are a bunch of files that show up in the untracked section and that you want Git to just not see. That’s where the .gitignore file comes in.
4. [Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
    - Fork the repo to your account.
    - Clone the repo locally: `git clone https://github.com/<USERNAME>/python-data-analytics.git`
5. Make changes to a file and commit them.
   - `git status` – Make sure your current area is clean.
   - `git pull` – Get the latest version from the remote. This saves merging issues later.
   - Edit your files and make your changes.
   - `git status` – Find all files that are changed. Make sure to watch untracked files too!
   - `git add [files] `– Add the changed files to the staging area.
   - `git commit -m "message"` – Make your new commit.
6. [Pushing commits to a remote repository](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository): `git push origin main`

> Never put confidential information into a public repository on GitHub. Passwords, API keys, and similar items should not be committed to a repo. Someone will find them eventually.

[Adding locally hosted code to GitHub](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github): If your code is stored locally on your computer and is tracked by Git or not tracked by any version control system (VCS), you can import the code to GitHub using GitHub CLI or Git commands.

> You can use [organizations](https://docs.github.com/en/organizations) to collaborate with an unlimited number of people across many projects at once, while managing access to your data and customizing settings.


## Installing Python

### Intro to Terminal
- [Windows Commands](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands)

Windows has two command-line shells: the **Command shell** and **PowerShell**. Each shell is a software program that provides direct communication between you and the operating system or application, providing an environment to automate IT operations.
- The **Command shell** was the first shell built into Windows to automate routine tasks, like user account management or nightly backups, with batch (.bat) files. With Windows Script Host, you could run more sophisticated scripts in the Command shell.
- **PowerShell** was designed to extend the capabilities of the Command shell to run PowerShell commands called cmdlets. Cmdlets are similar to Windows Commands but provide a more extensible scripting language. You can run both Windows Commands and PowerShell cmdlets in PowerShell, but the Command shell can only run Windows Commands and not PowerShell cmdlets.

Windows has created a new, open-source **Windows Terminal** to be a universal console host. It acts as an interface to multiple shells, allowing you to start the Command Prompt, PowerShell, and any other shell that you might have available as different tabs in the same host:

The Windows Terminal is a modern, fast, efficient, powerful, and productive terminal application for users of command-line tools and shells like Command Prompt, PowerShell, and WSL. Its main features include multiple tabs, panes, Unicode and UTF-8 character support, a GPU accelerated text rendering engine, and custom themes, styles, and configurations.
- Download the Windows Terminal from the [Microsoft Store](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701)

Installing it from the Microsoft Store has a few advantages. One advantage is that it ensures that updates come automatically. Another advantage is that it’s painless to install. 

### Configuring Windows

#### App Execution Aliases
App execution aliases are a special kind of alias for Windows. For example, if you type python on the command line, Windows will automatically ask you if you want to install the Microsoft Store version of Python.

App execution aliases are a feature to make things easier to get started, but they can interfere with other programs. For instance, when you install pyenv for Windows and install a few Python versions, the app execution aliases will interfere by not allowing you to access those Python versions.

You can search for the app execution alias control panel from the Start menu. The entry is called *Manage app execution aliases*.

![App execution aliases](./images/img02.png)

You can usually turn all of these off, as you already have the Path environment variable to make sure apps are available on the command line.

#### Windows Explorer
In an attempt to make Windows Explorer easier to use for non-developer types, it hides some information that you’ll probably want to see, so you should enable the following:
- Show file extensions
- Show hidden files
- Show protected operating system files
- Show the full path in the title bar

You can access these options from the file explorer, which you can open with `Win+E`, click on the File tab in the top left, and choose *Change folder and search options*. Under the View tab, you’ll be able to find these settings.

![Windows Explorer](./images/img03.png)

#### Loosening Your Execution Policy
First open up Windows Terminal as an administrator.

> Note: To launch programs as an administrator, you can search for the app in the Start menu, and then right-click on it, and choose Run as administrator.

Once you have an administrator terminal session open, you should be presented with a PowerShell tab.

The execution policy sets how strict your system is about running scripts from other sources. For this tutorial, you’ll want to set it to `RemoteSigned`:
- `Set-ExecutionPolicy RemoteSigned`

You may not see the warning, because the execution policy might already be set. To double-check your setting, you can run `Get-ExecutionPolicy`.

> Without administrator privileges: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`


## Install Python with UV
- [UV Docs](https://docs.astral.sh/uv/)
- [Installing Python](https://docs.astral.sh/uv/guides/install-python/)

An extremely fast Python package and project manager, written in Rust.
- 🚀 A single tool to replace pip, pip-tools, pipx, poetry, pyenv, twine, virtualenv, and more.
- ⚡️ 10-100x faster than pip.
- 🐍 Installs and manages Python versions.
- 🛠️ Runs and installs Python applications.
- ❇️ Runs scripts, with support for inline dependency metadata.
- 🗂️ Provides comprehensive project management, with a universal lockfile.
- 🔩 Includes a pip-compatible interface for a performance boost with a familiar CLI.
- 🏢 Supports Cargo-style workspaces for scalable projects.
- 💾 Disk-space efficient, with a global cache for dependency deduplication.
- ⏬ Installable without Rust or Python via curl or pip.
- 🖥️ Supports macOS, Linux, and Windows.

Install uv with our official standalone installer:
- Linux and macOS: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Windows: `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`

> Already installed? Update UV: `uv self update`

Installation:
- To view available and installed Python versions: `uv python list`
- To install a specific Python version: `uv python install 3.13`

### Create a virtual environment

**A Python virtual environment is a folder structure that gives you everything you need to run a lightweight yet isolated Python environment.**

**Why we need a Python environment?** The short answer is that **Python isn’t great at dependency management**. If you’re not specific, then pip will **place all the external packages that you install in a folder called `site-packages/`** in your base Python installation.

Several issues can come up if all of your external packages land in the same folder. 
1. **Avoid System Pollution**
    - (Linux) If you install packages to your operating system’s global Python, these packages will mix with the system-relevant packages. This mix-up could have unexpected side effects on tasks crucial to your operating system’s normal behavior.
2. **Sidestep Dependency Conflicts**
    - One of your projects might require a different version of an external library than another one. If you have only one place to install packages, then you can’t work with two different versions of the same library. This is one of the most common reasons for the recommendation to use a Python virtual environment.
    - If you install two different versions of the same package into your global Python environment, the second installation overwrites the first one.
    - Example:
        - `pip install flask==1.1.4`
        - `pip install flask==2.0.1`
        - `pip list`
        - `pip show flask`
        - Try to do the same with virtual environment
3. **Minimize Reproducibility Issues**
    - If all your packages live in one location, then it’ll be difficult to only pin dependencies that are relevant for a single project.
    - If you use a separate virtual environment for each of your projects, then it’ll be more straightforward to read the project requirements from your pinned dependencies. 
4. **Dodge Installation Privilege Lockouts**
    - In a corporate work environment, you most likely won’t have administrative level of access to the machine that you’re working on.
    - If you use virtual environments, then you create a new installation location within the scope of your user privileges, which allows you to install and work with external packages.


- Create a virtual environment in the current directory: `uv venv --python=python3.13`
- Activate the virtual environment: `source venv/bin/activate` (Linux) or `.venv\Scripts\activate` (Windows)

By default, creates a virtual environment named `.venv` in the working directory. An alternative path may be provided positionally.

When you create a new virtual environment, Python creates a self-contained folder structure and copies or symlinks the Python executable files into that folder structure.


### Test your Python shell
- [The Interpreter, an Interactive Shell](https://python-course.eu/python-tutorial/interpreter-interactive-shell.php)
- [Interacting With Python](https://realpython.com/interacting-with-python/)

To start the Python shell, open the Command Prompt and run `python` or `py`. You should see the Python shell open with the version number printed to the screen.

When commands are read from a tty, the interpreter is said to be in interactive mode. In this mode it prompts for the next command with the primary prompt, usually three greater-than signs (>>>); for continuation lines it prompts with the secondary prompt, by default three dots (...). The interpreter prints a welcome message stating its version number and a copyright notice before printing the first prompt.

Now you can type Python commands into the shell. A simple command like `print("Hello World!")` will print the text `Hello World!` to the screen.

When you work interactively, every expression and statement you type in is **evaluated and executed immediately**.

Typing an end-of-file character (Control-D on Unix, `Control-Z` on Windows) at the primary prompt causes the interpreter to exit with a zero exit status. If that doesn’t work, you can exit the interpreter by typing the following command: `quit()`.


## Installing Python Modules
- [Python Modules and Packages – An Introduction](https://realpython.com/python-modules-packages/)

**Modular programming** refers to the process of breaking a large, unwieldy programming task into **separate, smaller, more manageable subtasks or modules**. Individual modules can then be cobbled together like building blocks to create a larger application.

There are several advantages to modularizing code in a large application:
- **Simplicity**: Rather than focusing on the entire problem at hand, a module typically focuses on one relatively small portion of the problem. If you’re working on a single module, you’ll have a smaller problem domain to wrap your head around. This makes development easier and less error-prone.
- **Maintainability**: Modules are typically designed so that they enforce logical boundaries between different problem domains. If modules are written in a way that minimizes interdependency, there is decreased likelihood that modifications to a single module will have an impact on other parts of the program. This makes it more viable for a team of many programmers to work collaboratively on a large application.
- **Reusability**: Functionality defined in a single module can be easily reused (through an appropriately defined interface) by other parts of the application. This eliminates the need to duplicate code.
- **Scoping**: Modules typically define a separate namespace, which helps avoid collisions between identifiers in different areas of a program.

There are three basic kinds of modules in Python:
- **[Python Standard Library](https://docs.python.org/3/library/)** is very extensive, offering a wide range of facilities.
    - The library contains **built-in modules** (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Python programmers.
    - As well as **modules written in Python** that provide standardized solutions for many problems that occur in everyday programming. They are available through the and are therefore installed with your Python installation.
- **User-defined modules** are written in Python and typically stored in files with a .py extension. The Python interpreter can import these modules from any location on the file system.
- **Third-party modules** are stored in the [Python Package Index (PyPI)](https://pypi.org/) (pronounced Pie Pea Eye) and can be installed using the pip tool.

We will manage Python packages with `UV`, a pip-compatible interface. Add `uv` to the beginning of any pip command to run it.

You can verify that pip is available by looking for the pip executable on your system. 
- `uv pip --version`

The pip install command always installs the latest published version of a package, but sometimes your code requires a specific package version to work correctly.

You want to create a specification of the dependencies and versions that you used to develop and test your application so that there are no surprises when you use the application in production.

These external dependencies are also called requirements. You’ll often find Python projects that pin their requirements in a file called `requirements.txt` or similar. The **requirements file format allows you to specify precisely which packages and versions should be installed.**

When you want to replicate the environment in another system, you can run `pip install`, using the `-r` switch to specify the requirements file:
- `uv pip install -r requirements.txt`

## Installing and running VSCode
- [Python Development in Visual Studio Code](https://realpython.com/python-development-visual-studio-code/)
- [Setting Up VS Code](https://realpython.com/python-coding-setup-windows/#setting-up-vs-code)
- [Advanced Visual Studio Code for Python Developers](https://realpython.com/advanced-visual-studio-code-python/)
- [Setting Up VSCode For Python: A Complete Guide](https://www.datacamp.com/tutorial/setting-up-vscode-python)
- [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)

Visual Studio Code is a lightweight but powerful source code editor which runs on your desktop and is available for Windows, macOS and Linux. It comes with built-in support for JavaScript, TypeScript and Node.js and has a rich ecosystem of extensions for other languages and runtimes (such as C++, C#, Java, Python, PHP, Go, .NET).

[Download Visual Studio Code](https://code.visualstudio.com/Download) and install it on your computer.

At its heart, Visual Studio Code is a code editor. Like many other code editors, VS Code adopts a common user interface and layout of an explorer on the left, showing all of the files and folders you have access to, and an editor on the right, showing the content of the files you have opened.

![VSCode User Interface](https://code.visualstudio.com/assets/docs/getstarted/userinterface/hero.png)

By starting VS Code in a folder, that folder becomes your "workspace".

Using a command prompt or terminal, open VS Code (`code`) in that folder (`.`) by entering the following command: `code .`

Install the **Python extension for Visual Studio Code** from the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)


Open the Command Palette (`Ctrl+Shift+P`), start typing `Python: Select Interpreter` command from the Command Palette. Select the Python interpreter associated with the virtual environment you created above (ex. `Python 3.13.2 ('.venv':'.venv')`).

> If you don't see the virtual environment you created above, you may need to restart VS Code.

Create a `.vscode` folder in the project root. In the new folder create a file `settings.json`:
```json
{
    "python.languageServer": "Pylance",
    "python.analysis.typeCheckingMode": "basic",
    "python.analysis.diagnosticMode": "workspace",
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.tabSize": 4,
    "editor.codeActionsOnSave": {
        "source.organizeImports.ruff": "explicit",
        "source.addMissingImports": "explicit",
        "source.formatDocument.ruff": "explicit",
        "source.fixAll.ruff": "explicit"
    },
    "ruff.importStrategy": "fromEnvironment",
    "ruff.lint.select": ["ALL"],
    "ruff.lineLength": 180,
    "ruff.lint.ignore": ["S105", "N815", "D104"],
    "ruff.exclude": ["**/tests/**"],
    "python.testing.pytestArgs": [
        "tests"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true,
    "cSpell.words": [
        "Pylance"
    ],
}
```

## Installing Jupyter Notebook

- [The Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/)
- [Jupyter Notebook: An Introduction](https://realpython.com/jupyter-notebook-introduction/)
- [Installing Jupyter](https://jupyter.org/install)
- [How to Use Jupyter Notebooks: The Ultimate Guide](https://www.datacamp.com/tutorial/tutorial-jupyter-notebook)
- [How to Use Jupyter Notebook: A Beginner’s Tutorial](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)
- [Tutorial: Advanced Jupyter Notebooks](https://www.dataquest.io/blog/advanced-jupyter-notebooks-tutorial/)
- [28 Jupyter Notebook Tips, Tricks, and Shortcuts](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)

The Jupyter Notebook is an open source web application that you can use to create and share documents that contain live code, equations, visualizations, and text. Jupyter Notebook is maintained by the people at Project Jupyter.

Jupyter Notebooks are a spin-off project from the IPython project, which used to have an IPython Notebook project itself. The name, Jupyter, comes from the core supported programming languages that it supports: Julia, Python, and R. Jupyter ships with the IPython kernel, which allows you to write your programs in Python, but there are currently over 100 other kernels that you can also use.

> A [major upgrade to the Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/latest/migrate_to_notebook7.html) interface is coming with Notebook 7! This upgrade will bring a heap of new features, but will also break backwards compatibility with many classic Notebook features and customizations.

Install the classic Jupyter Notebook with: `pip install notebook`. You can also add it to the `requirements.txt` file.

For starting the Jupyter Notebook Server just go to that location in your terminal and run the following command:

- `jupyter notebook`

This will start up Jupyter and your default browser should start (or open a new tab) to the following URL: `http://localhost:8888/tree`

We will learn the following:

- Creating a Notebook
- Running Cells
- The Menus
- Starting Terminals and Other Things
- Viewing What’s Running
- Adding Rich Content
- Exporting Notebooks

More information about Jupyter Notebooks: [Jupyter Notebook Tutorial](Jupyter_Notebook_tutorial.ipynb)

### Jupyter Notebooks in VS Code

- [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

Visual Studio Code supports working with Jupyter Notebooks natively, and through Python code files.

> If not already installed, install the [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) extension for VS Code.

To work with Python in Jupyter Notebooks, you must activate a Python environment in which you've installed the Jupyter package.

Once the appropriate environment is activated, you can create and open a Jupyter Notebook, connect to a remote Jupyter server for running code cells, and export a Jupyter Notebook as a Python file.

> [Markdown guide for cell formatting](https://www.markdownguide.org/basic-syntax/)

### Google Colab

- [Welcome to Google Colab!](https://colab.research.google.com/?utm_source=scs-index#scrollTo=Nma_JWh-W-IF)