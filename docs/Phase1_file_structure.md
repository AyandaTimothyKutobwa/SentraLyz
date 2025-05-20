| Path                                  | What it’s for                           |
| ------------------------------------- | --------------------------------------- |
| `ingestion/filebeat/filebeat.yml`     | For configuring log shippers            |
| `ingestion/syslog/syslog_receiver.py` | Your own Python syslog listener         |
| `normalization/apache_parser.py`      | A parser script for Apache logs         |
| `normalization/normalize_utils.py`    | Common parsing functions                |
| `configs/log_sources.yml`             | Config file listing supported log types |
| `tests/test_parsers.py`               | Unit test file for parsers              |
