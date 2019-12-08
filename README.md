[![Netlify Status](https://api.netlify.com/api/v1/badges/25254e78-cbaf-4cde-800a-41c1e7553351/deploy-status)](https://app.netlify.com/sites/lunik/deploys)

# lunik
Build files for the Lunik film club [website](http://lunik.it), substantially a Python script which
generates a single page static website with the planning of the films, configurable in the
`films.yaml` file.  The file `config.py` contains some other customizable variables, like the movie
images size (the images are automatically resized) or the footer text.

The website is automatically deployed by [netlify](https://www.netlify.com) at every commit, however
is possible to manually build it executing the `lunik.py` script.  Note that the script requires the
environment variable `GMAPS_KEY` set, the actual value is set inside the control panel of netlify.

