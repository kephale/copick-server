# As a module
from copick_server.server import serve_copick

serve_copick("/Users/kharrington/git/kephale/copick-server/example_copick.json", allowed_origins=["*"])

# Or from command line
# $ python copick_zarr_server.py path/to/copick_config.json --cors "*"