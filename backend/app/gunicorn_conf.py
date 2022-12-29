bind = '0.0.0.0:80'
backlog = 2048

workers = 1
worker_class = 'eventlet'
worker_connections = 1000
timeout = 30
keepalive = 1


spew = False

daemon = False
raw_env = []
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None


errorlog = '-'
loglevel = 'debug'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

enable_stdio_inheritance = True

proc_name = None