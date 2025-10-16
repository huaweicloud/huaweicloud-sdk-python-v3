from huaweicloudsdkcore.sdk_response import SdkResponse
from decimal import Decimal


class TestSdkResponse:
    def test_to_json_object(self):
        resp = SdkResponse()
        assert resp.to_json_object() is None

        resp.raw_content = b'{"key": "value"}'
        assert resp.to_json_object() == {"key": "value"}

    def test_to_json_object_with_parse_float(self):
        resp = SdkResponse()
        resp.raw_content = b'{"price": 9.99}'

        result = resp.to_json_object()
        assert isinstance(result["price"], float)

        result = resp.to_json_object(parse_float=Decimal)
        assert (isinstance(result["price"], Decimal))
