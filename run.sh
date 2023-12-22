check_python_version() {
    PYTHON_VERSION=$(python3 --version | cut -d " " -f2)
    REQUIRED_VERSION="3.10"

    if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" = "$REQUIRED_VERSION" ]; then
        return 0
    else
        return 1
    fi
}

if ! command -v python3 &> /dev/null || ! check_python_version; then
    echo "Python 3 is not installed or does not meet the minimum version requirement of 3.10."
    echo "Installing Python 3.10..."
    sudo apt update
    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install python3.10
    exit 1
fi

if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

source .venv/bin/activate

pip3 freeze | grep -qxF 'colored' || pip3 install colored
pip3 freeze | grep -qxF 'readchar' || pip3 install readchar

python3 main.py

deactivate