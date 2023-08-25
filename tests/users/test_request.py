import pytest


class TestUser:

    def test_get_user(self):
        pass

    def test_added_user_equal_to_created(self, add_user):
        user = add_user
        print(user)
        assert user["id"] == add_user["id"]

    def test_delete_user(self, generate_user):
        generated_user = generate_user
        assert generated_user["password"] == "2343f43r3"
