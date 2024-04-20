# Scraping Tool

This tool is designed to scrape product information from the Dental Stall website using Python and the FastAPI framework. It automates the process of extracting product names, prices, and images from each page of the catalogue and stores the scraped information in a local JSON file.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/scraping-tool.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the scraping tool, follow these steps:

1. Open a terminal window and navigate to the project directory.

2. Run the `main.py` script:

    ```bash
    python main.py --pages <page_limit> --proxy <proxy_string>
    ```

    Replace `<page_limit>` with the number of pages you want to scrape (optional). If not provided, the default page limit is 5. Replace `<proxy_string>` with the proxy server address (optional).

3. When prompted, enter the authentication token to start the scraping process or want to provide different token then go to authentication.py file change the token

4. Wait for the scraping process to complete. Once finished, the tool will print a message indicating the number of products scraped and updated in the database.

