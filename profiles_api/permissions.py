from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """allow the user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """check that the user is trying to edit their own profile"""

        #if the request is sth that doesn't affect security issues .. like viewing all profiles ..
        # do it :)
        if request.method in permissions.SAFE_METHODS:
            return True

        #check that the id of the user is the same as the requested users' changes...
        return obj.id == request.user.id
