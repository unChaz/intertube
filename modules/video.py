import re

class Video(object):
	def __init__(self, id, title, description, rating, keywords, views, duration):
		self.id = id
		self.title = title
		self.description = description
		self.rating = rating
		self.keywords = keywords
		self.views = views
		self.duration = duration

	def setTags(self):
		tags = []
		tags.append(self.title)
		tags += self.title.split()
		if self.keywords != 'none':
			tags += self.keywords.split(", ")
		pattern = re.compile(('the|a|in|on|for|by|[\.0-9]|[-]'), re.IGNORECASE) 
		for tag in tags:
			if pattern.match(tag):
				tags.remove(tag)
		self.tags = tags

	def getTags(self):
		tags = []
		tags += self.title.split()
		if self.keywords != 'None':
			tags += self.keywords.split(", ")
		pattern = re.compile(('the|a|in|on|for|by|[\.0-9]|[-]'), re.IGNORECASE) 
		for tag in tags:
			if pattern.match(tag):
				tags.remove(tag)
		return tags