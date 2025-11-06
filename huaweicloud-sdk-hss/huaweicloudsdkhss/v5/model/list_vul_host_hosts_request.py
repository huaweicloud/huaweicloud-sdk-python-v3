# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVulHostHostsRequest:

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
        'limit': 'int',
        'offset': 'int',
        'asset_value': 'str',
        'group_name': 'str',
        'host_name': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'severity_level': 'str',
        'handle_status': 'str',
        'status': 'str',
        'cluster_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'limit': 'limit',
        'offset': 'offset',
        'asset_value': 'asset_value',
        'group_name': 'group_name',
        'host_name': 'host_name',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'severity_level': 'severity_level',
        'handle_status': 'handle_status',
        'status': 'status',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, enterprise_project_id=None, limit=None, offset=None, asset_value=None, group_name=None, host_name=None, public_ip=None, private_ip=None, severity_level=None, handle_status=None, status=None, cluster_id=None):
        r"""ListVulHostHostsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 
        :type offset: int
        :param asset_value: **参数解释**: 资产重要性 **约束限制**: 不涉及 **取值范围**: - important ：重要资产 - common    ：一般资产 - test      ：测试资产  **默认取值**: 不涉及 
        :type asset_value: str
        :param group_name: **参数解释**: 服务器组 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type group_name: str
        :param host_name: **参数解释**: 主机名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type host_name: str
        :param public_ip: **参数解释**: 主机公有ip **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type public_ip: str
        :param private_ip: **参数解释**: 主机私有ip **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type private_ip: str
        :param severity_level: **参数解释**: 主机风险等级 **约束限制**: 不涉及 **取值范围**: - High：高危 - Medium：中危 - Low：低危 - Security：安全  **默认取值**: 不涉及 
        :type severity_level: str
        :param handle_status: **参数解释**: 主机的处置状态 **约束限制**: 不涉及 **取值范围**: - unhandled：待处理 - handled：已处理  **默认取值**: 不涉及 
        :type handle_status: str
        :param status: **参数解释**: 该漏洞状态包含的主机 **约束限制**: 不涉及 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：忽略 - vul_status_verified：验证中 - vul_status_fixing：修复中 - vul_status_fixed：修复完成 - vul_status_reboot：修复成功待重启 - vul_status_failed：修复失败 - vul_status_fix_after_reboot：重启后再次修复  **默认取值**: 不涉及 
        :type status: str
        :param cluster_id: **参数解释**: 集群id **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type cluster_id: str
        """
        
        

        self._enterprise_project_id = None
        self._limit = None
        self._offset = None
        self._asset_value = None
        self._group_name = None
        self._host_name = None
        self._public_ip = None
        self._private_ip = None
        self._severity_level = None
        self._handle_status = None
        self._status = None
        self._cluster_id = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.limit = limit
        self.offset = offset
        if asset_value is not None:
            self.asset_value = asset_value
        if group_name is not None:
            self.group_name = group_name
        if host_name is not None:
            self.host_name = host_name
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if severity_level is not None:
            self.severity_level = severity_level
        if handle_status is not None:
            self.handle_status = handle_status
        if status is not None:
            self.status = status
        if cluster_id is not None:
            self.cluster_id = cluster_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListVulHostHostsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListVulHostHostsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListVulHostHostsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListVulHostHostsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        r"""Gets the limit of this ListVulHostHostsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListVulHostHostsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVulHostHostsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListVulHostHostsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListVulHostHostsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :return: The offset of this ListVulHostHostsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListVulHostHostsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :param offset: The offset of this ListVulHostHostsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def asset_value(self):
        r"""Gets the asset_value of this ListVulHostHostsRequest.

        **参数解释**: 资产重要性 **约束限制**: 不涉及 **取值范围**: - important ：重要资产 - common    ：一般资产 - test      ：测试资产  **默认取值**: 不涉及 

        :return: The asset_value of this ListVulHostHostsRequest.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this ListVulHostHostsRequest.

        **参数解释**: 资产重要性 **约束限制**: 不涉及 **取值范围**: - important ：重要资产 - common    ：一般资产 - test      ：测试资产  **默认取值**: 不涉及 

        :param asset_value: The asset_value of this ListVulHostHostsRequest.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def group_name(self):
        r"""Gets the group_name of this ListVulHostHostsRequest.

        **参数解释**: 服务器组 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The group_name of this ListVulHostHostsRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ListVulHostHostsRequest.

        **参数解释**: 服务器组 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param group_name: The group_name of this ListVulHostHostsRequest.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def host_name(self):
        r"""Gets the host_name of this ListVulHostHostsRequest.

        **参数解释**: 主机名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The host_name of this ListVulHostHostsRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListVulHostHostsRequest.

        **参数解释**: 主机名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param host_name: The host_name of this ListVulHostHostsRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ListVulHostHostsRequest.

        **参数解释**: 主机公有ip **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The public_ip of this ListVulHostHostsRequest.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ListVulHostHostsRequest.

        **参数解释**: 主机公有ip **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param public_ip: The public_ip of this ListVulHostHostsRequest.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListVulHostHostsRequest.

        **参数解释**: 主机私有ip **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The private_ip of this ListVulHostHostsRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListVulHostHostsRequest.

        **参数解释**: 主机私有ip **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param private_ip: The private_ip of this ListVulHostHostsRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def severity_level(self):
        r"""Gets the severity_level of this ListVulHostHostsRequest.

        **参数解释**: 主机风险等级 **约束限制**: 不涉及 **取值范围**: - High：高危 - Medium：中危 - Low：低危 - Security：安全  **默认取值**: 不涉及 

        :return: The severity_level of this ListVulHostHostsRequest.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this ListVulHostHostsRequest.

        **参数解释**: 主机风险等级 **约束限制**: 不涉及 **取值范围**: - High：高危 - Medium：中危 - Low：低危 - Security：安全  **默认取值**: 不涉及 

        :param severity_level: The severity_level of this ListVulHostHostsRequest.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def handle_status(self):
        r"""Gets the handle_status of this ListVulHostHostsRequest.

        **参数解释**: 主机的处置状态 **约束限制**: 不涉及 **取值范围**: - unhandled：待处理 - handled：已处理  **默认取值**: 不涉及 

        :return: The handle_status of this ListVulHostHostsRequest.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this ListVulHostHostsRequest.

        **参数解释**: 主机的处置状态 **约束限制**: 不涉及 **取值范围**: - unhandled：待处理 - handled：已处理  **默认取值**: 不涉及 

        :param handle_status: The handle_status of this ListVulHostHostsRequest.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def status(self):
        r"""Gets the status of this ListVulHostHostsRequest.

        **参数解释**: 该漏洞状态包含的主机 **约束限制**: 不涉及 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：忽略 - vul_status_verified：验证中 - vul_status_fixing：修复中 - vul_status_fixed：修复完成 - vul_status_reboot：修复成功待重启 - vul_status_failed：修复失败 - vul_status_fix_after_reboot：重启后再次修复  **默认取值**: 不涉及 

        :return: The status of this ListVulHostHostsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListVulHostHostsRequest.

        **参数解释**: 该漏洞状态包含的主机 **约束限制**: 不涉及 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：忽略 - vul_status_verified：验证中 - vul_status_fixing：修复中 - vul_status_fixed：修复完成 - vul_status_reboot：修复成功待重启 - vul_status_failed：修复失败 - vul_status_fix_after_reboot：重启后再次修复  **默认取值**: 不涉及 

        :param status: The status of this ListVulHostHostsRequest.
        :type status: str
        """
        self._status = status

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListVulHostHostsRequest.

        **参数解释**: 集群id **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The cluster_id of this ListVulHostHostsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListVulHostHostsRequest.

        **参数解释**: 集群id **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param cluster_id: The cluster_id of this ListVulHostHostsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

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
        if not isinstance(other, ListVulHostHostsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
