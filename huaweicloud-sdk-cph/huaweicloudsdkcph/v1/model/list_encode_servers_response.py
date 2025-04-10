# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEncodeServersResponse(SdkResponse):

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
        'encode_servers': 'list[EncodeServer]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'encode_servers': 'encode_servers'
    }

    def __init__(self, request_id=None, encode_servers=None):
        r"""ListEncodeServersResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求的唯一标识ID。
        :type request_id: str
        :param encode_servers: 编码服务信息。
        :type encode_servers: list[:class:`huaweicloudsdkcph.v1.EncodeServer`]
        """
        
        super(ListEncodeServersResponse, self).__init__()

        self._request_id = None
        self._encode_servers = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if encode_servers is not None:
            self.encode_servers = encode_servers

    @property
    def request_id(self):
        r"""Gets the request_id of this ListEncodeServersResponse.

        请求的唯一标识ID。

        :return: The request_id of this ListEncodeServersResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListEncodeServersResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this ListEncodeServersResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def encode_servers(self):
        r"""Gets the encode_servers of this ListEncodeServersResponse.

        编码服务信息。

        :return: The encode_servers of this ListEncodeServersResponse.
        :rtype: list[:class:`huaweicloudsdkcph.v1.EncodeServer`]
        """
        return self._encode_servers

    @encode_servers.setter
    def encode_servers(self, encode_servers):
        r"""Sets the encode_servers of this ListEncodeServersResponse.

        编码服务信息。

        :param encode_servers: The encode_servers of this ListEncodeServersResponse.
        :type encode_servers: list[:class:`huaweicloudsdkcph.v1.EncodeServer`]
        """
        self._encode_servers = encode_servers

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
        if not isinstance(other, ListEncodeServersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
