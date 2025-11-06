# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulAffectedStatisticsResponseInfoCceDisabledVulList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_name': 'str',
        'host_id': 'str',
        'vul_name': 'str',
        'vul_id': 'str',
        'operation_description': 'str'
    }

    attribute_map = {
        'host_name': 'host_name',
        'host_id': 'host_id',
        'vul_name': 'vul_name',
        'vul_id': 'vul_id',
        'operation_description': 'operation_description'
    }

    def __init__(self, host_name=None, host_id=None, vul_name=None, vul_id=None, operation_description=None):
        r"""VulAffectedStatisticsResponseInfoCceDisabledVulList

        The model defined in huaweicloud sdk

        :param host_name: **参数解释**: 主机名称 **取值范围**: 字符长度0-64位 
        :type host_name: str
        :param host_id: **参数解释**: 主机id **取值范围**: 字符长度0-64位 
        :type host_id: str
        :param vul_name: **参数解释**: 漏洞名称 **取值范围**: 字符长度0-256位 
        :type vul_name: str
        :param vul_id: **参数解释**: 漏洞补丁编号 **取值范围**: 字符长度0-256 
        :type vul_id: str
        :param operation_description: **参数解释**: 操作提示 **取值范围**: 字符长度0-4096 
        :type operation_description: str
        """
        
        

        self._host_name = None
        self._host_id = None
        self._vul_name = None
        self._vul_id = None
        self._operation_description = None
        self.discriminator = None

        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if vul_name is not None:
            self.vul_name = vul_name
        if vul_id is not None:
            self.vul_id = vul_id
        if operation_description is not None:
            self.operation_description = operation_description

    @property
    def host_name(self):
        r"""Gets the host_name of this VulAffectedStatisticsResponseInfoCceDisabledVulList.

        **参数解释**: 主机名称 **取值范围**: 字符长度0-64位 

        :return: The host_name of this VulAffectedStatisticsResponseInfoCceDisabledVulList.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this VulAffectedStatisticsResponseInfoCceDisabledVulList.

        **参数解释**: 主机名称 **取值范围**: 字符长度0-64位 

        :param host_name: The host_name of this VulAffectedStatisticsResponseInfoCceDisabledVulList.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this VulAffectedStatisticsResponseInfoCceDisabledVulList.

        **参数解释**: 主机id **取值范围**: 字符长度0-64位 

        :return: The host_id of this VulAffectedStatisticsResponseInfoCceDisabledVulList.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this VulAffectedStatisticsResponseInfoCceDisabledVulList.

        **参数解释**: 主机id **取值范围**: 字符长度0-64位 

        :param host_id: The host_id of this VulAffectedStatisticsResponseInfoCceDisabledVulList.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def vul_name(self):
        r"""Gets the vul_name of this VulAffectedStatisticsResponseInfoCceDisabledVulList.

        **参数解释**: 漏洞名称 **取值范围**: 字符长度0-256位 

        :return: The vul_name of this VulAffectedStatisticsResponseInfoCceDisabledVulList.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this VulAffectedStatisticsResponseInfoCceDisabledVulList.

        **参数解释**: 漏洞名称 **取值范围**: 字符长度0-256位 

        :param vul_name: The vul_name of this VulAffectedStatisticsResponseInfoCceDisabledVulList.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def vul_id(self):
        r"""Gets the vul_id of this VulAffectedStatisticsResponseInfoCceDisabledVulList.

        **参数解释**: 漏洞补丁编号 **取值范围**: 字符长度0-256 

        :return: The vul_id of this VulAffectedStatisticsResponseInfoCceDisabledVulList.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this VulAffectedStatisticsResponseInfoCceDisabledVulList.

        **参数解释**: 漏洞补丁编号 **取值范围**: 字符长度0-256 

        :param vul_id: The vul_id of this VulAffectedStatisticsResponseInfoCceDisabledVulList.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def operation_description(self):
        r"""Gets the operation_description of this VulAffectedStatisticsResponseInfoCceDisabledVulList.

        **参数解释**: 操作提示 **取值范围**: 字符长度0-4096 

        :return: The operation_description of this VulAffectedStatisticsResponseInfoCceDisabledVulList.
        :rtype: str
        """
        return self._operation_description

    @operation_description.setter
    def operation_description(self, operation_description):
        r"""Sets the operation_description of this VulAffectedStatisticsResponseInfoCceDisabledVulList.

        **参数解释**: 操作提示 **取值范围**: 字符长度0-4096 

        :param operation_description: The operation_description of this VulAffectedStatisticsResponseInfoCceDisabledVulList.
        :type operation_description: str
        """
        self._operation_description = operation_description

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
        if not isinstance(other, VulAffectedStatisticsResponseInfoCceDisabledVulList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
