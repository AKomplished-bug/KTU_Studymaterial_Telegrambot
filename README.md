# KTU_Studymaterial_Telegrambot
This project is a Telegram bot designed to help BTech students of KTU university access study materials such as notes and previous year question papers for various departments like Computer Science, Civil, etc. The bot uses the Google Drive API to fetch and provide downloadable links to these materials.

## Table of Contents

- [Features](#features)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
- [Commands](#commands)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Select department, semester, and subject to access relevant study materials.
- Provides downloadable links to notes and previous year question papers.
- Uses Google Drive API to fetch materials from public folders.
- State management using FSMContext to handle user interactions seamlessly.

## Setup

### Prerequisites

- Python 3.7+
- A Telegram bot token from BotFather
- Google Cloud project with Drive API enabled
- Service account credentials for Google Drive API


### Installation

    Clone the repository

sh

git clone https://github.com/AKomplished-bug/KTU_Studymaterial_Telegrambot.git
cd KTU_Studymaterial_Telegrambot

    Create and activate a virtual environment

sh

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

    Install the dependencies

sh

pip install -r requirements.txt
### Configuration

Create a .env file in the root directory of your project and add your Telegram bot token:

sh

BOT_TOKEN=your_telegram_bot_token

    Google Cloud setup

    Enable the Google Drive API in your Google Cloud project.
    Create a service account and download the JSON key file. Save it in the root directory of your project with the name service_account.json.