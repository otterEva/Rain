from abc import ABC, abstractmethod


class BaseDAO(ABC):
    @abstractmethod
    async def find_by_id(self): ...

    @abstractmethod
    async def find_all(self): ...

    @abstractmethod
    async def add(self): ...
