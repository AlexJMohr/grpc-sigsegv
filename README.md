# gRPC SIGSEGV example

This repo reproduces a bug with gRPC / eventlet causing a SIGSEGV

## setup

Fill in account details in `app.py` (`DEVELOPER_TOKEN`, etc.)

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## run

```bash
./app.py
```

Go to `https://localhost:5000/` in your browser.
The flask server should crash with segmentation fault.
If not, try again but it is fairly likely.

## Example Output

```
Monkey Patching Eventlet
Enable faulthandler
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
Monkey Patching Eventlet
Enable faulthandler
 * Debugger is active!
 * Debugger PIN: 934-200-784
127.0.0.1 - - [16/Aug/2021 15:49:40] "GET / HTTP/1.1" 200 -
request 1 OK
127.0.0.1 - - [16/Aug/2021 15:49:42] "GET /test?i=1 HTTP/1.1" 200 -
Fatal Python error: Segmentation fault

Current thread 0x00007f50ba466740 (most recent call first):
  File "/home/amohr/tmp/grpc-bug/env/lib/python3.8/site-packages/grpc/_channel.py", line 595 in _consume_next_event
  File "/home/amohr/tmp/grpc-bug/env/lib/python3.8/site-packages/grpc/_channel.py", line 607 in _next_response
  File "/home/amohr/tmp/grpc-bug/env/lib/python3.8/site-packages/grpc/_channel.py", line 642 in _next
  File "/home/amohr/tmp/grpc-bug/env/lib/python3.8/site-packages/grpc/_channel.py", line 426 in __next__
  File "/home/amohr/tmp/grpc-bug/env/lib/python3.8/site-packages/google/ads/googleads/interceptors/exception_interceptor.py", line 92 in __next__
  File "/home/amohr/tmp/grpc-bug/env/lib/python3.8/site-packages/google/api_core/grpc_helpers.py", line 83 in __init__
  File "/home/amohr/tmp/grpc-bug/env/lib/python3.8/site-packages/google/api_core/grpc_helpers.py", line 160 in error_remapped_callable
  File "/home/amohr/tmp/grpc-bug/env/lib/python3.8/site-packages/google/api_core/gapic_v1/method.py", line 145 in __call__
  File "/home/amohr/tmp/grpc-bug/env/lib/python3.8/site-packages/google/ads/googleads/v8/services/services/google_ads_service/client.py", line 2859 in search_stream
  File "/home/amohr/tmp/grpc-bug/app.py", line 48 in test
  File "/home/amohr/tmp/grpc-bug/env/lib/python3.8/site-packages/flask/app.py", line 1499 in dispatch_request
  File "/home/amohr/tmp/grpc-bug/env/lib/python3.8/site-packages/flask/app.py", line 1513 in full_dispatch_request
  File "/home/amohr/tmp/grpc-bug/env/lib/python3.8/site-packages/flask/app.py", line 2070 in wsgi_app
  File "/home/amohr/tmp/grpc-bug/env/lib/python3.8/site-packages/flask/app.py", line 2088 in __call__
  File "/home/amohr/tmp/grpc-bug/env/lib/python3.8/site-packages/werkzeug/debug/__init__.py", line 309 in debug_application
  File "/home/amohr/tmp/grpc-bug/env/lib/python3.8/site-packages/werkzeug/serving.py", line 310 in execute
  File "/home/amohr/tmp/grpc-bug/env/lib/python3.8/site-packages/werkzeug/serving.py", line 319 in run_wsgi
  File "/home/amohr/tmp/grpc-bug/env/lib/python3.8/site-packages/werkzeug/serving.py", line 374 in handle_one_request
  File "/usr/lib/python3.8/http/server.py", line 427 in handle
  File "/home/amohr/tmp/grpc-bug/env/lib/python3.8/site-packages/werkzeug/serving.py", line 342 in handle
  File "/usr/lib/python3.8/socketserver.py", line 747 in __init__
  File "/usr/lib/python3.8/socketserver.py", line 360 in finish_request
  File "/usr/lib/python3.8/socketserver.py", line 683 in process_request_thread
  File "/usr/lib/python3.8/threading.py", line 870 in run
  File "/usr/lib/python3.8/threading.py", line 932 in _bootstrap_inner
  File "/home/amohr/tmp/grpc-bug/env/lib/python3.8/site-packages/eventlet/green/thread.py", line 63 in wrap_bootstrap_inner
  File "/usr/lib/python3.8/threading.py", line 890 in _bootstrap
  File "/home/amohr/tmp/grpc-bug/env/lib/python3.8/site-packages/eventlet/green/thread.py", line 42 in __thread_body
```