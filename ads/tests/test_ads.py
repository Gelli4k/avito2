import json

import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_add(api_client, user):
    data = {
        'name': "ooo",
        'author_id': user.id,
        'price': 10,
    }
    url = reverse('ad_create')
    res = api_client.post(
        url,
        data=json.dumps(data),
        content_type='application/json'
    )
