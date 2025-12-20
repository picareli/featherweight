from typing import Any


class Button:
    class CallMe:
        def __call__(self, *args: Any, **kwds: Any) -> Any:
            pass

    text: str
    is_selected: bool
    listeners: tuple[CallMe, ...]

    def broadcast(self):
        for x in self.listeners:
            x()
