# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulWhiteListDetailResponseInfo:

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
        'vul_id': 'str',
        'vul_name': 'str',
        'vul_type': 'str',
        'cves': 'list[VulWhiteListDetailResponseInfoCves]',
        'rule_type': 'str',
        'hosts': 'list[VulWhiteListDetailResponseInfoHosts]',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'vul_id': 'vul_id',
        'vul_name': 'vul_name',
        'vul_type': 'vul_type',
        'cves': 'cves',
        'rule_type': 'rule_type',
        'hosts': 'hosts',
        'description': 'description'
    }

    def __init__(self, id=None, vul_id=None, vul_name=None, vul_type=None, cves=None, rule_type=None, hosts=None, description=None):
        r"""VulWhiteListDetailResponseInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**: 白名单id **取值范围**: 字符长度0-256 
        :type id: str
        :param vul_id: **参数解释**: 漏洞id **取值范围**: 字符长度0-256 
        :type vul_id: str
        :param vul_name: **参数解释**: 漏洞名称 **取值范围**: 字符长度0-256 
        :type vul_name: str
        :param vul_type: **参数解释**: 漏洞类型 **取值范围**: - linux_vul：linux漏洞 - windows_vul：windows漏洞 - web_cms：Web-CMS漏洞 - app_vul：应用漏洞 
        :type vul_type: str
        :param cves: **参数解释**: 漏洞对应的cve列表 **取值范围**: 最小值0，最大值2147483647 
        :type cves: list[:class:`huaweicloudsdkhss.v5.VulWhiteListDetailResponseInfoCves`]
        :param rule_type: **参数解释**: 白名单规则类型 **取值范围**: - all_host：白名单应用于全部主机 - specific_host：白名单应用于指定主机 
        :type rule_type: str
        :param hosts: **参数解释**: 白名单规则为“指定主机”时，指定的主机列表 **取值范围**: 最小值0，最大值2147483647 
        :type hosts: list[:class:`huaweicloudsdkhss.v5.VulWhiteListDetailResponseInfoHosts`]
        :param description: **参数解释**: 白名单的描述信息 **取值范围**: 字符长度0-1000 
        :type description: str
        """
        
        

        self._id = None
        self._vul_id = None
        self._vul_name = None
        self._vul_type = None
        self._cves = None
        self._rule_type = None
        self._hosts = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if vul_id is not None:
            self.vul_id = vul_id
        if vul_name is not None:
            self.vul_name = vul_name
        if vul_type is not None:
            self.vul_type = vul_type
        if cves is not None:
            self.cves = cves
        if rule_type is not None:
            self.rule_type = rule_type
        if hosts is not None:
            self.hosts = hosts
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this VulWhiteListDetailResponseInfo.

        **参数解释**: 白名单id **取值范围**: 字符长度0-256 

        :return: The id of this VulWhiteListDetailResponseInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VulWhiteListDetailResponseInfo.

        **参数解释**: 白名单id **取值范围**: 字符长度0-256 

        :param id: The id of this VulWhiteListDetailResponseInfo.
        :type id: str
        """
        self._id = id

    @property
    def vul_id(self):
        r"""Gets the vul_id of this VulWhiteListDetailResponseInfo.

        **参数解释**: 漏洞id **取值范围**: 字符长度0-256 

        :return: The vul_id of this VulWhiteListDetailResponseInfo.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this VulWhiteListDetailResponseInfo.

        **参数解释**: 漏洞id **取值范围**: 字符长度0-256 

        :param vul_id: The vul_id of this VulWhiteListDetailResponseInfo.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def vul_name(self):
        r"""Gets the vul_name of this VulWhiteListDetailResponseInfo.

        **参数解释**: 漏洞名称 **取值范围**: 字符长度0-256 

        :return: The vul_name of this VulWhiteListDetailResponseInfo.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this VulWhiteListDetailResponseInfo.

        **参数解释**: 漏洞名称 **取值范围**: 字符长度0-256 

        :param vul_name: The vul_name of this VulWhiteListDetailResponseInfo.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def vul_type(self):
        r"""Gets the vul_type of this VulWhiteListDetailResponseInfo.

        **参数解释**: 漏洞类型 **取值范围**: - linux_vul：linux漏洞 - windows_vul：windows漏洞 - web_cms：Web-CMS漏洞 - app_vul：应用漏洞 

        :return: The vul_type of this VulWhiteListDetailResponseInfo.
        :rtype: str
        """
        return self._vul_type

    @vul_type.setter
    def vul_type(self, vul_type):
        r"""Sets the vul_type of this VulWhiteListDetailResponseInfo.

        **参数解释**: 漏洞类型 **取值范围**: - linux_vul：linux漏洞 - windows_vul：windows漏洞 - web_cms：Web-CMS漏洞 - app_vul：应用漏洞 

        :param vul_type: The vul_type of this VulWhiteListDetailResponseInfo.
        :type vul_type: str
        """
        self._vul_type = vul_type

    @property
    def cves(self):
        r"""Gets the cves of this VulWhiteListDetailResponseInfo.

        **参数解释**: 漏洞对应的cve列表 **取值范围**: 最小值0，最大值2147483647 

        :return: The cves of this VulWhiteListDetailResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.VulWhiteListDetailResponseInfoCves`]
        """
        return self._cves

    @cves.setter
    def cves(self, cves):
        r"""Sets the cves of this VulWhiteListDetailResponseInfo.

        **参数解释**: 漏洞对应的cve列表 **取值范围**: 最小值0，最大值2147483647 

        :param cves: The cves of this VulWhiteListDetailResponseInfo.
        :type cves: list[:class:`huaweicloudsdkhss.v5.VulWhiteListDetailResponseInfoCves`]
        """
        self._cves = cves

    @property
    def rule_type(self):
        r"""Gets the rule_type of this VulWhiteListDetailResponseInfo.

        **参数解释**: 白名单规则类型 **取值范围**: - all_host：白名单应用于全部主机 - specific_host：白名单应用于指定主机 

        :return: The rule_type of this VulWhiteListDetailResponseInfo.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this VulWhiteListDetailResponseInfo.

        **参数解释**: 白名单规则类型 **取值范围**: - all_host：白名单应用于全部主机 - specific_host：白名单应用于指定主机 

        :param rule_type: The rule_type of this VulWhiteListDetailResponseInfo.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def hosts(self):
        r"""Gets the hosts of this VulWhiteListDetailResponseInfo.

        **参数解释**: 白名单规则为“指定主机”时，指定的主机列表 **取值范围**: 最小值0，最大值2147483647 

        :return: The hosts of this VulWhiteListDetailResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.VulWhiteListDetailResponseInfoHosts`]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        r"""Sets the hosts of this VulWhiteListDetailResponseInfo.

        **参数解释**: 白名单规则为“指定主机”时，指定的主机列表 **取值范围**: 最小值0，最大值2147483647 

        :param hosts: The hosts of this VulWhiteListDetailResponseInfo.
        :type hosts: list[:class:`huaweicloudsdkhss.v5.VulWhiteListDetailResponseInfoHosts`]
        """
        self._hosts = hosts

    @property
    def description(self):
        r"""Gets the description of this VulWhiteListDetailResponseInfo.

        **参数解释**: 白名单的描述信息 **取值范围**: 字符长度0-1000 

        :return: The description of this VulWhiteListDetailResponseInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this VulWhiteListDetailResponseInfo.

        **参数解释**: 白名单的描述信息 **取值范围**: 字符长度0-1000 

        :param description: The description of this VulWhiteListDetailResponseInfo.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, VulWhiteListDetailResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
