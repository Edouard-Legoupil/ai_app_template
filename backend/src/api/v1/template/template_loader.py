import os
import yaml
from typing import Dict, Any, List

template_dir = os.path.join(os.path.dirname(__file__), ".")


def list_templates() -> List[str]:
    return [f for f in os.listdir(template_dir) if f.endswith(".yaml")]


def load_template(name: str) -> Dict[str, Any]:
    path = os.path.join(template_dir, name)
    with open(path, "r") as f:
        return yaml.safe_load(f)
