# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllResourcesRequest:

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
        'region_id': 'str',
        'ep_id': 'str',
        'type': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'x_auth_token': 'X-Auth-Token',
        'region_id': 'region_id',
        'ep_id': 'ep_id',
        'type': 'type',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, x_auth_token=None, region_id=None, ep_id=None, type=None, limit=None, marker=None):
        """ListAllResourcesRequest

        The model defined in huaweicloud sdk

        :param x_auth_token: 用户Token。 获取Token，请参考《统一身份认证服务API参考》的“获取用户Token”章节。请求响应成功后在响应消息头中包含的“X-Subject-Token”的值即为Token值。
        :type x_auth_token: str
        :param region_id: 区域ID
        :type region_id: str
        :param ep_id: 企业项目ID
        :type ep_id: str
        :param type: 资源类型（provider.type）
        :type type: str
        :param limit: 最大的返回数量
        :type limit: int
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页
        :type marker: str
        """
        
        

        self._x_auth_token = None
        self._region_id = None
        self._ep_id = None
        self._type = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.x_auth_token = x_auth_token
        if region_id is not None:
            self.region_id = region_id
        if ep_id is not None:
            self.ep_id = ep_id
        if type is not None:
            self.type = type
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def x_auth_token(self):
        """Gets the x_auth_token of this ListAllResourcesRequest.

        用户Token。 获取Token，请参考《统一身份认证服务API参考》的“获取用户Token”章节。请求响应成功后在响应消息头中包含的“X-Subject-Token”的值即为Token值。

        :return: The x_auth_token of this ListAllResourcesRequest.
        :rtype: str
        """
        return self._x_auth_token

    @x_auth_token.setter
    def x_auth_token(self, x_auth_token):
        """Sets the x_auth_token of this ListAllResourcesRequest.

        用户Token。 获取Token，请参考《统一身份认证服务API参考》的“获取用户Token”章节。请求响应成功后在响应消息头中包含的“X-Subject-Token”的值即为Token值。

        :param x_auth_token: The x_auth_token of this ListAllResourcesRequest.
        :type x_auth_token: str
        """
        self._x_auth_token = x_auth_token

    @property
    def region_id(self):
        """Gets the region_id of this ListAllResourcesRequest.

        区域ID

        :return: The region_id of this ListAllResourcesRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ListAllResourcesRequest.

        区域ID

        :param region_id: The region_id of this ListAllResourcesRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def ep_id(self):
        """Gets the ep_id of this ListAllResourcesRequest.

        企业项目ID

        :return: The ep_id of this ListAllResourcesRequest.
        :rtype: str
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        """Sets the ep_id of this ListAllResourcesRequest.

        企业项目ID

        :param ep_id: The ep_id of this ListAllResourcesRequest.
        :type ep_id: str
        """
        self._ep_id = ep_id

    @property
    def type(self):
        """Gets the type of this ListAllResourcesRequest.

        资源类型（provider.type）

        :return: The type of this ListAllResourcesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListAllResourcesRequest.

        资源类型（provider.type）

        :param type: The type of this ListAllResourcesRequest.
        :type type: str
        """
        self._type = type

    @property
    def limit(self):
        """Gets the limit of this ListAllResourcesRequest.

        最大的返回数量

        :return: The limit of this ListAllResourcesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAllResourcesRequest.

        最大的返回数量

        :param limit: The limit of this ListAllResourcesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListAllResourcesRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :return: The marker of this ListAllResourcesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListAllResourcesRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :param marker: The marker of this ListAllResourcesRequest.
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
        if not isinstance(other, ListAllResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
