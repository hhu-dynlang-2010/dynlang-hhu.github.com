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
         title = "Uploaded Solution for exercices week 10 to documentation repository",
         pubDate = datetime.datetime(2010, 7, 28, 11, 00)),
       PyRSS2Gen.RSSItem(
         title = "Uploaded Material for Lecture 12",
         pubDate = datetime.datetime(2010, 7, 15, 14, 12)),
       PyRSS2Gen.RSSItem(
         title = "Uploaded Material for Lecture 11",
         pubDate = datetime.datetime(2010, 7, 8, 11, 00)),
       PyRSS2Gen.RSSItem(
         title = "Uploaded Solution for exercices week 9 to documentation repository",
         pubDate = datetime.datetime(2010, 7, 8, 11, 00)),
       PyRSS2Gen.RSSItem(
         title = "Exercises week 10",
         pubDate = datetime.datetime(2010, 6, 30, 9, 00)),
       PyRSS2Gen.RSSItem(
         title = "Exercises week 9",
         pubDate = datetime.datetime(2010, 6, 22, 21, 00)),
       PyRSS2Gen.RSSItem(
         title = "Uploaded Material for Lecture 10",
         pubDate = datetime.datetime(2010, 6, 17, 13, 10)),
       PyRSS2Gen.RSSItem(
         title = "Uploaded Solution for exercices week 7 to documentation repository",
         pubDate = datetime.datetime(2010, 6, 10, 11, 45)),
       PyRSS2Gen.RSSItem(
         title = "Uploaded Material for Lecture 9",
         pubDate = datetime.datetime(2010, 6, 10, 11, 45)),
       PyRSS2Gen.RSSItem(
         title = "Fixed files for Exercises (2nd time)",
         pubDate = datetime.datetime(2010, 6, 7, 11, 9)),
       PyRSS2Gen.RSSItem(
         title = "Uploaded Material for Lecture 8",
         pubDate = datetime.datetime(2010, 6, 2, 15, 45)),
       PyRSS2Gen.RSSItem(
         title = "Fixed files for Exercises",
         pubDate = datetime.datetime(2010, 6, 2, 15, 30)),
       PyRSS2Gen.RSSItem(
         title = "Exercises week 7",
         pubDate = datetime.datetime(2010, 6, 1, 23, 16)),
       PyRSS2Gen.RSSItem(
         title = "Uploaded new version of blatt6.py",
         pubDate = datetime.datetime(2010, 5, 26, 17, 31)),
       PyRSS2Gen.RSSItem(
         title = "Uploaded Material for Lecture 7",
         pubDate = datetime.datetime(2010, 5, 26, 17, 30)),
       PyRSS2Gen.RSSItem(
         title = "Exercises week 6",
         pubDate = datetime.datetime(2010, 5, 25, 18, 30)),
       PyRSS2Gen.RSSItem(
         title = "Uploaded Material for Lecture 6",
         pubDate = datetime.datetime(2010, 5, 19, 15, 8)),
       PyRSS2Gen.RSSItem(
         title = "Exercises week 5",
         pubDate = datetime.datetime(2010, 5, 18, 17, 50)),
       PyRSS2Gen.RSSItem(
         title = "Uploaded Material for Lecture 5",
         pubDate = datetime.datetime(2010, 5, 17, 14, 0),
         description = "sorry for the delay"),
       PyRSS2Gen.RSSItem(
         title = "Exercises week 4",
         pubDate = datetime.datetime(2010, 5, 11, 9, 50)),
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

