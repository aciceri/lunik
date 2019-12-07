# lunik
Build files for the Lunik film club [website](http://lunik.it), substantially a Python script which
generates a single page static website with the planning of the films, configurable in the
`config.py`.

To correctly builds, it's required a file called `credentials.py`, which ignored by git because of
`.gitignore`. It must contains the following Python variables:

```
aws_access_key_id = ''
aws_secret_access_key = ''
aws_bucket_name = ''
gmaps_key = ''
```
