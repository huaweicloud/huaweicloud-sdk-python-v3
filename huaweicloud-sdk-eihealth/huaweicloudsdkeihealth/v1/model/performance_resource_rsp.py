# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PerformanceResourceRsp:

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
        'spec': 'SpecDto',
        'availability_zone_id': 'str',
        'space': 'int',
        'free_space': 'float',
        'charge_mode': 'str',
        'period_num': 'int',
        'job_quota': 'int',
        'create_time': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'resource_id': 'resource_id',
        'name': 'name',
        'spec': 'spec',
        'availability_zone_id': 'availability_zone_id',
        'space': 'space',
        'free_space': 'free_space',
        'charge_mode': 'charge_mode',
        'period_num': 'period_num',
        'job_quota': 'job_quota',
        'create_time': 'create_time',
        'status': 'status'
    }

    def __init__(self, id=None, resource_id=None, name=None, spec=None, availability_zone_id=None, space=None, free_space=None, charge_mode=None, period_num=None, job_quota=None, create_time=None, status=None):
        """PerformanceResourceRsp

        The model defined in huaweicloud sdk

        :param id: 实例ID
        :type id: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param name: 实例名称
        :type name: str
        :param spec: 
        :type spec: :class:`huaweicloudsdkeihealth.v1.SpecDto`
        :param availability_zone_id: 可用区
        :type availability_zone_id: str
        :param space: 最大容量, 单位GB
        :type space: int
        :param free_space: 可用容量，单位GB
        :type free_space: float
        :param charge_mode: 计费模式
        :type charge_mode: str
        :param period_num: 购买周期
        :type period_num: int
        :param job_quota: 运行的最大作业数量
        :type job_quota: int
        :param create_time: 购买时间
        :type create_time: str
        :param status: 状态
        :type status: str
        """
        
        

        self._id = None
        self._resource_id = None
        self._name = None
        self._spec = None
        self._availability_zone_id = None
        self._space = None
        self._free_space = None
        self._charge_mode = None
        self._period_num = None
        self._job_quota = None
        self._create_time = None
        self._status = None
        self.discriminator = None

        self.id = id
        self.resource_id = resource_id
        self.name = name
        self.spec = spec
        self.availability_zone_id = availability_zone_id
        self.space = space
        self.free_space = free_space
        self.charge_mode = charge_mode
        self.period_num = period_num
        if job_quota is not None:
            self.job_quota = job_quota
        self.create_time = create_time
        self.status = status

    @property
    def id(self):
        """Gets the id of this PerformanceResourceRsp.

        实例ID

        :return: The id of this PerformanceResourceRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PerformanceResourceRsp.

        实例ID

        :param id: The id of this PerformanceResourceRsp.
        :type id: str
        """
        self._id = id

    @property
    def resource_id(self):
        """Gets the resource_id of this PerformanceResourceRsp.

        资源ID

        :return: The resource_id of this PerformanceResourceRsp.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this PerformanceResourceRsp.

        资源ID

        :param resource_id: The resource_id of this PerformanceResourceRsp.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def name(self):
        """Gets the name of this PerformanceResourceRsp.

        实例名称

        :return: The name of this PerformanceResourceRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PerformanceResourceRsp.

        实例名称

        :param name: The name of this PerformanceResourceRsp.
        :type name: str
        """
        self._name = name

    @property
    def spec(self):
        """Gets the spec of this PerformanceResourceRsp.

        :return: The spec of this PerformanceResourceRsp.
        :rtype: :class:`huaweicloudsdkeihealth.v1.SpecDto`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this PerformanceResourceRsp.

        :param spec: The spec of this PerformanceResourceRsp.
        :type spec: :class:`huaweicloudsdkeihealth.v1.SpecDto`
        """
        self._spec = spec

    @property
    def availability_zone_id(self):
        """Gets the availability_zone_id of this PerformanceResourceRsp.

        可用区

        :return: The availability_zone_id of this PerformanceResourceRsp.
        :rtype: str
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        """Sets the availability_zone_id of this PerformanceResourceRsp.

        可用区

        :param availability_zone_id: The availability_zone_id of this PerformanceResourceRsp.
        :type availability_zone_id: str
        """
        self._availability_zone_id = availability_zone_id

    @property
    def space(self):
        """Gets the space of this PerformanceResourceRsp.

        最大容量, 单位GB

        :return: The space of this PerformanceResourceRsp.
        :rtype: int
        """
        return self._space

    @space.setter
    def space(self, space):
        """Sets the space of this PerformanceResourceRsp.

        最大容量, 单位GB

        :param space: The space of this PerformanceResourceRsp.
        :type space: int
        """
        self._space = space

    @property
    def free_space(self):
        """Gets the free_space of this PerformanceResourceRsp.

        可用容量，单位GB

        :return: The free_space of this PerformanceResourceRsp.
        :rtype: float
        """
        return self._free_space

    @free_space.setter
    def free_space(self, free_space):
        """Sets the free_space of this PerformanceResourceRsp.

        可用容量，单位GB

        :param free_space: The free_space of this PerformanceResourceRsp.
        :type free_space: float
        """
        self._free_space = free_space

    @property
    def charge_mode(self):
        """Gets the charge_mode of this PerformanceResourceRsp.

        计费模式

        :return: The charge_mode of this PerformanceResourceRsp.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this PerformanceResourceRsp.

        计费模式

        :param charge_mode: The charge_mode of this PerformanceResourceRsp.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def period_num(self):
        """Gets the period_num of this PerformanceResourceRsp.

        购买周期

        :return: The period_num of this PerformanceResourceRsp.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this PerformanceResourceRsp.

        购买周期

        :param period_num: The period_num of this PerformanceResourceRsp.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def job_quota(self):
        """Gets the job_quota of this PerformanceResourceRsp.

        运行的最大作业数量

        :return: The job_quota of this PerformanceResourceRsp.
        :rtype: int
        """
        return self._job_quota

    @job_quota.setter
    def job_quota(self, job_quota):
        """Sets the job_quota of this PerformanceResourceRsp.

        运行的最大作业数量

        :param job_quota: The job_quota of this PerformanceResourceRsp.
        :type job_quota: int
        """
        self._job_quota = job_quota

    @property
    def create_time(self):
        """Gets the create_time of this PerformanceResourceRsp.

        购买时间

        :return: The create_time of this PerformanceResourceRsp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this PerformanceResourceRsp.

        购买时间

        :param create_time: The create_time of this PerformanceResourceRsp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def status(self):
        """Gets the status of this PerformanceResourceRsp.

        状态

        :return: The status of this PerformanceResourceRsp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PerformanceResourceRsp.

        状态

        :param status: The status of this PerformanceResourceRsp.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, PerformanceResourceRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
