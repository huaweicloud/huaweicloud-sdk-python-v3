# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceInstancesRequest:

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
        'offset': 'str',
        'resource_type': 'str',
        'body': 'ResourceInstanceReqBody'
    }

    attribute_map = {
        'x_security_token': 'X-Security-Token',
        'limit': 'limit',
        'offset': 'offset',
        'resource_type': 'resource_type',
        'body': 'body'
    }

    def __init__(self, x_security_token=None, limit=None, offset=None, resource_type=None, body=None):
        """ListResourceInstancesRequest

        The model defined in huaweicloud sdk

        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param limit: 页面中最大结果数量。
        :type limit: int
        :param offset: 分页标记。
        :type offset: str
        :param resource_type: 资源类型。枚举值：organizations:policies（服务策略）、organizations:ous（组织OU）、organizations:accounts（账号信息） 、organizations:roots：（根）。
        :type resource_type: str
        :param body: Body of the ListResourceInstancesRequest
        :type body: :class:`huaweicloudsdkorganizations.v1.ResourceInstanceReqBody`
        """
        
        

        self._x_security_token = None
        self._limit = None
        self._offset = None
        self._resource_type = None
        self._body = None
        self.discriminator = None

        if x_security_token is not None:
            self.x_security_token = x_security_token
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.resource_type = resource_type
        if body is not None:
            self.body = body

    @property
    def x_security_token(self):
        """Gets the x_security_token of this ListResourceInstancesRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this ListResourceInstancesRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        """Sets the x_security_token of this ListResourceInstancesRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this ListResourceInstancesRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def limit(self):
        """Gets the limit of this ListResourceInstancesRequest.

        页面中最大结果数量。

        :return: The limit of this ListResourceInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListResourceInstancesRequest.

        页面中最大结果数量。

        :param limit: The limit of this ListResourceInstancesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListResourceInstancesRequest.

        分页标记。

        :return: The offset of this ListResourceInstancesRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListResourceInstancesRequest.

        分页标记。

        :param offset: The offset of this ListResourceInstancesRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def resource_type(self):
        """Gets the resource_type of this ListResourceInstancesRequest.

        资源类型。枚举值：organizations:policies（服务策略）、organizations:ous（组织OU）、organizations:accounts（账号信息） 、organizations:roots：（根）。

        :return: The resource_type of this ListResourceInstancesRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ListResourceInstancesRequest.

        资源类型。枚举值：organizations:policies（服务策略）、organizations:ous（组织OU）、organizations:accounts（账号信息） 、organizations:roots：（根）。

        :param resource_type: The resource_type of this ListResourceInstancesRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def body(self):
        """Gets the body of this ListResourceInstancesRequest.

        :return: The body of this ListResourceInstancesRequest.
        :rtype: :class:`huaweicloudsdkorganizations.v1.ResourceInstanceReqBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListResourceInstancesRequest.

        :param body: The body of this ListResourceInstancesRequest.
        :type body: :class:`huaweicloudsdkorganizations.v1.ResourceInstanceReqBody`
        """
        self._body = body

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
        if not isinstance(other, ListResourceInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
