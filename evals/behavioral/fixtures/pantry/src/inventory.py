"""Small capability snapshot, not a full application or runtime acceptance proof."""
CAPABILITIES = {"household_membership", "locations", "manual_inventory_add",
                "manual_inventory_edit", "manual_inventory_list", "inventory_change_history"}


def supports(capability):
    return capability in CAPABILITIES
