"""This module contains the general information for FabricVsanEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricVsanEpConsts():
    IF_ROLE_DIAG = "diag"
    IF_ROLE_FCOE_NAS_STORAGE = "fcoe-nas-storage"
    IF_ROLE_FCOE_STORAGE = "fcoe-storage"
    IF_ROLE_FCOE_UPLINK = "fcoe-uplink"
    IF_ROLE_MGMT = "mgmt"
    IF_ROLE_MONITOR = "monitor"
    IF_ROLE_NAS_STORAGE = "nas-storage"
    IF_ROLE_NETWORK = "network"
    IF_ROLE_NETWORK_FCOE_UPLINK = "network-fcoe-uplink"
    IF_ROLE_SERVER = "server"
    IF_ROLE_SERVICE = "service"
    IF_ROLE_STORAGE = "storage"
    IF_ROLE_UNKNOWN = "unknown"
    IF_TYPE_AGGREGATION = "aggregation"
    IF_TYPE_PHYSICAL = "physical"
    IF_TYPE_UNKNOWN = "unknown"
    IF_TYPE_VIRTUAL = "virtual"
    OPER_STATE_ERROR_MISCONFIGURED = "error-misconfigured"
    OPER_STATE_ERROR_RESERVED = "error-reserved"
    OPER_STATE_OK = "ok"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    SWITCH_ID_MGMT = "mgmt"
    ZONING_STATE_DISABLED = "disabled"
    ZONING_STATE_ENABLED = "enabled"


class FabricVsanEp(ManagedObject):
    """This is FabricVsanEp class."""

    consts = FabricVsanEpConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("FabricVsanEp", "fabricVsanEp", "vsan-[id]", VersionMeta.Version141a, "InputOutput", 0xff, [], ["read-only"], [u'fabricFcEstcEp', u'fabricFcSanEp', u'fabricFcSanPc', u'fabricFcoeEstcEp', u'fabricFcoeSanEp'], [u'fabricConsumer', u'fabricEtherRef'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "fcoe_vlan": MoPropertyMeta("fcoe_vlan", "fcoeVlan", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-4042", "4048-4093"]), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version141a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], ["1-4093"]), 
        "if_role": MoPropertyMeta("if_role", "ifRole", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], []), 
        "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], []), 
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,32}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["error-misconfigured", "error-reserved", "ok"], []), 
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE", "mgmt"], []), 
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []), 
        "zoning_state": MoPropertyMeta("zoning_state", "zoningState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["disabled", "enabled"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "fcoeVlan": "fcoe_vlan", 
        "id": "id", 
        "ifRole": "if_role", 
        "ifType": "if_type", 
        "locale": "locale", 
        "name": "name", 
        "operState": "oper_state", 
        "peerDn": "peer_dn", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "status": "status", 
        "switchId": "switch_id", 
        "transport": "transport", 
        "type": "type", 
        "zoningState": "zoning_state", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.ep_dn = None
        self.fcoe_vlan = None
        self.if_role = None
        self.if_type = None
        self.locale = None
        self.name = None
        self.oper_state = None
        self.peer_dn = None
        self.policy_owner = None
        self.status = None
        self.switch_id = None
        self.transport = None
        self.type = None
        self.zoning_state = None

        ManagedObject.__init__(self, "FabricVsanEp", parent_mo_or_dn, **kwargs)

