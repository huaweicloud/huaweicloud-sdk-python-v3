# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ElasticResourcePool:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'elastic_resource_pool_name': 'str',
        'id': 'int',
        'update_time': 'int',
        'queues': 'list[str]',
        'owner': 'str',
        'description': 'str',
        'max_cu': 'int',
        'min_cu': 'int',
        'actual_cu': 'int',
        'cidr_in_vpc': 'str',
        'create_time': 'int',
        'current_cu': 'int',
        'status': 'str',
        'resource_id': 'str',
        'fail_reason': 'str',
        'enterprise_project_id': 'str',
        'prepay_cu': 'int',
        'charging_mode': 'int',
        'manager': 'str',
        'label': 'dict(str, str)',
        'ipv6_enable': 'bool',
        'ipv6_cidr_in_subnet': 'str'
    }

    attribute_map = {
        'elastic_resource_pool_name': 'elastic_resource_pool_name',
        'id': 'id',
        'update_time': 'update_time',
        'queues': 'queues',
        'owner': 'owner',
        'description': 'description',
        'max_cu': 'max_cu',
        'min_cu': 'min_cu',
        'actual_cu': 'actual_cu',
        'cidr_in_vpc': 'cidr_in_vpc',
        'create_time': 'create_time',
        'current_cu': 'current_cu',
        'status': 'status',
        'resource_id': 'resource_id',
        'fail_reason': 'fail_reason',
        'enterprise_project_id': 'enterprise_project_id',
        'prepay_cu': 'prepay_cu',
        'charging_mode': 'charging_mode',
        'manager': 'manager',
        'label': 'label',
        'ipv6_enable': 'ipv6_enable',
        'ipv6_cidr_in_subnet': 'ipv6_cidr_in_subnet'
    }

    def __init__(self, elastic_resource_pool_name=None, id=None, update_time=None, queues=None, owner=None, description=None, max_cu=None, min_cu=None, actual_cu=None, cidr_in_vpc=None, create_time=None, current_cu=None, status=None, resource_id=None, fail_reason=None, enterprise_project_id=None, prepay_cu=None, charging_mode=None, manager=None, label=None, ipv6_enable=None, ipv6_cidr_in_subnet=None):
        r"""ElasticResourcePool

        The model defined in huaweicloud sdk

        :param elastic_resource_pool_name: 资源池名称
        :type elastic_resource_pool_name: str
        :param id: 资源池id
        :type id: int
        :param update_time: 更新时间
        :type update_time: int
        :param queues: 
        :type queues: list[str]
        :param owner: 用户名
        :type owner: str
        :param description: 资源池描述
        :type description: str
        :param max_cu: 最大cu数量
        :type max_cu: int
        :param min_cu: 最小cu数量
        :type min_cu: int
        :param actual_cu: 实际cu数量
        :type actual_cu: int
        :param cidr_in_vpc: 子网
        :type cidr_in_vpc: str
        :param create_time: 创建时间
        :type create_time: int
        :param current_cu: 当前cu数量
        :type current_cu: int
        :param status: 状态
        :type status: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param fail_reason: 创建失败原因
        :type fail_reason: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param prepay_cu: 预付费cu数量
        :type prepay_cu: int
        :param charging_mode: 计费类型
        :type charging_mode: int
        :param manager: 弹性资源池类型
        :type manager: str
        :param label: 弹性资源池属性字段。默认为标准版弹性资源池；{\&quot;spec\&quot;:\&quot;basic\&quot;}标识基础版弹性资源池；{\&quot;billing_spec_code\&quot;:\&quot;developer\&quot;}标识开发者弹性资源池。目前不支持其它属性设置。
        :type label: dict(str, str)
        :param ipv6_enable: 是否启用IPv6
        :type ipv6_enable: bool
        :param ipv6_cidr_in_subnet: IPv6子网网段
        :type ipv6_cidr_in_subnet: str
        """
        
        

        self._elastic_resource_pool_name = None
        self._id = None
        self._update_time = None
        self._queues = None
        self._owner = None
        self._description = None
        self._max_cu = None
        self._min_cu = None
        self._actual_cu = None
        self._cidr_in_vpc = None
        self._create_time = None
        self._current_cu = None
        self._status = None
        self._resource_id = None
        self._fail_reason = None
        self._enterprise_project_id = None
        self._prepay_cu = None
        self._charging_mode = None
        self._manager = None
        self._label = None
        self._ipv6_enable = None
        self._ipv6_cidr_in_subnet = None
        self.discriminator = None

        if elastic_resource_pool_name is not None:
            self.elastic_resource_pool_name = elastic_resource_pool_name
        if id is not None:
            self.id = id
        if update_time is not None:
            self.update_time = update_time
        if queues is not None:
            self.queues = queues
        if owner is not None:
            self.owner = owner
        if description is not None:
            self.description = description
        if max_cu is not None:
            self.max_cu = max_cu
        if min_cu is not None:
            self.min_cu = min_cu
        if actual_cu is not None:
            self.actual_cu = actual_cu
        if cidr_in_vpc is not None:
            self.cidr_in_vpc = cidr_in_vpc
        if create_time is not None:
            self.create_time = create_time
        if current_cu is not None:
            self.current_cu = current_cu
        if status is not None:
            self.status = status
        if resource_id is not None:
            self.resource_id = resource_id
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if prepay_cu is not None:
            self.prepay_cu = prepay_cu
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if manager is not None:
            self.manager = manager
        if label is not None:
            self.label = label
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if ipv6_cidr_in_subnet is not None:
            self.ipv6_cidr_in_subnet = ipv6_cidr_in_subnet

    @property
    def elastic_resource_pool_name(self):
        r"""Gets the elastic_resource_pool_name of this ElasticResourcePool.

        资源池名称

        :return: The elastic_resource_pool_name of this ElasticResourcePool.
        :rtype: str
        """
        return self._elastic_resource_pool_name

    @elastic_resource_pool_name.setter
    def elastic_resource_pool_name(self, elastic_resource_pool_name):
        r"""Sets the elastic_resource_pool_name of this ElasticResourcePool.

        资源池名称

        :param elastic_resource_pool_name: The elastic_resource_pool_name of this ElasticResourcePool.
        :type elastic_resource_pool_name: str
        """
        self._elastic_resource_pool_name = elastic_resource_pool_name

    @property
    def id(self):
        r"""Gets the id of this ElasticResourcePool.

        资源池id

        :return: The id of this ElasticResourcePool.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ElasticResourcePool.

        资源池id

        :param id: The id of this ElasticResourcePool.
        :type id: int
        """
        self._id = id

    @property
    def update_time(self):
        r"""Gets the update_time of this ElasticResourcePool.

        更新时间

        :return: The update_time of this ElasticResourcePool.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ElasticResourcePool.

        更新时间

        :param update_time: The update_time of this ElasticResourcePool.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def queues(self):
        r"""Gets the queues of this ElasticResourcePool.

        :return: The queues of this ElasticResourcePool.
        :rtype: list[str]
        """
        return self._queues

    @queues.setter
    def queues(self, queues):
        r"""Sets the queues of this ElasticResourcePool.

        :param queues: The queues of this ElasticResourcePool.
        :type queues: list[str]
        """
        self._queues = queues

    @property
    def owner(self):
        r"""Gets the owner of this ElasticResourcePool.

        用户名

        :return: The owner of this ElasticResourcePool.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this ElasticResourcePool.

        用户名

        :param owner: The owner of this ElasticResourcePool.
        :type owner: str
        """
        self._owner = owner

    @property
    def description(self):
        r"""Gets the description of this ElasticResourcePool.

        资源池描述

        :return: The description of this ElasticResourcePool.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ElasticResourcePool.

        资源池描述

        :param description: The description of this ElasticResourcePool.
        :type description: str
        """
        self._description = description

    @property
    def max_cu(self):
        r"""Gets the max_cu of this ElasticResourcePool.

        最大cu数量

        :return: The max_cu of this ElasticResourcePool.
        :rtype: int
        """
        return self._max_cu

    @max_cu.setter
    def max_cu(self, max_cu):
        r"""Sets the max_cu of this ElasticResourcePool.

        最大cu数量

        :param max_cu: The max_cu of this ElasticResourcePool.
        :type max_cu: int
        """
        self._max_cu = max_cu

    @property
    def min_cu(self):
        r"""Gets the min_cu of this ElasticResourcePool.

        最小cu数量

        :return: The min_cu of this ElasticResourcePool.
        :rtype: int
        """
        return self._min_cu

    @min_cu.setter
    def min_cu(self, min_cu):
        r"""Sets the min_cu of this ElasticResourcePool.

        最小cu数量

        :param min_cu: The min_cu of this ElasticResourcePool.
        :type min_cu: int
        """
        self._min_cu = min_cu

    @property
    def actual_cu(self):
        r"""Gets the actual_cu of this ElasticResourcePool.

        实际cu数量

        :return: The actual_cu of this ElasticResourcePool.
        :rtype: int
        """
        return self._actual_cu

    @actual_cu.setter
    def actual_cu(self, actual_cu):
        r"""Sets the actual_cu of this ElasticResourcePool.

        实际cu数量

        :param actual_cu: The actual_cu of this ElasticResourcePool.
        :type actual_cu: int
        """
        self._actual_cu = actual_cu

    @property
    def cidr_in_vpc(self):
        r"""Gets the cidr_in_vpc of this ElasticResourcePool.

        子网

        :return: The cidr_in_vpc of this ElasticResourcePool.
        :rtype: str
        """
        return self._cidr_in_vpc

    @cidr_in_vpc.setter
    def cidr_in_vpc(self, cidr_in_vpc):
        r"""Sets the cidr_in_vpc of this ElasticResourcePool.

        子网

        :param cidr_in_vpc: The cidr_in_vpc of this ElasticResourcePool.
        :type cidr_in_vpc: str
        """
        self._cidr_in_vpc = cidr_in_vpc

    @property
    def create_time(self):
        r"""Gets the create_time of this ElasticResourcePool.

        创建时间

        :return: The create_time of this ElasticResourcePool.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ElasticResourcePool.

        创建时间

        :param create_time: The create_time of this ElasticResourcePool.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def current_cu(self):
        r"""Gets the current_cu of this ElasticResourcePool.

        当前cu数量

        :return: The current_cu of this ElasticResourcePool.
        :rtype: int
        """
        return self._current_cu

    @current_cu.setter
    def current_cu(self, current_cu):
        r"""Sets the current_cu of this ElasticResourcePool.

        当前cu数量

        :param current_cu: The current_cu of this ElasticResourcePool.
        :type current_cu: int
        """
        self._current_cu = current_cu

    @property
    def status(self):
        r"""Gets the status of this ElasticResourcePool.

        状态

        :return: The status of this ElasticResourcePool.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ElasticResourcePool.

        状态

        :param status: The status of this ElasticResourcePool.
        :type status: str
        """
        self._status = status

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ElasticResourcePool.

        资源ID

        :return: The resource_id of this ElasticResourcePool.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ElasticResourcePool.

        资源ID

        :param resource_id: The resource_id of this ElasticResourcePool.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this ElasticResourcePool.

        创建失败原因

        :return: The fail_reason of this ElasticResourcePool.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this ElasticResourcePool.

        创建失败原因

        :param fail_reason: The fail_reason of this ElasticResourcePool.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ElasticResourcePool.

        企业项目ID

        :return: The enterprise_project_id of this ElasticResourcePool.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ElasticResourcePool.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ElasticResourcePool.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def prepay_cu(self):
        r"""Gets the prepay_cu of this ElasticResourcePool.

        预付费cu数量

        :return: The prepay_cu of this ElasticResourcePool.
        :rtype: int
        """
        return self._prepay_cu

    @prepay_cu.setter
    def prepay_cu(self, prepay_cu):
        r"""Sets the prepay_cu of this ElasticResourcePool.

        预付费cu数量

        :param prepay_cu: The prepay_cu of this ElasticResourcePool.
        :type prepay_cu: int
        """
        self._prepay_cu = prepay_cu

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ElasticResourcePool.

        计费类型

        :return: The charging_mode of this ElasticResourcePool.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ElasticResourcePool.

        计费类型

        :param charging_mode: The charging_mode of this ElasticResourcePool.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def manager(self):
        r"""Gets the manager of this ElasticResourcePool.

        弹性资源池类型

        :return: The manager of this ElasticResourcePool.
        :rtype: str
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        r"""Sets the manager of this ElasticResourcePool.

        弹性资源池类型

        :param manager: The manager of this ElasticResourcePool.
        :type manager: str
        """
        self._manager = manager

    @property
    def label(self):
        r"""Gets the label of this ElasticResourcePool.

        弹性资源池属性字段。默认为标准版弹性资源池；{\"spec\":\"basic\"}标识基础版弹性资源池；{\"billing_spec_code\":\"developer\"}标识开发者弹性资源池。目前不支持其它属性设置。

        :return: The label of this ElasticResourcePool.
        :rtype: dict(str, str)
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this ElasticResourcePool.

        弹性资源池属性字段。默认为标准版弹性资源池；{\"spec\":\"basic\"}标识基础版弹性资源池；{\"billing_spec_code\":\"developer\"}标识开发者弹性资源池。目前不支持其它属性设置。

        :param label: The label of this ElasticResourcePool.
        :type label: dict(str, str)
        """
        self._label = label

    @property
    def ipv6_enable(self):
        r"""Gets the ipv6_enable of this ElasticResourcePool.

        是否启用IPv6

        :return: The ipv6_enable of this ElasticResourcePool.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        r"""Sets the ipv6_enable of this ElasticResourcePool.

        是否启用IPv6

        :param ipv6_enable: The ipv6_enable of this ElasticResourcePool.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def ipv6_cidr_in_subnet(self):
        r"""Gets the ipv6_cidr_in_subnet of this ElasticResourcePool.

        IPv6子网网段

        :return: The ipv6_cidr_in_subnet of this ElasticResourcePool.
        :rtype: str
        """
        return self._ipv6_cidr_in_subnet

    @ipv6_cidr_in_subnet.setter
    def ipv6_cidr_in_subnet(self, ipv6_cidr_in_subnet):
        r"""Sets the ipv6_cidr_in_subnet of this ElasticResourcePool.

        IPv6子网网段

        :param ipv6_cidr_in_subnet: The ipv6_cidr_in_subnet of this ElasticResourcePool.
        :type ipv6_cidr_in_subnet: str
        """
        self._ipv6_cidr_in_subnet = ipv6_cidr_in_subnet

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
        if not isinstance(other, ElasticResourcePool):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
