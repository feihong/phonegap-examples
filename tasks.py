import os
import os.path as op
from invoke import run, task


@task
def serve(projectname):
    js_dir = op.join(projectname, 'www/js')
    if not op.exists(js_dir):
        os.mkdir(js_dir)
    if not op.exists(op.join(js_dir, 'bundle.js')):
        build(projectname)
    run("""
    cd %(proj)s
    phonegap serve
    """ % {'proj': projectname})


@task
def build(projectname):
    run("""browserify --extension=.babel \
      %(proj)s/www/babel/app.babel \
      -o %(proj)s/www/js/bundle.js \
      -t [ babelify --extensions .babel --presets [ es2015 react ] ]
    """ % {'proj': projectname})


@task
def watch(projectname):
    run("""watchify --extension=.babel \
      %(proj)s/www/babel/app.babel \
      -o %(proj)s/www/js/bundle.js \
      -t [ babelify --extensions .babel --presets [ es2015 react ] ] \
      -v
    """ % {'proj': projectname})
