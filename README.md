# Voice Assistant Application

This is a simple voice assistant application that uses Flask, Whisper for audio transcription, and ChatGPT for generating responses. This guide will walk you through the steps to get the application up and running in your browser.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installing Python](#installing-python)
3. [Setting Up the Project](#setting-up-the-project)
4. [Running the Application](#running-the-application)
5. [Using the Application](#using-the-application)
6. [Troubleshooting](#troubleshooting)

## Prerequisites

Before you begin, ensure you have the following:
- A computer with internet access.
- Basic knowledge of using the command line (Terminal on macOS/Linux or Command Prompt/PowerShell on Windows).

## Installing Python

1. **Download Python:**
   - Go to the [official Python website](https://www.python.org/downloads/).
   - Click on the "Download Python" button. The website should automatically suggest the best version for your operating system.

2. **Install Python:**
   - **Windows:**
     - Run the downloaded installer.
     - Make sure to check the box that says "Add Python to PATH" before clicking "Install Now".
   - **macOS:**
     - Open the downloaded `.pkg` file and follow the installation instructions.
   - **Linux:**
     - Open your terminal and run the following command:
       ```bash
       sudo apt update
       sudo apt install python3 python3-pip
       ```

3. **Verify Installation:**
   - Open your command line interface (Terminal or Command Prompt).
   - Type the following command and press Enter:
     ```bash
     python --version
     ```
   - You should see the installed version of Python. If you see an error, try `python3 --version`.

## Setting Up the Project

1. **Clone the Repository:**
   - Open your command line interface.
   - Navigate to the directory where you want to store the project. For example:
     ```bash
     cd path/to/your/directory
     ```
   - Clone the repository (replace `your-repo-url` with the actual URL of your repository):
     ```bash
     git clone your-repo-url
     ```
   - Navigate into the project directory:
     ```bash
     cd your-repo-name
     ```

2. **Create a Virtual Environment (Optional but Recommended):**
   - A virtual environment helps manage dependencies for your project.
   - Run the following command to create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - **Windows:**
       ```bash
       venv\Scripts\activate
       ```
     - **macOS/Linux:**
       ```bash
       source venv/bin/activate
       ```

3. **Install Required Packages:**
   - Ensure you have `pip` installed (it comes with Python).
   - Install the required packages by running:
     ```bash
     pip install -r requirements.txt
     ```
   - If you don't have a `requirements.txt` file, you can manually install the necessary packages:
     ```bash
     pip install Flask sounddevice numpy scipy openai whisper
     ```

4. **Set Up API Keys:**
   - You will need an OpenAI API key to use the ChatGPT functionality.
   - Sign up at [OpenAI](https://openai.com/) and obtain your API key.
   - Create a file named `creds.py` in the project directory and add the following line:
     ```python
     openaiapikey = 'your_openai_api_key_here'
     ```

## Running the Application

1. **Start the Flask Server:**
   - In your command line interface, ensure you are in the project directory and your virtual environment is activated.
   - Run the following command to start the Flask application:
     ```bash
     python main.py
     ```
   - You should see output indicating that the server is running, typically on `http://127.0.0.1:5000/`.

2. **Open Your Browser:**
   - Open your web browser and navigate to `http://127.0.0.1:5000/`.
   - You should see the voice assistant interface.

## Using the Application

- Click the microphone button to start speaking your questions or commands related to cryptocurrency.
- The assistant will listen, transcribe your speech, and provide a response based on your input.

## Troubleshooting

- **If you encounter issues starting the server:**
  - Ensure that you have installed all required packages.
  - Check for any error messages in the command line for clues.

- **If the microphone does not work:**
  - Ensure your microphone is connected and working.
  - Check your browser permissions to allow microphone access.

- **If you receive an error related to OpenAI:**
  - Verify that your API key is correct and that you have access to the OpenAI API.

## Conclusion

You have successfully set up and run the Voice Assistant application! Feel free to explore and modify the code to enhance its functionality. If you have any questions or need further assistance, don't hesitate to ask.
