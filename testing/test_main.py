"""
Test main
"""
import random
from flask import url_for


def test_get_item(client):
    """
    test get item
    :param client:
    :return:
    """
    random_item_id = random.randint(1,100)
    url = url_for('get_item', item_id=random_item_id)
    response = client.get(url)
    assert response.status_code == 200
    assert response.json['item']['id'] == random_item_id
