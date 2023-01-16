# Deploying a Flask App using the Encrypted Tux Repository

The Encrypted Tux repository on GitHub (https://github.com/Anshieee/Encrypted-Tux) provides a guide for achieving complete anonymity and privacy online using Linux. One of the components of this guide is a Flask application that demonstrates how to encrypt and secure your internet connection. This wiki page will provide instructions on how to deploy the Flask app on a server.

## Prerequisites

Before deploying the Flask app, you will need the following:

 - A server with Linux installed (we recommend using Ubuntu)
 - Python 3 and pip installed on the server
 - A virtual environment set up on the server (we recommend using virtualenv)

## Deployment Steps

1. Clone the Encrypted Tux repository on GitHub to your server:

```bash
git clone https://github.com/Anshieee/Encrypted-Tux.git
```

2. Create and activate a virtual environment:

```bash
virtualenv venv
source venv/bin/activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Set the environment variable for the Flask app:

```bash
export FLASK_APP=app.py
```

5. Run the Flask app:
```bash
flask run
```

6. The app should now be accessible on **http://localhost:5000**
7. To run the app on a production server, you can use a web server gateway interface (WSGI) server such as Gunicorn or uWSGI.

## Conclusion

By following the above steps, you should be able to deploy the Flask app from the Encrypted Tux repository on a server. Keep in mind that this guide is intended as a starting point, and your specific requirements may vary.
