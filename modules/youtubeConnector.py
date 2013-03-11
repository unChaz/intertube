from gluon import *
from video import *

class YouTubeConnector(object):
	def __init__(self):
		self.gdata = current.gdata
		self.yt_service = self.gdata.youtube.service.YouTubeService()
		# Turn on HTTPS/SSL access.
		# Note: SSL is not available at this time for uploads.
		self.yt_service.ssl = True
		self.yt_service.developer_key = 'AI39si5mIClz6YRx724Qalfj1qOT2b28Rkok_ZT2JBSUeArg0Gx3Kl5tcPFlF__ywVF1lKbzl3T9O5OkFFdQlbKETnTO8dpzQg'
		self.yt_service.client_id = '624211066611.apps.googleusercontent.com'

	def buildList(self, feed):
		"""Builds a list of videos from a given YouTubeVideoFeed"""
		list = []
		for entry in feed.entry:
			if entry.GetSwfUrl():
				swf_url = entry.GetSwfUrl()
				title = str(entry.title.text)
				description = self.parseDescription(str(entry.media.description))
				if entry.rating:
					rating = float(entry.rating.average)
				else:
					rating = 0
	
				keywords = str(entry.media.keywords.text)
				duration = float(entry.media.duration.seconds)
				#views = int(entry.statistics.view_count)
				#TODO
				views = 0
				id = self.parseID(entry.id)
				video = Video(id, title, description, rating, keywords, views, duration)
				video.setTags()
				list.append(video)

		return list

	def searchByKeyword(self, search_terms):
		"""Returns a feed of videos."""
		#  http://gdata-python-client.googlecode.com/hg/pydocs/gdata.youtube.html#YouTubeVideoFeed
		yt_service = self.gdata.youtube.service.YouTubeService(additional_headers={'GData-Version': '1'})
		query = self.gdata.youtube.service.YouTubeVideoQuery()
		query.vq = search_terms
		query.racy = 'exclude'
		query.orderby = "relevance"
		query.max_results = 50
		feed = yt_service.YouTubeQuery(query)
		return self.buildList(feed)


	def parseID(self, longID):
		"""Pulls the ID out of the ID of an entry."""
		split = str(longID).split("/")
		return split[len(split) - 2][:-1]

	def parseDescription(self, formattedDesc):
		"""Pulls the Description out of the Description HTML of an entry."""
		return formattedDesc[formattedDesc.find('type="plain">')+13:formattedDesc.find("</ns0:description>")]
