import json
from typing import List
from django.db import models
from django.contrib.auth.models import User

import json
from typing import List
from django.db import models
from django.contrib.auth.models import User

class Result(models.Model):
    input_data = models.TextField(unique=True)
    result_data = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result: {self.result_data}"


class UserResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'result']

    def __str__(self):
        return f"{self.user.username} - {self.result.id}"


class Repository():
    def save_result(self, user: User, input: List[int], output: int) -> Result:
        result, is_created = Result.objects.get_or_create(
            input_data = json.dumps(input), 
            defaults={
                "result_data": output
            }
        )
    
        UserResult.objects.get_or_create(
            user = user,
            result = result
        )

        return result
    
    def get_result_or_none(self, input: List[int]) -> int | None:
        try:
            result = Result.objects.get(input_data=json.dumps(input))
            return result.result_data
        except Result.DoesNotExist:
            return None
    
