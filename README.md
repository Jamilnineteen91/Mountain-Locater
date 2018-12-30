# Mountain-Locator
This program locates and displays mountains of various countries.
## Steps
1. Scrape wikipedia for region coordinates and the coordinates of the mountains that pertain to that region.
2. Save all coordinates to a new csv file.
3. Import data from csv file into a new database.
4. Retrieve data from the newly created database and display it on a map.

## Built with
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) - The web scrapper used.
- [CSV](https://docs.python.org/3/library/csv.html) - The CSV writer.
- [Requests](https://docs.python.org/3/library/re.html) - Web requester.
- [Sqlite](https://docs.python.org/2/library/sqlite3.html) - Database.
- [Folium](https://pypi.org/project/folium/) - Map generator.
- [regex](https://docs.python.org/3/library/re.html) - String parser for coordinates.

## Acknowledgments
Web source: [https://en.wikipedia.org/wiki/Main_Page](https://en.wikipedia.org/wiki/Main_Page)

# Status
__INCOMPLETE__
