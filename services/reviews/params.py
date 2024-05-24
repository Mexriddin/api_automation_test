class Params:
    reviews_list_params = lambda self, offset, limit, sort_by, order_by: \
        {
            "offset": offset,
            "limit": limit,
            "sort_by": sort_by,
            "order_by": order_by
        }
