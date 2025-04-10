# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateForwardingInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_snat': 'bool'
    }

    attribute_map = {
        'enable_snat': 'enable_snat'
    }

    def __init__(self, enable_snat=None):
        r"""UpdateForwardingInfo

        The model defined in huaweicloud sdk

        :param enable_snat: **参数说明**：是否启用SNAT配置。企业版实例开启SNAT配置后，可以在公共网络中进行外部通信。 约束：只有企业版实例支持配置SNAT配置，SNAT配置开启后将不支持关闭 **取值范围**： - true: 启用SNAT配置 
        :type enable_snat: bool
        """
        
        

        self._enable_snat = None
        self.discriminator = None

        self.enable_snat = enable_snat

    @property
    def enable_snat(self):
        r"""Gets the enable_snat of this UpdateForwardingInfo.

        **参数说明**：是否启用SNAT配置。企业版实例开启SNAT配置后，可以在公共网络中进行外部通信。 约束：只有企业版实例支持配置SNAT配置，SNAT配置开启后将不支持关闭 **取值范围**： - true: 启用SNAT配置 

        :return: The enable_snat of this UpdateForwardingInfo.
        :rtype: bool
        """
        return self._enable_snat

    @enable_snat.setter
    def enable_snat(self, enable_snat):
        r"""Sets the enable_snat of this UpdateForwardingInfo.

        **参数说明**：是否启用SNAT配置。企业版实例开启SNAT配置后，可以在公共网络中进行外部通信。 约束：只有企业版实例支持配置SNAT配置，SNAT配置开启后将不支持关闭 **取值范围**： - true: 启用SNAT配置 

        :param enable_snat: The enable_snat of this UpdateForwardingInfo.
        :type enable_snat: bool
        """
        self._enable_snat = enable_snat

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
        if not isinstance(other, UpdateForwardingInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
