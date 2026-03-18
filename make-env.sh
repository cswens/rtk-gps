#!/bin/bash

set -e

ENV_PATH=./.venv

if [ ! -d "$ENV_PATH" ]; then
    echo "Creating virtual environment at $ENV_PATH"
    python -m venv $ENV_PATH

    echo "Activating virtual environment and installing dependencies"
    source $ENV_PATH/bin/activate

    pip install --upgrade pip==22.0.2
    pip install -r requirements.txt
else
    echo "Virtual environment already exists at $ENV_PATH. Activating it."
    source $ENV_PATH/bin/activate
fi

