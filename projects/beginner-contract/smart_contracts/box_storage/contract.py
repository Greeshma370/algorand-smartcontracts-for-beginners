from algopy import ARC4Contract, String , BoxMap
from algopy import arc4


class UserStruct(arc4.Struct):
    name: arc4.String
    id: arc4.UInt64
    asset: arc4.UInt64


class Box(arc4.ARC4Contract):
    def __init__(self) -> None:
        # Create a box map with a key prefix
        self.user_map = BoxMap(arc4.UInt64, UserStruct, key_prefix="users")

    @arc4.abimethod
    def box_map_set(self, key: arc4.UInt64, value: UserStruct) -> bool:
        # Update the value in the box map
        assert key in self.user_map, "Key does not exist in box map"
        self.user_map[key] = value.copy()
        assert self.user_map[key] == value
        return True

    @arc4.abimethod
    def box_map_get(self, key: arc4.UInt64) -> UserStruct:
        # Read the value from the box map
        assert key in self.user_map, "Key does not exist in box map"
        return self.user_map[key]

    @arc4.abimethod
    def box_map_exists(self, key: arc4.UInt64) -> bool:
        # Check if the key exists in box map
        return key in self.user_map

    @arc4.abimethod
    def box_map_delete(self, key: arc4.UInt64) -> None:
        # Delete the box
        del self.user_map[key]
