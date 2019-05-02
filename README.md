Python North West Website
=========================

                     \\\\
          ,-.   ,-.  \\\\
        .'   `.' O `. \\\
      ,'       `.    `.`\
      :    `.    `    ; \
       `.    `.     ,' .\
      ,:::._,:::._,:::. \
      ::O:::::::::::::; \
       `::::::;:::::;' .\
    \\\\.`::;' `::;' .\\\
    \\\\\\....\\....\\\\\

A website for _Python North West_, a usergroup for the Python programming
language based in Manchester, UK. We meet on the _third Thursday_ of every 
month, _7pm_ at _The Federation_.


Installation
------------

To set up the project for development, it is recommended that you create
a [virtual environment] in which to work. 

The project requires:

* _Python 3.6_
* _Django 2.x.x_ and the other dependencies as listed in the `requirements.txt` 
  file (`pip install -r requirements.txt`)

By default the project is configured for _production_, minus sensitive config
which is not committed to version control. For your development environment
you will need to:

* Create a `settings_secret.py` file in the `pynwproj` directory (see 
  `settings_secret.py.template` for an example)
* Set the `DJANGO_DEVELOPMENT` environment variable, which will cause the 
  settings in `settings_dev.py` to be imported and override those in the
  production settings file.

[virtual environment]: https://virtualenv.pypa.io/en/stable/
