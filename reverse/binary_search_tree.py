from __future__ import annotations

from typing import Callable, Generic, Optional, TypeVar

T = TypeVar('T')


class BSTNode(Generic[T]):
    left: Optional[BSTNode]
    right: Optional[BSTNode]

    def __init__(self, value: T) -> None:
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value: T) -> None:
        side = 'left' if value < self.value else 'right'

        if (side_node := getattr(self, side)) is None:
            setattr(self, side, BSTNode(value))
        else:
            side_node.insert(value)

    def contains(self, target: T) -> bool:
        if target == self.value:
            return True

        side = 'left' if target < self.value else 'right'
        if (side_node := getattr(self, side)) is not None:
            return side_node.contains(target)

        return False

    def get_max(self) -> T:
        return self.value if self.right is None else self.right.get_max()

    def for_each(self, fn: Callable[[T], None]) -> None:
        fn(self.value)
        for node in (self.left, self.right):
            if node is not None:
                node.for_each(fn)

    @staticmethod
    def in_order_print(node: BSTNode) -> None:
        if node.left is not None:
            node.left.in_order_print(node.left)

        print(node.value)

        if node.right is not None:
            node.right.in_order_print(node.right)

    def bft_print(self, node: BSTNode) -> None:
        if node is self:
            print(node.value)

        nodes = (node.right, node.left)

        for sub_node in nodes:
            if sub_node is not None:
                print(sub_node.value)

        for sub_node in nodes:
            if sub_node is not None:
                self.bft_print(sub_node)

    def dft_print(self, node: BSTNode) -> None:
        print(node.value)

        for sub_node in (node.left, node.right):
            if sub_node is not None:
                self.dft_print(sub_node)

    def pre_order_dft(self, node: BSTNode) -> None:
        print(node.value)

        for sub_node in (node.left, node.right):
            if sub_node is not None:
                self.pre_order_dft(sub_node)

    def post_order_dft(self, node: BSTNode) -> None:
        for sub_node in (node.left, node.right):
            if sub_node is not None:
                self.post_order_dft(sub_node)

        print(node.value)
