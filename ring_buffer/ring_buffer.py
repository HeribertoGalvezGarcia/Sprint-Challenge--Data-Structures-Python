from typing import Generic, List, TypeVar

T = TypeVar('T')


class RingBuffer(Generic[T]):
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self._storage = []

    def append(self, item: T) -> None:
        self._storage.append(item)

    def get(self) -> List[T]:
        entries = []
        for i, entry in enumerate(self._storage):
            try:
                entries[i % self.capacity] = entry
            except IndexError:
                entries.append(entry)

        return entries
