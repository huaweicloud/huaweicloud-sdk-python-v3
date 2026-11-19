# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportVulReportRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_value': 'str',
        'group_name': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'severity_level': 'str',
        'handle_status': 'str',
        'status': 'str',
        'host_ids': 'list[str]',
        'cluster_id': 'str'
    }

    attribute_map = {
        'asset_value': 'asset_value',
        'group_name': 'group_name',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'severity_level': 'severity_level',
        'handle_status': 'handle_status',
        'status': 'status',
        'host_ids': 'host_ids',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, asset_value=None, group_name=None, host_name=None, host_ip=None, severity_level=None, handle_status=None, status=None, host_ids=None, cluster_id=None):
        r"""ExportVulReportRequestInfo

        The model defined in huaweicloud sdk

        :param asset_value: **参数解释**： 资产重要性 **约束限制**： 不涉及 **取值范围**： - important：重要资产 - common：一般资产 - test：测试资产  **默认取值**： 不涉及 
        :type asset_value: str
        :param group_name: **参数解释**： 服务器组名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 
        :type group_name: str
        :param host_name: **参数解释**： 主机名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 
        :type host_name: str
        :param host_ip: **参数解释**： 主机IP **约束限制**： 不涉及 **取值范围**： 字符长度1-64位 **默认取值**： 不涉及 
        :type host_ip: str
        :param severity_level: **参数解释**： 漏洞风险等级 **约束限制**： 不涉及 **取值范围**： - Security：安全 - High：高危 - Medium：中危 - Low：低危  **默认取值**： 不涉及 
        :type severity_level: str
        :param handle_status: **参数解释**： 漏洞处理状态 **约束限制**： 必填 **取值范围**： - handled：已处理 - unhandled：未处理  **默认取值**： 不涉及 
        :type handle_status: str
        :param status: **参数解释**： 漏洞状态 **约束限制**： 不涉及 **取值范围**： 字符长度1-32位 **默认取值**： 不涉及 
        :type status: str
        :param host_ids: **参数解释**： 主机ID列表 **约束限制**： 不涉及 **取值范围**： 0-1000个主机ID **默认取值**： 不涉及 
        :type host_ids: list[str]
        :param cluster_id: **参数解释**： 集群ID **约束限制**： 不涉及 **取值范围**： 字符长度1-64位 **默认取值**： 不涉及 
        :type cluster_id: str
        """
        
        

        self._asset_value = None
        self._group_name = None
        self._host_name = None
        self._host_ip = None
        self._severity_level = None
        self._handle_status = None
        self._status = None
        self._host_ids = None
        self._cluster_id = None
        self.discriminator = None

        if asset_value is not None:
            self.asset_value = asset_value
        if group_name is not None:
            self.group_name = group_name
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if severity_level is not None:
            self.severity_level = severity_level
        self.handle_status = handle_status
        if status is not None:
            self.status = status
        if host_ids is not None:
            self.host_ids = host_ids
        if cluster_id is not None:
            self.cluster_id = cluster_id

    @property
    def asset_value(self):
        r"""Gets the asset_value of this ExportVulReportRequestInfo.

        **参数解释**： 资产重要性 **约束限制**： 不涉及 **取值范围**： - important：重要资产 - common：一般资产 - test：测试资产  **默认取值**： 不涉及 

        :return: The asset_value of this ExportVulReportRequestInfo.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this ExportVulReportRequestInfo.

        **参数解释**： 资产重要性 **约束限制**： 不涉及 **取值范围**： - important：重要资产 - common：一般资产 - test：测试资产  **默认取值**： 不涉及 

        :param asset_value: The asset_value of this ExportVulReportRequestInfo.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def group_name(self):
        r"""Gets the group_name of this ExportVulReportRequestInfo.

        **参数解释**： 服务器组名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :return: The group_name of this ExportVulReportRequestInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ExportVulReportRequestInfo.

        **参数解释**： 服务器组名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :param group_name: The group_name of this ExportVulReportRequestInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def host_name(self):
        r"""Gets the host_name of this ExportVulReportRequestInfo.

        **参数解释**： 主机名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :return: The host_name of this ExportVulReportRequestInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ExportVulReportRequestInfo.

        **参数解释**： 主机名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :param host_name: The host_name of this ExportVulReportRequestInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ExportVulReportRequestInfo.

        **参数解释**： 主机IP **约束限制**： 不涉及 **取值范围**： 字符长度1-64位 **默认取值**： 不涉及 

        :return: The host_ip of this ExportVulReportRequestInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ExportVulReportRequestInfo.

        **参数解释**： 主机IP **约束限制**： 不涉及 **取值范围**： 字符长度1-64位 **默认取值**： 不涉及 

        :param host_ip: The host_ip of this ExportVulReportRequestInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def severity_level(self):
        r"""Gets the severity_level of this ExportVulReportRequestInfo.

        **参数解释**： 漏洞风险等级 **约束限制**： 不涉及 **取值范围**： - Security：安全 - High：高危 - Medium：中危 - Low：低危  **默认取值**： 不涉及 

        :return: The severity_level of this ExportVulReportRequestInfo.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this ExportVulReportRequestInfo.

        **参数解释**： 漏洞风险等级 **约束限制**： 不涉及 **取值范围**： - Security：安全 - High：高危 - Medium：中危 - Low：低危  **默认取值**： 不涉及 

        :param severity_level: The severity_level of this ExportVulReportRequestInfo.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def handle_status(self):
        r"""Gets the handle_status of this ExportVulReportRequestInfo.

        **参数解释**： 漏洞处理状态 **约束限制**： 必填 **取值范围**： - handled：已处理 - unhandled：未处理  **默认取值**： 不涉及 

        :return: The handle_status of this ExportVulReportRequestInfo.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this ExportVulReportRequestInfo.

        **参数解释**： 漏洞处理状态 **约束限制**： 必填 **取值范围**： - handled：已处理 - unhandled：未处理  **默认取值**： 不涉及 

        :param handle_status: The handle_status of this ExportVulReportRequestInfo.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def status(self):
        r"""Gets the status of this ExportVulReportRequestInfo.

        **参数解释**： 漏洞状态 **约束限制**： 不涉及 **取值范围**： 字符长度1-32位 **默认取值**： 不涉及 

        :return: The status of this ExportVulReportRequestInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ExportVulReportRequestInfo.

        **参数解释**： 漏洞状态 **约束限制**： 不涉及 **取值范围**： 字符长度1-32位 **默认取值**： 不涉及 

        :param status: The status of this ExportVulReportRequestInfo.
        :type status: str
        """
        self._status = status

    @property
    def host_ids(self):
        r"""Gets the host_ids of this ExportVulReportRequestInfo.

        **参数解释**： 主机ID列表 **约束限制**： 不涉及 **取值范围**： 0-1000个主机ID **默认取值**： 不涉及 

        :return: The host_ids of this ExportVulReportRequestInfo.
        :rtype: list[str]
        """
        return self._host_ids

    @host_ids.setter
    def host_ids(self, host_ids):
        r"""Sets the host_ids of this ExportVulReportRequestInfo.

        **参数解释**： 主机ID列表 **约束限制**： 不涉及 **取值范围**： 0-1000个主机ID **默认取值**： 不涉及 

        :param host_ids: The host_ids of this ExportVulReportRequestInfo.
        :type host_ids: list[str]
        """
        self._host_ids = host_ids

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ExportVulReportRequestInfo.

        **参数解释**： 集群ID **约束限制**： 不涉及 **取值范围**： 字符长度1-64位 **默认取值**： 不涉及 

        :return: The cluster_id of this ExportVulReportRequestInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ExportVulReportRequestInfo.

        **参数解释**： 集群ID **约束限制**： 不涉及 **取值范围**： 字符长度1-64位 **默认取值**： 不涉及 

        :param cluster_id: The cluster_id of this ExportVulReportRequestInfo.
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
        if not isinstance(other, ExportVulReportRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
