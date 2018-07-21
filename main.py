#!/usr/bin/env python3

# educated.me

import feedparser
import html2text
import time
import sys

# d = feedparser.parse('https://dou.ua/calendar/feed/%D0%B2%D1%81%D0%B5%20%D1%82%D0%B5%D0%BC%D1%8B/%D0%9A%D0%B8%D0%B5%D0%B2')
d = feedparser.parse('http://www.reddit.com/r/python/.rss')

# print(d.feed.title)
for e in d.entries:
    print(e.title)
    # print ( ' - ',html2text.html2text(e.description))