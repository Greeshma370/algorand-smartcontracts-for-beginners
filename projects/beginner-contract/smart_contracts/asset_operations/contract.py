from algopy import ARC4Contract, arc4, BoxMap

class AssetMetadata(arc4.Struct):
    total: arc4.UInt64
    decimals: arc4.UInt32
    default_frozen: arc4.Bool
    unit_name: arc4.String
    name: arc4.String
    url: arc4.String
    metadata_hash: arc4.DynamicBytes  # Corrected type
    manager_addr: arc4.Address
    reserve_addr: arc4.Address
    freeze_addr: arc4.Address
    clawback_addr: arc4.Address

class RemintContract(ARC4Contract):
    def __init__(self) -> None:
        self.asset_metadata = BoxMap(arc4.UInt64, AssetMetadata, key_prefix="assetmeta")
        self.user_map = BoxMap(arc4.String, arc4.UInt64, key_prefix="users")  # user_id -> last_asset_id

    @arc4.abimethod
    def create_asset(self, meta: AssetMetadata) -> arc4.UInt64:
        new_asset_id = arc4.UInt64(1)  # Placeholder, must be arc4.UInt64
        self.asset_metadata[new_asset_id] = meta.copy()
        return new_asset_id
