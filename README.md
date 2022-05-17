# gRPC SIGSEGV example

This repo reproduces a bug with gRPC / eventlet causing a SIGSEGV

## setup

```bash
git submodule update --init --recursive
```

Fill in account details in `app.py` (`DEVELOPER_TOKEN`, etc.)

```bash
python3 -m venv env
source env/bin/activate
pip install --upgrade pip setuptools
GRPC_PYTHON_CFLAGS='-g' pip install -r requirements.txt
```

## run

```bash
./app.py
# or run with gunicorn:
./run-with-gunicorn.sh
```

Go to `https://localhost:5000/` in your browser.
The flask server should crash with assertion failed.
If running with gunicorn, the worker will crash and restart.
If not, try again but it is fairly likely.

## Example Output

```
127.0.0.1 - - [05/May/2022 09:26:09] "GET / HTTP/1.1" 200 -
E0505 09:26:15.737590610  200702 activity.h:154]             assertion failed: g_current_activity_ == nullptr
Fatal Python error: Aborted

Current thread 0x00007f35f7446740 (most recent call first):
  File "/home/amohr/work/grpc-sigsegv/env/lib/python3.10/site-packages/grpc/_channel.py", line 595 in _consume_next_event
  File "/home/amohr/work/grpc-sigsegv/env/lib/python3.10/site-packages/grpc/_channel.py", line 607 in _next_response
  File "/home/amohr/work/grpc-sigsegv/env/lib/python3.10/site-packages/grpc/_channel.py", line 642 in _next
  File "/home/amohr/work/grpc-sigsegv/env/lib/python3.10/site-packages/grpc/_channel.py", line 426 in __next__
  File "/home/amohr/work/grpc-sigsegv/env/lib/python3.10/site-packages/google/ads/googleads/interceptors/response_wrappers.py", line 88 in __next__
  File "/home/amohr/work/grpc-sigsegv/env/lib/python3.10/site-packages/google/api_core/grpc_helpers.py", line 73 in __init__
  File "/home/amohr/work/grpc-sigsegv/env/lib/python3.10/site-packages/google/api_core/grpc_helpers.py", line 147 in error_remapped_callable
  File "/home/amohr/work/grpc-sigsegv/env/lib/python3.10/site-packages/google/api_core/gapic_v1/method.py", line 154 in __call__
  File "/home/amohr/work/grpc-sigsegv/env/lib/python3.10/site-packages/google/ads/googleads/v10/services/services/google_ads_service/client.py", line 3426 in search_stream
  File "/home/amohr/work/grpc-sigsegv/app.py", line 49 in test
  File "/home/amohr/work/grpc-sigsegv/env/lib/python3.10/site-packages/flask/app.py", line 1509 in dispatch_request
  File "/home/amohr/work/grpc-sigsegv/env/lib/python3.10/site-packages/flask/app.py", line 1523 in full_dispatch_request
  File "/home/amohr/work/grpc-sigsegv/env/lib/python3.10/site-packages/flask/app.py", line 2077 in wsgi_app
  File "/home/amohr/work/grpc-sigsegv/env/lib/python3.10/site-packages/flask/app.py", line 2095 in __call__
  File "/home/amohr/work/grpc-sigsegv/env/lib/python3.10/site-packages/werkzeug/debug/__init__.py", line 311 in debug_application
  File "/home/amohr/work/grpc-sigsegv/env/lib/python3.10/site-packages/werkzeug/serving.py", line 324 in execute
  File "/home/amohr/work/grpc-sigsegv/env/lib/python3.10/site-packages/werkzeug/serving.py", line 335 in run_wsgi
  File "/opt/python-dbg/lib/python3.10/http/server.py", line 415 in handle_one_request
  File "/opt/python-dbg/lib/python3.10/http/server.py", line 427 in handle
  File "/home/amohr/work/grpc-sigsegv/env/lib/python3.10/site-packages/werkzeug/serving.py", line 363 in handle
  File "/opt/python-dbg/lib/python3.10/socketserver.py", line 747 in __init__
  File "/opt/python-dbg/lib/python3.10/socketserver.py", line 360 in finish_request
  File "/opt/python-dbg/lib/python3.10/socketserver.py", line 683 in process_request_thread
  File "/opt/python-dbg/lib/python3.10/threading.py", line 946 in run
  File "/opt/python-dbg/lib/python3.10/threading.py", line 1009 in _bootstrap_inner
  File "/home/amohr/work/grpc-sigsegv/env/lib/python3.10/site-packages/eventlet/green/thread.py", line 64 in wrap_bootstrap_inner
  File "/opt/python-dbg/lib/python3.10/threading.py", line 966 in _bootstrap
  File "/home/amohr/work/grpc-sigsegv/env/lib/python3.10/site-packages/eventlet/green/thread.py", line 43 in __thread_body

Extension modules: greenlet._greenlet, __original_module__thread, __original_module_select, __original_module_time, markupsafe._speedups, grpc._cython.cygrpc, google.protobuf.pyext._message, yaml._yaml (total: 8)
```
