from invoke import run, task


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
