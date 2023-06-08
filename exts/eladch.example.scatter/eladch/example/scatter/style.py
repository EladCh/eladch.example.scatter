__all__ = ["scatter_window_style"]

from omni.ui import color as cl
from omni.ui import constant as fl
from omni.ui import url
import omni.kit.app
import omni.ui as ui
import pathlib

EXTENSION_FOLDER_PATH = pathlib.Path(
    omni.kit.app.get_app().get_extension_manager().get_extension_path_by_module(__name__)
)

# Pre-defined constants. It's possible to change them runtime.
cl.scatter_window_hovered = cl("#2b2e2e")
cl.scatter_window_text = cl("#9e9e9e")
fl.scatter_window_attr_hspacing = 10
fl.scatter_window_attr_spacing = 1
fl.scatter_window_group_spacing = 2

# The main style dict
scatter_window_style = {
    "Label::attribute_name": {
        "color": cl.scatter_window_text,
        "margin_height": fl.scatter_window_attr_spacing,
        "margin_width": fl.scatter_window_attr_hspacing,
    },
    "CollapsableFrame::group": {"margin_height": fl.scatter_window_group_spacing},
    "CollapsableFrame::group:hovered": {"secondary_color": cl.scatter_window_hovered},
}