#!/usr/bin/env python

#      Copyright (C) 2013 Karsten Heymann
#      https://github.com/kasimon/autoembed
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with XBMC; see the file COPYING.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html

#  Usage as app:
#    ./autoembed.py https://twitter.com/kasimon/status/297346759519264768
#    <blockquote class="twitter-tweet" lang="de"><p>How to untar an atomic bomb: <a href="http://t.co/RQ1sIjF4" title="http://xkcd.com/1168/">xkcd.com/1168/</a></p>&mdash; Karsten Heymann (@kasimon) <a href="https://twitter.com/kasimon/status/297346759519264768">1. Februar 2013</a></blockquote>
#    <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
#
#  Usage as library:
#  >>> from autoembed import autoembed
#  >>> print autoembed('https://twitter.com/kasimon/status/297346759519264768')
#  <blockquote class="twitter-tweet" lang="de"><p>How to untar an atomic bomb: <a href="http://t.co/RQ1sIjF4" title="http://xkcd.com/1168/">xkcd.com/1168/</a></p>&mdash; Karsten Heymann (@kasimon) <a href="https://twitter.com/kasimon/status/297346759519264768">1. Februar 2013</a></blockquote>
#  <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

import json
import urllib2
from bs4 import BeautifulSoup

def autoembed(url):
    page = BeautifulSoup(urllib2.urlopen(url))
    embedurl = page.find(type="application/json+oembed")['href']
    result = None
    if embedurl:
        embed = json.load(urllib2.urlopen(embedurl))
        if embed['type']=='rich' and embed.has_key('html'):
            result=embed['html'].encode('utf-8')
    if not result:
        result = '<a href="%s">%s</a>' % (url,url)
    return result

if __name__=='__main__':
    import sys
    for url in sys.argv[1:]:
        embed = autoembed(url)
        print embed.encode('utf-8')
