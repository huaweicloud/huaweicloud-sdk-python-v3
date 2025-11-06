# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulAffectedStatisticsResponseInfoDataList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'vul_num': 'int'
    }

    attribute_map = {
        'type': 'type',
        'vul_num': 'vul_num'
    }

    def __init__(self, type=None, vul_num=None):
        r"""VulAffectedStatisticsResponseInfoDataList

        The model defined in huaweicloud sdk

        :param type: **参数解释**: 漏洞类型 **取值范围**: - linux_vul：linux漏洞 - windows_vul：windows漏洞 - web_cms：Web-CMS漏洞 - app_vul：应用漏洞 - urgent_vul：应急漏洞 
        :type type: str
        :param vul_num: **参数解释**: 该漏洞类型的漏洞数量 **取值范围**: 最小值0，最大值2147483647 
        :type vul_num: int
        """
        
        

        self._type = None
        self._vul_num = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if vul_num is not None:
            self.vul_num = vul_num

    @property
    def type(self):
        r"""Gets the type of this VulAffectedStatisticsResponseInfoDataList.

        **参数解释**: 漏洞类型 **取值范围**: - linux_vul：linux漏洞 - windows_vul：windows漏洞 - web_cms：Web-CMS漏洞 - app_vul：应用漏洞 - urgent_vul：应急漏洞 

        :return: The type of this VulAffectedStatisticsResponseInfoDataList.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this VulAffectedStatisticsResponseInfoDataList.

        **参数解释**: 漏洞类型 **取值范围**: - linux_vul：linux漏洞 - windows_vul：windows漏洞 - web_cms：Web-CMS漏洞 - app_vul：应用漏洞 - urgent_vul：应急漏洞 

        :param type: The type of this VulAffectedStatisticsResponseInfoDataList.
        :type type: str
        """
        self._type = type

    @property
    def vul_num(self):
        r"""Gets the vul_num of this VulAffectedStatisticsResponseInfoDataList.

        **参数解释**: 该漏洞类型的漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The vul_num of this VulAffectedStatisticsResponseInfoDataList.
        :rtype: int
        """
        return self._vul_num

    @vul_num.setter
    def vul_num(self, vul_num):
        r"""Sets the vul_num of this VulAffectedStatisticsResponseInfoDataList.

        **参数解释**: 该漏洞类型的漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :param vul_num: The vul_num of this VulAffectedStatisticsResponseInfoDataList.
        :type vul_num: int
        """
        self._vul_num = vul_num

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
        if not isinstance(other, VulAffectedStatisticsResponseInfoDataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
