# Tiny URL-Generator
This is a URL shortening web application built using Flask and SQLAlchemy. The purpose of this application is to provide short URLs that can be used instead of long URLs to access websites. This can be useful in situations where a long URL needs to be shared, for example on social media, where character limits can be a concern.

## Technologies Used
Python 3<br>
Flask<br>
SQLAlchemy<br>
SQLite<br>
## Getting Started
Clone the repository: git clone https://github.com/mohamedmuqheet/tinyurl-generator<br> 
Navigate to the project directory: URL-shortener<br>
Create a virtual environment: python3 -m venv venv<br>
Activate the virtual environment: source venv/bin/activate<br>
Install the required packages: pip install -r requirements.txt<br>
Start the application: python3 app.py<br>
Visit http://localhost:5000 in your web browser to access the application.<br>
## Features
Shorten a long URL by entering it into the input field on the home page.<br>
View a list of all URLs that have been shortened by visiting /urls.<br>
Redirect to the original long URL by visiting the shortened URL.<br>
## Screenshots
![Screenshot](https://github.com/mohamedmuqheet/tinyurl-generator/raw/master/Screenshot%20(334).png"URL_shortener")<br>

## Usage
Enter a long URL into the input field on the home page and click "Shorten".<br>
The application will create a short URL for the long URL and return it.<br>
Copy the short URL and use it to access the original long URL.<br>
To view a list of all shortened URLs, visit /urls.<br>
## Contributor
Mohamed Muqheeth
## License
This project is licensed under the MIT License - see the LICENSE file for details.
