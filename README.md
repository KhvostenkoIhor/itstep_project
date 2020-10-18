# IT Step general project

# 0. Install common tools
```bash
# Debian core Linux
apt install -y python3.8 python3-dev
pip install pipenv
pipenv check    # check pipenv for correct work
```

# 1. Startup project

## Set .env file and update variables:
```bash
cd it_step_project
cp .env.example .env

# Django secret key: https://djecrety.ir
```
## 2. Setup environment
```bash
pipenv install
pipenv shell
```