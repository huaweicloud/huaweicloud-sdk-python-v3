# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CdmCreateClusterReqCluster:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schedule_boot_time': 'str',
        'is_schedule_boot_off': 'bool',
        'instances': 'list[Instance]',
        'datastore': 'Datastore',
        'extended_properties': 'ExtendedProperties',
        'schedule_off_time': 'str',
        'vpc_id': 'str',
        'name': 'str',
        'sys_tags': 'list[SysTags]',
        'is_auto_off': 'bool'
    }

    attribute_map = {
        'schedule_boot_time': 'scheduleBootTime',
        'is_schedule_boot_off': 'isScheduleBootOff',
        'instances': 'instances',
        'datastore': 'datastore',
        'extended_properties': 'extended_properties',
        'schedule_off_time': 'scheduleOffTime',
        'vpc_id': 'vpcId',
        'name': 'name',
        'sys_tags': 'sys_tags',
        'is_auto_off': 'isAutoOff'
    }

    def __init__(self, schedule_boot_time=None, is_schedule_boot_off=None, instances=None, datastore=None, extended_properties=None, schedule_off_time=None, vpc_id=None, name=None, sys_tags=None, is_auto_off=None):
        r"""CdmCreateClusterReqCluster

        The model defined in huaweicloud sdk

        :param schedule_boot_time: 定时开机的时间，CDM集群会在每天这个时间开机
        :type schedule_boot_time: str
        :param is_schedule_boot_off: 选择是否启用定时开关机功能。定时开关机功能和自动关机功能不可同时开启
        :type is_schedule_boot_off: bool
        :param instances: 节点列表，请参见instances参数说明
        :type instances: list[:class:`huaweicloudsdkcdm.v1.Instance`]
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkcdm.v1.Datastore`
        :param extended_properties: 
        :type extended_properties: :class:`huaweicloudsdkcdm.v1.ExtendedProperties`
        :param schedule_off_time: 定时关机的时间，定时关机时系统不会等待未完成的作业执行完成
        :type schedule_off_time: str
        :param vpc_id: 指定虚拟私有云ID，用于集群网络配置
        :type vpc_id: str
        :param name: 集群名称
        :type name: str
        :param sys_tags: 企业项目信息，请参见•sys_tags参数说明
        :type sys_tags: list[:class:`huaweicloudsdkcdm.v1.SysTags`]
        :param is_auto_off: 选择是否启用自动关机功能，自动关机功能和定时开关机功能不可同时开启。如果选择自动关机，则当集群中无作业运行且无定时作业时，等待15分钟后集群将自动关机来帮您节约成本
        :type is_auto_off: bool
        """
        
        

        self._schedule_boot_time = None
        self._is_schedule_boot_off = None
        self._instances = None
        self._datastore = None
        self._extended_properties = None
        self._schedule_off_time = None
        self._vpc_id = None
        self._name = None
        self._sys_tags = None
        self._is_auto_off = None
        self.discriminator = None

        if schedule_boot_time is not None:
            self.schedule_boot_time = schedule_boot_time
        if is_schedule_boot_off is not None:
            self.is_schedule_boot_off = is_schedule_boot_off
        if instances is not None:
            self.instances = instances
        if datastore is not None:
            self.datastore = datastore
        if extended_properties is not None:
            self.extended_properties = extended_properties
        if schedule_off_time is not None:
            self.schedule_off_time = schedule_off_time
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if name is not None:
            self.name = name
        if sys_tags is not None:
            self.sys_tags = sys_tags
        if is_auto_off is not None:
            self.is_auto_off = is_auto_off

    @property
    def schedule_boot_time(self):
        r"""Gets the schedule_boot_time of this CdmCreateClusterReqCluster.

        定时开机的时间，CDM集群会在每天这个时间开机

        :return: The schedule_boot_time of this CdmCreateClusterReqCluster.
        :rtype: str
        """
        return self._schedule_boot_time

    @schedule_boot_time.setter
    def schedule_boot_time(self, schedule_boot_time):
        r"""Sets the schedule_boot_time of this CdmCreateClusterReqCluster.

        定时开机的时间，CDM集群会在每天这个时间开机

        :param schedule_boot_time: The schedule_boot_time of this CdmCreateClusterReqCluster.
        :type schedule_boot_time: str
        """
        self._schedule_boot_time = schedule_boot_time

    @property
    def is_schedule_boot_off(self):
        r"""Gets the is_schedule_boot_off of this CdmCreateClusterReqCluster.

        选择是否启用定时开关机功能。定时开关机功能和自动关机功能不可同时开启

        :return: The is_schedule_boot_off of this CdmCreateClusterReqCluster.
        :rtype: bool
        """
        return self._is_schedule_boot_off

    @is_schedule_boot_off.setter
    def is_schedule_boot_off(self, is_schedule_boot_off):
        r"""Sets the is_schedule_boot_off of this CdmCreateClusterReqCluster.

        选择是否启用定时开关机功能。定时开关机功能和自动关机功能不可同时开启

        :param is_schedule_boot_off: The is_schedule_boot_off of this CdmCreateClusterReqCluster.
        :type is_schedule_boot_off: bool
        """
        self._is_schedule_boot_off = is_schedule_boot_off

    @property
    def instances(self):
        r"""Gets the instances of this CdmCreateClusterReqCluster.

        节点列表，请参见instances参数说明

        :return: The instances of this CdmCreateClusterReqCluster.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.Instance`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this CdmCreateClusterReqCluster.

        节点列表，请参见instances参数说明

        :param instances: The instances of this CdmCreateClusterReqCluster.
        :type instances: list[:class:`huaweicloudsdkcdm.v1.Instance`]
        """
        self._instances = instances

    @property
    def datastore(self):
        r"""Gets the datastore of this CdmCreateClusterReqCluster.

        :return: The datastore of this CdmCreateClusterReqCluster.
        :rtype: :class:`huaweicloudsdkcdm.v1.Datastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this CdmCreateClusterReqCluster.

        :param datastore: The datastore of this CdmCreateClusterReqCluster.
        :type datastore: :class:`huaweicloudsdkcdm.v1.Datastore`
        """
        self._datastore = datastore

    @property
    def extended_properties(self):
        r"""Gets the extended_properties of this CdmCreateClusterReqCluster.

        :return: The extended_properties of this CdmCreateClusterReqCluster.
        :rtype: :class:`huaweicloudsdkcdm.v1.ExtendedProperties`
        """
        return self._extended_properties

    @extended_properties.setter
    def extended_properties(self, extended_properties):
        r"""Sets the extended_properties of this CdmCreateClusterReqCluster.

        :param extended_properties: The extended_properties of this CdmCreateClusterReqCluster.
        :type extended_properties: :class:`huaweicloudsdkcdm.v1.ExtendedProperties`
        """
        self._extended_properties = extended_properties

    @property
    def schedule_off_time(self):
        r"""Gets the schedule_off_time of this CdmCreateClusterReqCluster.

        定时关机的时间，定时关机时系统不会等待未完成的作业执行完成

        :return: The schedule_off_time of this CdmCreateClusterReqCluster.
        :rtype: str
        """
        return self._schedule_off_time

    @schedule_off_time.setter
    def schedule_off_time(self, schedule_off_time):
        r"""Sets the schedule_off_time of this CdmCreateClusterReqCluster.

        定时关机的时间，定时关机时系统不会等待未完成的作业执行完成

        :param schedule_off_time: The schedule_off_time of this CdmCreateClusterReqCluster.
        :type schedule_off_time: str
        """
        self._schedule_off_time = schedule_off_time

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CdmCreateClusterReqCluster.

        指定虚拟私有云ID，用于集群网络配置

        :return: The vpc_id of this CdmCreateClusterReqCluster.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CdmCreateClusterReqCluster.

        指定虚拟私有云ID，用于集群网络配置

        :param vpc_id: The vpc_id of this CdmCreateClusterReqCluster.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def name(self):
        r"""Gets the name of this CdmCreateClusterReqCluster.

        集群名称

        :return: The name of this CdmCreateClusterReqCluster.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CdmCreateClusterReqCluster.

        集群名称

        :param name: The name of this CdmCreateClusterReqCluster.
        :type name: str
        """
        self._name = name

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this CdmCreateClusterReqCluster.

        企业项目信息，请参见•sys_tags参数说明

        :return: The sys_tags of this CdmCreateClusterReqCluster.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.SysTags`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this CdmCreateClusterReqCluster.

        企业项目信息，请参见•sys_tags参数说明

        :param sys_tags: The sys_tags of this CdmCreateClusterReqCluster.
        :type sys_tags: list[:class:`huaweicloudsdkcdm.v1.SysTags`]
        """
        self._sys_tags = sys_tags

    @property
    def is_auto_off(self):
        r"""Gets the is_auto_off of this CdmCreateClusterReqCluster.

        选择是否启用自动关机功能，自动关机功能和定时开关机功能不可同时开启。如果选择自动关机，则当集群中无作业运行且无定时作业时，等待15分钟后集群将自动关机来帮您节约成本

        :return: The is_auto_off of this CdmCreateClusterReqCluster.
        :rtype: bool
        """
        return self._is_auto_off

    @is_auto_off.setter
    def is_auto_off(self, is_auto_off):
        r"""Sets the is_auto_off of this CdmCreateClusterReqCluster.

        选择是否启用自动关机功能，自动关机功能和定时开关机功能不可同时开启。如果选择自动关机，则当集群中无作业运行且无定时作业时，等待15分钟后集群将自动关机来帮您节约成本

        :param is_auto_off: The is_auto_off of this CdmCreateClusterReqCluster.
        :type is_auto_off: bool
        """
        self._is_auto_off = is_auto_off

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
        if not isinstance(other, CdmCreateClusterReqCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
