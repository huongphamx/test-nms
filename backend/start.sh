#! /usr/bin/env sh
set -e

. /app/pre_start.sh

exec uvicorn app.main:app --host=0.0.0.0
