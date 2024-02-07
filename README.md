# AI-Driven E-Commerce Email Assistant

## Introduction

A web application leveraging Python, Flask, and OpenAI API to facilitate e-commerce operations by generating and translating customer service emails. Designed for e-commerce store owners and customer service departments, this tool automates responses to customer inquiries, enhancing efficiency and communication.

## Presentation

View presentation [PDF file](https://drive.google.com/file/d/1KQR3ODE5WfpmS47ECYmoupwww_cSpAGl/view?usp=sharing)

## Features

- Automatic email generation in response to customer comments
- Integration with OpenAI API for content creation and translation
- User-friendly web interface for easy operation
- Multi-language support for global e-commerce communication

## Tech Stack

- Python
- Flask
- OpenAI API

## Environment

Developed and tested for Linux.

## Installation and Setup

1. Check Python Version
   Ensure you have Python 3 installed by running:
   `python3 --version`
   If Python is not installed, follow the instructions here: [Install Python on Ubuntu](https://www.makeuseof.com/install-python-ubuntu/).

2. Update your package list and install pip:
   `sudo apt update`
   `sudo apt install python3-pip`

3. Install virtual environment tools:
   `sudo apt install virtualenv virtualenvwrapper`

4. Configure the virtual environment:

   - Open file:
     `nano ~/.bashrc`
   - Add the following lines to the end of the file:
     `WORKON_HOME=$HOME/.virtualenvs`
     `VIRTUAL_ENVWRAPPER_PYTHON=/usr/bin/python3`
     `source /usr/share/virtualenvwrapper/virtualenvwrapper.sh`

5. Create a new virtual environment:
   `mkvirtualenv example`

6. Work on virtual environment:
   `workon example`

7. Clone this repository.

8. Navigate into the project directory:
   `cd ai-ecommerce-email-assistant`

9. Install the requirements:
   `pip install -r requirements.txt`

10. [OpenAI Migration](https://github.com/openai/openai-python/discussions/742):
    `openai migrate`

11. [Get your API key](https://beta.openai.com/account/api-keys)

12. Add OpenAI API Key to the Virtual Environment`s Environment Variables

    - Open or create an .env file within your virtual environment:
      `nano .env`
    - In the .env file, enter the following line, replacing your_api_key_here with your actual OpenAI API key:
      `OPENAI_API_KEY=your_api_key_here`
    - Activate the environment variables in your current session:
      `source .env`
    - Test if the OpenAI API Key was successfully added by printing it:
      `echo $OPENAI_API_KEY`
      If the command prints your API key, it has been successfully added to the environment variables.

13. Running the Application
    `python3 app.py`
    At this point, you can access the application by going to [http://localhost:5000](http://localhost:5000).
