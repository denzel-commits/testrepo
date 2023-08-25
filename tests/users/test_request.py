import pytest


class TestUser:

    def test_get_user(self):
        pass

    def test_added_user_equal_to_created(self, add_user):
        user = add_user
        print(user)
        assert user.get("id") == add_user.get("id")

    def test_update_user(self):
        pass

    def test_delete_user(self):
        pass
