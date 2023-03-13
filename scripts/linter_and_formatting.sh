#!/usr/bin/env bash

cd "$(dirname "${BASH_SOURCE[0]}")"/..

echo "sorting imports"
echo "-----------------------"
poetry run isort src/ tests/

echo "autoformatting code"
echo "-----------------------"
poetry run black src/ tests/

echo "run flake"
echo "-----------------------"
poetry run flake8 src/ tests/

echo "running mypy"
echo "-----------------------"

poetry run python -m mypy src/ tests/
