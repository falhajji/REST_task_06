from rest_framework.permissions import BasePermission
from datetime	import date

class IsAuthor(BasePermission):
    message = "You must be the author of this article to edit it."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.user == request.user):
            return True
        else:
            return False


class IsValidBooking(BasePermission):
    message = "You cannot cancel or modify a booking if it is more than 3 days away."

    def has_object_permission(self, request, view, obj):
        if (obj.date - date.today()).days >=3:
            return True
        else:
            return False