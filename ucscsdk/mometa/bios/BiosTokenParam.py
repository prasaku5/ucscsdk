"""This module contains the general information for BiosTokenParam ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosTokenParamConsts():
    pass


class BiosTokenParam(ManagedObject):
    """This is BiosTokenParam class."""

    consts = BiosTokenParamConsts()
    naming_props = set([u'targetTokenName'])

    mo_meta = MoMeta("BiosTokenParam", "biosTokenParam", "tokn-param-[target_token_name]", VersionMeta.Version201b, "InputOutput", 0x1f, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], [u'biosTokenFeatureGroup'], [u'biosTokenSettings'], [None])

    prop_meta = {
        "type": MoPropertyMeta("type", "Type", "string", VersionMeta.Version201k, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "legacy_prop_id": MoPropertyMeta("legacy_prop_id", "legacyPropId", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "param_name": MoPropertyMeta("param_name", "paramName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "target_token_name": MoPropertyMeta("target_token_name", "targetTokenName", "string", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x10, 1, 510, None, [], []), 
        "ui_group_name": MoPropertyMeta("ui_group_name", "uiGroupName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "Type": "type", 
        "childAction": "child_action", 
        "dn": "dn", 
        "legacyPropId": "legacy_prop_id", 
        "paramName": "param_name", 
        "rn": "rn", 
        "status": "status", 
        "targetTokenName": "target_token_name", 
        "uiGroupName": "ui_group_name", 
    }

    def __init__(self, parent_mo_or_dn, target_token_name, **kwargs):
        self._dirty_mask = 0
        self.target_token_name = target_token_name
        self.type = None
        self.child_action = None
        self.legacy_prop_id = None
        self.param_name = None
        self.status = None
        self.ui_group_name = None

        ManagedObject.__init__(self, "BiosTokenParam", parent_mo_or_dn, **kwargs)

