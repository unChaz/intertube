from gluon import *
    
class UserData(object):
    def __init__(self, user):
		"""Needs to get the user ID and store that as user. We can retrieve the other information using the id key"""
		self.db = current.db
		self.user = user
    
    def channelExists(self, channelName):
        """Will determine if the channel name given exists for the global user
            channelName must be a string."""
        for row in self.db(self.db.user_channels.owner_id==self.user).select():
            if row.channel_title.lower() == channelName.lower():
                return True
        return False
        
    def createChannel(self, channelName):
    ##Creates the channel if it does not exist.
    ##channelName must be a string.
		if not self.channelExists(channelName):
			self.db.user_channels.insert(owner_id=self.user, channel_title=channelName)
			
    def deleteChannel(self, channelName):
		"""deletes channel if it exists.
		channelName must be a string."""
		if self.channelExists(channelName):
			self.db(self.db.user_channels.channel_title.lower()==channelName.lower()).delete()
			
    def getChannels(self):
		"""Returns a list of channels for the given user"""
		channels = []
		for row in self.db(self.db.user_channels.owner_id==self.user).select():
			channels.append(row.channel_title)
		return channels

    def updateTags(self, channel, tags):
        """Will update the tags in the database. channel is a string representing the name of the channel. tags is a list of tuples."""
        for key, value in tags.items():
            if self.tagExists(channel, key):
                self.changeTagValue(channel, key, value)
            else:
                self.createTag(channel, key, value)
            
    def tagExists(self, channelName, tagName):
        """Checks to see if the tag is in the db. channelName is a string. tagName is a string."""
        for row in self.db(self.db.tags.owner_id==self.user and self.db.tags.channel==channelName).select():
            if row.tag_name.lower() == tagName.lower():
                return True
        return False
        
    def changeTagValue(self, channelName, tagName, tagValue):
        """Updates the value of the tag to the given value. channelName is a string. tagName is a string. tagValue is an int."""
        self.db(self.db.tags.owner_id==self.user and self.db.tags.channel==channelName and self.db.tags.tag_name==tagName).update(tag_value=int(tagValue))
        
    def createTag(self, channelName, tagName, tagValue):
        """Adds the tag to the db. channelName is a string. tagName is a string. tagValue is an int."""
        if not self.tagExists(channelName, tagName):
            self.db.tags.insert(owner_id=self.user, channel=channelName, tag_name=tagName, tag_value=int(tagValue))

    def getTags(self, channelName):
        tags = dict()
        for row in self.db(self.db.tags.owner_id==self.user).select():
            if row.channel == channelName:
                tags.update({row.tag_name: row.tag_value})
        return tags
