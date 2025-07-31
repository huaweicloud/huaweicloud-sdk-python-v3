# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KubernetesClusterInfo:

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
        'cluster_name': 'str',
        'cluster_id': 'str',
        'cluster_type': 'str',
        'status': 'str',
        'version': 'str',
        'total_nodes_number': 'int',
        'active_nodes_number': 'int',
        'creation_timestamp': 'int',
        'agent_installed_num': 'int',
        'agent_install_failed_num': 'int',
        'agent_not_install_num': 'int',
        'agent_ds_install_status': 'str',
        'agent_ds_failed_reason': 'str',
        'last_operate_timestamp': 'int',
        'last_scan_time': 'int',
        'sys_vul_num': 'int',
        'app_vul_num': 'int',
        'emg_vul_num': 'int',
        'risk_assess_num': 'int',
        'sec_comp_num': 'int'
    }

    attribute_map = {
        'id': 'id',
        'cluster_name': 'cluster_name',
        'cluster_id': 'cluster_id',
        'cluster_type': 'cluster_type',
        'status': 'status',
        'version': 'version',
        'total_nodes_number': 'total_nodes_number',
        'active_nodes_number': 'active_nodes_number',
        'creation_timestamp': 'creation_timestamp',
        'agent_installed_num': 'agent_installed_num',
        'agent_install_failed_num': 'agent_install_failed_num',
        'agent_not_install_num': 'agent_not_install_num',
        'agent_ds_install_status': 'agent_ds_install_status',
        'agent_ds_failed_reason': 'agent_ds_failed_reason',
        'last_operate_timestamp': 'last_operate_timestamp',
        'last_scan_time': 'last_scan_time',
        'sys_vul_num': 'sys_vul_num',
        'app_vul_num': 'app_vul_num',
        'emg_vul_num': 'emg_vul_num',
        'risk_assess_num': 'risk_assess_num',
        'sec_comp_num': 'sec_comp_num'
    }

    def __init__(self, id=None, cluster_name=None, cluster_id=None, cluster_type=None, status=None, version=None, total_nodes_number=None, active_nodes_number=None, creation_timestamp=None, agent_installed_num=None, agent_install_failed_num=None, agent_not_install_num=None, agent_ds_install_status=None, agent_ds_failed_reason=None, last_operate_timestamp=None, last_scan_time=None, sys_vul_num=None, app_vul_num=None, emg_vul_num=None, risk_assess_num=None, sec_comp_num=None):
        r"""KubernetesClusterInfo

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param cluster_id: 集群ID
        :type cluster_id: str
        :param cluster_type: 集群类型
        :type cluster_type: str
        :param status: 集群状态，包含如下11种。   - Available：可用，表示集群处于正常状态。   - Unavailable：不可用，表示集群异常，需手动删除或联系管理员删除。   - ScalingUp：扩容中，表示集群正处于扩容过程中。   - ScalingDown：缩容中，表示集群正处于缩容过程中。   - Creating：创建中，表示集群正处于创建过程中。   - Deleting：删除中，表示集群正处于删除过程中。   - Upgrading：升级中，表示集群正处于升级过程中。   - Resizing：规格变更中，表示集群正处于变更规格中。   - RollingBack：回滚中，表示集群正处于回滚过程中。   - RollbackFailed：回滚异常，表示集群回滚异常，需联系管理员进行回滚重试。   - Empty：集群无任何资源
        :type status: str
        :param version: 集群版本
        :type version: str
        :param total_nodes_number: 节点总数
        :type total_nodes_number: int
        :param active_nodes_number: 正常节点数
        :type active_nodes_number: int
        :param creation_timestamp: 创建时间戳
        :type creation_timestamp: int
        :param agent_installed_num: 集群下已安装agent节点数
        :type agent_installed_num: int
        :param agent_install_failed_num: 集群下安装失败节点数
        :type agent_install_failed_num: int
        :param agent_not_install_num: 集群下未安装agent节点数
        :type agent_not_install_num: int
        :param agent_ds_install_status: 集群下agent-ds安装状态，关联agent相关信息时则需同时考虑last_operate_time时间，包含如下2种。   - NotInstall：未状态。   - Installed：已安装。
        :type agent_ds_install_status: str
        :param agent_ds_failed_reason: 操作失败原因
        :type agent_ds_failed_reason: str
        :param last_operate_timestamp: 最近操作时间戳，daemonset脚本安装操作时间，间隔10分钟以内时，agent仍处于安装中
        :type last_operate_timestamp: int
        :param last_scan_time: 集群最近一次扫描时间戳
        :type last_scan_time: int
        :param sys_vul_num: 集群下系统漏洞个数
        :type sys_vul_num: int
        :param app_vul_num: 集群下应用漏洞个数
        :type app_vul_num: int
        :param emg_vul_num: 集群下应急漏洞个数
        :type emg_vul_num: int
        :param risk_assess_num: 集群下风险评估问题个数
        :type risk_assess_num: int
        :param sec_comp_num: 集群下安全合规问题个数
        :type sec_comp_num: int
        """
        
        

        self._id = None
        self._cluster_name = None
        self._cluster_id = None
        self._cluster_type = None
        self._status = None
        self._version = None
        self._total_nodes_number = None
        self._active_nodes_number = None
        self._creation_timestamp = None
        self._agent_installed_num = None
        self._agent_install_failed_num = None
        self._agent_not_install_num = None
        self._agent_ds_install_status = None
        self._agent_ds_failed_reason = None
        self._last_operate_timestamp = None
        self._last_scan_time = None
        self._sys_vul_num = None
        self._app_vul_num = None
        self._emg_vul_num = None
        self._risk_assess_num = None
        self._sec_comp_num = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if status is not None:
            self.status = status
        if version is not None:
            self.version = version
        if total_nodes_number is not None:
            self.total_nodes_number = total_nodes_number
        if active_nodes_number is not None:
            self.active_nodes_number = active_nodes_number
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if agent_installed_num is not None:
            self.agent_installed_num = agent_installed_num
        if agent_install_failed_num is not None:
            self.agent_install_failed_num = agent_install_failed_num
        if agent_not_install_num is not None:
            self.agent_not_install_num = agent_not_install_num
        if agent_ds_install_status is not None:
            self.agent_ds_install_status = agent_ds_install_status
        if agent_ds_failed_reason is not None:
            self.agent_ds_failed_reason = agent_ds_failed_reason
        if last_operate_timestamp is not None:
            self.last_operate_timestamp = last_operate_timestamp
        if last_scan_time is not None:
            self.last_scan_time = last_scan_time
        if sys_vul_num is not None:
            self.sys_vul_num = sys_vul_num
        if app_vul_num is not None:
            self.app_vul_num = app_vul_num
        if emg_vul_num is not None:
            self.emg_vul_num = emg_vul_num
        if risk_assess_num is not None:
            self.risk_assess_num = risk_assess_num
        if sec_comp_num is not None:
            self.sec_comp_num = sec_comp_num

    @property
    def id(self):
        r"""Gets the id of this KubernetesClusterInfo.

        id

        :return: The id of this KubernetesClusterInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this KubernetesClusterInfo.

        id

        :param id: The id of this KubernetesClusterInfo.
        :type id: str
        """
        self._id = id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this KubernetesClusterInfo.

        集群名称

        :return: The cluster_name of this KubernetesClusterInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this KubernetesClusterInfo.

        集群名称

        :param cluster_name: The cluster_name of this KubernetesClusterInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this KubernetesClusterInfo.

        集群ID

        :return: The cluster_id of this KubernetesClusterInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this KubernetesClusterInfo.

        集群ID

        :param cluster_id: The cluster_id of this KubernetesClusterInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this KubernetesClusterInfo.

        集群类型

        :return: The cluster_type of this KubernetesClusterInfo.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this KubernetesClusterInfo.

        集群类型

        :param cluster_type: The cluster_type of this KubernetesClusterInfo.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def status(self):
        r"""Gets the status of this KubernetesClusterInfo.

        集群状态，包含如下11种。   - Available：可用，表示集群处于正常状态。   - Unavailable：不可用，表示集群异常，需手动删除或联系管理员删除。   - ScalingUp：扩容中，表示集群正处于扩容过程中。   - ScalingDown：缩容中，表示集群正处于缩容过程中。   - Creating：创建中，表示集群正处于创建过程中。   - Deleting：删除中，表示集群正处于删除过程中。   - Upgrading：升级中，表示集群正处于升级过程中。   - Resizing：规格变更中，表示集群正处于变更规格中。   - RollingBack：回滚中，表示集群正处于回滚过程中。   - RollbackFailed：回滚异常，表示集群回滚异常，需联系管理员进行回滚重试。   - Empty：集群无任何资源

        :return: The status of this KubernetesClusterInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this KubernetesClusterInfo.

        集群状态，包含如下11种。   - Available：可用，表示集群处于正常状态。   - Unavailable：不可用，表示集群异常，需手动删除或联系管理员删除。   - ScalingUp：扩容中，表示集群正处于扩容过程中。   - ScalingDown：缩容中，表示集群正处于缩容过程中。   - Creating：创建中，表示集群正处于创建过程中。   - Deleting：删除中，表示集群正处于删除过程中。   - Upgrading：升级中，表示集群正处于升级过程中。   - Resizing：规格变更中，表示集群正处于变更规格中。   - RollingBack：回滚中，表示集群正处于回滚过程中。   - RollbackFailed：回滚异常，表示集群回滚异常，需联系管理员进行回滚重试。   - Empty：集群无任何资源

        :param status: The status of this KubernetesClusterInfo.
        :type status: str
        """
        self._status = status

    @property
    def version(self):
        r"""Gets the version of this KubernetesClusterInfo.

        集群版本

        :return: The version of this KubernetesClusterInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this KubernetesClusterInfo.

        集群版本

        :param version: The version of this KubernetesClusterInfo.
        :type version: str
        """
        self._version = version

    @property
    def total_nodes_number(self):
        r"""Gets the total_nodes_number of this KubernetesClusterInfo.

        节点总数

        :return: The total_nodes_number of this KubernetesClusterInfo.
        :rtype: int
        """
        return self._total_nodes_number

    @total_nodes_number.setter
    def total_nodes_number(self, total_nodes_number):
        r"""Sets the total_nodes_number of this KubernetesClusterInfo.

        节点总数

        :param total_nodes_number: The total_nodes_number of this KubernetesClusterInfo.
        :type total_nodes_number: int
        """
        self._total_nodes_number = total_nodes_number

    @property
    def active_nodes_number(self):
        r"""Gets the active_nodes_number of this KubernetesClusterInfo.

        正常节点数

        :return: The active_nodes_number of this KubernetesClusterInfo.
        :rtype: int
        """
        return self._active_nodes_number

    @active_nodes_number.setter
    def active_nodes_number(self, active_nodes_number):
        r"""Sets the active_nodes_number of this KubernetesClusterInfo.

        正常节点数

        :param active_nodes_number: The active_nodes_number of this KubernetesClusterInfo.
        :type active_nodes_number: int
        """
        self._active_nodes_number = active_nodes_number

    @property
    def creation_timestamp(self):
        r"""Gets the creation_timestamp of this KubernetesClusterInfo.

        创建时间戳

        :return: The creation_timestamp of this KubernetesClusterInfo.
        :rtype: int
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        r"""Sets the creation_timestamp of this KubernetesClusterInfo.

        创建时间戳

        :param creation_timestamp: The creation_timestamp of this KubernetesClusterInfo.
        :type creation_timestamp: int
        """
        self._creation_timestamp = creation_timestamp

    @property
    def agent_installed_num(self):
        r"""Gets the agent_installed_num of this KubernetesClusterInfo.

        集群下已安装agent节点数

        :return: The agent_installed_num of this KubernetesClusterInfo.
        :rtype: int
        """
        return self._agent_installed_num

    @agent_installed_num.setter
    def agent_installed_num(self, agent_installed_num):
        r"""Sets the agent_installed_num of this KubernetesClusterInfo.

        集群下已安装agent节点数

        :param agent_installed_num: The agent_installed_num of this KubernetesClusterInfo.
        :type agent_installed_num: int
        """
        self._agent_installed_num = agent_installed_num

    @property
    def agent_install_failed_num(self):
        r"""Gets the agent_install_failed_num of this KubernetesClusterInfo.

        集群下安装失败节点数

        :return: The agent_install_failed_num of this KubernetesClusterInfo.
        :rtype: int
        """
        return self._agent_install_failed_num

    @agent_install_failed_num.setter
    def agent_install_failed_num(self, agent_install_failed_num):
        r"""Sets the agent_install_failed_num of this KubernetesClusterInfo.

        集群下安装失败节点数

        :param agent_install_failed_num: The agent_install_failed_num of this KubernetesClusterInfo.
        :type agent_install_failed_num: int
        """
        self._agent_install_failed_num = agent_install_failed_num

    @property
    def agent_not_install_num(self):
        r"""Gets the agent_not_install_num of this KubernetesClusterInfo.

        集群下未安装agent节点数

        :return: The agent_not_install_num of this KubernetesClusterInfo.
        :rtype: int
        """
        return self._agent_not_install_num

    @agent_not_install_num.setter
    def agent_not_install_num(self, agent_not_install_num):
        r"""Sets the agent_not_install_num of this KubernetesClusterInfo.

        集群下未安装agent节点数

        :param agent_not_install_num: The agent_not_install_num of this KubernetesClusterInfo.
        :type agent_not_install_num: int
        """
        self._agent_not_install_num = agent_not_install_num

    @property
    def agent_ds_install_status(self):
        r"""Gets the agent_ds_install_status of this KubernetesClusterInfo.

        集群下agent-ds安装状态，关联agent相关信息时则需同时考虑last_operate_time时间，包含如下2种。   - NotInstall：未状态。   - Installed：已安装。

        :return: The agent_ds_install_status of this KubernetesClusterInfo.
        :rtype: str
        """
        return self._agent_ds_install_status

    @agent_ds_install_status.setter
    def agent_ds_install_status(self, agent_ds_install_status):
        r"""Sets the agent_ds_install_status of this KubernetesClusterInfo.

        集群下agent-ds安装状态，关联agent相关信息时则需同时考虑last_operate_time时间，包含如下2种。   - NotInstall：未状态。   - Installed：已安装。

        :param agent_ds_install_status: The agent_ds_install_status of this KubernetesClusterInfo.
        :type agent_ds_install_status: str
        """
        self._agent_ds_install_status = agent_ds_install_status

    @property
    def agent_ds_failed_reason(self):
        r"""Gets the agent_ds_failed_reason of this KubernetesClusterInfo.

        操作失败原因

        :return: The agent_ds_failed_reason of this KubernetesClusterInfo.
        :rtype: str
        """
        return self._agent_ds_failed_reason

    @agent_ds_failed_reason.setter
    def agent_ds_failed_reason(self, agent_ds_failed_reason):
        r"""Sets the agent_ds_failed_reason of this KubernetesClusterInfo.

        操作失败原因

        :param agent_ds_failed_reason: The agent_ds_failed_reason of this KubernetesClusterInfo.
        :type agent_ds_failed_reason: str
        """
        self._agent_ds_failed_reason = agent_ds_failed_reason

    @property
    def last_operate_timestamp(self):
        r"""Gets the last_operate_timestamp of this KubernetesClusterInfo.

        最近操作时间戳，daemonset脚本安装操作时间，间隔10分钟以内时，agent仍处于安装中

        :return: The last_operate_timestamp of this KubernetesClusterInfo.
        :rtype: int
        """
        return self._last_operate_timestamp

    @last_operate_timestamp.setter
    def last_operate_timestamp(self, last_operate_timestamp):
        r"""Sets the last_operate_timestamp of this KubernetesClusterInfo.

        最近操作时间戳，daemonset脚本安装操作时间，间隔10分钟以内时，agent仍处于安装中

        :param last_operate_timestamp: The last_operate_timestamp of this KubernetesClusterInfo.
        :type last_operate_timestamp: int
        """
        self._last_operate_timestamp = last_operate_timestamp

    @property
    def last_scan_time(self):
        r"""Gets the last_scan_time of this KubernetesClusterInfo.

        集群最近一次扫描时间戳

        :return: The last_scan_time of this KubernetesClusterInfo.
        :rtype: int
        """
        return self._last_scan_time

    @last_scan_time.setter
    def last_scan_time(self, last_scan_time):
        r"""Sets the last_scan_time of this KubernetesClusterInfo.

        集群最近一次扫描时间戳

        :param last_scan_time: The last_scan_time of this KubernetesClusterInfo.
        :type last_scan_time: int
        """
        self._last_scan_time = last_scan_time

    @property
    def sys_vul_num(self):
        r"""Gets the sys_vul_num of this KubernetesClusterInfo.

        集群下系统漏洞个数

        :return: The sys_vul_num of this KubernetesClusterInfo.
        :rtype: int
        """
        return self._sys_vul_num

    @sys_vul_num.setter
    def sys_vul_num(self, sys_vul_num):
        r"""Sets the sys_vul_num of this KubernetesClusterInfo.

        集群下系统漏洞个数

        :param sys_vul_num: The sys_vul_num of this KubernetesClusterInfo.
        :type sys_vul_num: int
        """
        self._sys_vul_num = sys_vul_num

    @property
    def app_vul_num(self):
        r"""Gets the app_vul_num of this KubernetesClusterInfo.

        集群下应用漏洞个数

        :return: The app_vul_num of this KubernetesClusterInfo.
        :rtype: int
        """
        return self._app_vul_num

    @app_vul_num.setter
    def app_vul_num(self, app_vul_num):
        r"""Sets the app_vul_num of this KubernetesClusterInfo.

        集群下应用漏洞个数

        :param app_vul_num: The app_vul_num of this KubernetesClusterInfo.
        :type app_vul_num: int
        """
        self._app_vul_num = app_vul_num

    @property
    def emg_vul_num(self):
        r"""Gets the emg_vul_num of this KubernetesClusterInfo.

        集群下应急漏洞个数

        :return: The emg_vul_num of this KubernetesClusterInfo.
        :rtype: int
        """
        return self._emg_vul_num

    @emg_vul_num.setter
    def emg_vul_num(self, emg_vul_num):
        r"""Sets the emg_vul_num of this KubernetesClusterInfo.

        集群下应急漏洞个数

        :param emg_vul_num: The emg_vul_num of this KubernetesClusterInfo.
        :type emg_vul_num: int
        """
        self._emg_vul_num = emg_vul_num

    @property
    def risk_assess_num(self):
        r"""Gets the risk_assess_num of this KubernetesClusterInfo.

        集群下风险评估问题个数

        :return: The risk_assess_num of this KubernetesClusterInfo.
        :rtype: int
        """
        return self._risk_assess_num

    @risk_assess_num.setter
    def risk_assess_num(self, risk_assess_num):
        r"""Sets the risk_assess_num of this KubernetesClusterInfo.

        集群下风险评估问题个数

        :param risk_assess_num: The risk_assess_num of this KubernetesClusterInfo.
        :type risk_assess_num: int
        """
        self._risk_assess_num = risk_assess_num

    @property
    def sec_comp_num(self):
        r"""Gets the sec_comp_num of this KubernetesClusterInfo.

        集群下安全合规问题个数

        :return: The sec_comp_num of this KubernetesClusterInfo.
        :rtype: int
        """
        return self._sec_comp_num

    @sec_comp_num.setter
    def sec_comp_num(self, sec_comp_num):
        r"""Sets the sec_comp_num of this KubernetesClusterInfo.

        集群下安全合规问题个数

        :param sec_comp_num: The sec_comp_num of this KubernetesClusterInfo.
        :type sec_comp_num: int
        """
        self._sec_comp_num = sec_comp_num

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
        if not isinstance(other, KubernetesClusterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
