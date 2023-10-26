# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCentralNetworkCapabilitiesResponse(SdkResponse):

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
        'capabilities': 'list[CentralNetworkCapability]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'capabilities': 'capabilities'
    }

    def __init__(self, request_id=None, capabilities=None):
        """ListCentralNetworkCapabilitiesResponse

        The model defined in huaweicloud sdk

        :param request_id: 资源ID标识符。
        :type request_id: str
        :param capabilities: 租户能力列表
        :type capabilities: list[:class:`huaweicloudsdkcc.v3.CentralNetworkCapability`]
        """
        
        super(ListCentralNetworkCapabilitiesResponse, self).__init__()

        self._request_id = None
        self._capabilities = None
        self.discriminator = None

        self.request_id = request_id
        self.capabilities = capabilities

    @property
    def request_id(self):
        """Gets the request_id of this ListCentralNetworkCapabilitiesResponse.

        资源ID标识符。

        :return: The request_id of this ListCentralNetworkCapabilitiesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListCentralNetworkCapabilitiesResponse.

        资源ID标识符。

        :param request_id: The request_id of this ListCentralNetworkCapabilitiesResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def capabilities(self):
        """Gets the capabilities of this ListCentralNetworkCapabilitiesResponse.

        租户能力列表

        :return: The capabilities of this ListCentralNetworkCapabilitiesResponse.
        :rtype: list[:class:`huaweicloudsdkcc.v3.CentralNetworkCapability`]
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """Sets the capabilities of this ListCentralNetworkCapabilitiesResponse.

        租户能力列表

        :param capabilities: The capabilities of this ListCentralNetworkCapabilitiesResponse.
        :type capabilities: list[:class:`huaweicloudsdkcc.v3.CentralNetworkCapability`]
        """
        self._capabilities = capabilities

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListCentralNetworkCapabilitiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
