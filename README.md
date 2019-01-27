# Mountain-Locator
This program locates and displays mountains of various countries and is written in python. The purpose of this project was to gain knowledge on web scrapping, as well as reading & writing files and databases.

## Steps
1. Scrape web for region coordinates and the coordinates of the mountains that pertain to that region.
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
*Web sources*: 
- [https://en.wikipedia.org/wiki/Main_Page](https://en.wikipedia.org/wiki/Category:Lists_of_mountains_by_country)
- [https://www.nationmaster.com/](https://www.nationmaster.com/country-info/stats/Geography/Geographic-coordinates)

# Status
__INCOMPLETE__

*Checklist:*
- [x] Re-structure project directory.
- [ ] Fix country coord. parse.
- [ ] re-code map coord. for the country coord.
- [ ] Rename database table.
- [ ] Re-structure code to imcorporate new country queries.

## What I learned

- Project management steps (initializing, planning, execution, performance control, and closing the project)
- How to read & write files 
- How to read & write databases in python
- How to web-scrape

