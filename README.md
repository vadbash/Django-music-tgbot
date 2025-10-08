# Django Music Telegram Bot 🎵

A Telegram bot powered by Django that lets users download audio/video from YouTube links and provides a backend admin & REST API for managing users and usage history.

## Overview

**Django Music Telegram Bot** is a hybrid application combining a Telegram bot frontend with a Django backend. Users interact via Telegram by sending a YouTube video link, and the bot converts it into audio/video formats (e.g., MP3, MP4, WebM) and returns the file.  
Meanwhile, the Django portion handles user management, usage history tracking, and data access through both the Django Admin interface and a RESTful API via Django REST Framework.

**Key Capabilities:**

-   Accept YouTube URLs via Telegram and return downloadable media (audio/video).
    
-   Support multiple formats (mp3, mp4, webm, etc.).
    
-   Record user interactions (who requested what, when) in the database.
    
-   Manage users, view history, and inspect usage through Django Admin.
    
-   Provide a REST API for external integration or frontends.

## Installation

Follow these steps to set up and run the project:

1.  **Clone the repository**
    
    `git clone https://github.com/vadbash/Django-music-tgbot.git` 
    
2.  **Set up a Python environment** (recommended)
    
3.  **Install dependencies**
    
    `pip install -r requirements.txt` 
    
4.  **Configure Django settings**
    
    -   Add your Telegram bot token in settings or environment variables.
        
    -   Configure database settings (SQLite, PostgreSQL, etc.).
        
    -   If there are additional settings (e.g. media storage, API keys), add them accordingly.
        
5.  **Apply migrations**
    
6.  **Run the application / bot**
    
7.  **Access admin / API**
    
    -   Log in to Django Admin to view users, usage logs, etc.
        
    -   Use the REST API endpoints for external integrations (see API docs or browsable API).