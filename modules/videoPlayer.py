class VideoPlayer(object):
	"""TODO"""
	"""Implement listener to know when the video is done."""
	def __init__(self):
		self.channel = None
		self.preferences = None
		self.video = None

	def nowPlaying(self):
		return True

	def setChannel(self, channel):
		self.channel = channel		

	def playNextVideo(self):
		return self.channel.getVideo()
		"""Play the video"""

	def videoLiked(self):
		"""video object was liked"""
		channel.updateTags(self.nowPlaying.getTags(),1)
		session.flash = 'videoLiked'

	def videoDisLiked(self):
		"""video object was liked"""
		channel.updateTags(self.nowPlaying.getTags(),-1)
		session.flash = 'videoDisLiked'
		playNextVideo()

	def videoViewed(self):
		"""video object was liked"""
		channel.updateTags(self.nowPlaying.getTags(),0)
		session.flash = 'NextVideo'
		playNextVideo()
