# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeletePoolsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'pools': 'list[BatchDeletePoolsResp]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'pools': 'pools'
    }

    def __init__(self, request_id=None, pools=None):
        r"""BatchDeletePoolsResponse

        The model defined in huaweicloud sdk

        :param request_id: **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。
        :type request_id: str
        :param pools: 后端服务器组批量删除后的响应结果。
        :type pools: list[:class:`huaweicloudsdkelb.v3.BatchDeletePoolsResp`]
        """
        
        super().__init__()

        self._request_id = None
        self._pools = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if pools is not None:
            self.pools = pools

    @property
    def request_id(self):
        r"""Gets the request_id of this BatchDeletePoolsResponse.

        **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。

        :return: The request_id of this BatchDeletePoolsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this BatchDeletePoolsResponse.

        **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。

        :param request_id: The request_id of this BatchDeletePoolsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def pools(self):
        r"""Gets the pools of this BatchDeletePoolsResponse.

        后端服务器组批量删除后的响应结果。

        :return: The pools of this BatchDeletePoolsResponse.
        :rtype: list[:class:`huaweicloudsdkelb.v3.BatchDeletePoolsResp`]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        r"""Sets the pools of this BatchDeletePoolsResponse.

        后端服务器组批量删除后的响应结果。

        :param pools: The pools of this BatchDeletePoolsResponse.
        :type pools: list[:class:`huaweicloudsdkelb.v3.BatchDeletePoolsResp`]
        """
        self._pools = pools

    def to_dict(self):
        import warnings
        warnings.warn("BatchDeletePoolsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchDeletePoolsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
