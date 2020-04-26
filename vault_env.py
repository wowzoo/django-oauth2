import urllib.request
import json

from pathlib import Path


def get_env(token, url, env_path):
    # set header
    headers = {"X-Vault-Token": token}

    # set request
    request = urllib.request.Request(url, headers=headers)

    # get env
    with urllib.request.urlopen(request) as response:
        raw_data = response.read()
        encoding = response.info().get_content_charset('utf8')
        data = json.loads(raw_data.decode(encoding))

        secrets = data['data']['data']
        with open(env_path, 'w') as f:
            for k, v in secrets.items():
                f.write(f"{k}={v}\n")


def get_token(token):
    url = "http://localhost:8200/v1/auth/github/login"
    data = {
        "token": token
    }

    request = urllib.request.Request(url, data=bytes(json.dumps(data), 'utf-8'))
    with urllib.request.urlopen(request) as response:
        raw_data = response.read()
        encoding = response.info().get_content_charset('utf8')
        data = json.loads(raw_data.decode(encoding))

        client_token = data['auth']['client_token']

    return client_token


if __name__ == "__main__":
    # create env_files directory
    dir_path = Path("env_files")
    dir_path.mkdir(exist_ok=True)

    # get token
    github_token = "git_personal_access_token"
    token = get_token(github_token)

    # get postgres env
    url = "http://localhost:8200/v1/app/data/postgres"
    postgres_env_path = dir_path / "postgres.env"
    get_env(token, url, postgres_env_path)

    # get django common env
    url = "http://localhost:8200/v1/app/data/common/django"
    common_django_env_path = dir_path / "common-django.env"
    get_env(token, url, common_django_env_path)



