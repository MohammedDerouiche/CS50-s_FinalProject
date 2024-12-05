# CS50 Final Project: UK Salaries Analyser

This project involves developing a `Job Analyser` tool designed to help users learn about various job roles and make informed career decisions. It uses web scraping to collect job listing data, processes this data for reliability, and presents it through a web-based dashboard for interactive analysis.

## Methodology

The methodology of this project includes:

- Scraping job listings from GOV.UK website, using API requests and BeautifulSoup.
- Cleaning and transforming the collected data for accuracy and consistency.
- Developing a web-based dashboard using Flask and SQLite to present interactive visualizations.

## Skills, Languages, and Libraries

This project employs the following skills, languages, and libraries:

- **Programming Languages:** Python, SQL, HTML, CSS
- **Libraries:** 
  - `requests`: For HTTP requests
  - `BeautifulSoup`: For web scraping
  - `Pandas` and `NumPy`: For data processing
  - `Flask`: For web development
  - `SQLite`: For database management
  - `Bootstrap`: For front-end design
  - `ChartJS`: For interactive charts

- **Skills:** Web scraping, data cleaning, data transformation, exploratory data analysis (EDA), web development, data visualization

## Extracted Features

The web scraper collects a variety of features from job listings, providing a comprehensive dataset for analysis. The extracted features include:

- **jobTitle**: The title of the job
- **companyName**: The name of the company offering the job
- **location**: The location of the job
- **salary**: The salary range offered
- **jobDescription**: Detailed description of the job responsibilities
- **requirements**: The requirements or qualifications needed for the job
- **datePosted**: The date when the job was posted

