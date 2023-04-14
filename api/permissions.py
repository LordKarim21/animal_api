from rest_framework.permissions import BasePermission, SAFE_METHODS

method_user = ['PUT', 'POST']


class IsAdminOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        global method_user
        if request.method == SAFE_METHODS:
            return True
        elif request.method in method_user and request.user.is_authenticated:
            return True

        return request.user.is_authenticated

    def has_permission(self, request, view):
        global method_user
        if request.method in SAFE_METHODS:
            return True
        elif request.method in method_user and request.user.is_authenticated:
            return True

        return bool(request.user and request.user.is_staff)
