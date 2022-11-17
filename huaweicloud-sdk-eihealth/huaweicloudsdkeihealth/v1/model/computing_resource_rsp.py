# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComputingResourceRsp:

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
        'resource_id': 'str',
        'name': 'str',
        'spec': 'ComputingSpecDto',
        'ip': 'str',
        'system_disk': 'DiskDto',
        'data_disks': 'list[DiskDto]',
        'image': 'ImageDto',
        'charge_mode': 'str',
        'period_num': 'str',
        'create_time': 'str',
        'status': 'str',
        'availability_zone_id': 'str',
        'schedulable': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'resource_id': 'resource_id',
        'name': 'name',
        'spec': 'spec',
        'ip': 'ip',
        'system_disk': 'system_disk',
        'data_disks': 'data_disks',
        'image': 'image',
        'charge_mode': 'charge_mode',
        'period_num': 'period_num',
        'create_time': 'create_time',
        'status': 'status',
        'availability_zone_id': 'availability_zone_id',
        'schedulable': 'schedulable'
    }

    def __init__(self, id=None, resource_id=None, name=None, spec=None, ip=None, system_disk=None, data_disks=None, image=None, charge_mode=None, period_num=None, create_time=None, status=None, availability_zone_id=None, schedulable=None):
        """ComputingResourceRsp

        The model defined in huaweicloud sdk

        :param id: 实例ID
        :type id: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param name: 实例名称
        :type name: str
        :param spec: 
        :type spec: :class:`huaweicloudsdkeihealth.v1.ComputingSpecDto`
        :param ip: IP地址
        :type ip: str
        :param system_disk: 
        :type system_disk: :class:`huaweicloudsdkeihealth.v1.DiskDto`
        :param data_disks: 数据盘
        :type data_disks: list[:class:`huaweicloudsdkeihealth.v1.DiskDto`]
        :param image: 
        :type image: :class:`huaweicloudsdkeihealth.v1.ImageDto`
        :param charge_mode: 计费模式
        :type charge_mode: str
        :param period_num: 购买周期
        :type period_num: str
        :param create_time: 购买时间
        :type create_time: str
        :param status: 状态
        :type status: str
        :param availability_zone_id: 可用区
        :type availability_zone_id: str
        :param schedulable: 资源是否可调度
        :type schedulable: bool
        """
        
        

        self._id = None
        self._resource_id = None
        self._name = None
        self._spec = None
        self._ip = None
        self._system_disk = None
        self._data_disks = None
        self._image = None
        self._charge_mode = None
        self._period_num = None
        self._create_time = None
        self._status = None
        self._availability_zone_id = None
        self._schedulable = None
        self.discriminator = None

        self.id = id
        self.resource_id = resource_id
        self.name = name
        if spec is not None:
            self.spec = spec
        self.ip = ip
        if system_disk is not None:
            self.system_disk = system_disk
        if data_disks is not None:
            self.data_disks = data_disks
        if image is not None:
            self.image = image
        self.charge_mode = charge_mode
        if period_num is not None:
            self.period_num = period_num
        self.create_time = create_time
        self.status = status
        self.availability_zone_id = availability_zone_id
        if schedulable is not None:
            self.schedulable = schedulable

    @property
    def id(self):
        """Gets the id of this ComputingResourceRsp.

        实例ID

        :return: The id of this ComputingResourceRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComputingResourceRsp.

        实例ID

        :param id: The id of this ComputingResourceRsp.
        :type id: str
        """
        self._id = id

    @property
    def resource_id(self):
        """Gets the resource_id of this ComputingResourceRsp.

        资源ID

        :return: The resource_id of this ComputingResourceRsp.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ComputingResourceRsp.

        资源ID

        :param resource_id: The resource_id of this ComputingResourceRsp.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def name(self):
        """Gets the name of this ComputingResourceRsp.

        实例名称

        :return: The name of this ComputingResourceRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComputingResourceRsp.

        实例名称

        :param name: The name of this ComputingResourceRsp.
        :type name: str
        """
        self._name = name

    @property
    def spec(self):
        """Gets the spec of this ComputingResourceRsp.

        :return: The spec of this ComputingResourceRsp.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ComputingSpecDto`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this ComputingResourceRsp.

        :param spec: The spec of this ComputingResourceRsp.
        :type spec: :class:`huaweicloudsdkeihealth.v1.ComputingSpecDto`
        """
        self._spec = spec

    @property
    def ip(self):
        """Gets the ip of this ComputingResourceRsp.

        IP地址

        :return: The ip of this ComputingResourceRsp.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ComputingResourceRsp.

        IP地址

        :param ip: The ip of this ComputingResourceRsp.
        :type ip: str
        """
        self._ip = ip

    @property
    def system_disk(self):
        """Gets the system_disk of this ComputingResourceRsp.

        :return: The system_disk of this ComputingResourceRsp.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DiskDto`
        """
        return self._system_disk

    @system_disk.setter
    def system_disk(self, system_disk):
        """Sets the system_disk of this ComputingResourceRsp.

        :param system_disk: The system_disk of this ComputingResourceRsp.
        :type system_disk: :class:`huaweicloudsdkeihealth.v1.DiskDto`
        """
        self._system_disk = system_disk

    @property
    def data_disks(self):
        """Gets the data_disks of this ComputingResourceRsp.

        数据盘

        :return: The data_disks of this ComputingResourceRsp.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.DiskDto`]
        """
        return self._data_disks

    @data_disks.setter
    def data_disks(self, data_disks):
        """Sets the data_disks of this ComputingResourceRsp.

        数据盘

        :param data_disks: The data_disks of this ComputingResourceRsp.
        :type data_disks: list[:class:`huaweicloudsdkeihealth.v1.DiskDto`]
        """
        self._data_disks = data_disks

    @property
    def image(self):
        """Gets the image of this ComputingResourceRsp.

        :return: The image of this ComputingResourceRsp.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImageDto`
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ComputingResourceRsp.

        :param image: The image of this ComputingResourceRsp.
        :type image: :class:`huaweicloudsdkeihealth.v1.ImageDto`
        """
        self._image = image

    @property
    def charge_mode(self):
        """Gets the charge_mode of this ComputingResourceRsp.

        计费模式

        :return: The charge_mode of this ComputingResourceRsp.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this ComputingResourceRsp.

        计费模式

        :param charge_mode: The charge_mode of this ComputingResourceRsp.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def period_num(self):
        """Gets the period_num of this ComputingResourceRsp.

        购买周期

        :return: The period_num of this ComputingResourceRsp.
        :rtype: str
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this ComputingResourceRsp.

        购买周期

        :param period_num: The period_num of this ComputingResourceRsp.
        :type period_num: str
        """
        self._period_num = period_num

    @property
    def create_time(self):
        """Gets the create_time of this ComputingResourceRsp.

        购买时间

        :return: The create_time of this ComputingResourceRsp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ComputingResourceRsp.

        购买时间

        :param create_time: The create_time of this ComputingResourceRsp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def status(self):
        """Gets the status of this ComputingResourceRsp.

        状态

        :return: The status of this ComputingResourceRsp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ComputingResourceRsp.

        状态

        :param status: The status of this ComputingResourceRsp.
        :type status: str
        """
        self._status = status

    @property
    def availability_zone_id(self):
        """Gets the availability_zone_id of this ComputingResourceRsp.

        可用区

        :return: The availability_zone_id of this ComputingResourceRsp.
        :rtype: str
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        """Sets the availability_zone_id of this ComputingResourceRsp.

        可用区

        :param availability_zone_id: The availability_zone_id of this ComputingResourceRsp.
        :type availability_zone_id: str
        """
        self._availability_zone_id = availability_zone_id

    @property
    def schedulable(self):
        """Gets the schedulable of this ComputingResourceRsp.

        资源是否可调度

        :return: The schedulable of this ComputingResourceRsp.
        :rtype: bool
        """
        return self._schedulable

    @schedulable.setter
    def schedulable(self, schedulable):
        """Sets the schedulable of this ComputingResourceRsp.

        资源是否可调度

        :param schedulable: The schedulable of this ComputingResourceRsp.
        :type schedulable: bool
        """
        self._schedulable = schedulable

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
        if not isinstance(other, ComputingResourceRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
