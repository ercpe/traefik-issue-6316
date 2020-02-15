Code to reproduce https://github.com/containous/traefik/issues/6316

1. Start traefik with the provided toml configuration: `traefik --configfile traefik.toml`
1. Run the dummy server: `python3 dummyserver.py`
1. Execute: `curl -H 'X-Request-Header-With-Quotes: this is a "test"'  -v http://localhost:8081`


This produces a broken JSON document in `/tmp/access.log`:

```json
{
  "ClientAddr": "127.0.0.1:36554",
  "ClientHost": "127.0.0.1",
  "ClientPort": "36554",
  "ClientUsername": "-",
  "DownstreamContentSize": 0,
  "DownstreamStatus": 200,
  "Duration": 973552,
  "OriginContentSize": 0,
  "OriginDuration": 947995,
  "OriginStatus": 200,
  "Overhead": 25557,
  "RequestAddr": "localhost:8081",
  "RequestContentSize": 0,
  "RequestCount": 2,
  "RequestHost": "localhost",
  "RequestMethod": "GET",
  "RequestPath": "/",
  "RequestPort": "8081",
  "RequestProtocol": "HTTP/1.1",
  "RetryAttempts": 0,
  "RouterName": "Router-1@file",
  "ServiceAddr": "127.0.0.1:8000",
  "ServiceName": "my-service@file",
  "ServiceURL": {
    "Scheme": "http",
    "Opaque": "",
    "User": null,
    "Host": "127.0.0.1:8000",
    "Path": "/",
    "RawPath": "",
    "ForceQuery": false,
    "RawQuery": "",
    "Fragment": ""
  },
  "StartLocal": "2020-02-15T05:19:39.355892324+01:00",
  "StartUTC": "2020-02-15T04:19:39.355892324Z",
  "downstream_Content-Type": "text/plain",
  "downstream_Date": "Sat, 15 Feb 2020 04:19:39 GMT",
  "downstream_Server": "BaseHTTP/0.6 Python/3.7.5",
  "downstream_X-Response-Header-With-Quotes":"this is a "test"",
  "entryPointName": "web",
  "level": "info",
  "msg": "",
  "origin_Content-Type": "text/plain",
  "origin_Date": "Sat, 15 Feb 2020 04:19:39 GMT",
  "origin_Server": "BaseHTTP/0.6 Python/3.7.5",
  "origin_X-Response-Header-With-Quotes":"this is a "test"",
  "request_Accept": "*/*",
  "request_User-Agent": "curl/7.65.3",
  "request_X-Forwarded-Host": "localhost:8081",
  "request_X-Forwarded-Port": "8081",
  "request_X-Forwarded-Proto": "http",
  "request_X-Forwarded-Server": "minibox",
  "request_X-Real-Ip": "127.0.0.1",
  "request_X-Request-Header-With-Quotes":"this is a "test"",
  "time": "2020-02-15T05:19:39+01:00"
}


```
