from fastapi import APIRouter
from src.api.v1.template.template_loader import list_templates, load_template

router = APIRouter()


@router.get("/templates")
def get_templates():
    templates = list_templates()
    info = []
    for tname in templates:
        tdata = load_template(tname)
        info.append(
            {
                "file": tname,
                "name": tdata.get("name"),
                "sections": [s["name"] for s in tdata.get("sections", [])],
            }
        )
    return {"templates": info}
