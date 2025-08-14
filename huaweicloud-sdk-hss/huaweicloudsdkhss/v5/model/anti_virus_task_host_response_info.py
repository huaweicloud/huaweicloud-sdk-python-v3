# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AntiVirusTaskHostResponseInfo:

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
        'host_name': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'asset_value': 'str',
        'start_time': 'int',
        'run_duration': 'int',
        'scan_progress': 'str',
        'virus_num': 'int',
        'scan_file_num': 'int',
        'host_task_status': 'str',
        'fail_reason': 'str',
        'deleted': 'bool',
        'whether_using_quota': 'int',
        'agent_id': 'str',
        'os_type': 'str',
        'host_status': 'str',
        'agent_status': 'str',
        'protect_status': 'str',
        'os_name': 'str',
        'os_version': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'asset_value': 'asset_value',
        'start_time': 'start_time',
        'run_duration': 'run_duration',
        'scan_progress': 'scan_progress',
        'virus_num': 'virus_num',
        'scan_file_num': 'scan_file_num',
        'host_task_status': 'host_task_status',
        'fail_reason': 'fail_reason',
        'deleted': 'deleted',
        'whether_using_quota': 'whether_using_quota',
        'agent_id': 'agent_id',
        'os_type': 'os_type',
        'host_status': 'host_status',
        'agent_status': 'agent_status',
        'protect_status': 'protect_status',
        'os_name': 'os_name',
        'os_version': 'os_version'
    }

    def __init__(self, host_id=None, host_name=None, private_ip=None, public_ip=None, asset_value=None, start_time=None, run_duration=None, scan_progress=None, virus_num=None, scan_file_num=None, host_task_status=None, fail_reason=None, deleted=None, whether_using_quota=None, agent_id=None, os_type=None, host_status=None, agent_status=None, protect_status=None, os_name=None, os_version=None):
        r"""AntiVirusTaskHostResponseInfo

        The model defined in huaweicloud sdk

        :param host_id: **参数解释**： 主机ID **取值范围**： 字符长度1-64位 
        :type host_id: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param private_ip: **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 
        :type private_ip: str
        :param public_ip: **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 
        :type public_ip: str
        :param asset_value: 资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产
        :type asset_value: str
        :param start_time: 启动时间，毫秒
        :type start_time: int
        :param run_duration: 运行时长，秒
        :type run_duration: int
        :param scan_progress: 扫描进度
        :type scan_progress: str
        :param virus_num: 新发现病毒数量
        :type virus_num: int
        :param scan_file_num: 已扫描的文件数量
        :type scan_file_num: int
        :param host_task_status: 服务器扫描状态，包含如下4种   - scanning ：扫描中   - success ：扫描成功   - fail ：扫描失败   - cancel ：取消扫描
        :type host_task_status: str
        :param fail_reason: 失败原因
        :type fail_reason: str
        :param deleted: 是否删除，包含如下:   - true ：已删除   - false : 未删除
        :type deleted: bool
        :param whether_using_quota: 是否使用病毒查杀按次计费配额
        :type whether_using_quota: int
        :param agent_id: **参数解释**: Agent ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type agent_id: str
        :param os_type: **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 
        :type os_type: str
        :param host_status: 服务器状态
        :type host_status: str
        :param agent_status: Agent状态，包含如下6种。   - installed ：已安装。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。   - install_failed ：安装失败。   - installing ：安装中。   - not_online ：不在线的（除了在线以外的所有状态，仅作为查询条件）。
        :type agent_status: str
        :param protect_status: 防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。
        :type protect_status: str
        :param os_name: 操作系统名称
        :type os_name: str
        :param os_version: 系统版本
        :type os_version: str
        """
        
        

        self._host_id = None
        self._host_name = None
        self._private_ip = None
        self._public_ip = None
        self._asset_value = None
        self._start_time = None
        self._run_duration = None
        self._scan_progress = None
        self._virus_num = None
        self._scan_file_num = None
        self._host_task_status = None
        self._fail_reason = None
        self._deleted = None
        self._whether_using_quota = None
        self._agent_id = None
        self._os_type = None
        self._host_status = None
        self._agent_status = None
        self._protect_status = None
        self._os_name = None
        self._os_version = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if asset_value is not None:
            self.asset_value = asset_value
        if start_time is not None:
            self.start_time = start_time
        if run_duration is not None:
            self.run_duration = run_duration
        if scan_progress is not None:
            self.scan_progress = scan_progress
        if virus_num is not None:
            self.virus_num = virus_num
        if scan_file_num is not None:
            self.scan_file_num = scan_file_num
        if host_task_status is not None:
            self.host_task_status = host_task_status
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if deleted is not None:
            self.deleted = deleted
        if whether_using_quota is not None:
            self.whether_using_quota = whether_using_quota
        if agent_id is not None:
            self.agent_id = agent_id
        if os_type is not None:
            self.os_type = os_type
        if host_status is not None:
            self.host_status = host_status
        if agent_status is not None:
            self.agent_status = agent_status
        if protect_status is not None:
            self.protect_status = protect_status
        if os_name is not None:
            self.os_name = os_name
        if os_version is not None:
            self.os_version = os_version

    @property
    def host_id(self):
        r"""Gets the host_id of this AntiVirusTaskHostResponseInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :return: The host_id of this AntiVirusTaskHostResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this AntiVirusTaskHostResponseInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :param host_id: The host_id of this AntiVirusTaskHostResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this AntiVirusTaskHostResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this AntiVirusTaskHostResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this AntiVirusTaskHostResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this AntiVirusTaskHostResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def private_ip(self):
        r"""Gets the private_ip of this AntiVirusTaskHostResponseInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :return: The private_ip of this AntiVirusTaskHostResponseInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this AntiVirusTaskHostResponseInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :param private_ip: The private_ip of this AntiVirusTaskHostResponseInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this AntiVirusTaskHostResponseInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 

        :return: The public_ip of this AntiVirusTaskHostResponseInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this AntiVirusTaskHostResponseInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 

        :param public_ip: The public_ip of this AntiVirusTaskHostResponseInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def asset_value(self):
        r"""Gets the asset_value of this AntiVirusTaskHostResponseInfo.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :return: The asset_value of this AntiVirusTaskHostResponseInfo.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this AntiVirusTaskHostResponseInfo.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :param asset_value: The asset_value of this AntiVirusTaskHostResponseInfo.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def start_time(self):
        r"""Gets the start_time of this AntiVirusTaskHostResponseInfo.

        启动时间，毫秒

        :return: The start_time of this AntiVirusTaskHostResponseInfo.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this AntiVirusTaskHostResponseInfo.

        启动时间，毫秒

        :param start_time: The start_time of this AntiVirusTaskHostResponseInfo.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def run_duration(self):
        r"""Gets the run_duration of this AntiVirusTaskHostResponseInfo.

        运行时长，秒

        :return: The run_duration of this AntiVirusTaskHostResponseInfo.
        :rtype: int
        """
        return self._run_duration

    @run_duration.setter
    def run_duration(self, run_duration):
        r"""Sets the run_duration of this AntiVirusTaskHostResponseInfo.

        运行时长，秒

        :param run_duration: The run_duration of this AntiVirusTaskHostResponseInfo.
        :type run_duration: int
        """
        self._run_duration = run_duration

    @property
    def scan_progress(self):
        r"""Gets the scan_progress of this AntiVirusTaskHostResponseInfo.

        扫描进度

        :return: The scan_progress of this AntiVirusTaskHostResponseInfo.
        :rtype: str
        """
        return self._scan_progress

    @scan_progress.setter
    def scan_progress(self, scan_progress):
        r"""Sets the scan_progress of this AntiVirusTaskHostResponseInfo.

        扫描进度

        :param scan_progress: The scan_progress of this AntiVirusTaskHostResponseInfo.
        :type scan_progress: str
        """
        self._scan_progress = scan_progress

    @property
    def virus_num(self):
        r"""Gets the virus_num of this AntiVirusTaskHostResponseInfo.

        新发现病毒数量

        :return: The virus_num of this AntiVirusTaskHostResponseInfo.
        :rtype: int
        """
        return self._virus_num

    @virus_num.setter
    def virus_num(self, virus_num):
        r"""Sets the virus_num of this AntiVirusTaskHostResponseInfo.

        新发现病毒数量

        :param virus_num: The virus_num of this AntiVirusTaskHostResponseInfo.
        :type virus_num: int
        """
        self._virus_num = virus_num

    @property
    def scan_file_num(self):
        r"""Gets the scan_file_num of this AntiVirusTaskHostResponseInfo.

        已扫描的文件数量

        :return: The scan_file_num of this AntiVirusTaskHostResponseInfo.
        :rtype: int
        """
        return self._scan_file_num

    @scan_file_num.setter
    def scan_file_num(self, scan_file_num):
        r"""Sets the scan_file_num of this AntiVirusTaskHostResponseInfo.

        已扫描的文件数量

        :param scan_file_num: The scan_file_num of this AntiVirusTaskHostResponseInfo.
        :type scan_file_num: int
        """
        self._scan_file_num = scan_file_num

    @property
    def host_task_status(self):
        r"""Gets the host_task_status of this AntiVirusTaskHostResponseInfo.

        服务器扫描状态，包含如下4种   - scanning ：扫描中   - success ：扫描成功   - fail ：扫描失败   - cancel ：取消扫描

        :return: The host_task_status of this AntiVirusTaskHostResponseInfo.
        :rtype: str
        """
        return self._host_task_status

    @host_task_status.setter
    def host_task_status(self, host_task_status):
        r"""Sets the host_task_status of this AntiVirusTaskHostResponseInfo.

        服务器扫描状态，包含如下4种   - scanning ：扫描中   - success ：扫描成功   - fail ：扫描失败   - cancel ：取消扫描

        :param host_task_status: The host_task_status of this AntiVirusTaskHostResponseInfo.
        :type host_task_status: str
        """
        self._host_task_status = host_task_status

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this AntiVirusTaskHostResponseInfo.

        失败原因

        :return: The fail_reason of this AntiVirusTaskHostResponseInfo.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this AntiVirusTaskHostResponseInfo.

        失败原因

        :param fail_reason: The fail_reason of this AntiVirusTaskHostResponseInfo.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def deleted(self):
        r"""Gets the deleted of this AntiVirusTaskHostResponseInfo.

        是否删除，包含如下:   - true ：已删除   - false : 未删除

        :return: The deleted of this AntiVirusTaskHostResponseInfo.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        r"""Sets the deleted of this AntiVirusTaskHostResponseInfo.

        是否删除，包含如下:   - true ：已删除   - false : 未删除

        :param deleted: The deleted of this AntiVirusTaskHostResponseInfo.
        :type deleted: bool
        """
        self._deleted = deleted

    @property
    def whether_using_quota(self):
        r"""Gets the whether_using_quota of this AntiVirusTaskHostResponseInfo.

        是否使用病毒查杀按次计费配额

        :return: The whether_using_quota of this AntiVirusTaskHostResponseInfo.
        :rtype: int
        """
        return self._whether_using_quota

    @whether_using_quota.setter
    def whether_using_quota(self, whether_using_quota):
        r"""Sets the whether_using_quota of this AntiVirusTaskHostResponseInfo.

        是否使用病毒查杀按次计费配额

        :param whether_using_quota: The whether_using_quota of this AntiVirusTaskHostResponseInfo.
        :type whether_using_quota: int
        """
        self._whether_using_quota = whether_using_quota

    @property
    def agent_id(self):
        r"""Gets the agent_id of this AntiVirusTaskHostResponseInfo.

        **参数解释**: Agent ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The agent_id of this AntiVirusTaskHostResponseInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this AntiVirusTaskHostResponseInfo.

        **参数解释**: Agent ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param agent_id: The agent_id of this AntiVirusTaskHostResponseInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def os_type(self):
        r"""Gets the os_type of this AntiVirusTaskHostResponseInfo.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 

        :return: The os_type of this AntiVirusTaskHostResponseInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this AntiVirusTaskHostResponseInfo.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 

        :param os_type: The os_type of this AntiVirusTaskHostResponseInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def host_status(self):
        r"""Gets the host_status of this AntiVirusTaskHostResponseInfo.

        服务器状态

        :return: The host_status of this AntiVirusTaskHostResponseInfo.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        r"""Sets the host_status of this AntiVirusTaskHostResponseInfo.

        服务器状态

        :param host_status: The host_status of this AntiVirusTaskHostResponseInfo.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def agent_status(self):
        r"""Gets the agent_status of this AntiVirusTaskHostResponseInfo.

        Agent状态，包含如下6种。   - installed ：已安装。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。   - install_failed ：安装失败。   - installing ：安装中。   - not_online ：不在线的（除了在线以外的所有状态，仅作为查询条件）。

        :return: The agent_status of this AntiVirusTaskHostResponseInfo.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this AntiVirusTaskHostResponseInfo.

        Agent状态，包含如下6种。   - installed ：已安装。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。   - install_failed ：安装失败。   - installing ：安装中。   - not_online ：不在线的（除了在线以外的所有状态，仅作为查询条件）。

        :param agent_status: The agent_status of this AntiVirusTaskHostResponseInfo.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def protect_status(self):
        r"""Gets the protect_status of this AntiVirusTaskHostResponseInfo.

        防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。

        :return: The protect_status of this AntiVirusTaskHostResponseInfo.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this AntiVirusTaskHostResponseInfo.

        防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。

        :param protect_status: The protect_status of this AntiVirusTaskHostResponseInfo.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def os_name(self):
        r"""Gets the os_name of this AntiVirusTaskHostResponseInfo.

        操作系统名称

        :return: The os_name of this AntiVirusTaskHostResponseInfo.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        r"""Sets the os_name of this AntiVirusTaskHostResponseInfo.

        操作系统名称

        :param os_name: The os_name of this AntiVirusTaskHostResponseInfo.
        :type os_name: str
        """
        self._os_name = os_name

    @property
    def os_version(self):
        r"""Gets the os_version of this AntiVirusTaskHostResponseInfo.

        系统版本

        :return: The os_version of this AntiVirusTaskHostResponseInfo.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this AntiVirusTaskHostResponseInfo.

        系统版本

        :param os_version: The os_version of this AntiVirusTaskHostResponseInfo.
        :type os_version: str
        """
        self._os_version = os_version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AntiVirusTaskHostResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
