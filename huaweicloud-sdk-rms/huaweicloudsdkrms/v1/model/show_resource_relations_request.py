# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourceRelationsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_auth_token')

    openapi_types = {
        'x_auth_token': 'str',
        'resource_id': 'str',
        'direction': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'x_auth_token': 'X-Auth-Token',
        'resource_id': 'resource_id',
        'direction': 'direction',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, x_auth_token=None, resource_id=None, direction=None, limit=None, marker=None):
        """ShowResourceRelationsRequest

        The model defined in huaweicloud sdk

        :param x_auth_token: 用户Token。 获取Token，请参考《统一身份认证服务API参考》的“获取用户Token”章节。请求响应成功后在响应消息头中包含的“X-Subject-Token”的值即为Token值。
        :type x_auth_token: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param direction: 资源关系的指向
        :type direction: str
        :param limit: 最大的返回数量
        :type limit: int
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页
        :type marker: str
        """
        
        

        self._x_auth_token = None
        self._resource_id = None
        self._direction = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.x_auth_token = x_auth_token
        self.resource_id = resource_id
        self.direction = direction
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def x_auth_token(self):
        """Gets the x_auth_token of this ShowResourceRelationsRequest.

        用户Token。 获取Token，请参考《统一身份认证服务API参考》的“获取用户Token”章节。请求响应成功后在响应消息头中包含的“X-Subject-Token”的值即为Token值。

        :return: The x_auth_token of this ShowResourceRelationsRequest.
        :rtype: str
        """
        return self._x_auth_token

    @x_auth_token.setter
    def x_auth_token(self, x_auth_token):
        """Sets the x_auth_token of this ShowResourceRelationsRequest.

        用户Token。 获取Token，请参考《统一身份认证服务API参考》的“获取用户Token”章节。请求响应成功后在响应消息头中包含的“X-Subject-Token”的值即为Token值。

        :param x_auth_token: The x_auth_token of this ShowResourceRelationsRequest.
        :type x_auth_token: str
        """
        self._x_auth_token = x_auth_token

    @property
    def resource_id(self):
        """Gets the resource_id of this ShowResourceRelationsRequest.

        资源ID

        :return: The resource_id of this ShowResourceRelationsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ShowResourceRelationsRequest.

        资源ID

        :param resource_id: The resource_id of this ShowResourceRelationsRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def direction(self):
        """Gets the direction of this ShowResourceRelationsRequest.

        资源关系的指向

        :return: The direction of this ShowResourceRelationsRequest.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this ShowResourceRelationsRequest.

        资源关系的指向

        :param direction: The direction of this ShowResourceRelationsRequest.
        :type direction: str
        """
        self._direction = direction

    @property
    def limit(self):
        """Gets the limit of this ShowResourceRelationsRequest.

        最大的返回数量

        :return: The limit of this ShowResourceRelationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowResourceRelationsRequest.

        最大的返回数量

        :param limit: The limit of this ShowResourceRelationsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ShowResourceRelationsRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :return: The marker of this ShowResourceRelationsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ShowResourceRelationsRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :param marker: The marker of this ShowResourceRelationsRequest.
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
        if not isinstance(other, ShowResourceRelationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
