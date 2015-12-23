import os
import os.path as op
from invoke import run, task


@task
def serve(projectname):
    js_dir = op.join(projectname, 'www/js')
    babel_file = op.join(projectname, 'www/babel/app.babel')
    if not op.exists(js_dir):
        os.mkdir(js_dir)
    if op.exists(babel_file) and not op.exists(op.join(js_dir, 'bundle.js')):
        build(projectname)
    run("""
    cd %(proj)s
    phonegap serve
    """ % {'proj': projectname})


@task
def build(projectname):
    run("""browserify --debug --extension=.babel \
      %(proj)s/www/babel/app.babel \
      -o %(proj)s/www/js/bundle.js \
      -t [ babelify --extensions .babel --presets [ es2015 react ] ]
    """ % {'proj': projectname})


@task
def watch(projectname):
    run("""watchify --debug --extension=.babel \
      %(proj)s/www/babel/app.babel \
      -o %(proj)s/www/js/bundle.js \
      -t [ babelify --extensions .babel --presets [ es2015 react ] ] \
      -v
    """ % {'proj': projectname})
