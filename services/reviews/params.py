from services.commons.params import BaseParams


class Params(BaseParams):
    reviews_sort_order_params = lambda self, sort_by, order_by: \
        {
            "sort_by": sort_by,
            "order_by": order_by
        }
