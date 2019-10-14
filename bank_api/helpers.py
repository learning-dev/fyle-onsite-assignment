from rest_framework.pagination import LimitOffsetPagination


class bankPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 20
    min_limit = 1
    min_offset = 1
    max_offset = 20