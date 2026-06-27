class ResponseMessages:
    class GENERAL:
        READ = {"en": "Data retrieved successfully", "ar": "تم جلب البيانات بنجاح"}
        CREATE = {"en": "Data created successfully", "ar": "تم اضافة البيانات بنجاح"}
        UPDATE = {"en": "Data updated successfully", "ar": "تم تعديل البيانات بنجاح"}
        DELETE = {"en": "Data deleted successfully", "ar": "تم حذف البيانات بنجاح"}

    class AUTH:
        LOGIN_SUCCESS = {"en": "Login successful", "ar": "تسجيل دخول ناجح"}
        LOGIN_FAILED = {"en": "Invalid credentials", "ar": "بيانات عير صالحة"}
        LOGOUT_SUCCESS = {"en": "Logout successfully", "ar": "تسجيل خروج ناجح"}

    class Error:
        USER_NOT_FOUND = "User not found"
        INCORRECT_EMAIL_OR_PASSWORD = "Incorrect emails or password"
        DATABASE_CONNECTION_FAILUER = "Connection with Datasource is failed..."
        ORDER_NOT_FOUND = "Order not found"
        PRODUCT_NOT_FOUND = "Product not found"