import json

import allure
import requests
from allure_commons.types import AttachmentType
from jsonschema import validate
from requests import Response

from schemas.addproducttocart import post_addproducttocart


def add_to_cart_response(url) -> Response:
    response = requests.post(url)
    assert response.status_code == 200
    response_json_body = response.json()
    validate(response_json_body, post_addproducttocart)

    allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True),
                  name="Response", attachment_type=AttachmentType.JSON, extension="json")
    allure.attach(body=str(response.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")

    return response
