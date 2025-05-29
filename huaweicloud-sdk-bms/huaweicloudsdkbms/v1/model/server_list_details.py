# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerListDetails:

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
        'user_id': 'str',
        'name': 'str',
        'created': 'str',
        'updated': 'str',
        'tenant_id': 'str',
        'flavor': 'FlavorDetailInfos',
        'status': 'str',
        'task_state': 'str',
        'vm_state': 'str',
        'availability_zone': 'str',
        'fault': 'Fault',
        'in_recycle_bin': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'user_id',
        'name': 'name',
        'created': 'created',
        'updated': 'updated',
        'tenant_id': 'tenant_id',
        'flavor': 'flavor',
        'status': 'status',
        'task_state': 'task_state',
        'vm_state': 'vm_state',
        'availability_zone': 'availability_zone',
        'fault': 'fault',
        'in_recycle_bin': 'in_recycle_bin'
    }

    def __init__(self, id=None, user_id=None, name=None, created=None, updated=None, tenant_id=None, flavor=None, status=None, task_state=None, vm_state=None, availability_zone=None, fault=None, in_recycle_bin=None):
        r"""ServerListDetails

        The model defined in huaweicloud sdk

        :param id: 裸金属服务器ID，格式为UUID
        :type id: str
        :param user_id: 创建裸金属服务器的用户ID，格式为UUID。
        :type user_id: str
        :param name: 裸金属服务器名称
        :type name: str
        :param created: 裸金属服务器创建时间。时间戳格式为ISO 8601：YYYY-MM-DDTHH:MM:SSZ，例如：2019-05-22T03:30:52Z
        :type created: str
        :param updated: 裸金属服务器更新时间。时间戳格式为ISO 8601：YYYY-MM-DDTHH:MM:SSZ，例如：2019-05-22T04:30:52Z
        :type updated: str
        :param tenant_id: 裸金属服务器所属租户ID，格式为UUID。该参数和project_id表示相同的概念。
        :type tenant_id: str
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkbms.v1.FlavorDetailInfos`
        :param status: 裸金属服务器当前状态信息。  取值范围：  ACTIVE：运行中/正在关机/删除中 BUILD：创建中 ERROR：故障 HARD_REBOOT：强制重启中 REBOOT：重启中 DELETED：实例已被正常删除 SHUTOFF：关机/正在开机/删除中/重建中/重装操作系统中/重装操作系统失败/冻结
        :type status: str
        :param task_state: 扩展属性，裸金属服务器当前的任务状态。例如：rebooting：重启中reboot_started：普通重启reboot_started_hard：强制重启powering-off：关机中powering-on：开机中rebuilding：重建中scheduling：调度中deleting：删除中
        :type task_state: str
        :param vm_state: 扩展属性，裸金属服务器的稳定状态。例如：active：运行中shutoff：关机reboot：重启
        :type vm_state: str
        :param availability_zone: 扩展属性，裸金属服务器所在可用分区名称。
        :type availability_zone: str
        :param fault: 
        :type fault: :class:`huaweicloudsdkbms.v1.Fault`
        :param in_recycle_bin: 裸机是否在回收站中
        :type in_recycle_bin: bool
        """
        
        

        self._id = None
        self._user_id = None
        self._name = None
        self._created = None
        self._updated = None
        self._tenant_id = None
        self._flavor = None
        self._status = None
        self._task_state = None
        self._vm_state = None
        self._availability_zone = None
        self._fault = None
        self._in_recycle_bin = None
        self.discriminator = None

        self.id = id
        if user_id is not None:
            self.user_id = user_id
        self.name = name
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        self.tenant_id = tenant_id
        if flavor is not None:
            self.flavor = flavor
        self.status = status
        if task_state is not None:
            self.task_state = task_state
        if vm_state is not None:
            self.vm_state = vm_state
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if fault is not None:
            self.fault = fault
        if in_recycle_bin is not None:
            self.in_recycle_bin = in_recycle_bin

    @property
    def id(self):
        r"""Gets the id of this ServerListDetails.

        裸金属服务器ID，格式为UUID

        :return: The id of this ServerListDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ServerListDetails.

        裸金属服务器ID，格式为UUID

        :param id: The id of this ServerListDetails.
        :type id: str
        """
        self._id = id

    @property
    def user_id(self):
        r"""Gets the user_id of this ServerListDetails.

        创建裸金属服务器的用户ID，格式为UUID。

        :return: The user_id of this ServerListDetails.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ServerListDetails.

        创建裸金属服务器的用户ID，格式为UUID。

        :param user_id: The user_id of this ServerListDetails.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def name(self):
        r"""Gets the name of this ServerListDetails.

        裸金属服务器名称

        :return: The name of this ServerListDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ServerListDetails.

        裸金属服务器名称

        :param name: The name of this ServerListDetails.
        :type name: str
        """
        self._name = name

    @property
    def created(self):
        r"""Gets the created of this ServerListDetails.

        裸金属服务器创建时间。时间戳格式为ISO 8601：YYYY-MM-DDTHH:MM:SSZ，例如：2019-05-22T03:30:52Z

        :return: The created of this ServerListDetails.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ServerListDetails.

        裸金属服务器创建时间。时间戳格式为ISO 8601：YYYY-MM-DDTHH:MM:SSZ，例如：2019-05-22T03:30:52Z

        :param created: The created of this ServerListDetails.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this ServerListDetails.

        裸金属服务器更新时间。时间戳格式为ISO 8601：YYYY-MM-DDTHH:MM:SSZ，例如：2019-05-22T04:30:52Z

        :return: The updated of this ServerListDetails.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this ServerListDetails.

        裸金属服务器更新时间。时间戳格式为ISO 8601：YYYY-MM-DDTHH:MM:SSZ，例如：2019-05-22T04:30:52Z

        :param updated: The updated of this ServerListDetails.
        :type updated: str
        """
        self._updated = updated

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ServerListDetails.

        裸金属服务器所属租户ID，格式为UUID。该参数和project_id表示相同的概念。

        :return: The tenant_id of this ServerListDetails.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ServerListDetails.

        裸金属服务器所属租户ID，格式为UUID。该参数和project_id表示相同的概念。

        :param tenant_id: The tenant_id of this ServerListDetails.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def flavor(self):
        r"""Gets the flavor of this ServerListDetails.

        :return: The flavor of this ServerListDetails.
        :rtype: :class:`huaweicloudsdkbms.v1.FlavorDetailInfos`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this ServerListDetails.

        :param flavor: The flavor of this ServerListDetails.
        :type flavor: :class:`huaweicloudsdkbms.v1.FlavorDetailInfos`
        """
        self._flavor = flavor

    @property
    def status(self):
        r"""Gets the status of this ServerListDetails.

        裸金属服务器当前状态信息。  取值范围：  ACTIVE：运行中/正在关机/删除中 BUILD：创建中 ERROR：故障 HARD_REBOOT：强制重启中 REBOOT：重启中 DELETED：实例已被正常删除 SHUTOFF：关机/正在开机/删除中/重建中/重装操作系统中/重装操作系统失败/冻结

        :return: The status of this ServerListDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ServerListDetails.

        裸金属服务器当前状态信息。  取值范围：  ACTIVE：运行中/正在关机/删除中 BUILD：创建中 ERROR：故障 HARD_REBOOT：强制重启中 REBOOT：重启中 DELETED：实例已被正常删除 SHUTOFF：关机/正在开机/删除中/重建中/重装操作系统中/重装操作系统失败/冻结

        :param status: The status of this ServerListDetails.
        :type status: str
        """
        self._status = status

    @property
    def task_state(self):
        r"""Gets the task_state of this ServerListDetails.

        扩展属性，裸金属服务器当前的任务状态。例如：rebooting：重启中reboot_started：普通重启reboot_started_hard：强制重启powering-off：关机中powering-on：开机中rebuilding：重建中scheduling：调度中deleting：删除中

        :return: The task_state of this ServerListDetails.
        :rtype: str
        """
        return self._task_state

    @task_state.setter
    def task_state(self, task_state):
        r"""Sets the task_state of this ServerListDetails.

        扩展属性，裸金属服务器当前的任务状态。例如：rebooting：重启中reboot_started：普通重启reboot_started_hard：强制重启powering-off：关机中powering-on：开机中rebuilding：重建中scheduling：调度中deleting：删除中

        :param task_state: The task_state of this ServerListDetails.
        :type task_state: str
        """
        self._task_state = task_state

    @property
    def vm_state(self):
        r"""Gets the vm_state of this ServerListDetails.

        扩展属性，裸金属服务器的稳定状态。例如：active：运行中shutoff：关机reboot：重启

        :return: The vm_state of this ServerListDetails.
        :rtype: str
        """
        return self._vm_state

    @vm_state.setter
    def vm_state(self, vm_state):
        r"""Sets the vm_state of this ServerListDetails.

        扩展属性，裸金属服务器的稳定状态。例如：active：运行中shutoff：关机reboot：重启

        :param vm_state: The vm_state of this ServerListDetails.
        :type vm_state: str
        """
        self._vm_state = vm_state

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ServerListDetails.

        扩展属性，裸金属服务器所在可用分区名称。

        :return: The availability_zone of this ServerListDetails.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ServerListDetails.

        扩展属性，裸金属服务器所在可用分区名称。

        :param availability_zone: The availability_zone of this ServerListDetails.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def fault(self):
        r"""Gets the fault of this ServerListDetails.

        :return: The fault of this ServerListDetails.
        :rtype: :class:`huaweicloudsdkbms.v1.Fault`
        """
        return self._fault

    @fault.setter
    def fault(self, fault):
        r"""Sets the fault of this ServerListDetails.

        :param fault: The fault of this ServerListDetails.
        :type fault: :class:`huaweicloudsdkbms.v1.Fault`
        """
        self._fault = fault

    @property
    def in_recycle_bin(self):
        r"""Gets the in_recycle_bin of this ServerListDetails.

        裸机是否在回收站中

        :return: The in_recycle_bin of this ServerListDetails.
        :rtype: bool
        """
        return self._in_recycle_bin

    @in_recycle_bin.setter
    def in_recycle_bin(self, in_recycle_bin):
        r"""Sets the in_recycle_bin of this ServerListDetails.

        裸机是否在回收站中

        :param in_recycle_bin: The in_recycle_bin of this ServerListDetails.
        :type in_recycle_bin: bool
        """
        self._in_recycle_bin = in_recycle_bin

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
        if not isinstance(other, ServerListDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
