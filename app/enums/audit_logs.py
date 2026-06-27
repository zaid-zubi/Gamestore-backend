from enum import StrEnum


class AuditAction(StrEnum):
    # Auth
    LOGIN_SUCCESS = "login_success"
    LOGIN_FAILED = "login_failed"
    LOGOUT = "logout"

    # Products
    PRODUCT_VIEWED = "product_viewed"
    PRODUCT_LIST_VIEWED = "product_list_viewed"

    # Orders
    ORDER_CREATED = "order_created"
    ORDER_FAILED = "order_failed"

    # System
    UNAUTHORIZED_ACCESS = "unauthorized_access"