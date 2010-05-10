# encoding: utf-8
import datetime
import PyRSS2Gen

rss = PyRSS2Gen.RSS2(
    title = "Dynamische Programmiersprachen",
    link = "http://dynlang-hhu.github.com/",
    description = "",

    lastBuildDate = datetime.datetime.now(),

    items = [
       PyRSS2Gen.RSSItem(
         title = "Uploaded missing file 'factory.life'",
         pubDate = datetime.datetime(2010, 5, 10, 11, 13)),
       PyRSS2Gen.RSSItem(
         title = "(Blatt 3) Hinweis: Für Aufgabe 2.1 genügt es einen festen Ausschnitt des Feldes in dem zu implementierenden Viewer darzustellen.",
         pubDate = datetime.datetime(2010, 5, 8, 12, 15)),
       PyRSS2Gen.RSSItem(
         title = "Uploaded material for lecture 4 (Ruby)",
         pubDate = datetime.datetime(2010, 5, 8, 12, 10)),
       PyRSS2Gen.RSSItem(
         title = "Exercises week 3",
         pubDate = datetime.datetime(2010, 5, 4, 9, 50)),
       PyRSS2Gen.RSSItem(
         title = "Uploaded material for lecture 3",
         pubDate = datetime.datetime(2010, 4, 28, 17, 50)),
       PyRSS2Gen.RSSItem(
         title = "Exercises week 2",
         pubDate = datetime.datetime(2010, 4, 27, 16, 1),
         description = 'The next set of exercises is available.'),
       PyRSS2Gen.RSSItem(
         title = "Uploaded Slides for lecture 2",
         pubDate = datetime.datetime(2010, 4, 21, 15, 3)),
       PyRSS2Gen.RSSItem(
         title = "Exercises week 1",
         pubDate = datetime.datetime(2010, 4, 21, 9, 1),
         description = 'The first set of exercises is available.'),
       PyRSS2Gen.RSSItem(
         title = "New room for the lecture",
         pubDate = datetime.datetime(2010, 4, 15, 11, 42),
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

