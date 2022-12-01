# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeResponse:

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
        'name': 'str',
        'description': 'str',
        'created_at': 'str',
        'cluster_id': 'str',
        'cluster_node_state': 'str',
        'cluster_node_type': 'str',
        'firmware_name': 'str',
        'upgrade_firmware_version': 'str',
        'firmware_status': 'str',
        'firmware_upgrade_record': 'list[FirmwareUpdateRecord]',
        'state': 'str',
        'type': 'str',
        'active_status': 'str',
        'cpu': 'int',
        'gpu_num': 'object',
        'npu_num': 'object',
        'host_ips': 'list[str]',
        'tags': 'list[TagObject]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'created_at': 'created_at',
        'cluster_id': 'cluster_id',
        'cluster_node_state': 'cluster_node_state',
        'cluster_node_type': 'cluster_node_type',
        'firmware_name': 'firmware_name',
        'upgrade_firmware_version': 'upgrade_firmware_version',
        'firmware_status': 'firmware_status',
        'firmware_upgrade_record': 'firmware_upgrade_record',
        'state': 'state',
        'type': 'type',
        'active_status': 'active_status',
        'cpu': 'cpu',
        'gpu_num': 'gpu_num',
        'npu_num': 'npu_num',
        'host_ips': 'host_ips',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, description=None, created_at=None, cluster_id=None, cluster_node_state=None, cluster_node_type=None, firmware_name=None, upgrade_firmware_version=None, firmware_status=None, firmware_upgrade_record=None, state=None, type=None, active_status=None, cpu=None, gpu_num=None, npu_num=None, host_ips=None, tags=None):
        """NodeResponse

        The model defined in huaweicloud sdk

        :param id: 设备ID
        :type id: str
        :param name: 设备名称，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64
        :type name: str
        :param description: 设备描述，最大长度255，不允许^, ~, ＃, $, %, &amp;, *, &lt;, &gt;, (, ), [, ], {, }, &#39;, \&quot;, \\
        :type description: str
        :param created_at: 产生时间，如2021-10-15 14:45:22 GMT+08:00
        :type created_at: str
        :param cluster_id: 当该设备处于集群时，显示设备所属的集群ID
        :type cluster_id: str
        :param cluster_node_state: 设备所处集群状态，集群创建（cluster_create）、集群删除（cluster_delete）、添加集群工作节点设备（cluster_add_nodes）、删除集群工作节点设备（cluster_delete_node）、集群节点设备状态更新（cluster_node_state_update）
        :type cluster_node_state: str
        :param cluster_node_type: 当该设备处于集群时，显示所属的集群设备类型。 - cluster_controller 控制设备 - cluster_worker 工作设备
        :type cluster_node_type: str
        :param firmware_name: 固件名称。可包含大小写字母、数字、下划线、中划线,长度不超过60字符。必须以字母开头,字母或数字结尾
        :type firmware_name: str
        :param upgrade_firmware_version: 固件正在升级的版本
        :type upgrade_firmware_version: str
        :param firmware_status: 固件升级状态，1、2、3分别代表升级中，升级失败，升级成功
        :type firmware_status: str
        :param firmware_upgrade_record: 
        :type firmware_upgrade_record: list[:class:`huaweicloudsdkhilens.v3.FirmwareUpdateRecord`]
        :param state: 设备状态：UNCONNECTED(未注册)、RUNNING(运行中)、FAIL(故障)、STOPPED(停用)、UPGRADING(升级中)、FREEZE(冻结)
        :type state: str
        :param type: 设备类型
        :type type: str
        :param active_status: 设备激活状态，未激活（INACTIVE）和已激活（ACTIVATED）
        :type active_status: str
        :param cpu: 设备CPU个数
        :type cpu: int
        :param gpu_num: 设备GPU个数
        :type gpu_num: object
        :param npu_num: 设备NPU个数
        :type npu_num: object
        :param host_ips: 主机IP列表
        :type host_ips: list[str]
        :param tags: 设备标签对列表
        :type tags: list[:class:`huaweicloudsdkhilens.v3.TagObject`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._created_at = None
        self._cluster_id = None
        self._cluster_node_state = None
        self._cluster_node_type = None
        self._firmware_name = None
        self._upgrade_firmware_version = None
        self._firmware_status = None
        self._firmware_upgrade_record = None
        self._state = None
        self._type = None
        self._active_status = None
        self._cpu = None
        self._gpu_num = None
        self._npu_num = None
        self._host_ips = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_node_state is not None:
            self.cluster_node_state = cluster_node_state
        if cluster_node_type is not None:
            self.cluster_node_type = cluster_node_type
        if firmware_name is not None:
            self.firmware_name = firmware_name
        if upgrade_firmware_version is not None:
            self.upgrade_firmware_version = upgrade_firmware_version
        if firmware_status is not None:
            self.firmware_status = firmware_status
        if firmware_upgrade_record is not None:
            self.firmware_upgrade_record = firmware_upgrade_record
        if state is not None:
            self.state = state
        if type is not None:
            self.type = type
        if active_status is not None:
            self.active_status = active_status
        if cpu is not None:
            self.cpu = cpu
        if gpu_num is not None:
            self.gpu_num = gpu_num
        if npu_num is not None:
            self.npu_num = npu_num
        if host_ips is not None:
            self.host_ips = host_ips
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this NodeResponse.

        设备ID

        :return: The id of this NodeResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodeResponse.

        设备ID

        :param id: The id of this NodeResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this NodeResponse.

        设备名称，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64

        :return: The name of this NodeResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NodeResponse.

        设备名称，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64

        :param name: The name of this NodeResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this NodeResponse.

        设备描述，最大长度255，不允许^, ~, ＃, $, %, &, *, <, >, (, ), [, ], {, }, ', \", \\

        :return: The description of this NodeResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NodeResponse.

        设备描述，最大长度255，不允许^, ~, ＃, $, %, &, *, <, >, (, ), [, ], {, }, ', \", \\

        :param description: The description of this NodeResponse.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this NodeResponse.

        产生时间，如2021-10-15 14:45:22 GMT+08:00

        :return: The created_at of this NodeResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this NodeResponse.

        产生时间，如2021-10-15 14:45:22 GMT+08:00

        :param created_at: The created_at of this NodeResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def cluster_id(self):
        """Gets the cluster_id of this NodeResponse.

        当该设备处于集群时，显示设备所属的集群ID

        :return: The cluster_id of this NodeResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this NodeResponse.

        当该设备处于集群时，显示设备所属的集群ID

        :param cluster_id: The cluster_id of this NodeResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_node_state(self):
        """Gets the cluster_node_state of this NodeResponse.

        设备所处集群状态，集群创建（cluster_create）、集群删除（cluster_delete）、添加集群工作节点设备（cluster_add_nodes）、删除集群工作节点设备（cluster_delete_node）、集群节点设备状态更新（cluster_node_state_update）

        :return: The cluster_node_state of this NodeResponse.
        :rtype: str
        """
        return self._cluster_node_state

    @cluster_node_state.setter
    def cluster_node_state(self, cluster_node_state):
        """Sets the cluster_node_state of this NodeResponse.

        设备所处集群状态，集群创建（cluster_create）、集群删除（cluster_delete）、添加集群工作节点设备（cluster_add_nodes）、删除集群工作节点设备（cluster_delete_node）、集群节点设备状态更新（cluster_node_state_update）

        :param cluster_node_state: The cluster_node_state of this NodeResponse.
        :type cluster_node_state: str
        """
        self._cluster_node_state = cluster_node_state

    @property
    def cluster_node_type(self):
        """Gets the cluster_node_type of this NodeResponse.

        当该设备处于集群时，显示所属的集群设备类型。 - cluster_controller 控制设备 - cluster_worker 工作设备

        :return: The cluster_node_type of this NodeResponse.
        :rtype: str
        """
        return self._cluster_node_type

    @cluster_node_type.setter
    def cluster_node_type(self, cluster_node_type):
        """Sets the cluster_node_type of this NodeResponse.

        当该设备处于集群时，显示所属的集群设备类型。 - cluster_controller 控制设备 - cluster_worker 工作设备

        :param cluster_node_type: The cluster_node_type of this NodeResponse.
        :type cluster_node_type: str
        """
        self._cluster_node_type = cluster_node_type

    @property
    def firmware_name(self):
        """Gets the firmware_name of this NodeResponse.

        固件名称。可包含大小写字母、数字、下划线、中划线,长度不超过60字符。必须以字母开头,字母或数字结尾

        :return: The firmware_name of this NodeResponse.
        :rtype: str
        """
        return self._firmware_name

    @firmware_name.setter
    def firmware_name(self, firmware_name):
        """Sets the firmware_name of this NodeResponse.

        固件名称。可包含大小写字母、数字、下划线、中划线,长度不超过60字符。必须以字母开头,字母或数字结尾

        :param firmware_name: The firmware_name of this NodeResponse.
        :type firmware_name: str
        """
        self._firmware_name = firmware_name

    @property
    def upgrade_firmware_version(self):
        """Gets the upgrade_firmware_version of this NodeResponse.

        固件正在升级的版本

        :return: The upgrade_firmware_version of this NodeResponse.
        :rtype: str
        """
        return self._upgrade_firmware_version

    @upgrade_firmware_version.setter
    def upgrade_firmware_version(self, upgrade_firmware_version):
        """Sets the upgrade_firmware_version of this NodeResponse.

        固件正在升级的版本

        :param upgrade_firmware_version: The upgrade_firmware_version of this NodeResponse.
        :type upgrade_firmware_version: str
        """
        self._upgrade_firmware_version = upgrade_firmware_version

    @property
    def firmware_status(self):
        """Gets the firmware_status of this NodeResponse.

        固件升级状态，1、2、3分别代表升级中，升级失败，升级成功

        :return: The firmware_status of this NodeResponse.
        :rtype: str
        """
        return self._firmware_status

    @firmware_status.setter
    def firmware_status(self, firmware_status):
        """Sets the firmware_status of this NodeResponse.

        固件升级状态，1、2、3分别代表升级中，升级失败，升级成功

        :param firmware_status: The firmware_status of this NodeResponse.
        :type firmware_status: str
        """
        self._firmware_status = firmware_status

    @property
    def firmware_upgrade_record(self):
        """Gets the firmware_upgrade_record of this NodeResponse.

        :return: The firmware_upgrade_record of this NodeResponse.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.FirmwareUpdateRecord`]
        """
        return self._firmware_upgrade_record

    @firmware_upgrade_record.setter
    def firmware_upgrade_record(self, firmware_upgrade_record):
        """Sets the firmware_upgrade_record of this NodeResponse.

        :param firmware_upgrade_record: The firmware_upgrade_record of this NodeResponse.
        :type firmware_upgrade_record: list[:class:`huaweicloudsdkhilens.v3.FirmwareUpdateRecord`]
        """
        self._firmware_upgrade_record = firmware_upgrade_record

    @property
    def state(self):
        """Gets the state of this NodeResponse.

        设备状态：UNCONNECTED(未注册)、RUNNING(运行中)、FAIL(故障)、STOPPED(停用)、UPGRADING(升级中)、FREEZE(冻结)

        :return: The state of this NodeResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this NodeResponse.

        设备状态：UNCONNECTED(未注册)、RUNNING(运行中)、FAIL(故障)、STOPPED(停用)、UPGRADING(升级中)、FREEZE(冻结)

        :param state: The state of this NodeResponse.
        :type state: str
        """
        self._state = state

    @property
    def type(self):
        """Gets the type of this NodeResponse.

        设备类型

        :return: The type of this NodeResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NodeResponse.

        设备类型

        :param type: The type of this NodeResponse.
        :type type: str
        """
        self._type = type

    @property
    def active_status(self):
        """Gets the active_status of this NodeResponse.

        设备激活状态，未激活（INACTIVE）和已激活（ACTIVATED）

        :return: The active_status of this NodeResponse.
        :rtype: str
        """
        return self._active_status

    @active_status.setter
    def active_status(self, active_status):
        """Sets the active_status of this NodeResponse.

        设备激活状态，未激活（INACTIVE）和已激活（ACTIVATED）

        :param active_status: The active_status of this NodeResponse.
        :type active_status: str
        """
        self._active_status = active_status

    @property
    def cpu(self):
        """Gets the cpu of this NodeResponse.

        设备CPU个数

        :return: The cpu of this NodeResponse.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this NodeResponse.

        设备CPU个数

        :param cpu: The cpu of this NodeResponse.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def gpu_num(self):
        """Gets the gpu_num of this NodeResponse.

        设备GPU个数

        :return: The gpu_num of this NodeResponse.
        :rtype: object
        """
        return self._gpu_num

    @gpu_num.setter
    def gpu_num(self, gpu_num):
        """Sets the gpu_num of this NodeResponse.

        设备GPU个数

        :param gpu_num: The gpu_num of this NodeResponse.
        :type gpu_num: object
        """
        self._gpu_num = gpu_num

    @property
    def npu_num(self):
        """Gets the npu_num of this NodeResponse.

        设备NPU个数

        :return: The npu_num of this NodeResponse.
        :rtype: object
        """
        return self._npu_num

    @npu_num.setter
    def npu_num(self, npu_num):
        """Sets the npu_num of this NodeResponse.

        设备NPU个数

        :param npu_num: The npu_num of this NodeResponse.
        :type npu_num: object
        """
        self._npu_num = npu_num

    @property
    def host_ips(self):
        """Gets the host_ips of this NodeResponse.

        主机IP列表

        :return: The host_ips of this NodeResponse.
        :rtype: list[str]
        """
        return self._host_ips

    @host_ips.setter
    def host_ips(self, host_ips):
        """Sets the host_ips of this NodeResponse.

        主机IP列表

        :param host_ips: The host_ips of this NodeResponse.
        :type host_ips: list[str]
        """
        self._host_ips = host_ips

    @property
    def tags(self):
        """Gets the tags of this NodeResponse.

        设备标签对列表

        :return: The tags of this NodeResponse.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.TagObject`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this NodeResponse.

        设备标签对列表

        :param tags: The tags of this NodeResponse.
        :type tags: list[:class:`huaweicloudsdkhilens.v3.TagObject`]
        """
        self._tags = tags

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
        if not isinstance(other, NodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
