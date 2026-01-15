from typing import List

from django.contrib.auth.models import User

from . import logic
from .models import Repository


class AppService():
    def __init__(self):
        self.repoitory = Repository()

    def get_group_count_by_array(self, user: User, array: List[int]) -> int:
        result = self.repoitory.get_result_or_none(array)

        if not result:
            result = logic.get_group_count(array)

        self.repoitory.save_result(user=user, input=array, output=result)

        return result