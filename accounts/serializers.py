from rest_framework import serializers

from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = [
			'id',
			'username',
			'password',
			'codename',
			'first_name',
			'last_name',
			'created_at',
			'updated_at'
		]
		extra_kwargs = {
			'password': {
				'write_only': True
			}
		}