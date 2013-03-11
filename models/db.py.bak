# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'


from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db)
crud, service, plugins = Crud(db), Service(), PluginManager()

from gluon import current
current.auth = auth

## on logout clears the session
auth.settings.logout_onlogout = lambda user: session.clear()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

##Simplified database code
current_user_id = 0
if auth.is_logged_in():
    current_user_id = auth.user.id

db.define_table('user_channels',
            Field('owner_id', db.auth_user, default=current_user_id, writable = False),
            Field('channel_title', 'string'))
            
db.define_table('tags',
            Field('channel', 'string'),
            Field('owner_id', db.auth_user, default=current_user_id, writable=False),
            Field('tag_name', 'string'),
            Field('tag_value', 'integer'))
            
db.user_channels.channel_title.requires = IS_NOT_EMPTY()
db.tags.channel.requires = IS_NOT_EMPTY()
db.tags.channel.requires = IS_IN_DB(db, 'channel.channel_title')
db.tags.tag_name.requires = IS_NOT_EMPTY()
db.tags.tag_value.requires = IS_NOT_EMPTY()

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.rpx_account import use_janrain
use_janrain(auth, filename='private/janrain.key')

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)

mail.settings.server = settings.email_server
mail.settings.sender = settings.email_sender
mail.settings.login = settings.email_login
