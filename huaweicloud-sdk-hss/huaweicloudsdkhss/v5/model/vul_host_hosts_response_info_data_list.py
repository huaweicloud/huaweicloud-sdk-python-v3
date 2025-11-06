# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulHostHostsResponseInfoDataList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'agent_id': 'str',
        'host_name': 'str',
        'region_name': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'group_id': 'str',
        'group_name': 'str',
        'os_type': 'str',
        'asset_value': 'str',
        'scan_time': 'int',
        'severity_level': 'str',
        'score': 'int',
        'version': 'str',
        'handle_status': 'str',
        'vul_num_with_repair_priority_list': 'list[VulHostHostsResponseInfoVulNumWithRepairPriorityList]',
        'vul_ids_info': 'VulHostHostsResponseInfoVulIdsInfo'
    }

    attribute_map = {
        'host_id': 'host_id',
        'agent_id': 'agent_id',
        'host_name': 'host_name',
        'region_name': 'region_name',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'os_type': 'os_type',
        'asset_value': 'asset_value',
        'scan_time': 'scan_time',
        'severity_level': 'severity_level',
        'score': 'score',
        'version': 'version',
        'handle_status': 'handle_status',
        'vul_num_with_repair_priority_list': 'vul_num_with_repair_priority_list',
        'vul_ids_info': 'vul_ids_info'
    }

    def __init__(self, host_id=None, agent_id=None, host_name=None, region_name=None, public_ip=None, private_ip=None, group_id=None, group_name=None, os_type=None, asset_value=None, scan_time=None, severity_level=None, score=None, version=None, handle_status=None, vul_num_with_repair_priority_list=None, vul_ids_info=None):
        r"""VulHostHostsResponseInfoDataList

        The model defined in huaweicloud sdk

        :param host_id: **参数解释**: 主机id **取值范围**: 字符长度0-64位 
        :type host_id: str
        :param agent_id: **参数解释**: agent id **取值范围**: 字符长度0-64位 
        :type agent_id: str
        :param host_name: **参数解释**: 主机名称 **取值范围**: 字符长度0-64位 
        :type host_name: str
        :param region_name: **参数解释**: 地域 **取值范围**: 字符长度0-32位 
        :type region_name: str
        :param public_ip: **参数解释**: 服务器公网ip **取值范围**: 字符长度0-128位 
        :type public_ip: str
        :param private_ip: **参数解释**: 服务器私网ip **取值范围**: 字符长度0-4096位 
        :type private_ip: str
        :param group_id: **参数解释**: 服务器组id **取值范围**: 字符长度0-128位 
        :type group_id: str
        :param group_name: **参数解释**: 服务器组名称 **取值范围**: 字符长度0-256位 
        :type group_name: str
        :param os_type: **参数解释**: 操作系统类型 **取值范围**: - Linux ：Linux系统 - Windows ：Windows系统
        :type os_type: str
        :param asset_value: **参数解释**: 资产重要性 **取值范围**: 字符长度0-32位 
        :type asset_value: str
        :param scan_time: **参数解释**: 最近扫描时间 **取值范围**: 最小值0，最大值2^63-1 
        :type scan_time: int
        :param severity_level: **参数解释**: 主机风险 **取值范围**: 字符长度0-32位 
        :type severity_level: str
        :param score: **参数解释**: 主机风险分数 **取值范围**: 最小值0，最大值100 
        :type score: int
        :param version: **参数解释**: 主机配额 **取值范围**: 字符长度0-64位 
        :type version: str
        :param handle_status: **参数解释**: 主机配额 **取值范围**: - unhandled：待处理 - handled：已处理 
        :type handle_status: str
        :param vul_num_with_repair_priority_list: **参数解释**: 各个漏洞修复优先级下的漏洞数量 
        :type vul_num_with_repair_priority_list: list[:class:`huaweicloudsdkhss.v5.VulHostHostsResponseInfoVulNumWithRepairPriorityList`]
        :param vul_ids_info: 
        :type vul_ids_info: :class:`huaweicloudsdkhss.v5.VulHostHostsResponseInfoVulIdsInfo`
        """
        
        

        self._host_id = None
        self._agent_id = None
        self._host_name = None
        self._region_name = None
        self._public_ip = None
        self._private_ip = None
        self._group_id = None
        self._group_name = None
        self._os_type = None
        self._asset_value = None
        self._scan_time = None
        self._severity_level = None
        self._score = None
        self._version = None
        self._handle_status = None
        self._vul_num_with_repair_priority_list = None
        self._vul_ids_info = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if agent_id is not None:
            self.agent_id = agent_id
        if host_name is not None:
            self.host_name = host_name
        if region_name is not None:
            self.region_name = region_name
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if os_type is not None:
            self.os_type = os_type
        if asset_value is not None:
            self.asset_value = asset_value
        if scan_time is not None:
            self.scan_time = scan_time
        if severity_level is not None:
            self.severity_level = severity_level
        if score is not None:
            self.score = score
        if version is not None:
            self.version = version
        if handle_status is not None:
            self.handle_status = handle_status
        if vul_num_with_repair_priority_list is not None:
            self.vul_num_with_repair_priority_list = vul_num_with_repair_priority_list
        if vul_ids_info is not None:
            self.vul_ids_info = vul_ids_info

    @property
    def host_id(self):
        r"""Gets the host_id of this VulHostHostsResponseInfoDataList.

        **参数解释**: 主机id **取值范围**: 字符长度0-64位 

        :return: The host_id of this VulHostHostsResponseInfoDataList.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this VulHostHostsResponseInfoDataList.

        **参数解释**: 主机id **取值范围**: 字符长度0-64位 

        :param host_id: The host_id of this VulHostHostsResponseInfoDataList.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def agent_id(self):
        r"""Gets the agent_id of this VulHostHostsResponseInfoDataList.

        **参数解释**: agent id **取值范围**: 字符长度0-64位 

        :return: The agent_id of this VulHostHostsResponseInfoDataList.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this VulHostHostsResponseInfoDataList.

        **参数解释**: agent id **取值范围**: 字符长度0-64位 

        :param agent_id: The agent_id of this VulHostHostsResponseInfoDataList.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def host_name(self):
        r"""Gets the host_name of this VulHostHostsResponseInfoDataList.

        **参数解释**: 主机名称 **取值范围**: 字符长度0-64位 

        :return: The host_name of this VulHostHostsResponseInfoDataList.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this VulHostHostsResponseInfoDataList.

        **参数解释**: 主机名称 **取值范围**: 字符长度0-64位 

        :param host_name: The host_name of this VulHostHostsResponseInfoDataList.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def region_name(self):
        r"""Gets the region_name of this VulHostHostsResponseInfoDataList.

        **参数解释**: 地域 **取值范围**: 字符长度0-32位 

        :return: The region_name of this VulHostHostsResponseInfoDataList.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        r"""Sets the region_name of this VulHostHostsResponseInfoDataList.

        **参数解释**: 地域 **取值范围**: 字符长度0-32位 

        :param region_name: The region_name of this VulHostHostsResponseInfoDataList.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def public_ip(self):
        r"""Gets the public_ip of this VulHostHostsResponseInfoDataList.

        **参数解释**: 服务器公网ip **取值范围**: 字符长度0-128位 

        :return: The public_ip of this VulHostHostsResponseInfoDataList.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this VulHostHostsResponseInfoDataList.

        **参数解释**: 服务器公网ip **取值范围**: 字符长度0-128位 

        :param public_ip: The public_ip of this VulHostHostsResponseInfoDataList.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this VulHostHostsResponseInfoDataList.

        **参数解释**: 服务器私网ip **取值范围**: 字符长度0-4096位 

        :return: The private_ip of this VulHostHostsResponseInfoDataList.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this VulHostHostsResponseInfoDataList.

        **参数解释**: 服务器私网ip **取值范围**: 字符长度0-4096位 

        :param private_ip: The private_ip of this VulHostHostsResponseInfoDataList.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def group_id(self):
        r"""Gets the group_id of this VulHostHostsResponseInfoDataList.

        **参数解释**: 服务器组id **取值范围**: 字符长度0-128位 

        :return: The group_id of this VulHostHostsResponseInfoDataList.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this VulHostHostsResponseInfoDataList.

        **参数解释**: 服务器组id **取值范围**: 字符长度0-128位 

        :param group_id: The group_id of this VulHostHostsResponseInfoDataList.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this VulHostHostsResponseInfoDataList.

        **参数解释**: 服务器组名称 **取值范围**: 字符长度0-256位 

        :return: The group_name of this VulHostHostsResponseInfoDataList.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this VulHostHostsResponseInfoDataList.

        **参数解释**: 服务器组名称 **取值范围**: 字符长度0-256位 

        :param group_name: The group_name of this VulHostHostsResponseInfoDataList.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def os_type(self):
        r"""Gets the os_type of this VulHostHostsResponseInfoDataList.

        **参数解释**: 操作系统类型 **取值范围**: - Linux ：Linux系统 - Windows ：Windows系统

        :return: The os_type of this VulHostHostsResponseInfoDataList.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this VulHostHostsResponseInfoDataList.

        **参数解释**: 操作系统类型 **取值范围**: - Linux ：Linux系统 - Windows ：Windows系统

        :param os_type: The os_type of this VulHostHostsResponseInfoDataList.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def asset_value(self):
        r"""Gets the asset_value of this VulHostHostsResponseInfoDataList.

        **参数解释**: 资产重要性 **取值范围**: 字符长度0-32位 

        :return: The asset_value of this VulHostHostsResponseInfoDataList.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this VulHostHostsResponseInfoDataList.

        **参数解释**: 资产重要性 **取值范围**: 字符长度0-32位 

        :param asset_value: The asset_value of this VulHostHostsResponseInfoDataList.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def scan_time(self):
        r"""Gets the scan_time of this VulHostHostsResponseInfoDataList.

        **参数解释**: 最近扫描时间 **取值范围**: 最小值0，最大值2^63-1 

        :return: The scan_time of this VulHostHostsResponseInfoDataList.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        r"""Sets the scan_time of this VulHostHostsResponseInfoDataList.

        **参数解释**: 最近扫描时间 **取值范围**: 最小值0，最大值2^63-1 

        :param scan_time: The scan_time of this VulHostHostsResponseInfoDataList.
        :type scan_time: int
        """
        self._scan_time = scan_time

    @property
    def severity_level(self):
        r"""Gets the severity_level of this VulHostHostsResponseInfoDataList.

        **参数解释**: 主机风险 **取值范围**: 字符长度0-32位 

        :return: The severity_level of this VulHostHostsResponseInfoDataList.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this VulHostHostsResponseInfoDataList.

        **参数解释**: 主机风险 **取值范围**: 字符长度0-32位 

        :param severity_level: The severity_level of this VulHostHostsResponseInfoDataList.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def score(self):
        r"""Gets the score of this VulHostHostsResponseInfoDataList.

        **参数解释**: 主机风险分数 **取值范围**: 最小值0，最大值100 

        :return: The score of this VulHostHostsResponseInfoDataList.
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this VulHostHostsResponseInfoDataList.

        **参数解释**: 主机风险分数 **取值范围**: 最小值0，最大值100 

        :param score: The score of this VulHostHostsResponseInfoDataList.
        :type score: int
        """
        self._score = score

    @property
    def version(self):
        r"""Gets the version of this VulHostHostsResponseInfoDataList.

        **参数解释**: 主机配额 **取值范围**: 字符长度0-64位 

        :return: The version of this VulHostHostsResponseInfoDataList.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this VulHostHostsResponseInfoDataList.

        **参数解释**: 主机配额 **取值范围**: 字符长度0-64位 

        :param version: The version of this VulHostHostsResponseInfoDataList.
        :type version: str
        """
        self._version = version

    @property
    def handle_status(self):
        r"""Gets the handle_status of this VulHostHostsResponseInfoDataList.

        **参数解释**: 主机配额 **取值范围**: - unhandled：待处理 - handled：已处理 

        :return: The handle_status of this VulHostHostsResponseInfoDataList.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this VulHostHostsResponseInfoDataList.

        **参数解释**: 主机配额 **取值范围**: - unhandled：待处理 - handled：已处理 

        :param handle_status: The handle_status of this VulHostHostsResponseInfoDataList.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def vul_num_with_repair_priority_list(self):
        r"""Gets the vul_num_with_repair_priority_list of this VulHostHostsResponseInfoDataList.

        **参数解释**: 各个漏洞修复优先级下的漏洞数量 

        :return: The vul_num_with_repair_priority_list of this VulHostHostsResponseInfoDataList.
        :rtype: list[:class:`huaweicloudsdkhss.v5.VulHostHostsResponseInfoVulNumWithRepairPriorityList`]
        """
        return self._vul_num_with_repair_priority_list

    @vul_num_with_repair_priority_list.setter
    def vul_num_with_repair_priority_list(self, vul_num_with_repair_priority_list):
        r"""Sets the vul_num_with_repair_priority_list of this VulHostHostsResponseInfoDataList.

        **参数解释**: 各个漏洞修复优先级下的漏洞数量 

        :param vul_num_with_repair_priority_list: The vul_num_with_repair_priority_list of this VulHostHostsResponseInfoDataList.
        :type vul_num_with_repair_priority_list: list[:class:`huaweicloudsdkhss.v5.VulHostHostsResponseInfoVulNumWithRepairPriorityList`]
        """
        self._vul_num_with_repair_priority_list = vul_num_with_repair_priority_list

    @property
    def vul_ids_info(self):
        r"""Gets the vul_ids_info of this VulHostHostsResponseInfoDataList.

        :return: The vul_ids_info of this VulHostHostsResponseInfoDataList.
        :rtype: :class:`huaweicloudsdkhss.v5.VulHostHostsResponseInfoVulIdsInfo`
        """
        return self._vul_ids_info

    @vul_ids_info.setter
    def vul_ids_info(self, vul_ids_info):
        r"""Sets the vul_ids_info of this VulHostHostsResponseInfoDataList.

        :param vul_ids_info: The vul_ids_info of this VulHostHostsResponseInfoDataList.
        :type vul_ids_info: :class:`huaweicloudsdkhss.v5.VulHostHostsResponseInfoVulIdsInfo`
        """
        self._vul_ids_info = vul_ids_info

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
        if not isinstance(other, VulHostHostsResponseInfoDataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
