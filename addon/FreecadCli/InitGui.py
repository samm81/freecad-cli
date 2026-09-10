"""FreeCAD GUI initialization — auto-starts the RPC server."""

import sys
from pathlib import Path

addon_dir = str(Path(__file__).resolve().parent)
if addon_dir not in sys.path:
    sys.path.insert(0, addon_dir)

import rpc_server  # noqa: E402

rpc_server.start()
