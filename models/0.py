from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'InterTube'
settings.subtitle = 'Endless Video Streaming'
settings.author = 'Lewis Christmas, Charles Ferguson, Justin Walker'
settings.author_email = 'you@example.com'
settings.keywords = 'Youtube, pandora, videos'
settings.description = ''
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = 'b31b0a9e-034d-4183-a206-d2dc9db14f32'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = ['datatable', 'dropdown', 'comments', 'mmodal', 'jqmobile', 'rating', 'utils', 'translate']
