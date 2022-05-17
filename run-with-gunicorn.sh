#!/bin/bash

# gunicorn automatically monkey patches
gunicorn -k gevent -w 1 -b localhost:5000 app:app
