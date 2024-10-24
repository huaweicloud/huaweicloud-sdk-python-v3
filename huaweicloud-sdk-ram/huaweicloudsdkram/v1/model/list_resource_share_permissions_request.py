# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceSharePermissionsRequest:

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
        'resource_share_id': 'str',
        'permission_name': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'x_security_token': 'X-Security-Token',
        'resource_share_id': 'resource_share_id',
        'permission_name': 'permission_name',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, x_security_token=None, resource_share_id=None, permission_name=None, limit=None, marker=None):
        """ListResourceSharePermissionsRequest

        The model defined in huaweicloud sdk

        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param resource_share_id: 资源共享实例的ID。
        :type resource_share_id: str
        :param permission_name: 共享资源权限的名称。
        :type permission_name: str
        :param limit: 分页页面的最大值。
        :type limit: int
        :param marker: 页面标记。
        :type marker: str
        """
        
        

        self._x_security_token = None
        self._resource_share_id = None
        self._permission_name = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if x_security_token is not None:
            self.x_security_token = x_security_token
        self.resource_share_id = resource_share_id
        if permission_name is not None:
            self.permission_name = permission_name
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def x_security_token(self):
        """Gets the x_security_token of this ListResourceSharePermissionsRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this ListResourceSharePermissionsRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        """Sets the x_security_token of this ListResourceSharePermissionsRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this ListResourceSharePermissionsRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def resource_share_id(self):
        """Gets the resource_share_id of this ListResourceSharePermissionsRequest.

        资源共享实例的ID。

        :return: The resource_share_id of this ListResourceSharePermissionsRequest.
        :rtype: str
        """
        return self._resource_share_id

    @resource_share_id.setter
    def resource_share_id(self, resource_share_id):
        """Sets the resource_share_id of this ListResourceSharePermissionsRequest.

        资源共享实例的ID。

        :param resource_share_id: The resource_share_id of this ListResourceSharePermissionsRequest.
        :type resource_share_id: str
        """
        self._resource_share_id = resource_share_id

    @property
    def permission_name(self):
        """Gets the permission_name of this ListResourceSharePermissionsRequest.

        共享资源权限的名称。

        :return: The permission_name of this ListResourceSharePermissionsRequest.
        :rtype: str
        """
        return self._permission_name

    @permission_name.setter
    def permission_name(self, permission_name):
        """Sets the permission_name of this ListResourceSharePermissionsRequest.

        共享资源权限的名称。

        :param permission_name: The permission_name of this ListResourceSharePermissionsRequest.
        :type permission_name: str
        """
        self._permission_name = permission_name

    @property
    def limit(self):
        """Gets the limit of this ListResourceSharePermissionsRequest.

        分页页面的最大值。

        :return: The limit of this ListResourceSharePermissionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListResourceSharePermissionsRequest.

        分页页面的最大值。

        :param limit: The limit of this ListResourceSharePermissionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListResourceSharePermissionsRequest.

        页面标记。

        :return: The marker of this ListResourceSharePermissionsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListResourceSharePermissionsRequest.

        页面标记。

        :param marker: The marker of this ListResourceSharePermissionsRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListResourceSharePermissionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
