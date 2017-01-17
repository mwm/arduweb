# Arduweb - a web server for arduboy games

This git repository is meant to be pushed to the
[heroku](https://www.heroku.com/) SAS platform. If you're not familiar
with heroku, work through their tutorial before trying to use
this. It's based on the
[Flask framework](http://flask.pocoo.org/). You'll want to get
familiar with that as well.

You can push it as is to verify that it will correctly serve the file
& repository on it. Open / to get the list of files in the
repository. Check that you can download the arduboy file (a zip file)
and the ardumate version of the repo (a json file). If that works, you
should be set.

Update the `static` directory to include your hex files, screenshots
and banner images. Make sure to update git to match. Then edit
`games.py` to describe your repository and the games you've just
installed. Commit that, then push it to heroku to launch it.

The html version of a repo page is probably better done as a template,
but I'd rather write code than a template, so you get code. If someone
wants to submit a PR with a version that uses templates and modern
HTML, I'd probably merge that.

The arduboy output for 1010 crashes Arduboy manager, but works in
Arduboy game loader. This is still being investigated.
