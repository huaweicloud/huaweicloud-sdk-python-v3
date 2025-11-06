# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulWhiteListVulOptionsResponseInfoDataList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vul_id': 'str',
        'vul_name': 'str'
    }

    attribute_map = {
        'vul_id': 'vul_id',
        'vul_name': 'vul_name'
    }

    def __init__(self, vul_id=None, vul_name=None):
        r"""VulWhiteListVulOptionsResponseInfoDataList

        The model defined in huaweicloud sdk

        :param vul_id: **参数解释**: 漏洞id **取值范围**: 字符长度0-256 
        :type vul_id: str
        :param vul_name: **参数解释**: 漏洞名称 **取值范围**: 字符长度0-256 
        :type vul_name: str
        """
        
        

        self._vul_id = None
        self._vul_name = None
        self.discriminator = None

        if vul_id is not None:
            self.vul_id = vul_id
        if vul_name is not None:
            self.vul_name = vul_name

    @property
    def vul_id(self):
        r"""Gets the vul_id of this VulWhiteListVulOptionsResponseInfoDataList.

        **参数解释**: 漏洞id **取值范围**: 字符长度0-256 

        :return: The vul_id of this VulWhiteListVulOptionsResponseInfoDataList.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this VulWhiteListVulOptionsResponseInfoDataList.

        **参数解释**: 漏洞id **取值范围**: 字符长度0-256 

        :param vul_id: The vul_id of this VulWhiteListVulOptionsResponseInfoDataList.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def vul_name(self):
        r"""Gets the vul_name of this VulWhiteListVulOptionsResponseInfoDataList.

        **参数解释**: 漏洞名称 **取值范围**: 字符长度0-256 

        :return: The vul_name of this VulWhiteListVulOptionsResponseInfoDataList.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this VulWhiteListVulOptionsResponseInfoDataList.

        **参数解释**: 漏洞名称 **取值范围**: 字符长度0-256 

        :param vul_name: The vul_name of this VulWhiteListVulOptionsResponseInfoDataList.
        :type vul_name: str
        """
        self._vul_name = vul_name

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
        if not isinstance(other, VulWhiteListVulOptionsResponseInfoDataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
