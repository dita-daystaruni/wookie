from rest_framework.pagination import PageNumberPagination


class ResultsSetPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = "page_size"
    max_page_size = 1000
