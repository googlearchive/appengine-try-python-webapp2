## Python webapp2 Skeleton for Google App Engine

A skeleton for building Python applications on Google App Engine with the
[webapp2 framework](https://code.google.com/p/webapp-improved/).

See our other [Google Cloud Platform github
repos](https://github.com/GoogleCloudPlatform) for sample applications and
scaffolding for other python frameworks and use cases.

## Run Locally
1. Install the [App Engine Python SDK](https://cloud.google.com/appengine/downloads).
See the README file for directions. You'll need python 2.7 and [pip 1.4 or later](http://www.pip-installer.org/en/latest/installing.html) installed too.

2. Clone this repo with

   ```
   git clone https://github.com/GoogleCloudPlatform/appengine-python-webapp2-skeleton.git
3. Run this project locally from the command line:

   ```
   dev_appserver.py .
   ```

Visit the application [http://localhost:8080](http://localhost:8080)

See [the development server documentation](https://cloud.google.com/appengine/docs/python/tools/devserver)
for options when running dev_appserver.

## Deploy
To deploy the application:

1. Use the Cloud Developer Console (console.developer.google.com)  to create a project/app id. (App id and project id are identical)
1. Use the [Admin Console](https://appengine.google.com) to view data, queues, and other AppEngine specific administration tasks.
1. [Deploy the
   application](https://cloud.google.com/appengine/docs/python/tools/uploadinganapp) with

   ```
   appcfg.py -A <your-project-id> --oauth2 update .
   ```
1. Congratulations!  Your application is now live at your-app-id.appspot.com

### Data Persistance Options
To add persistence to your models, use
[NDB](https://cloud.google.com/appengine/docs/python/ndb/) for
scale.  Consider
[CloudSQL](https://cloud.google.com/appengine/docs/python/cloud-sql/)
if you need a relational database.

### Installing Libraries
See the [Third party
libraries](https://cloud.google.com/appengine/docs/python/tools/libraries27)
page for libraries that are already included in the SDK.  To include SDK
libraries, add them in your app.yaml file. Other than libraries included in
the SDK, only pure python libraries may be added to an App Engine project. If you
would like more flexibility and customization over your project while still keeping
the powerful automatic infrastructure management of AppEngine, consider [Managed VMs]
 (https://cloud.google.com/appengine/docs/managed-vms/).

### Feedback
Star this repo if you found it useful. Use the github issue tracker to give
feedback on this repo.

## Contributing changes
See [CONTRIBUTING.md](CONTRIBUTING.md)

## Licensing
See [LICENSE](LICENSE)

## Author
Bill Prin, Takashi Matsuo
