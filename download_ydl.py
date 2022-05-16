from __future__ import unicode_literals


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'Musik/%(title)s-%(id)s.%(ext)s',
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

