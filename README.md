# Copick Server

A server for [copick](https://github.com/kephale/copick) projects.

## Installation

```bash
pip install .
```

## Usage

### Launch a server

#### Using a config file

```bash
python -m copick_server.server serve --config path/to/copick_config.json --cors "*" --port 8000
```

#### Using dataset IDs from CZ cryoET Data Portal

```bash
python -m copick_server.server serve --dataset-ids 10440 --cors "*" --port 8017
```

You can use multiple dataset IDs by repeating the option:

```bash
python -m copick_server.server serve --dataset-ids 10440 --dataset-ids 10441 --cors "*" --port 8017
```

#### Using uv run

With config file:
```bash
uv run copick_server/server.py serve --config ~/Data/copick/full_ml_challenge_czcdp.json --cors "*" --port 8017
```

With dataset IDs:
```bash
uv run copick_server/server.py serve --dataset-ids 10440 --cors "*" --port 8017
```

### Launch a client

#### Basic client

```bash
python -m copick_server.client
```

#### Client CLI

The client now supports CLI commands for various operations. You can specify a different server URL with the `--base-url` option.

```bash
# Create an empty segmentation
python -m copick_server.client create-segmentation \
    --base-url "http://localhost:8017" \
    --run-name 10440 \
    --voxel-size 10.012 \
    --user-id "myuser" \
    --session-id "mysession" \
    --name "membrane"
```

Using uv run:
```bash
uv run copick_server/client.py create-segmentation \
    --base-url "http://localhost:8017" \
    --run-name 10440 \
    --voxel-size 10.012 \
    --name "membrane"
```

Get CLI help:
```bash
python -m copick_server.client --help
python -m copick_server.client create-segmentation --help
```

## Running Tests

```bash
pip install ".[test]"
pytest
```

For coverage report:
```bash
pytest --cov=copick_server
```

## CLI Options

### Server Options

```
python -m copick_server.server serve --help
```

| Option            | Description                                            | Default       |
|-------------------|--------------------------------------------------------|---------------|
| -c, --config      | Path to the configuration file                         | None          |
| -ds, --dataset-ids| Dataset IDs to include in the project                  | None          |
| --overlay-root    | Root URL for the overlay storage                       | /tmp/overlay_root |
| --cors            | Origin to allow CORS. Use wildcard '*' to allow all    | None          |
| --host            | Bind socket to this host                               | 127.0.0.1     |
| --port            | Bind socket to this port                               | 8000          |
| --reload          | Enable auto-reload                                     | False         |

### Client Options

```
python -m copick_server.client create-segmentation --help
```

| Option            | Description                                            | Default       |
|-------------------|--------------------------------------------------------|---------------|
| --base-url        | Base URL of the Copick server                          | http://localhost:8017 |
| --run-name        | Name of the run to work with                           | (Required)    |
| --voxel-size      | Voxel size to use                                      | (Required)    |
| --user-id         | User ID for the segmentation                           | copickClient  |
| --session-id      | Session ID for the segmentation                        | copickSession |
| --name            | Name of the segmentation                               | (Required)    |
| --multilabel      | Flag for multilabel segmentation                       | False         |

## References

The idea is influenced by https://github.com/manzt/simple-zarr-server, but aimed at supporting https://github.com/kephale/copick.
