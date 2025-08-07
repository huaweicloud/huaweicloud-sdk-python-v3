# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpReputationMapResponseBodyIpReputationMap:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'idc': 'list[str]'
    }

    attribute_map = {
        'idc': 'idc'
    }

    def __init__(self, idc=None):
        r"""IpReputationMapResponseBodyIpReputationMap

        The model defined in huaweicloud sdk

        :param idc: **参数解释：** 威胁情报控制的内容类型 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type idc: list[str]
        """
        
        

        self._idc = None
        self.discriminator = None

        if idc is not None:
            self.idc = idc

    @property
    def idc(self):
        r"""Gets the idc of this IpReputationMapResponseBodyIpReputationMap.

        **参数解释：** 威胁情报控制的内容类型 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The idc of this IpReputationMapResponseBodyIpReputationMap.
        :rtype: list[str]
        """
        return self._idc

    @idc.setter
    def idc(self, idc):
        r"""Sets the idc of this IpReputationMapResponseBodyIpReputationMap.

        **参数解释：** 威胁情报控制的内容类型 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param idc: The idc of this IpReputationMapResponseBodyIpReputationMap.
        :type idc: list[str]
        """
        self._idc = idc

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
        if not isinstance(other, IpReputationMapResponseBodyIpReputationMap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
