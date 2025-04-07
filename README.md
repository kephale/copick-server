# Launch a server

```
uv run copick_server/demo_server.py
```

# Launch a client

```
uv run copick_server/client.py
```

# Running Tests

```
pip install ".[test]"
pytest
```

For coverage report:
```
pytest --cov=copick_server
```

# References

The idea is influenced by https://github.com/manzt/simple-zarr-server, but aimed at supporting https://github.com/copick/copick.
