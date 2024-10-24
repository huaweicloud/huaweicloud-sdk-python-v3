# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGroupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_security_token')

    openapi_types = {
        'x_security_token': 'str',
        'identity_store_id': 'str',
        'marker': 'str',
        'limit': 'int',
        'display_name': 'str'
    }

    attribute_map = {
        'x_security_token': 'X-Security-Token',
        'identity_store_id': 'identity_store_id',
        'marker': 'marker',
        'limit': 'limit',
        'display_name': 'display_name'
    }

    def __init__(self, x_security_token=None, identity_store_id=None, marker=None, limit=None, display_name=None):
        """ListGroupsRequest

        The model defined in huaweicloud sdk

        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param identity_store_id: 身份源的全局唯一标识符（ID）
        :type identity_store_id: str
        :param marker: 分页标记
        :type marker: str
        :param limit: 每个请求返回的最大结果数
        :type limit: int
        :param display_name: 通过显示名模糊查询用户组信息
        :type display_name: str
        """
        
        

        self._x_security_token = None
        self._identity_store_id = None
        self._marker = None
        self._limit = None
        self._display_name = None
        self.discriminator = None

        if x_security_token is not None:
            self.x_security_token = x_security_token
        self.identity_store_id = identity_store_id
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if display_name is not None:
            self.display_name = display_name

    @property
    def x_security_token(self):
        """Gets the x_security_token of this ListGroupsRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this ListGroupsRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        """Sets the x_security_token of this ListGroupsRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this ListGroupsRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def identity_store_id(self):
        """Gets the identity_store_id of this ListGroupsRequest.

        身份源的全局唯一标识符（ID）

        :return: The identity_store_id of this ListGroupsRequest.
        :rtype: str
        """
        return self._identity_store_id

    @identity_store_id.setter
    def identity_store_id(self, identity_store_id):
        """Sets the identity_store_id of this ListGroupsRequest.

        身份源的全局唯一标识符（ID）

        :param identity_store_id: The identity_store_id of this ListGroupsRequest.
        :type identity_store_id: str
        """
        self._identity_store_id = identity_store_id

    @property
    def marker(self):
        """Gets the marker of this ListGroupsRequest.

        分页标记

        :return: The marker of this ListGroupsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListGroupsRequest.

        分页标记

        :param marker: The marker of this ListGroupsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ListGroupsRequest.

        每个请求返回的最大结果数

        :return: The limit of this ListGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListGroupsRequest.

        每个请求返回的最大结果数

        :param limit: The limit of this ListGroupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def display_name(self):
        """Gets the display_name of this ListGroupsRequest.

        通过显示名模糊查询用户组信息

        :return: The display_name of this ListGroupsRequest.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ListGroupsRequest.

        通过显示名模糊查询用户组信息

        :param display_name: The display_name of this ListGroupsRequest.
        :type display_name: str
        """
        self._display_name = display_name

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
        if not isinstance(other, ListGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
