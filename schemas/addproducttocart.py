post_addproducttocart = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "additionalProperties": False,
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        },
        "message": {
            "type": "string"
        },
        "updatetopcartsectionhtml": {
            "type": "string"
        },
        "updateflyoutcartsectionhtml": {
            "type": "string"
        }
    },
    "required": [
        "success",
        "message",
        "updatetopcartsectionhtml",
        "updateflyoutcartsectionhtml"
    ]
}
