#!/usr/bin/env bash
kill -9 `ps aux | grep gunicorn | grep penny | awk '{ print $2 }'`