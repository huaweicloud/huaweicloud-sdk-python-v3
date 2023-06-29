# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpVirtual:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool'
    }

    attribute_map = {
        'enable': 'enable'
    }

    def __init__(self, enable=None):
        """IpVirtual

        The model defined in huaweicloud sdk

        :param enable: 是否启用虚拟IP功能。 启用虚拟IP功能将占用额外的ip地址，注意合理规划网络ip数量。 约束： * 只支持windows镜像。 * 只支持在创建服务器组时设置功能开关，不支持更新功能开关。 * 只支持具备dhcp动态分配ip能力的网络。
        :type enable: bool
        """
        
        

        self._enable = None
        self.discriminator = None

        self.enable = enable

    @property
    def enable(self):
        """Gets the enable of this IpVirtual.

        是否启用虚拟IP功能。 启用虚拟IP功能将占用额外的ip地址，注意合理规划网络ip数量。 约束： * 只支持windows镜像。 * 只支持在创建服务器组时设置功能开关，不支持更新功能开关。 * 只支持具备dhcp动态分配ip能力的网络。

        :return: The enable of this IpVirtual.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this IpVirtual.

        是否启用虚拟IP功能。 启用虚拟IP功能将占用额外的ip地址，注意合理规划网络ip数量。 约束： * 只支持windows镜像。 * 只支持在创建服务器组时设置功能开关，不支持更新功能开关。 * 只支持具备dhcp动态分配ip能力的网络。

        :param enable: The enable of this IpVirtual.
        :type enable: bool
        """
        self._enable = enable

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
        if not isinstance(other, IpVirtual):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
