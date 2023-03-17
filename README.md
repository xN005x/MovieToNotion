# MovieToNotion :movie_camera: ![GitHub](https://img.shields.io/github/license/uMatt/MovieToNotion?color=%20)

This is a simple Python script that retrieves data from the TMDB API and sends it to a Notion database.

## Installation

1. Clone the repository: `git clone https://github.com/uMatt/MovieToNotion.git`
2. Navigate to the directory: `cd MovieToNotion`
3. Install dependencies: `pip install -r requirements.txt`
4. Obtain your TMDB API key :
   - Go to [https://www.themoviedb.org/settings/api](https://www.themoviedb.org/settings/api) and sign up for an account or log in.
   - Click on "API" in the left-hand menu and then click on "Create" to create a new API key.
   - Copy your API key.
5. Obtain your Notion API key:
   - Go to [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations) and sign up for an account or log in.
   - Create a New Integration
   - Copy your API key.
6. Obtain the ID of the Notion database that you want to add data to:
   - Open the Notion database in your browser.
   - Copy the database ID from the URL. The ID is in the link `https://www.notion.so/<username>/<DATABASE_ID>?`.
7. Create a file named `.env` in the root directory of the project and add the following lines:
    ```
    TMDB_API_KEY=<your-tmdb-api-key>
    NOTION_API_KEY=<your-notion-api-key>
    NOTION_DATABASE_ID=<your-notion-database-id>
    LANGUAGE=<your_language>
    ```
    Replace `<your-tmdb-api-key>`, `<your-notion-api-key>`, `<your-notion-database-id>`, and `<your_language>` with your actual API keys and database ID.
7. Run the script: `python MovieToNotion.py`

## Usage

This script retrieves data from the TMDB API and adds it to a Notion database. You can modify the `MovieToNotion.py` file to retrieve different types of data or to add data to a different Notion database.

## Contributing

If you have any suggestions for improving this script, please submit a pull request or open an issue.

## License

This project is licensed under the  GNU GPLv3 License - see the [LICENSE](LICENSE) file for details.
