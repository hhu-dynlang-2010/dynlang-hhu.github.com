import datetime
import PyRSS2Gen

rss = PyRSS2Gen.RSS2(
    title = "Dynamische Programmiersprachen",
    link = "http://dynlang-hhu.github.com/",
    description = "",

    lastBuildDate = datetime.datetime.now(),

    items = [
       PyRSS2Gen.RSSItem(
         title = "New room for the lecture",
         pubDate = datetime.datetime(2011, 4, 15, 11, 42),
         description = 'Die Vorlesung findet mittwochs um 11-13 Uhr in Raum 25.12.02.33 statt.'),
       PyRSS2Gen.RSSItem(
         title = "Uploaded slides of lecture 1",
         pubDate = datetime.datetime(2010, 4, 14, 16, 23)),
       PyRSS2Gen.RSSItem(
         title = "Starting the web page",
         pubDate = datetime.datetime(2010, 4, 1, 11, 53)),
    ])

for item in rss.items:
    item.link = rss.link
    item.guid = PyRSS2Gen.Guid(str(item.pubDate), isPermaLink=False)

with open("lecture-rss.xml", "w") as f:
    rss.write_xml(f)
    f.close()

