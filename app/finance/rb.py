class RBTransaction:
    def __init__(self, 
                 transaction_id: int | None = None,
                 wallet_id: int | None = None,
                 category_id: int | None = None,
                 transaction_type: str | None = None,
                 is_essential: bool | None = None):
        self.id = transaction_id
        self.wallet_id = wallet_id
        self.category_id = category_id
        self.transaction_type = transaction_type
        self.is_essential = is_essential

    def to_dict(self) -> dict:
        data = {
            'id': self.id, 
            'wallet_id': self.wallet_id, 
            'category_id': self.category_id,
            'transaction_type': self.transaction_type,
            'is_essential': self.is_essential
        }
        return {k: v for k, v in data.items() if v is not None}
