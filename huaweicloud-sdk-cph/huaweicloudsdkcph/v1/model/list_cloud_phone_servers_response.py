# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCloudPhoneServersResponse(SdkResponse):

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
        'count': 'int',
        'servers': 'list[Server]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'count': 'count',
        'servers': 'servers'
    }

    def __init__(self, request_id=None, count=None, servers=None):
        r"""ListCloudPhoneServersResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求的唯一标识ID。
        :type request_id: str
        :param count: 实例总数。
        :type count: int
        :param servers: 云手机服务器信息。
        :type servers: list[:class:`huaweicloudsdkcph.v1.Server`]
        """
        
        super(ListCloudPhoneServersResponse, self).__init__()

        self._request_id = None
        self._count = None
        self._servers = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if count is not None:
            self.count = count
        if servers is not None:
            self.servers = servers

    @property
    def request_id(self):
        r"""Gets the request_id of this ListCloudPhoneServersResponse.

        请求的唯一标识ID。

        :return: The request_id of this ListCloudPhoneServersResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListCloudPhoneServersResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this ListCloudPhoneServersResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def count(self):
        r"""Gets the count of this ListCloudPhoneServersResponse.

        实例总数。

        :return: The count of this ListCloudPhoneServersResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListCloudPhoneServersResponse.

        实例总数。

        :param count: The count of this ListCloudPhoneServersResponse.
        :type count: int
        """
        self._count = count

    @property
    def servers(self):
        r"""Gets the servers of this ListCloudPhoneServersResponse.

        云手机服务器信息。

        :return: The servers of this ListCloudPhoneServersResponse.
        :rtype: list[:class:`huaweicloudsdkcph.v1.Server`]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        r"""Sets the servers of this ListCloudPhoneServersResponse.

        云手机服务器信息。

        :param servers: The servers of this ListCloudPhoneServersResponse.
        :type servers: list[:class:`huaweicloudsdkcph.v1.Server`]
        """
        self._servers = servers

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
        if not isinstance(other, ListCloudPhoneServersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
