# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPermissionVersionsRequest:

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
        'limit': 'int',
        'marker': 'str',
        'permission_id': 'str'
    }

    attribute_map = {
        'x_security_token': 'X-Security-Token',
        'limit': 'limit',
        'marker': 'marker',
        'permission_id': 'permission_id'
    }

    def __init__(self, x_security_token=None, limit=None, marker=None, permission_id=None):
        r"""ListPermissionVersionsRequest

        The model defined in huaweicloud sdk

        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param limit: 分页页面的最大值。
        :type limit: int
        :param marker: 页面标记。
        :type marker: str
        :param permission_id: 共享资源权限的ID。
        :type permission_id: str
        """
        
        

        self._x_security_token = None
        self._limit = None
        self._marker = None
        self._permission_id = None
        self.discriminator = None

        if x_security_token is not None:
            self.x_security_token = x_security_token
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        self.permission_id = permission_id

    @property
    def x_security_token(self):
        r"""Gets the x_security_token of this ListPermissionVersionsRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this ListPermissionVersionsRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        r"""Sets the x_security_token of this ListPermissionVersionsRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this ListPermissionVersionsRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def limit(self):
        r"""Gets the limit of this ListPermissionVersionsRequest.

        分页页面的最大值。

        :return: The limit of this ListPermissionVersionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPermissionVersionsRequest.

        分页页面的最大值。

        :param limit: The limit of this ListPermissionVersionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListPermissionVersionsRequest.

        页面标记。

        :return: The marker of this ListPermissionVersionsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListPermissionVersionsRequest.

        页面标记。

        :param marker: The marker of this ListPermissionVersionsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def permission_id(self):
        r"""Gets the permission_id of this ListPermissionVersionsRequest.

        共享资源权限的ID。

        :return: The permission_id of this ListPermissionVersionsRequest.
        :rtype: str
        """
        return self._permission_id

    @permission_id.setter
    def permission_id(self, permission_id):
        r"""Sets the permission_id of this ListPermissionVersionsRequest.

        共享资源权限的ID。

        :param permission_id: The permission_id of this ListPermissionVersionsRequest.
        :type permission_id: str
        """
        self._permission_id = permission_id

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
        if not isinstance(other, ListPermissionVersionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
