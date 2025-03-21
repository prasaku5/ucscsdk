"""This module contains the general information for LsbootLocalStorage ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LsbootLocalStorageConsts():
    pass


class LsbootLocalStorage(ManagedObject):
    """This is LsbootLocalStorage class."""

    consts = LsbootLocalStorageConsts()
    naming_props = set([])

    mo_meta = MoMeta("LsbootLocalStorage", "lsbootLocalStorage", "local-storage", VersionMeta.Version111a, "InputOutput", 0xf, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-server-policy", "ls-storage", "ls-storage-policy"], [u'lsbootStorage'], [u'lsbootDefaultLocalImage', u'lsbootEmbeddedLocalDiskImage', u'lsbootEmbeddedLocalLunImage', u'lsbootLocalDiskImage', u'lsbootLocalHddImage', u'lsbootNvme', u'lsbootUsbExternalImage', u'lsbootUsbFlashStorageImage', u'lsbootUsbInternalImage'], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "LsbootLocalStorage", parent_mo_or_dn, **kwargs)

