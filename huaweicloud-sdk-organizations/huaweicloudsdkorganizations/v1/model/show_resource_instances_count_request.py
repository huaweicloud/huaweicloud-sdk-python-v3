# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourceInstancesCountRequest:

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
        'resource_type': 'str',
        'body': 'ResourceInstanceReqBody'
    }

    attribute_map = {
        'x_security_token': 'X-Security-Token',
        'resource_type': 'resource_type',
        'body': 'body'
    }

    def __init__(self, x_security_token=None, resource_type=None, body=None):
        """ShowResourceInstancesCountRequest

        The model defined in huaweicloud sdk

        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param resource_type: 资源类型。枚举值：organizations:policies（服务策略）、organizations:ous（组织OU）、organizations:accounts（账号信息） 、organizations:roots：（根）。
        :type resource_type: str
        :param body: Body of the ShowResourceInstancesCountRequest
        :type body: :class:`huaweicloudsdkorganizations.v1.ResourceInstanceReqBody`
        """
        
        

        self._x_security_token = None
        self._resource_type = None
        self._body = None
        self.discriminator = None

        if x_security_token is not None:
            self.x_security_token = x_security_token
        self.resource_type = resource_type
        if body is not None:
            self.body = body

    @property
    def x_security_token(self):
        """Gets the x_security_token of this ShowResourceInstancesCountRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this ShowResourceInstancesCountRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        """Sets the x_security_token of this ShowResourceInstancesCountRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this ShowResourceInstancesCountRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def resource_type(self):
        """Gets the resource_type of this ShowResourceInstancesCountRequest.

        资源类型。枚举值：organizations:policies（服务策略）、organizations:ous（组织OU）、organizations:accounts（账号信息） 、organizations:roots：（根）。

        :return: The resource_type of this ShowResourceInstancesCountRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ShowResourceInstancesCountRequest.

        资源类型。枚举值：organizations:policies（服务策略）、organizations:ous（组织OU）、organizations:accounts（账号信息） 、organizations:roots：（根）。

        :param resource_type: The resource_type of this ShowResourceInstancesCountRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def body(self):
        """Gets the body of this ShowResourceInstancesCountRequest.

        :return: The body of this ShowResourceInstancesCountRequest.
        :rtype: :class:`huaweicloudsdkorganizations.v1.ResourceInstanceReqBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ShowResourceInstancesCountRequest.

        :param body: The body of this ShowResourceInstancesCountRequest.
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
        if not isinstance(other, ShowResourceInstancesCountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
