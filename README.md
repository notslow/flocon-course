# FloCon Data Science Concepts and Techniques
__Andrew Fast, Ph.D.__

This repository contains the support files for "Introduction to Data Science - Concepts and Techniques" course being presented in conjunction with [FloCon](https://flocon.org). These files provide some minimal examples of traditional data science algorithms applied to NetFlow and other cybersecurity data.

There multiple ways to run and access this data:

  - [Run In A Browser](#run-in-a-browser)
  - [Run with Anaconda](#run-with-anaconda)
  - [Run using Docker](#run-using-docker)
  - [Run using VSCode](#run-using-vscode)

## Run In A Browser

The course is available in a browser via the [Binder Service](https://mybinder.org). Click the badge below to get started.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/notslow/flocon-course/master)

## Run with Anaconda

Anaconda is a popular Python distribution. It includes the ability to run Jupyter Notebooks.  Download Anaconda [here](https://www.anaconda.com). 

You will need to either:
- Clone the file from github: `git clone https://github.com/notslow/flocon-course.git` 
- Download and unpack the source files directly: [https://github.com/notslow/flocon-course/releases/tag/v2021](https://github.com/notslow/flocon-course/releases/tag/v2021)

Once the files are downloaded, you will need to install the required packages. Choose *ONE* of the following methods:
- Install the packages using `conda` or `pip` on the CLI e.g., `conda install --file requirements.txt`
- Evaluate `dependencies.ipynb` via Jupyter Notebooks. 

## Run using Docker

Docker is a popular method for running software in "containers". First, you will need to grab the files from GitHub using *ONE* of the following methods:

- Clone the file from github: `git clone https://github.com/notslow/flocon-course.git` 
- Download and unpack the source files directly: [https://github.com/notslow/flocon-course/releases/tag/v2021](https://github.com/notslow/flocon-course/releases/tag/v2021)

Then navigate on the command-line to the directory with the files then from the terminal prompt type: `docker run -p 8888:8888 -v $(pwd):/home/jovyan/work jupyter/minimal-notebook`
Then copy and paste the link that appears in the terminal window into your browser

You will need to install the proper Python dependencies for the course. This can be achieved via *ONE* of the following methods:
- Evaluate `dependencies.ipynb` via Jupyter Notebooks. 
- Open a terminal from the "New" drop down menu in the top right of your screen, then type `cd work; pip install -r requirements.txt` at the prompt

## Run using VSCode

VSCode is a common tool for software engineers. You will need to install a plugin for VSCode titled "Jupyter Notebook" from the VSCode Marketplace.  You will also  need to ensure the `ipykernel` python module is installed and available in your environment. Then download the notebook files for the course:

- Clone the file from github: `git clone https://github.com/notslow/flocon-course.git` 
- Download and unpack the source files directly: [https://github.com/notslow/flocon-course/releases/tag/v2021](https://github.com/notslow/flocon-course/releases/tag/v2021)

Finally, install the dependencies using *ONE* of the following methods:

- Evaluate `dependencies.ipynb` via Jupyter Notebooks. 
- Open a new terminal window then type `pip install -r requirements.txt` at the prompt
