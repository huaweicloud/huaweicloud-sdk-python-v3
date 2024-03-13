# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Ipv6Bandwidth:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'bandwidth_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'bandwidth_type': 'bandwidth_type'
    }

    def __init__(self, id=None, bandwidth_type=None):
        """Ipv6Bandwidth

        The model defined in huaweicloud sdk

        :param id: IPv6带宽的ID。
        :type id: str
        :param bandwidth_type: 带宽类型。  指定带宽ID，则该参数不生效。 不指定带宽的情况下，如果当前带宽类型下没有带宽，自动在该带宽类型下创建带宽，有则使用最近创建的带宽。 约束：指定的bandwidth_type必须在对应弹性公网IP类型的allow_share_bandwidth_types中才能使用
        :type bandwidth_type: str
        """
        
        

        self._id = None
        self._bandwidth_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if bandwidth_type is not None:
            self.bandwidth_type = bandwidth_type

    @property
    def id(self):
        """Gets the id of this Ipv6Bandwidth.

        IPv6带宽的ID。

        :return: The id of this Ipv6Bandwidth.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Ipv6Bandwidth.

        IPv6带宽的ID。

        :param id: The id of this Ipv6Bandwidth.
        :type id: str
        """
        self._id = id

    @property
    def bandwidth_type(self):
        """Gets the bandwidth_type of this Ipv6Bandwidth.

        带宽类型。  指定带宽ID，则该参数不生效。 不指定带宽的情况下，如果当前带宽类型下没有带宽，自动在该带宽类型下创建带宽，有则使用最近创建的带宽。 约束：指定的bandwidth_type必须在对应弹性公网IP类型的allow_share_bandwidth_types中才能使用

        :return: The bandwidth_type of this Ipv6Bandwidth.
        :rtype: str
        """
        return self._bandwidth_type

    @bandwidth_type.setter
    def bandwidth_type(self, bandwidth_type):
        """Sets the bandwidth_type of this Ipv6Bandwidth.

        带宽类型。  指定带宽ID，则该参数不生效。 不指定带宽的情况下，如果当前带宽类型下没有带宽，自动在该带宽类型下创建带宽，有则使用最近创建的带宽。 约束：指定的bandwidth_type必须在对应弹性公网IP类型的allow_share_bandwidth_types中才能使用

        :param bandwidth_type: The bandwidth_type of this Ipv6Bandwidth.
        :type bandwidth_type: str
        """
        self._bandwidth_type = bandwidth_type

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
        if not isinstance(other, Ipv6Bandwidth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
