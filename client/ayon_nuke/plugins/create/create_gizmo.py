import nuke
from ayon_nuke.api import (
    NukeCreator,
    NukeCreatorError,
    maintained_selection
)


class CreateGizmo(NukeCreator):
    """Add Publishable Group as gizmo"""

    settings_category = "nuke"

    identifier = "create_gizmo"
    label = "Gizmo (group)"
    product_type = "gizmo"
    icon = "file-archive-o"
    default_variants = ["ViewerInput", "Lut", "Effect"]

    # plugin attributes
    node_color = "0x7533c1ff"

    def create_instance_node(
        self,
        node_name,
        knobs=None,
        parent=None,
        node_type=None
    ):
        with maintained_selection():
            if self.selected_nodes:
                node = self.selected_nodes[0]
                if node.Class() != "Group":
                    raise NukeCreatorError(
                        "Creator error: Select only 'Group' node type")
                created_node = node
            else:
                created_node = nuke.collapseToGroup()

            created_node["tile_color"].setValue(
                int(self.node_color, 16))

            created_node["name"].setValue(node_name)

            return created_node

    def create(self, product_name, instance_data, pre_create_data):
        # make sure product name is unique
        self.check_existing_product(product_name)

        instance = super(CreateGizmo, self).create(
            product_name,
            instance_data,
            pre_create_data
        )

        return instance

    def set_selected_nodes(self, pre_create_data):
        if pre_create_data.get("use_selection"):
            self.selected_nodes = nuke.selectedNodes()
            if self.selected_nodes == []:
                raise NukeCreatorError("Creator error: No active selection")
            elif len(self.selected_nodes) > 1:
                NukeCreatorError("Creator error: Select only one 'Group' node")
        else:
            self.selected_nodes = []
