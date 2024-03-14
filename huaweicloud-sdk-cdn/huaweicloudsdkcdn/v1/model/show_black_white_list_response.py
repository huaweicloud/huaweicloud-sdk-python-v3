# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBlackWhiteListResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'int',
        'ip_list': 'list[str]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'ip_list': 'ip_list',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, type=None, ip_list=None, x_request_id=None):
        """ShowBlackWhiteListResponse

        The model defined in huaweicloud sdk

        :param type: IP黑白名单类型（0：关闭IP黑白名单功能，1：黑名单，2：白名单）。
        :type type: int
        :param ip_list: IP黑白名单列表。
        :type ip_list: list[str]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowBlackWhiteListResponse, self).__init__()

        self._type = None
        self._ip_list = None
        self._x_request_id = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if ip_list is not None:
            self.ip_list = ip_list
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def type(self):
        """Gets the type of this ShowBlackWhiteListResponse.

        IP黑白名单类型（0：关闭IP黑白名单功能，1：黑名单，2：白名单）。

        :return: The type of this ShowBlackWhiteListResponse.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowBlackWhiteListResponse.

        IP黑白名单类型（0：关闭IP黑白名单功能，1：黑名单，2：白名单）。

        :param type: The type of this ShowBlackWhiteListResponse.
        :type type: int
        """
        self._type = type

    @property
    def ip_list(self):
        """Gets the ip_list of this ShowBlackWhiteListResponse.

        IP黑白名单列表。

        :return: The ip_list of this ShowBlackWhiteListResponse.
        :rtype: list[str]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        """Sets the ip_list of this ShowBlackWhiteListResponse.

        IP黑白名单列表。

        :param ip_list: The ip_list of this ShowBlackWhiteListResponse.
        :type ip_list: list[str]
        """
        self._ip_list = ip_list

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ShowBlackWhiteListResponse.

        :return: The x_request_id of this ShowBlackWhiteListResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ShowBlackWhiteListResponse.

        :param x_request_id: The x_request_id of this ShowBlackWhiteListResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowBlackWhiteListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
