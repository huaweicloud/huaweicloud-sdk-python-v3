# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulScanTaskStatisticsResponseInfoLastScanTaskRiskyHostNum:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'urgent_vul': 'int'
    }

    attribute_map = {
        'urgent_vul': 'urgent_vul'
    }

    def __init__(self, urgent_vul=None):
        r"""VulScanTaskStatisticsResponseInfoLastScanTaskRiskyHostNum

        The model defined in huaweicloud sdk

        :param urgent_vul: **参数解释**: 应急漏洞影响的主机数 **取值范围**: 最小值0，最大值2147483647 
        :type urgent_vul: int
        """
        
        

        self._urgent_vul = None
        self.discriminator = None

        if urgent_vul is not None:
            self.urgent_vul = urgent_vul

    @property
    def urgent_vul(self):
        r"""Gets the urgent_vul of this VulScanTaskStatisticsResponseInfoLastScanTaskRiskyHostNum.

        **参数解释**: 应急漏洞影响的主机数 **取值范围**: 最小值0，最大值2147483647 

        :return: The urgent_vul of this VulScanTaskStatisticsResponseInfoLastScanTaskRiskyHostNum.
        :rtype: int
        """
        return self._urgent_vul

    @urgent_vul.setter
    def urgent_vul(self, urgent_vul):
        r"""Sets the urgent_vul of this VulScanTaskStatisticsResponseInfoLastScanTaskRiskyHostNum.

        **参数解释**: 应急漏洞影响的主机数 **取值范围**: 最小值0，最大值2147483647 

        :param urgent_vul: The urgent_vul of this VulScanTaskStatisticsResponseInfoLastScanTaskRiskyHostNum.
        :type urgent_vul: int
        """
        self._urgent_vul = urgent_vul

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VulScanTaskStatisticsResponseInfoLastScanTaskRiskyHostNum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
