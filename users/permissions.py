from rest_framework import permissions

class IsModer(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moders').exists()


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsOwnerOrModer(permissions.BasePermission):
    def has_permission(self, request, view):
        return True  # Разрешаем доступ, фильтрация будет в queryset

    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff or request.user.groups.filter(name='moders').exists()

