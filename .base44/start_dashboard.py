"""Start the source-backed dashboard with its normal public auth gate."""
import os
from pathlib import Path

import yaml

home = Path(os.environ["HERMES_HOME"])
home.mkdir(parents=True, exist_ok=True)
config_path = home / "config.yaml"
config = yaml.safe_load(config_path.read_text(encoding="utf-8")) if config_path.exists() else {}
config = config or {}
dashboard = config.setdefault("dashboard", {})
dashboard.setdefault("basic_auth", {}).setdefault("username", "admin")
dashboard["public_url"] = f"https://3000-{os.environ['BASE44_PUBLIC_HOST_SUFFIX']}"
config_path.write_text(yaml.safe_dump(config), encoding="utf-8")

from hermes_cli.plugins import discover_plugins
from hermes_cli.web_server import start_server

discover_plugins()
start_server(host="0.0.0.0", port=9119, open_browser=False)
