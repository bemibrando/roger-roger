# Roger Roger Project
<img src="https://img.shields.io/github/last-commit/bemibrando/roger-roger?style=for-the-badge" height="24px"> &nbsp; <img src="https://img.shields.io/badge/status-In%20Progress-yellow?style=for-the-badge" height="24px">

This is a virtual assistent, build with python to assist my life.

<b>Build with:</b>

<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" height="24px"> <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" height="24px">

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Project Composition](#project-composition)
  - [Screenshot](#screenshot)
  - [Built with](#built-with)
  - [Links](#links)
- [How to use](#how-to-use)
  - [Install and Run](#install-and-run)
  - [How to use the project](#how-to-use-the-project)
- [Useful Resources](#useful-resources)
- [Author](#author)

## Overview

### <b id="the-challenge">The challenge</b>
- Update finance worksheet scanning a Receipt's QR Code.
- Create a backupfile to each update.
- Edit scrapped information before update worksheet.

### <b id="project-composition">Project Composition</b>
- Open a window when starts the project.
- Navigation between "pages".
- Open Camera to Read QR Code.
- Scrap information from receipt page.
- Edit scrapped information before update excel file.
- Check if exist the file to add the information, if not create it.
- Add this information into a backup file and update pre-selected excel file.


### <b id="buid-with">Build with</b>
- Python: main language programming
- Pandas: to manipulate data in spreadsheets
- BeautifulSoup: to scrap webpage information
- Tkinter: to build GUI

### <b id="links">Links</b>
- Solution URL: [GitHub Repository](https://github.com/bemibrando/roger-roger/)

## How to use

### Install and Run
1. Make a clone of this repository and access the directory.
```
$ git clone git@github.com:bemibrando/roger-roger.git && cd roger-roger
```

2. [Install Python](https://www.python.org/downloads/)

3. Install the dependencies
```
$ pip install pip
```

4. Run the system 
```
$ python rogerSystem.py
```

### How to use the project
1. Make a copy of the `global_settings_default.py` and change it to `global_settings.py`
    - This will allow the files to be stored in a folder.
    - If you want to change the storege place of the files, you can open the `global_settings.py` and edit the path, files names and sheets name.
2. To use functionality `Scan QR Code` you need to have a webcam. 


<br /><br />



<br /><br />

## <b id="useful-resources">Useful Resources</b>
- [Python](https://www.python.org/) - Python is a high-level, general-purpose programming language.
- [Python tkinter package](https://docs.python.org/3/library/tkinter.html) - Tk interface is the standeard Python interface to the Tcl/Tk GUI toolkit.
- [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/) - Beautiful Soup is a Python library for pulling data out of HTML and XML files.
- [Pandas PyData](https://pandas.pydata.org/) - Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.

## Author
<div sytle="display: inline-block;">
    <figure>
        <a href="https://github.com/bemibrando" target="_blank">
            <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/102377919?v=4" width="100px" alt="Bianca Emi profile's photo"> <br />
            <sub style="text-align: center; font-size: 1.4em;"><b>Bianca Emi</b></sub>
        </a>
    </figure>
    <p>Made with ♥ by <a href="https://github.com/bemibrando" target="_blank">Bianca Emi</a> 👋 Get in touch!</p>
    <div align="start">
        <a href="https://www.linkedin.com/in/bianca-emi/" target="_blank">
            <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
        </a>   
        <a href="https://twitter.com/bemibrando" target="_blank">
            <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white">
        </a>   
        <a href="mailto: bemi.brando@outlook.com">
            <img src="https://img.shields.io/badge/bemi.brando@outlook.com-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white">
        </a><br/>
    </div>
</div>