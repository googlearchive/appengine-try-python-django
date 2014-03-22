## Django Framework Skeleton for Google App Engine

A skeleton for building Python applications on Google App Engine with the
[Django framework](https://www.djangoproject.com/), using [djangoappengine](http://djangoappengine.readthedocs.org/en/latest/).

This skeleton is a bare-bones "hello world" application.

See our other [Google Cloud Platform github
repos](https://github.com/GoogleCloudPlatform) for sample applications and
scaffolding for other Python frameworks and use cases.

## Run Locally
1. Install the [App Engine Python SDK](https://developers.google.com/appengine/downloads).
See the README file for directions. You'll need Python 2.7, [pip 1.4 or later](http://www.pip-installer.org/en/latest/installing.html), and [mercurial](http://mercurial.selenic.com/) (`hg`) installed too.
If you're missing `hg` you can install it with `pip install mercurial` once you have `pip` installed.

2. Clone this repo with:

   ```
   git clone https://github.com/GoogleCloudPlatform/appengine-django-skeleton.git
   ```
3. Install dependencies in the project's directory - App Engine
   can only import libraries from inside your project directory.
   ```
   cd appengine-django-skeleton

   ./build.sh
   ```
4. Run this project locally from the command line:

   ```
   ./manage.py runserver
   ```

See the output in your browser at [http://localhost:8000](http://localhost:8000)

This sample uses `manage.py` to call the development server. See [the other management commands](http://djangoappengine.readthedocs.org/en/latest/management.html)
for other options.

## Deploy
To deploy the application:

1. Use the [Admin Console](https://appengine.google.com) to create an app.
1. Replace `your-app-id` in `app.yaml` with the app id from the previous step.
1. [Deploy the
   application](https://developers.google.com/appengine/docs/python/tools/uploadinganapp) with:
   `appcfg.py --oauth2 update [projectDirectory]` or use the App Engine Launcher.
1. Congratulations! Your application is now live at `your-app-id`.appspot.com.

## Next Steps
This skeleton includes TODO markers you can search for to determine some of the
basic areas you will want to customize.

This is a very simple Django application. Check out the
[Django site](https://www.djangoproject.com/) for ideas on how to extend the
application.

### Datastore
`djangoappengine` provides built-in support for App Engine's NoSQL datastore.
See the documentation for [supported and unsupported features](http://djangoappengine.readthedocs.org/en/latest/db.html)
from the core Django library.

### Installing Libraries
See the [third-party
libraries](https://developers.google.com/appengine/docs/python/tools/libraries27)
page for libraries that are already included in the SDK. To include SDK
libraries, add them in your app.yaml file. Other than libraries included in
the SDK, only pure python libraries may be added to an App Engine project.

### Feedback
Star this repo if you found it useful. Use the github issue tracker to give
feedback on this repo and to ask for scaffolds for other use cases.

## Contributing changes
See [CONTRIB.md](CONTRIB.md)

## Licensing
See [LICENSE](LICENSE)
