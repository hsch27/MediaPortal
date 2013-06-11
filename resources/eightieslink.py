﻿#	-*-	coding:	utf-8	-*-

from Plugins.Extensions.MediaPortal.resources.imports import *

class EightiesLink:
	def __init__(self, session):
		print "EightiesLink:"
		self.session = session
		self._callback = None
		self._errback = None
		self.baseurl = ''
		self.title = ''
		self.artist = ''
		self.album = ''
		
	def getLink(self, cb_play, cb_err, title, artist, album, url, token):
		self._callback = cb_play
		self._errback = cb_err
		self.title = title
		self.artist = artist
		self.album = album
		self.baseurl = "http://www."+token+"smusicvids.com/"
		
		getPage(url, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.getVid).addErrback(cb_err)

	def getVid(self, data):
		stream_url = re.findall('(/vid/.*?.flv)', data, re.S)
		if stream_url:
			stream_url = "%s%s" % (self.baseurl, stream_url[0])
			print stream_url
			self._callback(self.title, stream_url, self.album, self.artist)
		else:
			self._errback('stream_url not found!')			
