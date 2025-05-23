# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutopilotEniNetworkUpdate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subnets': 'list[AutopilotNetworkSubnet]'
    }

    attribute_map = {
        'subnets': 'subnets'
    }

    def __init__(self, subnets=None):
        r"""AutopilotEniNetworkUpdate

        The model defined in huaweicloud sdk

        :param subnets: IPv4子网ID列表。 只允许新增子网，不可删除已有子网，请谨慎选择。  请求体中需包含所有已经存在的subnet。
        :type subnets: list[:class:`huaweicloudsdkcce.v3.AutopilotNetworkSubnet`]
        """
        
        

        self._subnets = None
        self.discriminator = None

        if subnets is not None:
            self.subnets = subnets

    @property
    def subnets(self):
        r"""Gets the subnets of this AutopilotEniNetworkUpdate.

        IPv4子网ID列表。 只允许新增子网，不可删除已有子网，请谨慎选择。  请求体中需包含所有已经存在的subnet。

        :return: The subnets of this AutopilotEniNetworkUpdate.
        :rtype: list[:class:`huaweicloudsdkcce.v3.AutopilotNetworkSubnet`]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        r"""Sets the subnets of this AutopilotEniNetworkUpdate.

        IPv4子网ID列表。 只允许新增子网，不可删除已有子网，请谨慎选择。  请求体中需包含所有已经存在的subnet。

        :param subnets: The subnets of this AutopilotEniNetworkUpdate.
        :type subnets: list[:class:`huaweicloudsdkcce.v3.AutopilotNetworkSubnet`]
        """
        self._subnets = subnets

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
        if not isinstance(other, AutopilotEniNetworkUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
