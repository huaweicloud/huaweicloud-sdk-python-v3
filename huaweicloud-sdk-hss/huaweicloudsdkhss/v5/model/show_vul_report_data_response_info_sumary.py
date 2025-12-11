# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVulReportDataResponseInfoSumary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vul_num_repair_necessity': 'int'
    }

    attribute_map = {
        'vul_num_repair_necessity': 'vul_num_repair_necessity'
    }

    def __init__(self, vul_num_repair_necessity=None):
        r"""ShowVulReportDataResponseInfoSumary

        The model defined in huaweicloud sdk

        :param vul_num_repair_necessity: **参数解释**: 紧急修复漏洞数量 **取值范围**: 最小值0，最大值1000000 
        :type vul_num_repair_necessity: int
        """
        
        

        self._vul_num_repair_necessity = None
        self.discriminator = None

        if vul_num_repair_necessity is not None:
            self.vul_num_repair_necessity = vul_num_repair_necessity

    @property
    def vul_num_repair_necessity(self):
        r"""Gets the vul_num_repair_necessity of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: 紧急修复漏洞数量 **取值范围**: 最小值0，最大值1000000 

        :return: The vul_num_repair_necessity of this ShowVulReportDataResponseInfoSumary.
        :rtype: int
        """
        return self._vul_num_repair_necessity

    @vul_num_repair_necessity.setter
    def vul_num_repair_necessity(self, vul_num_repair_necessity):
        r"""Sets the vul_num_repair_necessity of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: 紧急修复漏洞数量 **取值范围**: 最小值0，最大值1000000 

        :param vul_num_repair_necessity: The vul_num_repair_necessity of this ShowVulReportDataResponseInfoSumary.
        :type vul_num_repair_necessity: int
        """
        self._vul_num_repair_necessity = vul_num_repair_necessity

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
        if not isinstance(other, ShowVulReportDataResponseInfoSumary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
