from services.commons.params import BaseParams


class Params(BaseParams):
    keep_payments = lambda self, keep: {"keep_payments": True} if keep == True else {"keep_payments": False}



