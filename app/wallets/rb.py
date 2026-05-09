class RBWallet:
    def __init__(self,
                 wallet_id: int | None = None,
                 wallet_type: str | None = None,
                 name: str | None = None):
        self.id = wallet_id
        self.type = wallet_type
        self.name = name

    def to_dict(self) -> dict:
        data = {'id': self.id, 'type': self.type, 'name': self.name}
        return {k: v for k, v in data.items() if v is not None}
