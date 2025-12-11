# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeAgentsRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operate_all': 'bool',
        'host_name': 'str',
        'host_id': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'version': 'str',
        'protect_status': 'str',
        'os_type': 'str',
        'policy_group_id': 'str',
        'group_id': 'str',
        'asset_value': 'str',
        'host_id_list': 'list[str]'
    }

    attribute_map = {
        'operate_all': 'operate_all',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'version': 'version',
        'protect_status': 'protect_status',
        'os_type': 'os_type',
        'policy_group_id': 'policy_group_id',
        'group_id': 'group_id',
        'asset_value': 'asset_value',
        'host_id_list': 'host_id_list'
    }

    def __init__(self, operate_all=None, host_name=None, host_id=None, private_ip=None, public_ip=None, version=None, protect_status=None, os_type=None, policy_group_id=None, group_id=None, asset_value=None, host_id_list=None):
        r"""UpgradeAgentsRequestInfo

        The model defined in huaweicloud sdk

        :param operate_all: **参数解释**: 是否全量升级 **约束限制**: 不涉及 **取值范围**: - true: 全量升级，不需要填写host_id_list，按照其余筛选条件筛选符合升级的服务器。 - false: 非全量升级，需要填写host_id_list，只升级host_id_list中包含的服务器。  **默认取值**: false 
        :type operate_all: bool
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param host_id: **参数解释**： 服务器（主机）的唯一标识ID **取值范围**： 字符长度1-64位 
        :type host_id: str
        :param private_ip: **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 
        :type private_ip: str
        :param public_ip: **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位，支持IPv4或IPv6格式（IPv4长度7-15位，IPv6长度15-39位） 
        :type public_ip: str
        :param version: **参数解释**： 防护版本 **约束限制**: 不涉及 **取值范围**： - hss.version.basic ：基础版。 - hss.version.advanced ：专业版。 - hss.version.enterprise ：企业版。 - hss.version.premium ：旗舰版。 - hss.version.wtp ：网页防篡改版。 - hss.version.container.enterprise：容器版。  **默认取值**: 不涉及 
        :type version: str
        :param protect_status: **参数解释**： 防护状态 **约束限制**: 不涉及 **取值范围**： - closed ：未防护。 - opened ：防护中。  **默认取值**: 不涉及 
        :type protect_status: str
        :param os_type: **参数解释**： 操作系统类型 **约束限制**: 不涉及 **取值范围**： - Linux：Linux系统。 - Windows：Windows系统。  **默认取值**: 不涉及 
        :type os_type: str
        :param policy_group_id: **参数解释**： 策略组ID **取值范围**： 字符长度36-64位
        :type policy_group_id: str
        :param group_id: **参数解释**: 主机所属服务器组的唯一标识ID **取值范围**: 字符长度0-64位 
        :type group_id: str
        :param asset_value: 资产重要性 **参数解释**： 资产重要性 **约束限制**: 不涉及 **取值范围**： - important ：重要资产。 - common ：一般资产。 - test ：测试资产。  **默认取值**: 不涉及
        :type asset_value: str
        :param host_id_list: **参数解释**: 服务器ID列表 **取值范围**: 不涉及 
        :type host_id_list: list[str]
        """
        
        

        self._operate_all = None
        self._host_name = None
        self._host_id = None
        self._private_ip = None
        self._public_ip = None
        self._version = None
        self._protect_status = None
        self._os_type = None
        self._policy_group_id = None
        self._group_id = None
        self._asset_value = None
        self._host_id_list = None
        self.discriminator = None

        self.operate_all = operate_all
        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if version is not None:
            self.version = version
        if protect_status is not None:
            self.protect_status = protect_status
        if os_type is not None:
            self.os_type = os_type
        if policy_group_id is not None:
            self.policy_group_id = policy_group_id
        if group_id is not None:
            self.group_id = group_id
        if asset_value is not None:
            self.asset_value = asset_value
        if host_id_list is not None:
            self.host_id_list = host_id_list

    @property
    def operate_all(self):
        r"""Gets the operate_all of this UpgradeAgentsRequestInfo.

        **参数解释**: 是否全量升级 **约束限制**: 不涉及 **取值范围**: - true: 全量升级，不需要填写host_id_list，按照其余筛选条件筛选符合升级的服务器。 - false: 非全量升级，需要填写host_id_list，只升级host_id_list中包含的服务器。  **默认取值**: false 

        :return: The operate_all of this UpgradeAgentsRequestInfo.
        :rtype: bool
        """
        return self._operate_all

    @operate_all.setter
    def operate_all(self, operate_all):
        r"""Sets the operate_all of this UpgradeAgentsRequestInfo.

        **参数解释**: 是否全量升级 **约束限制**: 不涉及 **取值范围**: - true: 全量升级，不需要填写host_id_list，按照其余筛选条件筛选符合升级的服务器。 - false: 非全量升级，需要填写host_id_list，只升级host_id_list中包含的服务器。  **默认取值**: false 

        :param operate_all: The operate_all of this UpgradeAgentsRequestInfo.
        :type operate_all: bool
        """
        self._operate_all = operate_all

    @property
    def host_name(self):
        r"""Gets the host_name of this UpgradeAgentsRequestInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this UpgradeAgentsRequestInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this UpgradeAgentsRequestInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this UpgradeAgentsRequestInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this UpgradeAgentsRequestInfo.

        **参数解释**： 服务器（主机）的唯一标识ID **取值范围**： 字符长度1-64位 

        :return: The host_id of this UpgradeAgentsRequestInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this UpgradeAgentsRequestInfo.

        **参数解释**： 服务器（主机）的唯一标识ID **取值范围**： 字符长度1-64位 

        :param host_id: The host_id of this UpgradeAgentsRequestInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def private_ip(self):
        r"""Gets the private_ip of this UpgradeAgentsRequestInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :return: The private_ip of this UpgradeAgentsRequestInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this UpgradeAgentsRequestInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :param private_ip: The private_ip of this UpgradeAgentsRequestInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this UpgradeAgentsRequestInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位，支持IPv4或IPv6格式（IPv4长度7-15位，IPv6长度15-39位） 

        :return: The public_ip of this UpgradeAgentsRequestInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this UpgradeAgentsRequestInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位，支持IPv4或IPv6格式（IPv4长度7-15位，IPv6长度15-39位） 

        :param public_ip: The public_ip of this UpgradeAgentsRequestInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def version(self):
        r"""Gets the version of this UpgradeAgentsRequestInfo.

        **参数解释**： 防护版本 **约束限制**: 不涉及 **取值范围**： - hss.version.basic ：基础版。 - hss.version.advanced ：专业版。 - hss.version.enterprise ：企业版。 - hss.version.premium ：旗舰版。 - hss.version.wtp ：网页防篡改版。 - hss.version.container.enterprise：容器版。  **默认取值**: 不涉及 

        :return: The version of this UpgradeAgentsRequestInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this UpgradeAgentsRequestInfo.

        **参数解释**： 防护版本 **约束限制**: 不涉及 **取值范围**： - hss.version.basic ：基础版。 - hss.version.advanced ：专业版。 - hss.version.enterprise ：企业版。 - hss.version.premium ：旗舰版。 - hss.version.wtp ：网页防篡改版。 - hss.version.container.enterprise：容器版。  **默认取值**: 不涉及 

        :param version: The version of this UpgradeAgentsRequestInfo.
        :type version: str
        """
        self._version = version

    @property
    def protect_status(self):
        r"""Gets the protect_status of this UpgradeAgentsRequestInfo.

        **参数解释**： 防护状态 **约束限制**: 不涉及 **取值范围**： - closed ：未防护。 - opened ：防护中。  **默认取值**: 不涉及 

        :return: The protect_status of this UpgradeAgentsRequestInfo.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this UpgradeAgentsRequestInfo.

        **参数解释**： 防护状态 **约束限制**: 不涉及 **取值范围**： - closed ：未防护。 - opened ：防护中。  **默认取值**: 不涉及 

        :param protect_status: The protect_status of this UpgradeAgentsRequestInfo.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def os_type(self):
        r"""Gets the os_type of this UpgradeAgentsRequestInfo.

        **参数解释**： 操作系统类型 **约束限制**: 不涉及 **取值范围**： - Linux：Linux系统。 - Windows：Windows系统。  **默认取值**: 不涉及 

        :return: The os_type of this UpgradeAgentsRequestInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this UpgradeAgentsRequestInfo.

        **参数解释**： 操作系统类型 **约束限制**: 不涉及 **取值范围**： - Linux：Linux系统。 - Windows：Windows系统。  **默认取值**: 不涉及 

        :param os_type: The os_type of this UpgradeAgentsRequestInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def policy_group_id(self):
        r"""Gets the policy_group_id of this UpgradeAgentsRequestInfo.

        **参数解释**： 策略组ID **取值范围**： 字符长度36-64位

        :return: The policy_group_id of this UpgradeAgentsRequestInfo.
        :rtype: str
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, policy_group_id):
        r"""Sets the policy_group_id of this UpgradeAgentsRequestInfo.

        **参数解释**： 策略组ID **取值范围**： 字符长度36-64位

        :param policy_group_id: The policy_group_id of this UpgradeAgentsRequestInfo.
        :type policy_group_id: str
        """
        self._policy_group_id = policy_group_id

    @property
    def group_id(self):
        r"""Gets the group_id of this UpgradeAgentsRequestInfo.

        **参数解释**: 主机所属服务器组的唯一标识ID **取值范围**: 字符长度0-64位 

        :return: The group_id of this UpgradeAgentsRequestInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this UpgradeAgentsRequestInfo.

        **参数解释**: 主机所属服务器组的唯一标识ID **取值范围**: 字符长度0-64位 

        :param group_id: The group_id of this UpgradeAgentsRequestInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def asset_value(self):
        r"""Gets the asset_value of this UpgradeAgentsRequestInfo.

        资产重要性 **参数解释**： 资产重要性 **约束限制**: 不涉及 **取值范围**： - important ：重要资产。 - common ：一般资产。 - test ：测试资产。  **默认取值**: 不涉及

        :return: The asset_value of this UpgradeAgentsRequestInfo.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this UpgradeAgentsRequestInfo.

        资产重要性 **参数解释**： 资产重要性 **约束限制**: 不涉及 **取值范围**： - important ：重要资产。 - common ：一般资产。 - test ：测试资产。  **默认取值**: 不涉及

        :param asset_value: The asset_value of this UpgradeAgentsRequestInfo.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this UpgradeAgentsRequestInfo.

        **参数解释**: 服务器ID列表 **取值范围**: 不涉及 

        :return: The host_id_list of this UpgradeAgentsRequestInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this UpgradeAgentsRequestInfo.

        **参数解释**: 服务器ID列表 **取值范围**: 不涉及 

        :param host_id_list: The host_id_list of this UpgradeAgentsRequestInfo.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

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
        if not isinstance(other, UpgradeAgentsRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
