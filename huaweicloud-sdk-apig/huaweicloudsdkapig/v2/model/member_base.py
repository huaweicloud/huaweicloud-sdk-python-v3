# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MemberBase:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'host': 'str',
        'weight': 'int'
    }

    attribute_map = {
        'host': 'host',
        'weight': 'weight'
    }

    def __init__(self, host=None, weight=None):
        """MemberBase - a model defined in huaweicloud sdk"""
        
        

        self._host = None
        self._weight = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if weight is not None:
            self.weight = weight

    @property
    def host(self):
        """Gets the host of this MemberBase.

        后端服务器地址  后端实例类型为ip时生效

        :return: The host of this MemberBase.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this MemberBase.

        后端服务器地址  后端实例类型为ip时生效

        :param host: The host of this MemberBase.
        :type: str
        """
        self._host = host

    @property
    def weight(self):
        """Gets the weight of this MemberBase.

        权重值。  允许您对云服务器进行评级，权重值越大，转发到该云服务的请求数量越多。权重只对加权轮询和加权最小连接算法生效  仅VPC通道类型为2时有效。

        :return: The weight of this MemberBase.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this MemberBase.

        权重值。  允许您对云服务器进行评级，权重值越大，转发到该云服务的请求数量越多。权重只对加权轮询和加权最小连接算法生效  仅VPC通道类型为2时有效。

        :param weight: The weight of this MemberBase.
        :type: int
        """
        self._weight = weight

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
        if not isinstance(other, MemberBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
