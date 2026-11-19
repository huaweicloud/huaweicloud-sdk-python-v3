# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVulAffectInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'host_id': 'str',
        'vul_type': 'str',
        'vul_id': 'str',
        'handle_status': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'host_id': 'host_id',
        'vul_type': 'vul_type',
        'vul_id': 'vul_id',
        'handle_status': 'handle_status'
    }

    def __init__(self, enterprise_project_id=None, host_id=None, vul_type=None, vul_id=None, handle_status=None):
        r"""ShowVulAffectInfoRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param host_id: **参数解释**: 主机ID，不传时查询该漏洞影响范围内的所有主机 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type host_id: str
        :param vul_type: **参数解释**: 漏洞类型 **约束限制**: 不涉及 **取值范围**: - linux_vul：Linux漏洞。 - windows_vul：Windows漏洞。 - web_cms：Web-CMS漏洞。 - app_vul：应用漏洞。 - urgent_vul：应急漏洞。  **默认取值**: 不涉及 
        :type vul_type: str
        :param vul_id: **参数解释**: 漏洞ID **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type vul_id: str
        :param handle_status: **参数解释**: 漏洞处理状态 **约束限制**: 不涉及 **取值范围**: - handled：已处理。 - unhandled：未处理。  **默认取值**: 不涉及 
        :type handle_status: str
        """
        
        

        self._enterprise_project_id = None
        self._host_id = None
        self._vul_type = None
        self._vul_id = None
        self._handle_status = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if host_id is not None:
            self.host_id = host_id
        if vul_type is not None:
            self.vul_type = vul_type
        self.vul_id = vul_id
        if handle_status is not None:
            self.handle_status = handle_status

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowVulAffectInfoRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ShowVulAffectInfoRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowVulAffectInfoRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ShowVulAffectInfoRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def host_id(self):
        r"""Gets the host_id of this ShowVulAffectInfoRequest.

        **参数解释**: 主机ID，不传时查询该漏洞影响范围内的所有主机 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The host_id of this ShowVulAffectInfoRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ShowVulAffectInfoRequest.

        **参数解释**: 主机ID，不传时查询该漏洞影响范围内的所有主机 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param host_id: The host_id of this ShowVulAffectInfoRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def vul_type(self):
        r"""Gets the vul_type of this ShowVulAffectInfoRequest.

        **参数解释**: 漏洞类型 **约束限制**: 不涉及 **取值范围**: - linux_vul：Linux漏洞。 - windows_vul：Windows漏洞。 - web_cms：Web-CMS漏洞。 - app_vul：应用漏洞。 - urgent_vul：应急漏洞。  **默认取值**: 不涉及 

        :return: The vul_type of this ShowVulAffectInfoRequest.
        :rtype: str
        """
        return self._vul_type

    @vul_type.setter
    def vul_type(self, vul_type):
        r"""Sets the vul_type of this ShowVulAffectInfoRequest.

        **参数解释**: 漏洞类型 **约束限制**: 不涉及 **取值范围**: - linux_vul：Linux漏洞。 - windows_vul：Windows漏洞。 - web_cms：Web-CMS漏洞。 - app_vul：应用漏洞。 - urgent_vul：应急漏洞。  **默认取值**: 不涉及 

        :param vul_type: The vul_type of this ShowVulAffectInfoRequest.
        :type vul_type: str
        """
        self._vul_type = vul_type

    @property
    def vul_id(self):
        r"""Gets the vul_id of this ShowVulAffectInfoRequest.

        **参数解释**: 漏洞ID **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The vul_id of this ShowVulAffectInfoRequest.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this ShowVulAffectInfoRequest.

        **参数解释**: 漏洞ID **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param vul_id: The vul_id of this ShowVulAffectInfoRequest.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def handle_status(self):
        r"""Gets the handle_status of this ShowVulAffectInfoRequest.

        **参数解释**: 漏洞处理状态 **约束限制**: 不涉及 **取值范围**: - handled：已处理。 - unhandled：未处理。  **默认取值**: 不涉及 

        :return: The handle_status of this ShowVulAffectInfoRequest.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this ShowVulAffectInfoRequest.

        **参数解释**: 漏洞处理状态 **约束限制**: 不涉及 **取值范围**: - handled：已处理。 - unhandled：未处理。  **默认取值**: 不涉及 

        :param handle_status: The handle_status of this ShowVulAffectInfoRequest.
        :type handle_status: str
        """
        self._handle_status = handle_status

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
        if not isinstance(other, ShowVulAffectInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
