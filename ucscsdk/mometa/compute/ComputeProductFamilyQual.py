"""This module contains the general information for ComputeProductFamilyQual ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputeProductFamilyQualConsts():
    PRODUCT_FAMILY_UCS_CLASSIC = "ucs-classic"
    PRODUCT_FAMILY_UCS_CLASSIC_3GEN = "ucs-classic-3gen"
    PRODUCT_FAMILY_UCS_CLASSIC_4GEN = "ucs-classic-4gen"
    PRODUCT_FAMILY_UCS_MINI = "ucs-mini"


class ComputeProductFamilyQual(ManagedObject):
    """This is ComputeProductFamilyQual class."""

    consts = ComputeProductFamilyQualConsts()
    naming_props = set([u'productFamily'])

    mo_meta = MoMeta("ComputeProductFamilyQual", "computeProductFamilyQual", "product-qualifier-[product_family]", VersionMeta.Version141a, "InputOutput", 0x1f, [], ["admin", "pn-policy", "read-only"], [u'computeDomainQual'], [], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "product_family": MoPropertyMeta("product_family", "productFamily", "string", VersionMeta.Version141a, MoPropertyMeta.NAMING, 0x4, None, None, None, ["ucs-classic", "ucs-classic-3gen", "ucs-classic-4gen", "ucs-mini"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "productFamily": "product_family", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, product_family, **kwargs):
        self._dirty_mask = 0
        self.product_family = product_family
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "ComputeProductFamilyQual", parent_mo_or_dn, **kwargs)

