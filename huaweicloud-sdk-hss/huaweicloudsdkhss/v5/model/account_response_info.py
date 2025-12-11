# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccountResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_name': 'str',
        'account_id': 'str',
        'organization_id': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'host_num': 'int',
        'vulnerability_num': 'int',
        'baseline_num': 'int',
        'intrusion_num': 'int'
    }

    attribute_map = {
        'account_name': 'account_name',
        'account_id': 'account_id',
        'organization_id': 'organization_id',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'host_num': 'host_num',
        'vulnerability_num': 'vulnerability_num',
        'baseline_num': 'baseline_num',
        'intrusion_num': 'intrusion_num'
    }

    def __init__(self, account_name=None, account_id=None, organization_id=None, project_id=None, project_name=None, host_num=None, vulnerability_num=None, baseline_num=None, intrusion_num=None):
        r"""AccountResponseInfo

        The model defined in huaweicloud sdk

        :param account_name: **参数解释**: 账号的唯一名称，用于标识账号身份； **取值范围**: 字符长度1-64位，支持字母、数字、连字符、下划线，不能以特殊字符开头或结尾 
        :type account_name: str
        :param account_id: **参数解释**: 账号的唯一标识ID，用于唯一确定某个账号； **取值范围**: 字符长度1-64位，符合平台账号ID命名规范（如UUID或数字组合） 
        :type account_id: str
        :param organization_id: **参数解释**: 账号所属组织的唯一标识ID； **取值范围**: 字符长度1-64位，符合平台组织ID命名规范 
        :type organization_id: str
        :param project_id: **参数解释**: 账号所属项目的唯一标识ID； **取值范围**: 字符长度1-64位，符合平台项目ID命名规范； 
        :type project_id: str
        :param project_name: **参数解释**: 账号所属项目的名称，用于直观标识项目； **取值范围**: 字符长度1-64位，支持字母、数字、连字符、下划线及中文，无复杂度额外要求 
        :type project_name: str
        :param host_num: **参数解释**: 当前账号下已关联的主机总数量； **取值范围**: 非负整数，最小值0，最大值取决于平台资源配额；单位：台 
        :type host_num: int
        :param vulnerability_num: **参数解释**: 当前账号下主机存在的漏洞风险总数量； **取值范围**: 非负整数，取值范围0-2147483647；单位：个 
        :type vulnerability_num: int
        :param baseline_num: **参数解释**: 当前账号下主机基线检测未通过的风险总数量； **取值范围**: 非负整数，取值范围0-2147483647；单位：个 
        :type baseline_num: int
        :param intrusion_num: **参数解释**: 当前账号下主机发生的安全入侵告警总数量； **取值范围**: 非负整数，取值范围0-2147483647；单位：条 
        :type intrusion_num: int
        """
        
        

        self._account_name = None
        self._account_id = None
        self._organization_id = None
        self._project_id = None
        self._project_name = None
        self._host_num = None
        self._vulnerability_num = None
        self._baseline_num = None
        self._intrusion_num = None
        self.discriminator = None

        if account_name is not None:
            self.account_name = account_name
        if account_id is not None:
            self.account_id = account_id
        if organization_id is not None:
            self.organization_id = organization_id
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if host_num is not None:
            self.host_num = host_num
        if vulnerability_num is not None:
            self.vulnerability_num = vulnerability_num
        if baseline_num is not None:
            self.baseline_num = baseline_num
        if intrusion_num is not None:
            self.intrusion_num = intrusion_num

    @property
    def account_name(self):
        r"""Gets the account_name of this AccountResponseInfo.

        **参数解释**: 账号的唯一名称，用于标识账号身份； **取值范围**: 字符长度1-64位，支持字母、数字、连字符、下划线，不能以特殊字符开头或结尾 

        :return: The account_name of this AccountResponseInfo.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        r"""Sets the account_name of this AccountResponseInfo.

        **参数解释**: 账号的唯一名称，用于标识账号身份； **取值范围**: 字符长度1-64位，支持字母、数字、连字符、下划线，不能以特殊字符开头或结尾 

        :param account_name: The account_name of this AccountResponseInfo.
        :type account_name: str
        """
        self._account_name = account_name

    @property
    def account_id(self):
        r"""Gets the account_id of this AccountResponseInfo.

        **参数解释**: 账号的唯一标识ID，用于唯一确定某个账号； **取值范围**: 字符长度1-64位，符合平台账号ID命名规范（如UUID或数字组合） 

        :return: The account_id of this AccountResponseInfo.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this AccountResponseInfo.

        **参数解释**: 账号的唯一标识ID，用于唯一确定某个账号； **取值范围**: 字符长度1-64位，符合平台账号ID命名规范（如UUID或数字组合） 

        :param account_id: The account_id of this AccountResponseInfo.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def organization_id(self):
        r"""Gets the organization_id of this AccountResponseInfo.

        **参数解释**: 账号所属组织的唯一标识ID； **取值范围**: 字符长度1-64位，符合平台组织ID命名规范 

        :return: The organization_id of this AccountResponseInfo.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        r"""Sets the organization_id of this AccountResponseInfo.

        **参数解释**: 账号所属组织的唯一标识ID； **取值范围**: 字符长度1-64位，符合平台组织ID命名规范 

        :param organization_id: The organization_id of this AccountResponseInfo.
        :type organization_id: str
        """
        self._organization_id = organization_id

    @property
    def project_id(self):
        r"""Gets the project_id of this AccountResponseInfo.

        **参数解释**: 账号所属项目的唯一标识ID； **取值范围**: 字符长度1-64位，符合平台项目ID命名规范； 

        :return: The project_id of this AccountResponseInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this AccountResponseInfo.

        **参数解释**: 账号所属项目的唯一标识ID； **取值范围**: 字符长度1-64位，符合平台项目ID命名规范； 

        :param project_id: The project_id of this AccountResponseInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this AccountResponseInfo.

        **参数解释**: 账号所属项目的名称，用于直观标识项目； **取值范围**: 字符长度1-64位，支持字母、数字、连字符、下划线及中文，无复杂度额外要求 

        :return: The project_name of this AccountResponseInfo.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this AccountResponseInfo.

        **参数解释**: 账号所属项目的名称，用于直观标识项目； **取值范围**: 字符长度1-64位，支持字母、数字、连字符、下划线及中文，无复杂度额外要求 

        :param project_name: The project_name of this AccountResponseInfo.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def host_num(self):
        r"""Gets the host_num of this AccountResponseInfo.

        **参数解释**: 当前账号下已关联的主机总数量； **取值范围**: 非负整数，最小值0，最大值取决于平台资源配额；单位：台 

        :return: The host_num of this AccountResponseInfo.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        r"""Sets the host_num of this AccountResponseInfo.

        **参数解释**: 当前账号下已关联的主机总数量； **取值范围**: 非负整数，最小值0，最大值取决于平台资源配额；单位：台 

        :param host_num: The host_num of this AccountResponseInfo.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def vulnerability_num(self):
        r"""Gets the vulnerability_num of this AccountResponseInfo.

        **参数解释**: 当前账号下主机存在的漏洞风险总数量； **取值范围**: 非负整数，取值范围0-2147483647；单位：个 

        :return: The vulnerability_num of this AccountResponseInfo.
        :rtype: int
        """
        return self._vulnerability_num

    @vulnerability_num.setter
    def vulnerability_num(self, vulnerability_num):
        r"""Sets the vulnerability_num of this AccountResponseInfo.

        **参数解释**: 当前账号下主机存在的漏洞风险总数量； **取值范围**: 非负整数，取值范围0-2147483647；单位：个 

        :param vulnerability_num: The vulnerability_num of this AccountResponseInfo.
        :type vulnerability_num: int
        """
        self._vulnerability_num = vulnerability_num

    @property
    def baseline_num(self):
        r"""Gets the baseline_num of this AccountResponseInfo.

        **参数解释**: 当前账号下主机基线检测未通过的风险总数量； **取值范围**: 非负整数，取值范围0-2147483647；单位：个 

        :return: The baseline_num of this AccountResponseInfo.
        :rtype: int
        """
        return self._baseline_num

    @baseline_num.setter
    def baseline_num(self, baseline_num):
        r"""Sets the baseline_num of this AccountResponseInfo.

        **参数解释**: 当前账号下主机基线检测未通过的风险总数量； **取值范围**: 非负整数，取值范围0-2147483647；单位：个 

        :param baseline_num: The baseline_num of this AccountResponseInfo.
        :type baseline_num: int
        """
        self._baseline_num = baseline_num

    @property
    def intrusion_num(self):
        r"""Gets the intrusion_num of this AccountResponseInfo.

        **参数解释**: 当前账号下主机发生的安全入侵告警总数量； **取值范围**: 非负整数，取值范围0-2147483647；单位：条 

        :return: The intrusion_num of this AccountResponseInfo.
        :rtype: int
        """
        return self._intrusion_num

    @intrusion_num.setter
    def intrusion_num(self, intrusion_num):
        r"""Sets the intrusion_num of this AccountResponseInfo.

        **参数解释**: 当前账号下主机发生的安全入侵告警总数量； **取值范围**: 非负整数，取值范围0-2147483647；单位：条 

        :param intrusion_num: The intrusion_num of this AccountResponseInfo.
        :type intrusion_num: int
        """
        self._intrusion_num = intrusion_num

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
        if not isinstance(other, AccountResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
