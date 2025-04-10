# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPermissionsRequest:

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
        'resource_type': 'str',
        'permission_type': 'str'
    }

    attribute_map = {
        'x_security_token': 'X-Security-Token',
        'limit': 'limit',
        'marker': 'marker',
        'resource_type': 'resource_type',
        'permission_type': 'permission_type'
    }

    def __init__(self, x_security_token=None, limit=None, marker=None, resource_type=None, permission_type=None):
        r"""ListPermissionsRequest

        The model defined in huaweicloud sdk

        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param limit: 分页页面的最大值。
        :type limit: int
        :param marker: 页面标记。
        :type marker: str
        :param resource_type: 资源类型的名称。
        :type resource_type: str
        :param permission_type: 权限类型。RAM_MANAGED表示RAM托管的权限，CUSTOMER_MANAGED表示租户创建的自定义的权限，ALL表示所有的权限。
        :type permission_type: str
        """
        
        

        self._x_security_token = None
        self._limit = None
        self._marker = None
        self._resource_type = None
        self._permission_type = None
        self.discriminator = None

        if x_security_token is not None:
            self.x_security_token = x_security_token
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if resource_type is not None:
            self.resource_type = resource_type
        if permission_type is not None:
            self.permission_type = permission_type

    @property
    def x_security_token(self):
        r"""Gets the x_security_token of this ListPermissionsRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this ListPermissionsRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        r"""Sets the x_security_token of this ListPermissionsRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this ListPermissionsRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def limit(self):
        r"""Gets the limit of this ListPermissionsRequest.

        分页页面的最大值。

        :return: The limit of this ListPermissionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPermissionsRequest.

        分页页面的最大值。

        :param limit: The limit of this ListPermissionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListPermissionsRequest.

        页面标记。

        :return: The marker of this ListPermissionsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListPermissionsRequest.

        页面标记。

        :param marker: The marker of this ListPermissionsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListPermissionsRequest.

        资源类型的名称。

        :return: The resource_type of this ListPermissionsRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListPermissionsRequest.

        资源类型的名称。

        :param resource_type: The resource_type of this ListPermissionsRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def permission_type(self):
        r"""Gets the permission_type of this ListPermissionsRequest.

        权限类型。RAM_MANAGED表示RAM托管的权限，CUSTOMER_MANAGED表示租户创建的自定义的权限，ALL表示所有的权限。

        :return: The permission_type of this ListPermissionsRequest.
        :rtype: str
        """
        return self._permission_type

    @permission_type.setter
    def permission_type(self, permission_type):
        r"""Sets the permission_type of this ListPermissionsRequest.

        权限类型。RAM_MANAGED表示RAM托管的权限，CUSTOMER_MANAGED表示租户创建的自定义的权限，ALL表示所有的权限。

        :param permission_type: The permission_type of this ListPermissionsRequest.
        :type permission_type: str
        """
        self._permission_type = permission_type

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
        if not isinstance(other, ListPermissionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
